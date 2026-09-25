#!/usr/bin/env python3
"""Wave3 Arm5: hygiene-gated first-party crawl (search-seed only)."""
from __future__ import annotations

import csv
import json
import re
import ssl
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 MailFinder-Wave3-Hygiene/1.0"
TIMEOUT = 25
ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
INPUT = ROOT / "input.csv"

# Monday domain → live crawl domain when Monday field is stale/NXDOMAIN/parked
LIVE_CRAWL_DOMAIN = {
    "13028403427": "psv.xyz",  # psvfoundry.com NXDOMAIN
    "13028359182": "checkmatecapital.net",  # checkmatecap.com → /lander parked
}

# Search-seed only: name + live domain when Monday domain differs
SEARCH_DOMAIN = {
    "13028403427": "psv.xyz",
}

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
FIRST_PARTY_PATHS = [
    "/",
    "/team",
    "/team/",
    "/our-team",
    "/our-team/",
    "/about",
    "/about-us",
    "/about-us/",
    "/people",
    "/contact",
    "/contact-us",
    "/leadership",
]

GENERIC_PREFIXES = (
    "info@",
    "hello@",
    "contact@",
    "investors@",
    "press@",
    "team@",
    "care@",
    "support@",
    "sales@",
    "privacy@",
    "legal@",
    "media@",
    "office@",
    "general@",
    "esg@",
    "service@",
    "user@",
)


def fetch(url: str, follow_redirect: bool = True) -> tuple[str | None, str | None, str | None]:
    """Returns (body, error, final_url)."""
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
            final = r.geturl()
            ct = r.headers.get("Content-Type", "")
            body = r.read(2_000_000)
            if "pdf" in ct.lower() or url.lower().endswith(".pdf"):
                return None, "pdf", final
            text = body.decode("utf-8", errors="replace")
            return text, None, final
    except Exception as e:
        return None, str(e)[:200], url


def decode_cfemail(encoded: str) -> str:
    try:
        r = int(encoded[:2], 16)
        return "".join(chr(int(encoded[i : i + 2], 16) ^ r) for i in range(2, len(encoded), 2))
    except Exception:
        return ""


def extract_emails(text: str) -> set[str]:
    if not text:
        return set()
    out = set()
    for m in EMAIL_RE.findall(text):
        m = m.lower().strip(".")
        if any(x in m for x in ("example.com", "sentry.io", "wixpress", "schema.org", "domain.com")):
            continue
        out.add(m)
    for enc in re.findall(r'data-cfemail="([a-f0-9]+)"', text, re.I):
        dec = decode_cfemail(enc)
        if "@" in dec:
            out.add(dec.lower())
    for enc in re.findall(r"/cdn-cgi/l/email-protection#([a-f0-9]+)", text, re.I):
        dec = decode_cfemail(enc)
        if "@" in dec:
            out.add(dec.lower())
    for m in re.findall(r'mailto:([^\s"\'<>?]+)', text, re.I):
        out.add(urllib.parse.unquote(m.split("?")[0]).lower())
    return out


def name_tokens(name: str) -> list[str]:
    parts = re.sub(r"[^a-zA-Z\s]", " ", name).lower().split()
    skip = {"dr", "mr", "ms", "mrs", "vc"}
    return [p for p in parts if p not in skip and len(p) > 1]


def name_near_email(text: str, name: str, email: str, window: int = 900) -> bool:
    if not text:
        return False
    tl = text.lower()
    email_l = email.lower()
    idx = tl.find(email_l)
    if idx < 0:
        return False
    chunk = tl[max(0, idx - window) : idx + window + len(email_l)]
    tokens = name_tokens(name)
    if len(tokens) >= 2:
        return tokens[0] in chunk and tokens[-1] in chunk
    return tokens[0] in chunk if tokens else False


def is_generic(email: str) -> bool:
    return any(email.startswith(p) for p in GENERIC_PREFIXES)


def email_on_domain(email: str, domain: str) -> bool:
    dom = domain.lower().strip()
    el = email.lower().split("@")[-1]
    return el == dom or el.endswith("." + dom) or dom.endswith(el.split(".")[-2] + "." + el.split(".")[-1])


def save_evidence(slug: str, url: str, text: str) -> Path:
    safe = re.sub(r"[^a-zA-Z0-9._-]", "_", slug)[:160]
    fp = EVIDENCE / f"{safe}.html"
    fp.write_text(f"<!-- source: {url} -->\n{text[:400_000]}", encoding="utf-8", errors="replace")
    return fp


def search_seed_urls(name: str, domain: str) -> list[str]:
    """Name + domain seed via DuckDuckGo HTML (first-party links only)."""
    q = urllib.parse.quote_plus(f'site:{domain} "{name}"')
    ddg = f"https://html.duckduckgo.com/html/?q={q}"
    text, err, _ = fetch(ddg)
    if not text:
        return [ddg]
    urls = []
    for m in re.findall(r'uddg=([^&"]+)', text):
        u = urllib.parse.unquote(m)
        if domain in u.lower():
            urls.append(u)
    return [ddg] + urls[:8]


