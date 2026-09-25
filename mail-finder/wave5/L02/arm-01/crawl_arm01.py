#!/usr/bin/env python3
"""Wave5 L02 arm-01 — first-party team/about/people/contact mailto (public HTTP only)."""
from __future__ import annotations

import csv
import html as html_lib
import json
import re
import ssl
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT / "evidence"
INPUT_CSV = ROOT / "input.csv"
RESULTS_CSV = ROOT / "results.csv"
STAMP_JSON = ROOT / "stamp-list.json"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
CTX = ssl.create_default_context()
METHOD = "wave5-L02-arm01-first-party-team"

PATH_SUFFIXES = (
    "",
    "/team",
    "/people",
    "/about",
    "/about-us",
    "/our-team",
    "/leadership",
    "/contact",
    "/contact-us",
)

GENERIC_LOCAL = frozenset(
    {
        "info",
        "hello",
        "team",
        "contact",
        "contacto",
        "ventures",
        "support",
        "sales",
        "admin",
        "office",
        "secretary",
        "press",
        "media",
        "bookings",
        "infocolombia",
        "soporte",
        "servicioalcliente",
        "investors",
        "investor",
    }
)

EXTRA_PATHS: dict[str, list[str]] = {
    "clicoh.com": ["/sobre-clicoh", "/enviar-con-clicoh", "/blog", "/en"],
    "saviaventures.com": ["/privacy-policy/", "/privacy-policy"],
    "dibanka.co": [
        "/sobre-dibanka/",
        "/web/sobre-dibanka/",
        "/linea-etica-dibanka/",
        "/comunicado-publico/",
    ],
    "angelventures.vc": ["/portfolio", "/avnetwork", "/innovation", "/usfund"],
    "epicangelnetwork.com": ["/team"],
}

SEAT_NOTES: dict[str, str] = {
    "13028370683": (
        "Bryony Parker on homepage team roster (Dealflow & Portfolio); no mailto on page. "
        "Privacy policy lists contacto@ / contact@saviaventures.com (generic — not stamped)."
    ),
    "13028358405": (
        "Crawled home (/en redirect), sobre-clicoh, enviar-con-clicoh, blog, and standard "
        "team/about paths: no @clicoh.com in HTML; Camilo Arango not listed."
    ),
    "13100506379": (
        "Camilo Kejner on /team (Managing Partner) with LinkedIn link only; site-wide "
        "mailto infocolombia@angelventures.vc (generic regional inbox — not co-attributed)."
    ),
    "13028336730": (
        "sobre-dibanka and standard team/about/contact paths: no Carlos Iván Vargas Perdomo "
        "in page source; no person@dibanka.co mailto on first-party pages crawled."
    ),
    "13028371786": (
        "Home and /team (Softr): generic mailto info@epicangelnetwork.com only; "
        "Carolina Ocampo-Maya not present in HTML source."
    ),
}

MAILTO_RE = re.compile(
    r'mailto:([a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,})',
    re.I,
)


def fetch(url: str, timeout: int = 25) -> tuple[int | None, str, str]:
    req = urllib.request.Request(
        url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9,es;q=0.8"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return resp.status, resp.geturl(), body
    except urllib.error.HTTPError as exc:
        return exc.code, url, exc.read().decode("utf-8", errors="replace")
    except Exception as exc:  # noqa: BLE001
        return None, url, str(exc)


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
        u = u.split("#")[0].rstrip("/") or u
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


def name_tokens(name: str) -> list[str]:
    n = re.sub(r"[^\w\s'-]", " ", name, flags=re.UNICODE)
    parts = [
        p
        for p in n.split()
        if len(p) > 2
        and p.lower()
        not in ("mba", "dr", "eng", "and", "the", "von", "de", "del", "la", "ivan")
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


def domain_matches(email: str, domain: str) -> bool:
    host = email.split("@", 1)[1].lower()
    d = domain.lower().removeprefix("www.")
    return host == d or host.endswith("." + d)


def is_person_email(email: str, domain: str) -> bool:
    local = email.split("@", 1)[0].lower()
    if not domain_matches(email, domain):
        return False
    if local in GENERIC_LOCAL:
        return False
    for g in GENERIC_LOCAL:
        if local.startswith(g + ".") or local.endswith("." + g):
            return False
    return True


def excerpt_for(html: str, contact: str, email: str, window: int = 500) -> str | None:
    html_l = html.lower()
    email_l = email.lower()
    pos = 0
    while True:
        idx = html_l.find(email_l, pos)
        if idx == -1:
            break
        chunk = html[max(0, idx - window) : min(len(html), idx + len(email) + window)]
        if name_in_text(contact, chunk):
            return re.sub(r"\s+", " ", html_lib.unescape(chunk)).strip()[:500]
        pos = idx + 1
    return None


def crawl_seat(row: dict) -> dict:
    domain = row["Domain"].strip()
    website = row["Website"].strip()
    contact = row["Contact_name"].strip()
    mid = row["Monday_item_id"].strip()
    checked: list[str] = []
    best: tuple[str, str, str] | None = None

    for url in candidate_urls(website, domain):
        code, final, html = fetch(url)
        label = f"{url} ({code if code is not None else 'ERR'})"
        if final and final != url:
            label = f"{url} -> {final} ({code if code is not None else 'ERR'})"
        checked.append(label)
        if code is None or code >= 400 or not html or html.startswith("HTTP"):
            continue
        if len(html) > 500:
            slug = re.sub(r"[^a-z0-9]+", "-", urlparse(final).path.strip("/") or "home")
            snap = EVIDENCE / f"{domain.replace('.', '_')}_{slug[:40]}.html"
            if not snap.exists():
                snap.write_text(html[:800_000], encoding="utf-8")
        for email in sorted(set(m.split("?")[0].lower() for m in MAILTO_RE.findall(html))):
            if not is_person_email(email, domain):
                continue
            ex = excerpt_for(html, contact, email)
            if ex:
                best = (email, final, ex)
                break
        if best:
            break

    status = "FOUND" if best else "EMPTY"
    notes = "" if best else SEAT_NOTES.get(mid, "No person mailto co-occurring with Contact_name on crawled pages.")

    return {
        **{k: row.get(k, "") for k in row if k not in ("Status", "LinkedIn", "Owner")},
        "Email": best[0] if best else "",
        "Source_URL": best[1] if best else "",
        "Checked_URLs": " | ".join(checked),
        "Status": status,
        "Notes": notes,
        "Method": METHOD,
        "_excerpt": best[2] if best else "",
    }


def main() -> None:
    EVIDENCE.mkdir(exist_ok=True)
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

    stamps: list[dict] = []
    for r in results:
        if r["Status"] != "FOUND":
            continue
        stamps.append(
            {
                "monday_item_id": r["Monday_item_id"],
                "email": r["Email"],
                "source_url": r["Source_URL"],
                "excerpt": r["_excerpt"],
            }
        )
        slug = re.sub(r"[^a-z0-9]+", "-", r["Contact_name"].lower()).strip("-")
        (EVIDENCE / f"{slug}-excerpt.md").write_text(
            f"# {r['Contact_name']}\n\n**Source:** {r['Source_URL']}\n\n**Excerpt:**\n\n{r['_excerpt']}\n",
            encoding="utf-8",
        )

    STAMP_JSON.write_text(json.dumps(stamps, indent=2) + "\n", encoding="utf-8")
    found = sum(1 for r in results if r["Status"] == "FOUND")
    print(f"Wrote {RESULTS_CSV}: {len(results)} rows, {found} FOUND")


if __name__ == "__main__":
    main()
