#!/usr/bin/env python3
"""Wave4 L02 arm-04: firm-site mailto + name co-occurrence (public HTTP only)."""
from __future__ import annotations

import csv
import json
import re
import html as html_lib
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT / "evidence"
UA = "MailFinder-Wave4-L02-arm04/1.0 (Teclogi; public research)"

PATH_SEEDS = [
    "/",
    "/team",
    "/team/",
    "/people",
    "/about",
    "/about-us",
    "/our-team",
    "/leadership",
    "/contact",
    "/contact-us",
]

GENERIC_LOCAL = {
    "info",
    "hello",
    "contact",
    "team",
    "support",
    "sales",
    "press",
    "media",
    "hr",
    "jobs",
    "careers",
    "office",
    "admin",
    "enquiries",
    "inquiries",
    "privacy",
    "legal",
    "ir",
    "investor",
    "investors",
    "comms",
    "communications",
}

MAILTO_RE = re.compile(
    r'mailto:([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})',
    re.I,
)
CFEMAIL_RE = re.compile(
    r'data-cfemail=["\']([a-f0-9]+)["\']',
    re.I,
)


def cf_decode(hex_str: str) -> str:
    try:
        r = int(hex_str[:2], 16)
        return "".join(
            chr(int(hex_str[i : i + 2], 16) ^ r) for i in range(2, len(hex_str), 2)
        )
    except Exception:
        return ""


def fetch(url: str, timeout: int = 25) -> tuple[int | None, str, bytes, str | None]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            final = resp.geturl()
            body = resp.read()
            return resp.status, final, body, None
    except Exception as e:
        return None, url, b"", str(e)


def name_tokens(name: str) -> list[str]:
    n = re.sub(r"[^\w\s'-]", " ", name, flags=re.UNICODE)
    parts = [
        p
        for p in n.split()
        if len(p) > 2
        and p.lower()
        not in ("mba", "dr", "eng", "ipma", "and", "the", "von", "de", "del", "la")
    ]
    return parts


def name_in_text(name: str, text: str) -> bool:
    t = html_lib.unescape(text).lower()
    parts = [p.lower() for p in name_tokens(name)]
    if not parts:
        return False
    if len(parts) >= 2:
        if parts[0] in t and parts[-1] in t:
            return True
        if " ".join(parts) in t:
            return True
    return parts[0] in t


def extract_mailtos(html: str) -> list[str]:
    out: list[str] = []
    for m in MAILTO_RE.findall(html):
        out.append(m.split("?")[0].lower())
    for hx in CFEMAIL_RE.findall(html):
        dec = cf_decode(hx)
        if "@" in dec:
            out.append(dec.lower())
    return sorted(set(out))


def is_generic(email: str) -> bool:
    local = email.split("@")[0].lower()
    if local in GENERIC_LOCAL:
        return True
    for g in GENERIC_LOCAL:
        if local.startswith(g + ".") or local.endswith("." + g):
            return True
    return False


def mailto_blocks(html: str) -> list[tuple[str, str]]:
    """Return (email, surrounding_html_snippet) for each mailto anchor."""
    blocks: list[tuple[str, str]] = []
    for m in re.finditer(
        r"(?is)(.{0,400}mailto:[^\"\'>\s]+.{0,400})",
        html,
    ):
        chunk = m.group(1)
        for em in MAILTO_RE.findall(chunk):
            blocks.append((em.split("?")[0].lower(), chunk))
    for m in re.finditer(
        r"(?is)(.{0,400}data-cfemail=[\"'][a-f0-9]+[\"'].{0,400})",
        html,
    ):
        chunk = m.group(1)
        for hx in CFEMAIL_RE.findall(chunk):
            dec = cf_decode(hx)
            if "@" in dec:
                blocks.append((dec.lower(), chunk))
    return blocks


def crawl_website(website: str, domain: str) -> dict:
    parsed = urllib.parse.urlparse(website)
    base_host = parsed.netloc or domain
    scheme = parsed.scheme or "https"
    base = f"{scheme}://{base_host}"

    checked: list[str] = []
    pages: dict[str, str] = {}

    for path in PATH_SEEDS:
        url = base.rstrip("/") + (path if path.startswith("/") else "/" + path)
        if url in checked:
            continue
        status, final, body, err = fetch(url)
        checked.append(final if status else url)
        if status and 200 <= status < 400:
            text = body.decode("utf-8", errors="replace")
            slug = re.sub(r"[^a-zA-Z0-9._-]", "_", urllib.parse.urlparse(final).path or "root")[
                :60
            ]
            fname = f"{domain.replace('.', '_')}{slug}.html"
            (EVIDENCE / fname).write_text(text[:800_000], encoding="utf-8")
            pages[final] = text

    # Also try www variant if different
    if not base_host.startswith("www."):
        alt_base = f"{scheme}://www.{base_host}"
        for path in ("/team/", "/team", "/"):
            url = alt_base.rstrip("/") + path
            if url in checked:
                continue
            status, final, body, err = fetch(url)
            checked.append(final if status else url)
            if status and 200 <= status < 400:
                text = body.decode("utf-8", errors="replace")
                slug = re.sub(
                    r"[^a-zA-Z0-9._-]", "_", urllib.parse.urlparse(final).path or "root"
                )[:60]
                fname = f"www_{domain.replace('.', '_')}{slug}.html"
                (EVIDENCE / fname).write_text(text[:800_000], encoding="utf-8")
                pages[final] = text

    return {"checked_urls": checked, "pages": pages}


