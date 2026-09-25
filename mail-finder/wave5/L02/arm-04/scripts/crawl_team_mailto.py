#!/usr/bin/env python3
"""Crawl first-party team/about/people/contact paths for name+mailto (Wave5 L02 arm-04)."""
import csv
import json
import re
import ssl
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "input.csv"
EVIDENCE = ROOT / "evidence"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 MailFinder-W5-L02-arm04/1.0"
)

TEAM_PATHS = [
    "",
    "/team",
    "/team/",
    "/teams",
    "/teams/",
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
    "/contact",
    "/contact/",
    "/contact-us",
    "/contact-us/",
    "/Team",
    "/Team/",
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
    "media",
    "bookings",
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
    "ir",
}


def fetch(url: str, max_bytes: int = 500_000):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Upgrade-Insecure-Requests": "1",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=35, context=ctx) as r:
            body = r.read(max_bytes)
            return {
                "final_url": r.geturl(),
                "status": r.status,
                "html": body.decode("utf-8", errors="replace"),
                "error": None,
            }
    except Exception as e:
        err = str(e)
        if "403" in err:
            try:
                proc = subprocess.run(
                    [
                        "curl",
                        "-sS",
                        "-L",
                        "--max-time",
                        "35",
                        "-A",
                        UA,
                        "-w",
                        "\n__FINAL__%{url_effective}\n__CODE__%{http_code}",
                        url,
                    ],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                raw = proc.stdout or ""
                if "__FINAL__" in raw:
                    body, meta = raw.rsplit("\n__FINAL__", 1)
                    final_url = meta.split("\n__CODE__")[0].strip()
                    code_part = meta.split("\n__CODE__")[-1].strip()
                    status = int(code_part) if code_part.isdigit() else None
                    if status == 200 and body:
                        return {
                            "final_url": final_url or url,
                            "status": status,
                            "html": body[:500_000],
                            "error": None,
                        }
            except Exception:
                pass
        return {"final_url": url, "status": None, "html": "", "error": err}


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
        if "linkedin.com" in href.lower():
            continue
        if slug and slug in href.lower():
            found.add(urllib.parse.urljoin(base, href))
        if tokens and all(t.lower() in href.lower() for t in tokens[:2]):
            found.add(urllib.parse.urljoin(base, href))
    return list(found)[:10]


def person_path_guesses(origin: str, name: str):
    slug = slugify_name(name)
    if not slug:
        return []
    bases = ["/team/", "/teams/", "/people/", "/about/team/"]
    return [urllib.parse.urljoin(origin + "/", b + slug) for b in bases]


def scan_html(html: str, final_url: str, contact_name: str, domain: str):
    tokens = name_tokens(contact_name)
    hits = []
    base_dom = domain.replace("www.", "").lower()
    mailtos = re.findall(
        r"mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", html, flags=re.I
    )
    bare = re.findall(
        r"(?<![\w.])([a-zA-Z0-9._%+-]+@" + re.escape(base_dom) + r")(?![\w.])",
        html,
        flags=re.I,
    )
    candidates = list(dict.fromkeys(mailtos + bare))
    for email in candidates:
        local = email.split("@")[0].lower()
        if local in GENERIC_LOCAL:
            continue
        edomain = email.split("@")[1].lower()
        if base_dom not in edomain:
            continue
        for m in re.finditer(re.escape(email), html, flags=re.I):
            chunk = html[max(0, m.start() - 3000) : m.end() + 3000]
            chunk_text = re.sub(r"<[^>]+>", " ", chunk)
            chunk_text = re.sub(r"\s+", " ", chunk_text)
            if tokens and all(
                t.lower() in chunk_text.lower() for t in tokens[: min(2, len(tokens))]
            ):
                excerpt = chunk_text.strip()[:400]
                hits.append(
                    {"email": email, "source_url": final_url, "excerpt": excerpt}
                )
                break
    return hits


def crawl_row(row):
    website = row["Website"].strip()
    if not website.startswith("http"):
        website = "https://" + website
    parsed = urllib.parse.urlparse(website)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    domain = (row.get("Domain") or parsed.netloc).replace("www.", "")

    checked = []
    all_hits = []
    pages_html = {}
    contact_name = row.get("Contact_name") or row["Name"]

    seen = set()
    queue = []
    for p in TEAM_PATHS:
        u = urllib.parse.urljoin(origin + "/", p.lstrip("/") if p else "")
        if u not in seen:
            seen.add(u)
            queue.append(u)
    for u in person_path_guesses(origin, contact_name):
        if u not in seen:
            seen.add(u)
            queue.append(u)

    idx = 0
    while idx < len(queue) and len(queue) <= 40:
        url = queue[idx]
        idx += 1
        res = fetch(url)
        label = res["final_url"]
        if res["error"]:
            checked.append(f"{url} (ERROR: {res['error'][:120]})")
            continue
        checked.append(f"{label} ({res['status']})")
        html = res["html"]
        if html:
            pages_html[label] = html
            hits = scan_html(html, label, contact_name, domain)
            for h in hits:
                if h not in all_hits:
                    all_hits.append(h)
            for pu in discover_person_urls(label, html, contact_name):
                if pu not in seen:
                    seen.add(pu)
                    queue.append(pu)

    return {
        "Monday_item_id": row["Monday_item_id"],
        "Name": row["Name"],
        "Contact_name": contact_name,
        "Firm": row.get("Firm", ""),
        "Domain": domain,
        "Website": website,
        "Priority": row.get("Priority", ""),
        "checked_urls": checked,
        "hits": all_hits,
        "pages_fetched": list(pages_html.keys()),
    }


def main():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(INPUT.open()))
    out = [crawl_row(r) for r in rows]
    (ROOT / "scripts" / "crawl_results.json").write_text(
        json.dumps(out, indent=2), encoding="utf-8"
    )
    for item in out:
        print(
            json.dumps(
                {
                    "id": item["Monday_item_id"],
                    "name": item["Contact_name"],
                    "hits": item["hits"],
                    "n_checked": len(item["checked_urls"]),
                }
            ),
            flush=True,
        )


if __name__ == "__main__":
    main()
