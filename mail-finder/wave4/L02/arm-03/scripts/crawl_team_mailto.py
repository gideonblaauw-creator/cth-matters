#!/usr/bin/env python3
"""Crawl first-party team paths for name+mailto co-occurrence (Wave4 L02 arm-03)."""
import csv
import json
import re
import ssl
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "input.csv"
EVIDENCE = ROOT / "evidence"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

TEAM_PATHS = [
    "",
    "/team",
    "/team/",
    "/people",
    "/people/",
    "/about",
    "/about/",
    "/about-us",
    "/about-us/",
    "/our-team",
    "/our-team/",
    "/leadership",
    "/leadership/",
    "/about/team",
    "/about/team/",
    "/about-us/team",
    "/about-us/team/",
]

GENERIC_LOCAL = {
    "info",
    "hello",
    "team",
    "contact",
    "support",
    "general",
    "investors",
    "press",
    "careers",
    "hr",
    "admin",
    "office",
    "enquiries",
    "inquiries",
    "mail",
    "sales",
    "marketing",
    "privacy",
    "legal",
    "ventures",
    "grievance",
}


def fetch(url: str, max_bytes: int = 400_000):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            body = r.read(max_bytes)
            return {
                "final_url": r.geturl(),
                "status": r.status,
                "html": body.decode("utf-8", errors="replace"),
                "error": None,
            }
    except Exception as e:
        return {"final_url": url, "status": None, "html": "", "error": str(e)}


def name_tokens(name: str):
    name = re.sub(r"^(Dr\.|Mr\.|Mrs\.|Ms\.)\s+", "", name, flags=re.I)
    name = re.sub(r",.*$", "", name)
    parts = [p for p in re.split(r"\s+", name.strip()) if len(p) > 2]
    return parts


def slugify_name(name: str):
    name = re.sub(r",.*$", "", name).strip().lower()
    return re.sub(r"[^a-z0-9]+", "-", name).strip("-")


def discover_person_urls(base: str, html: str, name: str):
    slug = slugify_name(name)
    tokens = name_tokens(name)
    found = set()
    for m in re.finditer(r'href=["\']([^"\']+)["\']', html, flags=re.I):
        href = m.group(1)
        if slug and slug in href.lower():
            found.add(urllib.parse.urljoin(base, href))
        if tokens and all(t.lower() in href.lower() for t in tokens[:2]):
            found.add(urllib.parse.urljoin(base, href))
    return list(found)[:8]


def scan_html(html: str, final_url: str, name: str, domain: str):
    tokens = name_tokens(name)
    hits = []
    mailtos = re.findall(
        r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', html, flags=re.I
    )
    # also bare emails in page source (same co-occurrence gate)
    bare = re.findall(
        r'(?<![\w.])([a-zA-Z0-9._%+-]+@'
        + re.escape(domain.replace("www.", ""))
        + r')(?![\w.])',
        html,
        flags=re.I,
    )
    candidates = list(dict.fromkeys(mailtos + bare))
    for email in candidates:
        local = email.split("@")[0].lower()
        if local in GENERIC_LOCAL:
            continue
        edomain = email.split("@")[1].lower()
        if domain.lower() not in edomain and edomain not in domain.lower():
            # allow www. variant
            base_dom = domain.replace("www.", "")
            if base_dom not in edomain:
                continue
        for m in re.finditer(re.escape(email), html, flags=re.I):
            chunk = html[max(0, m.start() - 3000) : m.end() + 3000]
            chunk_text = re.sub(r"<[^>]+>", " ", chunk)
            chunk_text = re.sub(r"\s+", " ", chunk_text)
            if tokens and all(t.lower() in chunk_text.lower() for t in tokens[: min(2, len(tokens))]):
                hits.append({"email": email, "source_url": final_url})
                break
    return hits


def crawl_row(row):
    website = row["Website"].strip()
    if not website.startswith("http"):
        website = "https://" + website
    parsed = urllib.parse.urlparse(website)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    domain = row["Domain"] or parsed.netloc.replace("www.", "")

    checked = []
    all_hits = []
    pages_html = {}

    urls_to_try = [urllib.parse.urljoin(origin + "/", p.lstrip("/") if p else "") for p in TEAM_PATHS]
    # normalize
    seen = set()
    queue = []
    for u in urls_to_try:
        if u not in seen:
            seen.add(u)
            queue.append(u)

    for url in queue:
        res = fetch(url)
        label = res["final_url"]
        if res["error"]:
            checked.append(f"{url} (ERROR: {res['error']})")
            continue
        checked.append(f"{label} ({res['status']})")
        html = res["html"]
        pages_html[label] = html
        hits = scan_html(html, label, row["Name"], domain)
        for h in hits:
            if h not in all_hits:
                all_hits.append(h)
        for pu in discover_person_urls(label, html, row["Name"]):
            if pu not in seen:
                seen.add(pu)
                queue.append(pu)

    return {
        "Monday_item_id": row["Monday_item_id"],
        "Name": row["Name"],
        "Domain": domain,
        "Website": website,
        "Priority": row.get("Priority", ""),
        "checked_urls": checked,
        "hits": all_hits,
        "pages_fetched": list(pages_html.keys()),
    }


def main():
    rows = list(csv.DictReader(INPUT.open()))
    out = [crawl_row(r) for r in rows]
    (ROOT / "scripts" / "crawl_results.json").write_text(json.dumps(out, indent=2))
    for item in out:
        print(
            json.dumps(
                {
                    "id": item["Monday_item_id"],
                    "name": item["Name"],
                    "hits": item["hits"],
                    "n_checked": len(item["checked_urls"]),
                }
            ),
            flush=True,
        )


if __name__ == "__main__":
    main()
