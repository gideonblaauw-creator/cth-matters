#!/usr/bin/env python3
"""Deep crawl for citation-grade person@firm emails on resolved domains."""
from __future__ import annotations

import base64
import csv
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML_DIR = ROOT / "html"
USER_AGENT = "MailFinder-Teclogi-Deep50/1.0 (+research; polite)"

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
CFEMAIL_RE = re.compile(r'data-cfemail="([0-9a-fA-F]+)"')


def decode_cfemail(hex_str: str) -> str:
    try:
        r = int(hex_str[:2], 16)
        return "".join(chr(int(hex_str[i : i + 2], 16) ^ r) for i in range(2, len(hex_str), 2))
    except Exception:
        return ""


def fetch(url: str, timeout: int = 15) -> tuple[int, str, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.geturl(), resp.read()
    except Exception as e:
        return 0, url, str(e).encode()


def norm_domain(d: str) -> str:
    d = d.strip().lower()
    d = re.sub(r"^https?://", "", d)
    d = d.split("/")[0]
    if d.startswith("www."):
        d = d[4:]
    return d


def website_url(domain: str) -> str:
    return f"https://{norm_domain(domain)}"


def save_html(domain: str, path_suffix: str, content: bytes) -> str:
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^a-zA-Z0-9._-]", "_", f"{domain}_{path_suffix}")[:120]
    p = HTML_DIR / f"{safe}.html"
    p.write_bytes(content)
    return str(p.relative_to(ROOT))


def extract_emails_from_text(text: str, domain: str) -> set[str]:
    found = set()
    for m in CFEMAIL_RE.finditer(text):
        dec = decode_cfemail(m.group(1))
        if dec and "@" in dec:
            found.add(dec.lower())
    for m in EMAIL_RE.findall(text):
        em = m.lower().rstrip(".")
        if domain in em or em.split("@")[-1].endswith(domain.split(".")[-1]):
            found.add(em)
    return found


def name_tokens(name: str) -> list[str]:
    name = unescape(name)
    name = re.sub(r",.*$", "", name)
    name = re.sub(r"\b(MBA|Dr\.?|Eng\.?|IPMA|SDG)\b\.?", "", name, flags=re.I)
    parts = re.findall(r"[A-Za-zÀ-ÿ]+", name)
    return [p.lower() for p in parts if len(p) > 1]


def name_near_email(text: str, email: str, tokens: list[str], window: int = 800) -> bool:
    text_l = text.lower()
    idx = text_l.find(email.lower())
    if idx < 0:
        return False
    chunk = text_l[max(0, idx - window) : idx + window]
    hits = sum(1 for t in tokens if t in chunk)
    if len(tokens) >= 2 and hits >= 2:
        return True
    if tokens and hits >= 1 and any(t in email.lower() for t in tokens):
        return True
    return False


def wayback_urls(domain: str, path: str) -> list[str]:
    cdx = (
        f"https://web.archive.org/cdx/search/cdx?url={urllib.parse.quote(domain + path)}"
        f"&output=json&limit=3&filter=statuscode:200&collapse=urlkey"
    )
    status, _, body = fetch(cdx, timeout=20)
    if status != 200:
        return []
    try:
        rows = json.loads(body.decode("utf-8", errors="replace"))
        if len(rows) < 2:
            return []
        urls = []
        for row in rows[1:]:
            if len(row) >= 3:
                ts, orig = row[1], row[2]
                urls.append(f"https://web.archive.org/web/{ts}/{orig}")
        return urls
    except Exception:
        return []


PATHS = [
    "/",
    "/about",
    "/team",
    "/people",
    "/contact",
]


@dataclass
class CrawlResult:
    emails: list[tuple[str, str, str, str]] = field(default_factory=list)  # email, url, method, excerpt
    checked: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def crawl_person(name: str, domain: str) -> CrawlResult:
    domain = norm_domain(domain)
    res = CrawlResult()
    tokens = name_tokens(name)
    all_pages: list[tuple[str, str]] = []

    for path in PATHS:
        url = website_url(domain) + (path if path != "/" else "")
        status, final, body = fetch(url)
        res.checked.append(final if status else url)
        if status and body and not body.startswith(b"Traceback"):
            save_html(domain, path.strip("/") or "root", body)
            text = body.decode("utf-8", errors="replace")
            all_pages.append((final, text))
            for em in extract_emails_from_text(text, domain):
                if name_near_email(text, em, tokens):
                    excerpt = text[max(0, text.lower().find(em.lower()) - 200) : text.lower().find(em.lower()) + 200]
                    excerpt = re.sub(r"\s+", " ", excerpt)[:400]
                    res.emails.append((em, final, "website_source", excerpt))
        time.sleep(0.35)

    # Wayback + PDF skipped in batch mode (see brief: run manually for stubborn seats)
    res.notes.append("wayback/pdf: deferred in batch crawl for latency")

    # dedupe emails
    seen = set()
    deduped = []
    for item in res.emails:
        if item[0] not in seen:
            seen.add(item[0])
            deduped.append(item)
    res.emails = deduped
    return res


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: crawl.py 'Name' domain.tld")
        sys.exit(1)
    r = crawl_person(sys.argv[1], sys.argv[2])
    print(json.dumps({"emails": r.emails, "checked": r.checked, "notes": r.notes}, indent=2))
