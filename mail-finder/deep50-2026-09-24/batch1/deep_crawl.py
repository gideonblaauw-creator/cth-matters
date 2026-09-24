#!/usr/bin/env python3
"""Polite firm-domain deep crawl for Mail Finder batch1."""
import re
import json
import html
import base64
import urllib.parse
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup

UA = "MailFinder-Teclogi-Deep50/1.0 (+research; polite)"
TIMEOUT = 25
ROOT = Path(__file__).resolve().parent
HTML_DIR = ROOT / "html"

EMAIL_RE = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
)
PATHS = [
    "/",
    "/team",
    "/teams",
    "/people",
    "/about",
    "/about-us",
    "/leadership",
    "/contact",
    "/contact-us",
    "/portfolio",
    "/investment-team",
    "/our-team",
    "/who-we-are",
    "/partners",
    "/staff",
    "/team/",
    "/about/",
]


def fetch(url: str) -> tuple[str | None, str | None]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            ct = r.headers.get("Content-Type", "")
            body = r.read(2_000_000)
            if "pdf" in ct.lower() or url.lower().endswith(".pdf"):
                return None, "pdf"
            try:
                text = body.decode("utf-8", errors="replace")
            except Exception:
                text = body.decode("latin-1", errors="replace")
            return text, None
    except Exception as e:
        return None, str(e)


def decode_cfemail(encoded: str) -> str:
    try:
        r = int(encoded[:2], 16)
        return "".join(chr(int(encoded[i : i + 2], 16) ^ r) for i in range(2, len(encoded), 2))
    except Exception:
        return ""


def extract_emails(text: str) -> set[str]:
    if not text:
        return set()
    out = set()
    for m in EMAIL_RE.findall(text):
        m = m.lower().strip(".")
        if not any(x in m for x in ("example.com", "sentry.io", "wixpress", "schema.org")):
            out.add(m)
    for enc in re.findall(r'data-cfemail="([a-f0-9]+)"', text, re.I):
        dec = decode_cfemail(enc)
        if "@" in dec:
            out.add(dec.lower())
    for enc in re.findall(r"/cdn-cgi/l/email-protection#([a-f0-9]+)", text, re.I):
        dec = decode_cfemail(enc)
        if "@" in dec:
            out.add(dec.lower())
    for m in re.findall(r'mailto:([^\s"\'<>?]+)', text, re.I):
        out.add(urllib.parse.unquote(m.split("?")[0]).lower())
    return out


def extract_next_data(text: str) -> str:
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', text, re.S)
    return m.group(1) if m else ""


def name_tokens(name: str) -> list[str]:
    parts = re.sub(r"[^a-zA-Z\s]", " ", name).lower().split()
    skip = {"dr", "mr", "ms", "mrs"}
    return [p for p in parts if p not in skip and len(p) > 1]


def name_near_email(text: str, name: str, email: str, window: int = 800) -> bool:
    if not text:
        return False
    tl = text.lower()
    email_l = email.lower()
    idx = tl.find(email_l)
    if idx < 0:
        return False
    chunk = tl[max(0, idx - window) : idx + window + len(email_l)]
    tokens = name_tokens(name)
    if len(tokens) >= 2:
        return tokens[0] in chunk and tokens[-1] in chunk
    return tokens[0] in chunk if tokens else False


def wayback_urls(domain: str) -> list[str]:
    cdx = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&limit=80&filter=statuscode:200"
    req = urllib.request.Request(cdx, headers={"User-Agent": UA})
    urls = []
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            data = json.loads(r.read().decode())
        for row in data[1:]:
            orig = row[2] if len(row) > 2 else ""
            if any(p in orig.lower() for p in ("team", "people", "about", "contact", "leadership")):
                ts = row[1]
                urls.append(f"https://web.archive.org/web/{ts}/{orig}")
    except Exception:
        pass
    return urls[:15]


def crawl_domain(domain: str, person_name: str) -> dict:
    domain = domain.strip().lower().replace("https://", "").replace("http://", "").strip("/")
    checked = []
    all_emails: dict[str, list[str]] = {}
    attributions = []
    errors = []

    bases = [f"https://{domain}", f"https://www.{domain}"]
    live_urls = []
    for base in bases:
        for p in PATHS:
            live_urls.append(base + p)

    for url in live_urls:
        text, err = fetch(url)
        checked.append(url)
        if err == "pdf":
            continue
        if text is None:
            if err:
                errors.append(f"{url}: {err[:120]}")
            continue
        slug = re.sub(r"[^a-zA-Z0-9._-]", "_", url.replace("https://", ""))[:180]
        (HTML_DIR / f"{slug}.html").write_text(text[:500_000], encoding="utf-8", errors="replace")
        emails = extract_emails(text)
        nd = extract_next_data(text)
        if nd:
            emails |= extract_emails(nd)
        for e in emails:
            all_emails.setdefault(e, []).append(url)
            if person_name and name_near_email(text + nd, person_name, e):
                attributions.append({"email": e, "source_url": url, "method": "live_site"})

    for wb in wayback_urls(domain):
        text, err = fetch(wb)
        checked.append(wb)
        if not text:
            continue
        emails = extract_emails(text)
        for e in emails:
            all_emails.setdefault(e, []).append(wb)
            if person_name and name_near_email(text, person_name, e):
                attributions.append({"email": e, "source_url": wb, "method": "wayback"})

    # site search via common sitemap
    for sm in (f"https://{domain}/sitemap.xml", f"https://www.{domain}/sitemap.xml"):
        text, _ = fetch(sm)
        checked.append(sm)
        if not text:
            continue
        for loc in re.findall(r"<loc>([^<]+)</loc>", text)[:40]:
            if any(k in loc.lower() for k in ("team", "people", "about", "contact", "partner", "staff")):
                t2, _ = fetch(loc)
                checked.append(loc)
                if not t2:
                    continue
                for e in extract_emails(t2):
                    all_emails.setdefault(e, []).append(loc)
                    if person_name and name_near_email(t2, person_name, e):
                        attributions.append({"email": e, "source_url": loc, "method": "sitemap_page"})

    # dedupe attributions prefer firm domain email
    seen = set()
    uniq_attr = []
    for a in attributions:
        k = (a["email"], a["source_url"])
        if k not in seen:
            seen.add(k)
            uniq_attr.append(a)

    return {
        "domain": domain,
        "person": person_name,
        "checked_urls": checked,
        "all_emails": all_emails,
        "attributions": uniq_attr,
        "errors": errors[:5],
    }


if __name__ == "__main__":
    import sys
    domain, name = sys.argv[1], sys.argv[2]
    print(json.dumps(crawl_domain(domain, name), indent=2))
