#!/usr/bin/env python3
"""One targeted Wayback CDX pass per seat on /team, /about, or /people."""
import csv
import json
import re
import urllib.parse
import urllib.request
from html import unescape
from pathlib import Path

UA = "MailFinderResearch/1.0 (cth-matters; L08-arm08) contact@example.com"
ROOT = Path(__file__).resolve().parent.parent
EV = ROOT / "evidence"

# path choice per domain (single CDX target per seat)
PATH_BY_DOMAIN = {
    "acumen.org": "/team",
}

GENERIC_LOCAL = {
    "info", "contact", "hello", "support", "team", "careers", "jobs", "press",
    "media", "ir", "investor", "investors", "admin", "office", "mail", "enquiries",
    "inquiries", "hr", "marketing", "sales", "privacy", "legal", "noreply", "no-reply",
}


def fetch(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def strip_tags(html: str) -> str:
    html = re.sub(r"(?is)<script.*?>.*?</script>", " ", html)
    html = re.sub(r"(?is)<style.*?>.*?</style>", " ", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    return unescape(re.sub(r"\s+", " ", text))


def name_variants(full: str) -> list[str]:
    full = full.strip()
    variants = {full}
    no_dr = re.sub(r"^Dr\.?\s+", "", full, flags=re.I).strip()
    variants.add(no_dr)
    parts = no_dr.split()
    if len(parts) >= 2:
        variants.add(f"{parts[0]} {parts[-1]}")
        variants.add(parts[0])
        variants.add(parts[-1])
    return [v for v in variants if len(v) >= 3]


def is_person_email(email: str, domain: str) -> bool:
    email = email.lower().strip()
    if "@" not in email:
        return False
    local, _, dom = email.partition("@")
    dom = dom.lower()
    base = domain.lower().removeprefix("www.")
    if not (dom == base or dom.endswith("." + base)):
        return False
    local = local.split("?")[0]
    if local in GENERIC_LOCAL:
        return False
    return True


def emails_in_html(html: str, domain: str) -> list[str]:
    found = set()
    for m in re.finditer(r"mailto:([^\s\"'<>?]+)", html, re.I):
        found.add(unescape(m.group(1)))
    for m in re.finditer(r"[\w.+-]+@" + re.escape(domain) + r"\b", html, re.I):
        found.add(m.group(0))
    return [e for e in found if is_person_email(e, domain)]


def name_on_page(html: str, variants: list[str]) -> bool:
    text = strip_tags(html).lower()
    html_low = html.lower()
    for v in variants:
        vl = v.lower()
        if vl in text or vl in html_low:
            return True
    return False


def email_near_name(html: str, variants: list[str], emails: list[str], domain: str) -> str | None:
    if not emails:
        return None
    # block-level chunks
    chunks = re.split(
        r"(?is)(<(?:div|section|article|li|tr|p|h[1-6])[\s>])",
        html,
    )
    for i in range(0, len(chunks), 2):
        block = chunks[i] + (chunks[i + 1] if i + 1 < len(chunks) else "")
        if not name_on_page(block, variants):
            continue
        block_emails = emails_in_html(block, domain)
        for em in block_emails:
            if em in emails:
                return em
    if name_on_page(html, variants) and len(emails) == 1:
        return emails[0]
    return None


def cdx_lookup(domain: str, path: str) -> tuple[str, list]:
    # one CDX query: exact path prefix only (no domain-wide crawl)
    target = f"{domain}{path}"
    q = urllib.parse.urlencode(
        {
            "url": target,
            "matchType": "prefix",
            "output": "json",
            "filter": "statuscode:200",
            "collapse": "urlkey",
            "limit": "500",
        }
    )
    cdx_api = f"https://web.archive.org/cdx/search/cdx?{q}"
    raw = fetch(cdx_api).decode("utf-8", errors="replace")
    EV.joinpath(f"cdx-{domain.replace('.', '_')}.json").write_text(raw)
    data = json.loads(raw) if raw.strip() else []
    if not data:
        return cdx_api, []
    header, *rows = data
    return cdx_api, [dict(zip(header, row)) for row in rows]


def domain_from_website(url: str) -> str:
    p = urllib.parse.urlparse(url if "://" in url else "https://" + url)
    host = p.netloc or p.path
    return host.lower().removeprefix("www.")


def url_name_score(url: str, name: str) -> int:
    path = urllib.parse.urlparse(url).path.lower()
    no_dr = re.sub(r"^dr\.?\s+", "", name, flags=re.I).strip().lower()
    tokens = [t for t in re.split(r"\s+", no_dr) if len(t) >= 3]
    score = 0
    for t in tokens:
        t_slug = t.replace(".", "")
        if t_slug in path.replace("-", "").replace("_", ""):
            score += 3
        if t_slug in path:
            score += 2
    # hyphenated slug e.g. eduardo-campos
    if len(tokens) >= 2:
        slug = f"{tokens[0]}-{tokens[-1]}"
        if slug in path:
            score += 5
    if re.search(r"/team/?$", path) or path.endswith("/about") or path.endswith("/people"):
        score += 1
    return score


def pick_snapshot(rows: list, name: str) -> dict | None:
    if not rows:
        return None
    latest: dict[str, dict] = {}
    for r in rows:
        url = r.get("original", "")
        if not url:
            continue
        if url not in latest or r.get("timestamp", "") > latest[url].get("timestamp", ""):
            latest[url] = r
    candidates = list(latest.values())
    return max(
        candidates,
        key=lambda r: (
            url_name_score(r.get("original", ""), name),
            r.get("timestamp", ""),
        ),
    )


def excerpt(html: str, email: str, variants: list[str]) -> str:
    text = strip_tags(html)
    idx = text.lower().find(email.lower())
    if idx < 0:
        for v in variants:
            idx = text.lower().find(v.lower())
            if idx >= 0:
                break
    start = max(0, idx - 120)
    end = min(len(text), idx + 180)
    snip = text[start:end].strip()
    return snip[:400]


def process_row(row: dict) -> dict:
    item_id = row["item_id"]
    name = row["contact_name"]
    firm = row.get("firm", "")
    website = row["website"]
    domain = domain_from_website(website)
    path = PATH_BY_DOMAIN.get(domain, "/team")
    variants = name_variants(name)

    cdx_api, rows = cdx_lookup(domain, path)
    snap = pick_snapshot(rows, name)
    checked = [cdx_api]

    if not snap:
        return {
            "Monday_item_id": item_id,
            "Name": name,
            "Firm": firm,
            "Domain": domain,
            "Priority": row.get("priority", ""),
            "Email": "",
            "Email_type": "",
            "Confidence": "",
            "Source_URL": "",
            "Checked_URLs": " | ".join(checked),
            "Status": "EMPTY",
            "Notes": f"No Wayback CDX captures (HTTP 200) for {domain}{path} prefix.",
            "Method": "wave4_L08_arm08_wayback_cdx_team_about_people",
        }

    orig = snap.get("original") or f"https://{domain}{path}"
    ts = snap["timestamp"]
    wayback = f"https://web.archive.org/web/{ts}/{orig}"
    checked.append(wayback)

    raw_url = f"https://web.archive.org/web/{ts}id_/{orig}"
    checked.append(raw_url)
    try:
        html = fetch(raw_url).decode("utf-8", errors="replace")
    except Exception:
        try:
            html = fetch(wayback).decode("utf-8", errors="replace")
        except Exception as e:
            return {
                "Monday_item_id": item_id,
                "Name": name,
                "Firm": firm,
                "Domain": domain,
                "Priority": row.get("priority", ""),
                "Email": "",
                "Email_type": "",
                "Confidence": "",
                "Source_URL": "",
                "Checked_URLs": " | ".join(checked),
                "Status": "EMPTY",
                "Notes": f"CDX had captures for {domain}{path} but Wayback fetch failed: {e}",
                "Method": "wave4_L08_arm08_wayback_cdx_team_about_people",
            }

    slug = f"{item_id}-{re.sub(r'[^a-z0-9]+', '-', name.lower())[:40]}"
    EV.joinpath(f"wayback-{slug}.html").write_text(html[:500_000])

    emails = emails_in_html(html, domain)
    if not name_on_page(html, variants):
        note = (
            f"Wayback snapshot {ts} for {orig}: page archived but target name "
            f"({name}) not present; {len(emails)} person-domain emails seen."
        )
        return {
            "Monday_item_id": item_id,
            "Name": name,
            "Firm": firm,
            "Domain": domain,
            "Priority": row.get("priority", ""),
            "Email": "",
            "Email_type": "",
            "Confidence": "",
            "Source_URL": "",
            "Checked_URLs": " | ".join(checked),
            "Status": "EMPTY",
            "Notes": note,
            "Method": "wave4_L08_arm08_wayback_cdx_team_about_people",
        }

    hit = email_near_name(html, variants, emails, domain)
    if not hit:
        note = (
            f"Wayback {ts}: {name} on page but no co-located person@{domain} mailto/text "
            f"(emails found: {', '.join(emails) or 'none'})."
        )
        return {
            "Monday_item_id": item_id,
            "Name": name,
            "Firm": firm,
            "Domain": domain,
            "Priority": row.get("priority", ""),
            "Email": "",
            "Email_type": "",
            "Confidence": "",
            "Source_URL": "",
            "Checked_URLs": " | ".join(checked),
            "Status": "EMPTY",
            "Notes": note,
            "Method": "wave4_L08_arm08_wayback_cdx_team_about_people",
        }

    ex = excerpt(html, hit, variants)
    return {
        "Monday_item_id": item_id,
        "Name": name,
        "Firm": firm,
        "Domain": domain,
        "Priority": row.get("priority", ""),
        "Email": hit,
        "Email_type": "personal",
        "Confidence": "high",
        "Source_URL": wayback,
        "Checked_URLs": " | ".join(checked),
        "Status": "FOUND",
        "Notes": f"Name + {hit} co-occur on archived {path} page ({ts}).",
        "Method": "wave4_L08_arm08_wayback_cdx_team_about_people",
        "Evidence_excerpt": ex,
    }


def main():
    with (ROOT / "input.csv").open() as f:
        rows = list(csv.DictReader(f))
    results = [process_row(r) for r in rows]
    fields = [
        "Monday_item_id", "Name", "Firm", "Domain", "Priority",
        "Email", "Email_type", "Confidence", "Source_URL", "Checked_URLs",
        "Status", "Notes", "Method",
    ]
    with (ROOT / "results.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(results)

    stamps = [
        {
            "Monday_item_id": r["Monday_item_id"],
            "Email": r["Email"],
            "Source_URL": r["Source_URL"],
            "Evidence_excerpt": r.get("Evidence_excerpt", ""),
        }
        for r in results
        if r["Status"] == "FOUND"
    ]
    (ROOT / "stamp-list.json").write_text(json.dumps(stamps, indent=2) + "\n")
    print(json.dumps({"found": len(stamps), "total": len(results)}, indent=2))
    for r in results:
        print(r["Monday_item_id"], r["Status"], r.get("Email") or "-", r["Notes"][:100])


if __name__ == "__main__":
    main()
