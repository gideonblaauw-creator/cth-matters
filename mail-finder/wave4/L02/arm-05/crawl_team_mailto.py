#!/usr/bin/env python3
"""Crawl firm-site team paths for name + mailto co-occurrence (L02 Arm 05)."""
import csv
import json
import re
import ssl
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EVID = ROOT / "evidence"
INPUT = ROOT / "input.csv"
UA = "Mozilla/5.0 (compatible; MailFinder-L02-Arm05/1.0; +https://github.com/gideonblaauw-creator/cth-matters)"
PATHS = [
    "",
    "/team",
    "/team/",
    "/people",
    "/people/",
    "/about",
    "/about/",
    "/our-team",
    "/our-team/",
    "/leadership",
    "/leadership/",
    "/about-us",
    "/about-us/",
    "/equipo",
    "/equipo/",
]

GENERIC = {
    "info",
    "hello",
    "team",
    "contact",
    "contacto",
    "support",
    "general",
    "investors",
    "press",
    "careers",
    "hr",
    "admin",
    "office",
    "ventures",
    "partnerships",
}

ctx = ssl.create_default_context()


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            body = r.read(500000)
            return {
                "final": r.geturl(),
                "status": r.status,
                "html": body.decode("utf-8", errors="replace"),
                "error": None,
            }
    except Exception as e:
        return {"final": url, "status": None, "html": "", "error": str(e)}


def base_urls(website: str):
    w = website.strip().rstrip("/")
    if not w.startswith("http"):
        w = "https://" + w
    parsed = urllib.parse.urlparse(w)
    bases = {w}
    if parsed.netloc.startswith("www."):
        bases.add(f"{parsed.scheme}://{parsed.netloc[4:]}{parsed.path or ''}".rstrip("/"))
    else:
        bases.add(f"{parsed.scheme}://www.{parsed.netloc}{parsed.path or ''}".rstrip("/"))
    return list(bases)


def name_tokens(name: str):
    name = re.sub(r"^(Dr\.|Mr\.|Mrs\.|Ms\.)\s+", "", name, flags=re.I)
    name = re.sub(r",.*$", "", name)
    return [p for p in re.split(r"\s+", name.strip()) if len(p) > 1]


def is_generic(email: str) -> bool:
    local = email.split("@")[0].lower()
    return local in GENERIC


def scan_name_mailto(html: str, name: str, domain: str):
    tokens = name_tokens(name)
    need = tokens if len(tokens) < 2 else tokens[:2]
    hits = []
    mailtos = re.findall(
        r"mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", html, flags=re.I
    )
    for email in set(mailtos):
        email = urllib.parse.unquote(email)
        if is_generic(email):
            continue
        edom = email.split("@")[1].lower()
        if domain.lower() not in edom and not edom.endswith("." + domain.lower()):
            continue
        for m in re.finditer(re.escape(email), html, flags=re.I):
            chunk = html[max(0, m.start() - 3000) : m.end() + 3000]
            chunk_text = re.sub(r"<[^>]+>", " ", chunk)
            low = chunk_text.lower()
            if all(t.lower() in low for t in need):
                hits.append(email)
                break
    return list(dict.fromkeys(hits))


def main():
    EVID.mkdir(parents=True, exist_ok=True)
    results = {}
    for row in csv.DictReader(INPUT.open()):
        mid = row["Monday_item_id"]
        name = row["Name"]
        domain = row["Domain"]
        website = row["Website"]
        checked = []
        all_hits = []
        saved = []
        for base in base_urls(website):
            for p in PATHS:
                url = (base + p) if p else base + "/"
                res = fetch(url)
                label = (
                    res["final"]
                    if not res["error"]
                    else f"{url} (ERROR: {res['error'][:80]})"
                )
                checked.append(label)
                if res["error"] or not res["html"]:
                    continue
                if "mailto:" in res["html"].lower():
                    slug = re.sub(r"[^a-z0-9]+", "-", domain + p)[:80]
                    fn = EVID / f"{mid}_{slug}.html"
                    fn.write_text(res["html"][:400000])
                    saved.append(fn.name)
                for h in scan_name_mailto(res["html"], name, domain):
                    all_hits.append({"email": h, "source": res["final"]})
        seen = {}
        for h in all_hits:
            seen.setdefault(h["email"], h["source"])
        results[mid] = {
            "name": name,
            "domain": domain,
            "checked": checked,
            "hits": [{"email": e, "source": s} for e, s in seen.items()],
            "saved": saved,
        }
    (ROOT / "crawl_scan.json").write_text(json.dumps(results, indent=2))
    print(json.dumps({k: v["hits"] for k, v in results.items()}, indent=2))


if __name__ == "__main__":
    main()
