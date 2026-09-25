#!/usr/bin/env python3
"""Wave4 L02 Arm 01 — first-party team/people mailto crawl (public HTTP only)."""
from __future__ import annotations

import csv
import json
import re
import ssl
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
INPUT_CSV = ROOT / "input.csv"
RESULTS_CSV = ROOT / "results.csv"
STAMP_JSON = ROOT / "stamp-list.json"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
CTX = ssl.create_default_context()

PATH_SUFFIXES = (
    "",
    "/team",
    "/people",
    "/about",
    "/our-team",
    "/leadership",
    "/contact",
)

GENERIC_LOCAL = frozenset(
    {
        "info",
        "hello",
        "team",
        "contact",
        "ventures",
        "support",
        "sales",
        "admin",
        "office",
        "secretary",
    }
)

EXTRA_PATHS: dict[str, list[str]] = {
    "clicoh.com": [
        "/sobre-clicoh",
        "/enviar-con-clicoh",
        "/blog",
    ],
    "maersk.com": [
        "https://web.archive.org/web/20241210154802id_/https://www.maersk.com/growth/",
    ],
}


def fetch(url: str, timeout: int = 15) -> tuple[int | None, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001 — record failure in Checked_URLs
        return None, str(exc)


def origin_from_website(website: str) -> str:
    parsed = urlparse(website)
    return f"{parsed.scheme}://{parsed.netloc}"


def candidate_urls(website: str, domain: str) -> list[str]:
    origin = origin_from_website(website)
    parsed = urlparse(website)
    base_path = parsed.path.rstrip("/")
    urls: list[str] = []
    seen: set[str] = set()

    def add(u: str) -> None:
        if u not in seen:
            seen.add(u)
            urls.append(u)

    add(website.rstrip("/") or website)
    path_prefix = base_path if base_path and base_path not in ("", "/") else ""
    for suffix in PATH_SUFFIXES:
        if suffix == "":
            continue
        if path_prefix:
            add(f"{origin}{path_prefix}{suffix}")
        else:
            add(origin + suffix)
    for extra in EXTRA_PATHS.get(domain, []):
        if extra.startswith("http"):
            add(extra)
        else:
            add(origin + extra)
    return urls


def extract_emails(html: str) -> set[str]:
    found = set(re.findall(r"mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", html, re.I))
    found.update(re.findall(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", html))
    return found


def is_person_email(email: str, domain: str) -> bool:
    local = email.split("@", 1)[0].lower()
    if domain not in email.lower():
        return False
    if local in GENERIC_LOCAL:
        return False
    return True


def name_cooccurs(html: str, contact_name: str, email: str, window: int = 900) -> str | None:
    html_l = html.lower()
    email_l = email.lower()
    name_l = contact_name.lower()
    parts = name_l.split()
    pos = 0
    while True:
        idx = html_l.find(email_l, pos)
        if idx == -1:
            break
        chunk = html[max(0, idx - window) : min(len(html), idx + len(email) + window)]
        chunk_l = chunk.lower()
        if name_l in chunk_l:
            return re.sub(r"\s+", " ", chunk.strip())[:500]
        if len(parts) >= 2 and parts[0] in chunk_l and parts[-1] in chunk_l:
            return re.sub(r"\s+", " ", chunk.strip())[:500]
        pos = idx + 1
    return None


def crawl_seat(row: dict) -> dict:
    domain = row["Domain"].strip()
    website = row["Website"].strip()
    contact = row["Contact_name"].strip()
    checked: list[str] = []
    best: tuple[str, str, str] | None = None  # email, source_url, excerpt

    for url in candidate_urls(website, domain):
        code, html = fetch(url)
        checked.append(f"{url} ({code if code is not None else 'ERR'})")
        if code is None or code >= 400 or not html:
            continue
        for email in extract_emails(html):
            if not is_person_email(email, domain):
                continue
            excerpt = name_cooccurs(html, contact, email)
            if excerpt:
                best = (email, url, excerpt)
                break
        if best:
            break

    status = "FOUND" if best else "EMPTY"
    notes = ""
    if domain == "maersk.com" and not best:
        notes = (
            "Live maersk.com/growth returned connection errors from Hands curl; "
            "Wayback id_ snapshot (2024-12) and readable homepage copy show venture "
            "content and Contact-the-team CTA only — no person@maersk.com mailto on page source."
        )
    elif domain == "clicoh.com" and not best:
        notes = (
            "First-party crawl of home, sobre-clicoh, enviar-con-clicoh, blog, and "
            "standard team paths: no @clicoh.com addresses in HTML/RSC; Camilo Arango not listed."
        )
    elif domain == "amazoninvestor.org" and not best:
        notes = (
            "Ricardo Politi profile on /people (modal bio, LinkedIn-style popup only). "
            "Contact page lists secretary@amazoninvestor.org (generic role inbox — not stamped)."
        )
    elif domain == "zenanicapital.com" and not best:
        notes = (
            "Alethia Wong on homepage #team with LinkedIn only; footer mailto info@zenanicapital.com "
            "(generic — not citation-grade for person)."
        )

    return {
        **row,
        "Email": best[0] if best else "",
        "Source_URL": best[1] if best else "",
        "Checked_URLs": " | ".join(checked),
        "Status": status,
        "Notes": notes,
        "Method": "wave4-L02-arm01-first-party-team",
        "_evidence": best[2] if best else "",
        "_monday_id": row["Monday_item_id"],
    }


def main() -> None:
    rows = list(csv.DictReader(INPUT_CSV.open(newline="", encoding="utf-8")))
    results = [crawl_seat(r) for r in rows]

    fieldnames = [
        "Monday_item_id",
        "Name",
        "Contact_name",
        "Firm",
        "Kind",
        "Priority",
        "Website",
        "Domain",
        "Email",
        "Source_URL",
        "Checked_URLs",
        "Status",
        "Notes",
        "Method",
    ]
    with RESULTS_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for r in results:
            w.writerow(r)

    stamps = []
    ev_dir = ROOT / "evidence"
    ev_dir.mkdir(exist_ok=True)
    for r in results:
        if r["Status"] != "FOUND":
            continue
        stamps.append(
            {
                "Monday_item_id": r["Monday_item_id"],
                "Email": r["Email"],
                "Source_URL": r["Source_URL"],
                "Evidence_excerpt": r["_evidence"],
            }
        )
        slug = re.sub(r"[^a-z0-9]+", "-", r["Contact_name"].lower()).strip("-")
        (ev_dir / f"{slug}.txt").write_text(r["_evidence"], encoding="utf-8")

    STAMP_JSON.write_text(json.dumps(stamps, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {RESULTS_CSV} ({len(results)} rows, {len(stamps)} FOUND)")


if __name__ == "__main__":
    main()