def attribute_seat(
    contact_name: str, domain: str, crawl: dict
) -> tuple[str | None, str | None, str, list[dict]]:
    """Returns email, source_url, notes, attributions."""
    attributions: list[dict] = []
    best: tuple[str, str, str] | None = None  # email, url, note

    for url, html in crawl["pages"].items():
        mailtos = extract_mailtos(html)
        page_has_name = name_in_text(contact_name, html)
        for em in mailtos:
            em_domain = em.split("@")[-1]
            if domain not in em_domain and em_domain != domain:
                continue
            if is_generic(em):
                continue
            if not page_has_name:
                continue
            # Prefer block-level co-occurrence
            block_hit = False
            for bem, chunk in mailto_blocks(html):
                if bem == em and name_in_text(contact_name, chunk):
                    block_hit = True
                    attributions.append(
                        {"email": em, "url": url, "block_cooccurrence": True}
                    )
                    break
            if block_hit or page_has_name:
                if not any(a["email"] == em and a["url"] == url for a in attributions):
                    attributions.append(
                        {"email": em, "url": url, "block_cooccurrence": block_hit}
                    )
                if best is None or block_hit:
                    note = (
                        f"mailto {em} on same page/block as {contact_name}"
                        if block_hit
                        else f"mailto {em} on page listing {contact_name} (page-level co-occurrence)"
                    )
                    best = (em, url, note)

    if best:
        return best[0], best[1], best[2], attributions
    return None, None, "No citation-grade person@firm mailto with name co-occurrence on crawled paths.", attributions


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    rows_out = []
    crawl_cache: dict[str, dict] = {}

    with (ROOT / "input.csv").open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            mid = row["Monday_item_id"]
            contact = row.get("Contact_name") or row.get("Name") or ""
            firm = row.get("Firm") or ""
            domain = row["Domain"].strip().lower()
            website = row["Website"].strip()
            priority = row.get("Priority", "P2")

            if domain not in crawl_cache:
                crawl_cache[domain] = crawl_website(website, domain)

            crawl = crawl_cache[domain]
            email, source, notes, attrs = attribute_seat(contact, domain, crawl)
            status = "FOUND" if email else "EMPTY"
            checked = " | ".join(dict.fromkeys(crawl["checked_urls"]))

            rows_out.append(
                {
                    "Monday_item_id": mid,
                    "Name": contact,
                    "Firm": firm,
                    "Domain": domain,
                    "Priority": priority,
                    "Email": email or "",
                    "Email_type": "person@firm" if email else "",
                    "Confidence": "high" if email else "",
                    "Source_URL": source or "",
                    "Checked_URLs": checked,
                    "Status": status,
                    "Notes": notes,
                    "Method": "wave4-L02-arm04-firm-mailto",
                }
            )

            slug = domain.replace(".", "_")
            (ROOT / "evidence" / f"{slug}_crawl.json").write_text(
                json.dumps(
                    {
                        "domain": domain,
                        "website": website,
                        "contact_name": contact,
                        "checked_urls": crawl["checked_urls"],
                        "attributions": attrs,
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )

    fieldnames = [
        "Monday_item_id",
        "Name",
        "Firm",
        "Domain",
        "Priority",
        "Email",
        "Email_type",
        "Confidence",
        "Source_URL",
        "Checked_URLs",
        "Status",
        "Notes",
        "Method",
    ]
    with (ROOT / "results.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_out)

    stamps = []
    for r in rows_out:
        stamps.append(
            {
                "monday_item_id": r["Monday_item_id"],
                "name": r["Name"],
                "status": r["Status"],
                "email_column": "email_mm7ffmz4" if r["Status"] == "FOUND" else None,
                "email": r["Email"] or None,
                "source_url": r["Source_URL"] or None,
                "notes_only": r["Status"] != "FOUND",
                "method": r["Method"],
            }
        )
    (ROOT / "stamp-list.json").write_text(json.dumps(stamps, indent=2), encoding="utf-8")
    print(json.dumps({"results": rows_out}, indent=2))


if __name__ == "__main__":
    main()
