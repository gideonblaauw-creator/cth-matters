#!/usr/bin/env python3
"""MF LI enrich-26 Arm A — first-party team/about/people/contact mailto (page-source only)."""
from __future__ import annotations

import csv
import html as html_lib
import json
import re
import ssl
import subprocess
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "input.csv"
EVIDENCE = ROOT / "evidence"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 MailFinder-LI-enrich-26-armA/1.0"
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
    "/contact",
    "/contact/",
    "/contact-us",
    "/contact-us/",
    "/Team",
    "/Team/",
    "/who-we-are",
    "/who-we-are/",
]

EXTRA_PATHS: dict[str, list[str]] = {
    "impacta.vc": ["/en/team", "/es/team", "/equipo"],
    "impact-partners.com": ["/en/team", "/fr/equipe"],
    "bii.co.uk": ["/about-bii/our-people", "/about-bii/leadership-team"],
    "iixglobal.com": ["/about-us/team", "/team-members"],
    "climate-kic.org": ["/about/team", "/people"],
    "anthosam.com": ["/about-us/team", "/team/"],
    "globalsocialimpact.es": ["/equipo", "/en/team"],
    "genesisarg.com": ["/equipo", "/team"],
    "dolmaimpact.com": ["/team", "/about"],
    "climatefocus.com": ["/about/team", "/team"],
    "deetkenimpact.com": ["/team", "/about-us"],
    "beyondimpact.vc": ["/team", "/about"],
    "oryximpact.com": ["/team", "/about"],
    "pangaeaimpact.com": ["/team", "/about"],
    "barakaimpact.com": ["/team", "/about"],
    "impactscience.vc": ["/team", "/about"],
    "impactshakers.com": ["/team", "/about"],
    "climatecapital.co": ["/team", "/about"],
    "j-impact.fund": ["/team", "/about"],
    "crossborder.ventures": ["/team", "/about"],
    "springimpactcapital.com": ["/team", "/about"],
    "impactassetscapital.com": ["/team", "/about"],
}

GENERIC_LOCAL = {
    "info",
    "hello",
    "invest",
    "team",
    "contact",
    "contacto",
    "support",
    "general",
    "investors",
    "investor",
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
    "communications",
    "reception",
    "secretary",
}


def fetch(url: str, max_bytes: int = 400_000):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=18, context=ctx) as r:
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
                        "18",
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
                            "html": body[:400_000],
                            "error": None,
                        }
            except Exception:
                pass
        return {"final_url": url, "status": None, "html": "", "error": err[:160]}


def name_tokens(name: str):
    name = re.sub(r"^(Dr\.|Mr\.|Mrs\.|Ms\.)\s+", "", name, flags=re.I)
    name = re.sub(r"\([^)]+\)", " ", name)
    name = re.sub(r",.*$", "", name)
    skip = {"mba", "cfa", "phd", "and", "the", "von", "de", "del", "la", "van"}
    return [
        p
        for p in re.split(r"[\s.]+", name.strip())
        if len(p) > 1 and p.lower() not in skip
    ]


def slugify_name(name: str):
    name = re.sub(r"\([^)]+\)", " ", name)
    name = re.sub(r",.*$", "", name).strip().lower()
    return re.sub(r"[^a-z0-9]+", "-", name).strip("-")


def domain_urls(domain: str) -> list[str]:
    origin = f"https://{domain}"
    seen: set[str] = set()
    out: list[str] = []

    def add(u: str) -> None:
        if u not in seen:
            seen.add(u)
            out.append(u)

    for p in TEAM_PATHS:
        add(urllib.parse.urljoin(origin + "/", p.lstrip("/") if p else ""))
    for extra in EXTRA_PATHS.get(domain, []):
        add(urllib.parse.urljoin(origin + "/", extra.lstrip("/")))
    return out


def person_urls(domain: str, name: str) -> list[str]:
    origin = f"https://{domain}"
    slug = slugify_name(name)
    if not slug:
        return []
    bases = ["/team/", "/teams/", "/people/", "/about/team/", "/team-members/"]
    return [urllib.parse.urljoin(origin + "/", b + slug) for b in bases]


def linkedin_only_near_name(html: str, contact_name: str) -> bool:
    tokens = name_tokens(contact_name)
    if not tokens:
        return False
    html_l = html.lower()
    for m in re.finditer(re.escape(tokens[0].lower()), html_l):
        chunk = html[max(0, m.start() - 2500) : m.end() + 2500]
        if len(tokens) >= 2 and tokens[-1].lower() not in chunk.lower():
            continue
        chunk_l = chunk.lower()
        if "linkedin.com" in chunk_l and "mailto:" not in chunk_l:
            if not re.search(r"[\w.+-]+@" + re.escape(tokens[0].lower()), chunk_l):
                return True
    return False