def wayback_team(domain: str) -> list[str]:
    cdx = (
        "https://web.archive.org/cdx/search/cdx?"
        f"url={domain}/*&output=json&limit=40&filter=statuscode:200"
    )
    text, err, _ = fetch(cdx)
    if not text:
        return []
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return []
    out = []
    for row in data[1:]:
        orig = row[2] if len(row) > 2 else ""
        ol = orig.lower()
        if any(p in ol for p in ("/team", "/about", "/people", "/our-team")):
            ts = row[1]
            out.append(f"https://web.archive.org/web/{ts}/{orig}")
    return out[:5]


def run_harvester(domain: str) -> tuple[list[str], list[str]]:
    checked = []
    emails: dict[str, str] = {}
    try:
        proc = subprocess.run(
            ["theHarvester", "-d", domain, "-b", "all", "-l", "80"],
            capture_output=True,
            text=True,
            timeout=120,
        )
        checked.append(f"theHarvester -d {domain}")
        blob = (proc.stdout or "") + (proc.stderr or "")
        for e in extract_emails(blob):
            if email_on_domain(e, domain) and not is_generic(e):
                emails[e] = "theHarvester"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return checked, list(emails.keys())


def verify_domain(domain: str) -> dict:
    domain = domain.strip().lower()
    notes = []
    canonical = None
    parked = False
    for base in (f"https://www.{domain}", f"https://{domain}"):
        text, err, final = fetch(base)
        if text:
            canonical = urllib.parse.urlparse(final).netloc or domain
            tl = text.lower()
            if any(
                x in tl
                for x in (
                    "domain is for sale",
                    "buy this domain",
                    "parked free",
                    "godaddy",
                    "sedo",
                    "hugedomains",
                )
            ) and len(text) < 50000:
                parked = True
            break
        notes.append(f"{base}: {err}")
    return {
        "domain": domain,
        "live": canonical is not None,
        "canonical_host": canonical,
        "parked_guess": parked,
        "verify_notes": notes,
    }


def sitemap_team_urls(domain: str) -> list[str]:
    urls = []
    for sm in (f"https://www.{domain}/sitemap.xml", f"https://{domain}/sitemap.xml"):
        text, _, _ = fetch(sm)
        if not text:
            continue
        for loc in re.findall(r"<loc>([^<]+)</loc>", text):
            ll = loc.lower()
            if domain in ll and any(k in ll for k in ("/team", "/people", "/our-team", "/about")):
                urls.append(loc)
    return urls[:25]


