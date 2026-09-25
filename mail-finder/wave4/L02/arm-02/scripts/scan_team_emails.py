#!/usr/bin/env python3
"""First-party firm-site crawl: mailto + name co-occurrence (Wave4 L02 Arm 02)."""
from __future__ import annotations

import json
import re
import ssl
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
UA = (
    "MailFinder-Wave4-L02-Arm02/1.0 "
    "(Teclogi research; +https://github.com/gideonblaauw-creator/cth-matters)"
)
TIMEOUT = 30
CTX = ssl.create_default_context()

PATH_SEEDS = [
    "/",
    "/team",
    "/team/",
    "/people",
    "/about",
    "/about-us",
    "/our-team",
    "/leadership",
    "/equipo",
    "/nosotros",
]

GENERIC_LOCAL = (
    "info",
    "hello",
    "team",
    "contact",
    "support",
    "sales",
    "career",
    "careers",
    "jobs",
    "hr",
    "press",
    "media",
    "ir",
    "investor",
    "investors",
    "enquiries",
    "inquiries",
    "office",
    "admin",
    "reception",
    "impact",
    "projects",
    "partnerships",
    "infocolombia",
)

MAILTO_RE = re.compile(r"mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", re.I)
EMAIL_RE = re.compile(
    r"(?<![\w.-])([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?![\w.-])"
)


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=CTX) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return {
                "url": resp.geturl(),
                "status": resp.status,
                "bytes": len(body.encode("utf-8", errors="replace")),
                "body": body,
                "error": None,
            }
    except urllib.error.HTTPError as e:
        return {"url": url, "status": e.code, "bytes": 0, "body": "", "error": str(e)}
    except Exception as e:
        return {"url": url, "status": 0, "bytes": 0, "body": "", "error": str(e)}


def norm_host(domain: str) -> str:
    return domain.lower().removeprefix("www.")


def is_generic(email: str) -> bool:
    local = email.split("@", 1)[0].lower()
    return local in GENERIC_LOCAL or local.startswith(("info", "hello", "team", "contact"))


def name_tokens(name: str) -> list[str]:
    parts = re.split(r"\s+", name.strip())
    out: list[str] = []
    for p in parts:
        p = re.sub(r"[^\w]", "", p, flags=re.UNICODE)
        if len(p) >= 3:
            out.append(p.lower())
    return out


def name_on_page(name: str, html: str) -> bool:
    low = html.lower()
    toks = name_tokens(name)
    if not toks:
        return False
    if all(t in low for t in toks[:2]):
        return True
    return toks[0] in low


def emails_on_domain(html: str, domain: str) -> set[str]:
    dom = norm_host(domain)
    out: set[str] = set()
    for m in MAILTO_RE.findall(html):
        out.add(m.lower())
    for m in EMAIL_RE.findall(html):
        if norm_host(m.split("@", 1)[1]) == dom:
            out.add(m.lower())
    return out


def cooccurrence(name: str, html: str, domain: str, window: int = 1200) -> list[dict]:
    hits: list[dict] = []
    low = html.lower()
    for tok in name_tokens(name)[:2]:
        start = 0
        while True:
            idx = low.find(tok, start)
            if idx < 0:
                break
            chunk = html[max(0, idx - window) : idx + window]
            for em in emails_on_domain(chunk, domain):
                if not is_generic(em):
                    hits.append(
                        {
                            "email": em,
                            "name_token": tok,
                            "window_chars": window,
                        }
                    )
            start = idx + len(tok)
    # de-dupe
    seen: set[str] = set()
    uniq: list[dict] = []
    for h in hits:
        if h["email"] in seen:
            continue
        seen.add(h["email"])
        uniq.append(h)
    return uniq


def crawl_seat(
    seat: dict,
) -> dict:
    monday_id = seat["Monday_item_id"]
    name = seat["Name"]
    website = seat["Website"]
    domain = seat["Domain"]
    extra_paths = seat.get("extra_paths")
    base = website.rstrip("/")
    paths = list(PATH_SEEDS)
    if extra_paths:
        for p in extra_paths:
            if p not in paths:
                paths.append(p)

    checked: list[dict] = []
    person_hits: list[dict] = []
    generics: set[str] = set()

    for path in paths:
        url = base + path if path != "/" else base + "/"
        if path == "/" and not website.endswith("/"):
            url = website if website.endswith("/") else website + "/"
        res = fetch(url)
        entry = {
            "requested": url,
            "final": res["url"],
            "status": res["status"],
            "bytes": res["bytes"],
            "error": res["error"],
            "name_present": False,
            "emails": [],
            "person_cooccurrence": [],
        }
        if res["status"] == 200 and res["body"]:
            entry["name_present"] = name_on_page(name, res["body"])
            em = emails_on_domain(res["body"], domain)
            entry["emails"] = sorted(em)
            for e in em:
                if is_generic(e):
                    generics.add(e)
            person_hits.extend(cooccurrence(name, res["body"], domain))
            entry["person_cooccurrence"] = cooccurrence(name, res["body"], domain)
        checked.append(entry)

    return {
        "Monday_item_id": monday_id,
        "Name": name,
        "Website": website,
        "Domain": domain,
        "checked": checked,
        "generic_emails_seen": sorted(generics),
        "person_cooccurrence": person_hits,
    }


SEATS = [
    {
        "Monday_item_id": "13028350632",
        "Name": "Amaya Baliño Sanz",
        "Website": "https://www.angelventures.vc/",
        "Domain": "angelventures.vc",
        "extra_paths": [],
    },
    {
        "Monday_item_id": "13028365646",
        "Name": "Ana Lucía Rodhas Alcántara",
        "Website": "https://hyatt.com",
        "Domain": "hyatt.com",
        "extra_paths": [
            "/en-US/about/hyatt-leadership",
        ],
    },
    {
        "Monday_item_id": "13028358627",
        "Name": "Andrés Méndez",
        "Website": "https://colaborativo.io",
        "Domain": "colaborativo.io",
        "extra_paths": [],
    },
    {
        "Monday_item_id": "13028366958",
        "Name": "Nathalie Couët",
        "Website": "https://senecaimpact.earth/",
        "Domain": "senecaimpact.earth",
        "extra_paths": ["/about-us/the-team/"],
    },
]


def main() -> None:
    out = [crawl_seat(s) for s in SEATS]
    path = ROOT / "scripts" / "team_email_scan.json"
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