def email_local_matches_person(local: str, tokens: list[str]) -> bool:
    local = local.lower().replace(".", "").replace("_", "")
    for t in tokens:
        tl = t.lower()
        if len(tl) >= 4 and tl in local:
            return True
        if len(tl) >= 3 and local.startswith(tl[0]) and tl in local:
            return True
    if len(tokens) >= 2:
        first, last = tokens[0].lower(), tokens[-1].lower()
        if len(last) >= 4 and last in local:
            return True
        if local.startswith(first[0]) and last[:4] in local:
            return True
    return False


def scan_html(html: str, final_url: str, contact_name: str, domain: str):
    html = html_lib.unescape(html)
    tokens = name_tokens(contact_name)
    hits = []
    base_dom = domain.replace("www.", "").lower()
    mailtos = re.findall(
        r"mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", html, flags=re.I
    )
    mailtos += re.findall(
        r'href=["\']mailto:([^"\']+)["\']', html, flags=re.I
    )
    mailtos = [html_lib.unescape(m.split("?")[0].strip()) for m in mailtos]
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
        if tokens and not email_local_matches_person(local, tokens):
            continue
        edomain = email.split("@")[1].lower()
        if base_dom not in edomain:
            continue
        for m in re.finditer(re.escape(email), html, flags=re.I):
            chunk = html[max(0, m.start() - 1200) : m.end() + 1200]
            chunk_text = re.sub(r"<[^>]+>", " ", chunk)
            chunk_text = re.sub(r"\s+", " ", chunk_text)
            if tokens and all(
                t.lower() in chunk_text.lower() for t in tokens[: min(2, len(tokens))]
            ):
                hits.append(
                    {
                        "email": email,
                        "source_url": final_url,
                        "excerpt": chunk_text.strip()[:500],
                    }
                )
                break
    return hits


def pick_best_hit(hits: list[dict], contact_name: str) -> dict | None:
    if not hits:
        return None
    slug = slugify_name(contact_name)

    def score(h: dict) -> tuple[int, int]:
        url = h["source_url"].lower()
        person_page = 2 if slug and slug in url else 0
        mailto = 1 if "mailto" in h.get("excerpt", "").lower() else 0
        return (person_page, mailto)

    return sorted(hits, key=score, reverse=True)[0]


def crawl_domain(domain: str) -> tuple[str, dict[str, tuple], list[str]]:
    """Returns domain, pages{url: (status, html)}, checked labels."""
    pages: dict[str, tuple[int | None, str]] = {}
    checked: list[str] = []
    urls = domain_urls(domain)

    def one(url: str):
        res = fetch(url)
        return url, res

    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(one, u): u for u in urls}
        for fut in as_completed(futs):
            url, res = fut.result()
            if res["error"]:
                checked.append(f"{url} (ERROR: {res['error']})")
            else:
                checked.append(f"{res['final_url']} ({res['status']})")
                if res["html"]:
                    pages[res["final_url"]] = (res["status"], res["html"])
    return domain, pages, checked


def crawl_row(row, domain_pages: dict, domain_checked: list[str]) -> dict:
    domain = row["Domain"].strip().replace("www.", "")
    contact_name = row.get("Contact_name") or row["Name"]
    pages = domain_pages.get(domain, {})
    checked = list(domain_checked.get(domain, []))

    extra_checked: list[str] = []
    all_pages = dict(pages)
    for url in person_urls(domain, contact_name):
        res = fetch(url)
        if res["error"]:
            extra_checked.append(f"{url} (ERROR: {res['error']})")
        else:
            extra_checked.append(f"{res['final_url']} ({res['status']})")
            if res["html"]:
                all_pages[res["final_url"]] = (res["status"], res["html"])

    checked = checked + extra_checked
    all_hits = []
    linkedin_only = False
    for final_url, (_status, html) in all_pages.items():
        for h in scan_html(html, final_url, contact_name, domain):
            if h not in all_hits:
                all_hits.append(h)
        if not all_hits and linkedin_only_near_name(html, contact_name):
            linkedin_only = True

    best = pick_best_hit(all_hits, contact_name)
    if best:
        all_hits = [best]

    return {
        "Monday_item_id": row["Monday_item_id"],
        "Name": row["Name"],
        "Contact_name": contact_name,
        "Firm": row.get("Firm", ""),
        "Domain": domain,
        "Priority": row.get("Priority", ""),
        "checked_urls": checked,
        "hits": all_hits,
        "linkedin_only_signal": linkedin_only and not all_hits,
    }


def main():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(INPUT.open()))
    domains = sorted({r["Domain"].strip().replace("www.", "") for r in rows})

    domain_pages: dict[str, dict] = {}
    domain_checked: dict[str, list] = {}
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(crawl_domain, d): d for d in domains}
        for fut in as_completed(futs):
            dom, pages, checked = fut.result()
            domain_pages[dom] = pages
            domain_checked[dom] = checked
            print(f"domain_done {dom} pages={len(pages)}", flush=True)

    out = [crawl_row(r, domain_pages, domain_checked) for r in rows]
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
                    "uncertain": item.get("linkedin_only_signal"),
                }
            ),
            flush=True,
        )


if __name__ == "__main__":
    main()