def hygiene_crawl_seat(
    monday_id: str,
    name: str,
    firm: str,
    domain: str,
    use_harvester: bool = True,
) -> dict:
    monday_domain = domain.strip().lower()
    crawl_domain = LIVE_CRAWL_DOMAIN.get(monday_id, monday_domain)
    seed_domain = SEARCH_DOMAIN.get(monday_id, monday_domain)
    domain = crawl_domain
    person = name if name and name != firm else (firm or name)
    checked: list[str] = []
    mailto_hits: list[dict] = []
    all_emails: dict[str, list[str]] = {}
    errors: list[str] = []
    domain_info = verify_domain(domain)
    if monday_domain != crawl_domain:
        domain_info["monday_domain"] = monday_domain
        domain_info["crawl_domain_override"] = crawl_domain
    checked.append(f"https://{domain}/")
    checked.append(f"https://www.{domain}/")

    base_hosts = []
    if domain_info.get("canonical_host"):
        base_hosts.append(domain_info["canonical_host"])
    base_hosts.extend([domain, f"www.{domain}"])
    seen_host = set()
    hosts = []
    for h in base_hosts:
        h = h.lower().replace("https://", "").strip("/")
        if h and h not in seen_host:
            seen_host.add(h)
            hosts.append(h)

    team_403 = False
    any_mailto_on_domain = False

    extra_team_urls = sitemap_team_urls(domain)
    for url in extra_team_urls:
        if url not in checked:
            pass  # fetched in loop below

    for host in hosts[:2]:
        base = f"https://{host}"
        paths = list(FIRST_PARTY_PATHS)
        for path in paths:
            url = base + path
            text, err, final = fetch(url)
            checked.append(url)
            if final and final not in checked:
                checked.append(final)
            if err == "pdf":
                continue
            if text is None:
                if err and "403" in err and "team" in path:
                    team_403 = True
                if err:
                    errors.append(f"{url}: {err[:100]}")
                continue
            slug = f"{monday_id}_{host}{path.replace('/', '_')}"
            save_evidence(slug, url, text)
            emails = extract_emails(text)
            if emails:
                any_mailto_on_domain = any(not is_generic(e) for e in emails) or any_mailto_on_domain
            for e in emails:
                all_emails.setdefault(e, []).append(url)
                if person and name_near_email(text, person, e) and email_on_domain(
                    e, domain
                ):
                    if not is_generic(e):
                        mailto_hits.append(
                            {
                                "email": e,
                                "source_url": url,
                                "co_occurrence": "name+mailto",
                            }
                        )

    for url in extra_team_urls:
        text, err, final = fetch(url)
        checked.append(url)
        if not text:
            continue
        slug = f"{monday_id}_sitemap_{urllib.parse.quote(url, safe='')[:35]}"
        save_evidence(slug, url, text)
        for e in extract_emails(text):
            all_emails.setdefault(e, []).append(url)
            if person and name_near_email(text, person, e) and email_on_domain(e, domain):
                if not is_generic(e):
                    mailto_hits.append(
                        {"email": e, "source_url": url, "co_occurrence": "sitemap_team"}
                    )

    # Search-seed: name + domain
    seed_checked = search_seed_urls(person, seed_domain)
    checked.extend(seed_checked)
    for url in seed_checked[1:]:
        if domain not in url.lower():
            continue
        text, err, _ = fetch(url)
        if not text:
            continue
        checked.append(url)
        slug = f"{monday_id}_seed_{urllib.parse.quote(url, safe='')[:40]}"
        save_evidence(slug, url, text)
        for e in extract_emails(text):
            all_emails.setdefault(e, []).append(url)
            if person and name_near_email(text, person, e) and email_on_domain(e, domain):
                if not is_generic(e):
                    mailto_hits.append(
                        {"email": e, "source_url": url, "co_occurrence": "search_seed"}
                    )

    harvester_checked: list[str] = []
    if use_harvester:
        harvester_checked, harvest_emails = run_harvester(domain)
        checked.extend(harvester_checked)
        for e in harvest_emails:
            all_emails.setdefault(e, []).append("theHarvester")

    # Wayback only if 403 on team OR mailto signal without person attribution
    need_wayback = team_403 or (
        any_mailto_on_domain and not mailto_hits and not any(is_generic(e) for e in all_emails if not is_generic(e))
    )
    if team_403 or (any_mailto_on_domain and not mailto_hits):
        for wb in wayback_team(domain):
            text, err, _ = fetch(wb)
            checked.append(wb)
            if not text:
                continue
            slug = f"{monday_id}_wayback"
            save_evidence(slug, wb, text)
            for e in extract_emails(text):
                all_emails.setdefault(e, []).append(wb)
                if person and name_near_email(text, person, e) and email_on_domain(e, domain):
                    if not is_generic(e):
                        mailto_hits.append(
                            {"email": e, "source_url": wb, "co_occurrence": "wayback"}
                        )

    # Dedupe hits prefer mailto: links
    seen = set()
    uniq_hits = []
    for h in mailto_hits:
        k = h["email"]
        if k not in seen:
            seen.add(k)
            uniq_hits.append(h)

    status = "EMPTY"
    email = ""
    source_url = ""
    notes_parts = []
    if uniq_hits:
        best = uniq_hits[0]
        status = "FOUND"
        email = best["email"]
        source_url = best["source_url"]
    else:
        gens = sorted(e for e in all_emails if is_generic(e))
        if gens:
            notes_parts.append(f"Generics only: {', '.join(gens[:6])}")
        if domain_info.get("parked_guess"):
            notes_parts.append("Domain may be parked/for-sale landing.")
        if not domain_info.get("live"):
            notes_parts.append("Domain did not return HTML on apex/www probe.")
        if team_403:
            notes_parts.append("Team path 403; optional Wayback attempted.")
        if not notes_parts:
            notes_parts.append("No person@firm mailto co-occurrence on first-party pass.")
        notes_parts.append("Escalate: regulatory/impact PDF if needed (no third HTML pass).")

    return {
        "Monday_item_id": monday_id,
        "Name": name,
        "Firm": firm,
        "Domain": monday_domain,
        "Crawl_domain": crawl_domain,
        "domain_verification": domain_info,
        "Email": email,
        "Status": status,
        "Source_URL": source_url,
        "Checked_URLs": checked,
        "mailto_hits": uniq_hits,
        "all_emails": all_emails,
        "errors": errors[:8],
        "Notes": "; ".join(notes_parts),
        "Method": "team_html_hygiene",
    }


def main():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    results = []
    with INPUT.open() as f:
        for row in csv.DictReader(f):
            r = hygiene_crawl_seat(
                row["Monday_item_id"],
                row.get("Name", ""),
                row.get("Firm", ""),
                row["Domain"],
            )
            results.append(r)
            out = ROOT / "evidence" / f"crawl_{row['Monday_item_id']}.json"
            out.write_text(json.dumps(r, indent=2), encoding="utf-8")
            print(row["Monday_item_id"], r["Status"], r.get("Email") or "-")
    (ROOT / "crawl_results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
