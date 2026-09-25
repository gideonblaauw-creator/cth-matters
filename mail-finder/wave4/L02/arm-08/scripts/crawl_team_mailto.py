#!/usr/bin/env python3
"""L02 Arm 08: first-party team/people mailto + name co-occurrence crawl."""
import csv
import json
import re
import ssl
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "input.csv"
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 MailFinder-L02-arm08/1.0"
)
TIMEOUT = 30

PATH_SEEDS = [
    "/team",
    "/people",
    "/about",
    "/about-us",
    "/our-team",
    "/leadership",
    "/equipe",
    "/equipo",
    "/en/team",
    "/contact",
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
    "sales",
    "marketing",
    "media",
    "privacy",
    "legal",
    "ventures",
    "investorrelations",
    "ir",
    "noreply",
    "no-reply",
}

MAILTO_RE = re.compile(
    r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', re.I
)


def fetch(url: str) -> tuple[str, int, str]:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*"}
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
            body = r.read(500_000).decode("utf-8", errors="replace")
            return r.geturl(), r.status, body
    except Exception as e:
        return url, 0, f"ERROR: {e}"


def name_tokens(name: str) -> list[str]:
    name = re.sub(r"^(Dr\.|Mr\.|Mrs\.|Ms\.)\s+", "", name, flags=re.I)
    name = re.sub(r",.*$", "", name)
    # strip parenthetical firm names
    name = re.sub(r"\([^)]*\)", "", name).strip()
    parts = [p for p in re.split(r"\s+", name) if len(p) > 2]
    return parts


def is_generic(email: str) -> bool:
    local = email.split("@")[0].lower()
    if local in GENERIC_LOCAL:
        return True
    for g in GENERIC_LOCAL:
        if local.startswith(g + ".") or local.endswith("." + g):
            return True
    return False


def name_in_chunk(chunk: str, tokens: list[str]) -> bool:
    if not tokens:
        return False
    chunk_l = re.sub(r"<[^>]+>", " ", chunk).lower()
    # require at least first + last (or single distinctive token if only one)
    if len(tokens) >= 2:
        return tokens[0].lower() in chunk_l and tokens[-1].lower() in chunk_l
    return tokens[0].lower() in chunk_l


def scan_page(html: str, name: str, domain: str) -> list[dict]:
    if html.startswith("ERROR"):
        return []
    tokens = name_tokens(name)
    hits = []
    seen = set()
    for email in MAILTO_RE.findall(html):
        email = email.split("?")[0]
        el = email.lower()
        if el in seen:
            continue
        seen.add(el)
        if is_generic(email):
            continue
        em_domain = email.split("@")[1].lower().removeprefix("www.")
        dom = domain.lower().removeprefix("www.")
        if not (em_domain == dom or em_domain.endswith("." + dom)):
            continue
        for m in re.finditer(re.escape(email), html, flags=re.I):
            chunk = html[max(0, m.start() - 3000) : m.end() + 3000]
            if name_in_chunk(chunk, tokens):
                hits.append({"email": email, "evidence_chunk": chunk[:8000]})
                break
    return hits


def crawl_seat(website: str, domain: str, name: str) -> dict:
    parsed = urllib.parse.urlparse(website)
    base = f"{parsed.scheme}://{parsed.netloc}"
    urls = [website.rstrip("/") + "/" if not website.endswith("/") else website]
    for path in PATH_SEEDS:
        urls.append(urllib.parse.urljoin(base + "/", path.lstrip("/")))
    # dedupe preserve order
    seen_u = set()
    ordered = []
    for u in urls:
        if u not in seen_u:
            seen_u.add(u)
            ordered.append(u)

    checked = []
    all_hits = []
    pages_html = {}

    for url in ordered:
        final, status, html = fetch(url)
        label = final if status else f"{url} ({html})"
        checked.append(label)
        if status and not html.startswith("ERROR"):
            pages_html[final] = html
            hits = scan_page(html, name, domain)
            for h in hits:
                all_hits.append({**h, "source_url": final})

    # profile slug guess from name
    tokens = name_tokens(name)
    if len(tokens) >= 2:
        slugs = [
            f"{tokens[0].lower()}-{tokens[-1].lower()}",
            f"{tokens[0].lower()}{tokens[-1].lower()}",
            tokens[-1].lower(),
        ]
        for slug in slugs:
            for prefix in ("/team/", "/people/", "/about-us/", "/en/team/"):
                u = urllib.parse.urljoin(base + "/", prefix.lstrip("/") + slug)
                if u in seen_u:
                    continue
                seen_u.add(u)
                final, status, html = fetch(u)
                checked.append(final if status else f"{u} ({html})")
                if status and not html.startswith("ERROR"):
                    pages_html[final] = html
                    for h in scan_page(html, name, domain):
                        all_hits.append({**h, "source_url": final})

    # dedupe hits by email
    by_email = {}
    for h in all_hits:
        by_email[h["email"].lower()] = h

    return {
        "checked": checked,
        "hits": list(by_email.values()),
        "pages_fetched": list(pages_html.keys()),
    }


def main():
    results = {}
    for row in csv.DictReader(INPUT.open(encoding="utf-8")):
        mid = row["Monday_item_id"]
        results[mid] = {
            "name": row["Name"],
            "firm": row["Firm"],
            "domain": row["Domain"],
            "website": row["Website"],
            **crawl_seat(row["Website"], row["Domain"], row["Name"]),
        }
        print(
            json.dumps(
                {
                    "id": mid,
                    "name": row["Name"],
                    "hits": [h["email"] for h in results[mid]["hits"]],
                }
            ),
            flush=True,
        )

    out = ROOT / "scripts" / "crawl_results.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
