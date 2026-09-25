#!/usr/bin/env python3
"""Fetch URLs and check name+personal-email co-occurrence for L06 arm-04."""
import re
import subprocess
import html as html_lib
from pathlib import Path
from urllib.parse import quote_plus, urlparse

UA = "MailFinderResearch/1.0"
EV = Path(__file__).parent / "fetched"
EV.mkdir(exist_ok=True)

GENERIC_LOCAL = {
    "press", "info", "hello", "contact", "bookings", "team", "impact",
    "support", "sales", "admin", "office", "media", "events", "enquiries",
    "inquiry", "inquiries", "partnersupport", "driveri", "communications",
    "marketing", "hr", "careers", "privacy", "legal", "noreply", "no-reply",
}

EMAIL_RE = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
    re.I,
)


def curl_fetch(url: str, timeout: int = 45) -> tuple[int, str]:
    slug = re.sub(r"[^a-zA-Z0-9._-]", "_", url)[:120]
    out = EV / f"curl_{slug}.body"
    code = subprocess.run(
        [
            "curl", "-sL", "-A", UA,
            "-w", "%{http_code}",
            "-o", str(out),
            "--max-time", str(timeout),
            url,
        ],
        capture_output=True,
        text=True,
    )
    http = code.stdout.strip()[-3:] if code.stdout else "000"
    try:
        body = out.read_text(errors="replace")
    except OSError:
        body = ""
    return int(http) if http.isdigit() else 0, body


def strip_html(text: str) -> str:
    text = re.sub(r"(?is)<script.*?>.*?</script>", " ", text)
    text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html_lib.unescape(text)
    return re.sub(r"\s+", " ", text)


def is_personal_email(email: str) -> bool:
    local = email.split("@")[0].lower()
    if local in GENERIC_LOCAL:
        return False
    # role inboxes like pr@, ir@
    if len(local) <= 3 and local.isalpha():
        return False
    return True


def name_variants(full_name: str) -> list[str]:
    parts = full_name.replace("ë", "e").replace("ö", "o").replace("ł", "l").split()
    variants = {full_name, full_name.replace("ë", "e").replace("ö", "o")}
    if len(parts) >= 2:
        variants.add(f"{parts[0]} {parts[-1]}")
        variants.add(f"{parts[-1]}")
        variants.add(parts[0])
    return [v for v in variants if len(v) > 2]


def name_on_page(plain: str, names: list[str]) -> bool:
    low = plain.lower()
    for n in names:
        if n.lower() in low:
            return True
        # accent-stripped
        nn = n.lower().replace("ë", "e").replace("ö", "o").replace("ł", "l").replace("ç", "c")
        if nn in low:
            return True
    return False


def check_page(body: str, names: list[str], domain_hint: str | None = None) -> list[dict]:
    plain = strip_html(body)
    if not name_on_page(plain, names):
        return []
    hits = []
    for em in set(EMAIL_RE.findall(body + " " + plain)):
        em_l = em.lower()
        if not is_personal_email(em_l):
            continue
        if domain_hint and domain_hint not in em_l:
            # allow adjacent context if firm name is target (Netradyne)
            pass
        # co-occurrence window: whole page is OK per brief ("SAME page")
        hits.append({"email": em_l, "excerpt": excerpt_around(plain, em_l, names)})
    return hits


def excerpt_around(plain: str, email: str, names: list[str], radius: int = 220) -> str:
    idx = plain.lower().find(email.lower())
    if idx < 0:
        for n in names:
            idx = plain.lower().find(n.lower())
            if idx >= 0:
                break
    start = max(0, idx - radius)
    end = min(len(plain), idx + len(email) + radius)
    return plain[start:end].strip()


def searx_urls(query: str, limit: int = 12) -> list[str]:
    endpoints = [
        "https://searx.be/search",
        "https://search.sapti.me/search",
        "https://paulgo.io/search",
    ]
    urls = []
    for base in endpoints:
        url = f"{base}?q={quote_plus(query)}&format=json"
        code, body = curl_fetch(url, timeout=25)
        if code != 200:
            continue
        try:
            import json
            data = json.loads(body)
            for r in data.get("results", [])[:limit]:
                u = r.get("url")
                if u and u not in urls:
                    urls.append(u)
        except Exception:
            continue
        if urls:
            break
    return urls


if __name__ == "__main__":
    import json
    seats = {
        "lasocki": {
            "names": name_variants("Michal Lasocki") + ["Michał Lasocki"],
            "queries": [
                '"Michal Lasocki" email',
                '"Michał Lasocki" eecventures',
                '"Michal Lasocki" speaker pdf',
                'site:eecventures.com Lasocki',
            ],
        },
        "chanrai": {
            "names": name_variants("Miheer Chanrai"),
            "queries": [
                '"Miheer Chanrai" email',
                '"Miheer Chanrai" climate.capital',
                '"Miheer Chanrai" podcast',
                '"Miheer Chanrai" speaker',
            ],
        },
        "saggioro": {
            "names": name_variants("Monica Saggioro Leal") + ["Monica Saggioro"],
            "queries": [
                '"Monica Saggioro" email maya.capital',
                '"Monica Saggioro Leal" podcast',
                'site:lavca.org Monica Saggioro',
                '"Monica Saggioro" speaker',
            ],
        },
        "couet": {
            "names": name_variants("Nathalie Couët") + ["Nathalie Couet"],
            "queries": [
                '"Nathalie Couët" email',
                '"Nathalie Couet" email',
                'site:senecaimpact.earth Nathalie',
                '"Nathalie Couet" speaker',
            ],
        },
        "netradyne": {
            "names": ["Netradyne"],
            "queries": [
                'site:netradyne.com "Media Contact" email',
                'Netradyne sarah.duckett@netradyne.com',
            ],
        },
    }
    seed_urls = [
        "https://www.eecventures.com/en/eec-ventures/",
        "https://www.eecventures.com/en/contact/",
        "https://www.eecventures.com/en/",
        "https://climate.capital/about",
        "https://climate.capital/",
        "https://www.maya.capital/team",
        "https://www.lavca.org/people/monica-saggioro/",
        "https://senecaimpact.earth/about-us/the-team/",
        "https://senecaimpact.earth/contact/",
        "https://women-in-green-hydrogen.net/nathalie-couet/",
        "https://www.netradyne.com/company/contact",
        "https://www.netradyne.com/news/netradyne-strengthens-leadership-team-with-new-cfo-and-coo-appointments",
        "https://www.netradyne.com/news/netradyne-celebrates-10th-anniversary-with-cross-country-customer-obsession-tour",
    ]
    report = {}
    for seat, cfg in seats.items():
        checked = []
        found = []
        urls = list(seed_urls if seat == "netradyne" else [])
        for q in cfg["queries"]:
            urls.extend(searx_urls(q))
        # dedupe
        seen = set()
        uniq = []
        for u in urls:
            if u not in seen:
                seen.add(u)
                uniq.append(u)
        for u in uniq[:40]:
            code, body = curl_fetch(u)
            checked.append({"url": u, "http": code})
            if code >= 400 or not body:
                continue
            hits = check_page(body, cfg["names"])
            for h in hits:
                found.append({"url": u, **h})
        report[seat] = {"checked": checked, "found": found}
    print(json.dumps(report, indent=2))
