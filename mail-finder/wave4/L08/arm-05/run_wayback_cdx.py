#!/usr/bin/env python3
"""One targeted Wayback CDX pass per seat on /team, /about, or /people."""
import json
import re
import csv
import urllib.parse
import urllib.request
from html import unescape

SEATS = [
    {
        "item_id": "13028399234",
        "name": "Brad Smith",
        "firm": "Brad Smith, CFA",
        "website": "https://centry.capital",
        "path": "/team",
    },
    {
        "item_id": "13028370683",
        "name": "Bryony Parker",
        "firm": "",
        "website": "https://savia.vc",
        "path": "/team",
    },
    {
        "item_id": "13028358405",
        "name": "Camilo Arango",
        "firm": "",
        "website": "https://clicoh.com",
        "path": "/team",
    },
    {
        "item_id": "13100506379",
        "name": "Camilo Kejner",
        "firm": "Angel Ventures",
        "website": "https://angelventures.vc",
        "path": "/team",
    },
    {
        "item_id": "13028336730",
        "name": "Carlos Iván Vargas Perdomo",
        "firm": "",
        "website": "https://dibanka.com",
        "path": "/team",
    },
]

UA = "Mozilla/5.0 (compatible; MailFinder-W4L08A05/1.0; +research)"


def fetch(url, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace"), resp.geturl()


def domain_from_website(website):
    host = urllib.parse.urlparse(website).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def name_tokens(name):
    parts = re.split(r"\s+", name.strip())
    # drop common particles for matching
    skip = {"de", "del", "la", "van", "von", "y"}
    return [p for p in parts if p.lower() not in skip and len(p) > 1]


def name_variants(name):
    n = name.lower()
    variants = {n}
    variants.add(n.replace("í", "i").replace("á", "a").replace("é", "e").replace("ó", "o").replace("ú", "u").replace("ñ", "n"))
    tokens = name_tokens(name)
    if len(tokens) >= 2:
        variants.add(f"{tokens[0].lower()} {tokens[-1].lower()}")
        variants.add(f"{tokens[-1].lower()}, {tokens[0].lower()}")
    return variants


def pick_path(website):
    """Choose one of /team, /about, /people from homepage hints (not Wayback)."""
    candidates = ["/team", "/about", "/people"]
    try:
        html, _ = fetch(website.rstrip("/") + "/")
        html_l = html.lower()
        scores = {}
        for p in candidates:
            scores[p] = html_l.count(f'href="{p}"') + html_l.count(f"href='{p}'") + html_l.count(p + "/")
        # Spanish equipo
        if scores["/team"] == 0 and "equipo" in html_l:
            return "/team"  # still use /team for CDX; may have captures under /team
        best = max(scores, key=scores.get)
        if scores[best] > 0:
            return best
    except Exception:
        pass
    return "/team"


def cdx_lookup(url_pattern):
    q = urllib.parse.urlencode(
        {
            "url": url_pattern,
            "output": "json",
            "filter": "statuscode:200",
            "limit": 15,
        }
    )
    api = f"https://web.archive.org/cdx/search/cdx?{q}"
    raw, _ = fetch(api)
    data = json.loads(raw)
    if not data or len(data) < 2:
        return api, []
    rows = []
    for row in data[1:]:
        # urlkey, timestamp, original, mimetype, statuscode, digest, length
        if len(row) >= 3:
            rows.append({"timestamp": row[1], "original": row[2]})
    return api, rows


def extract_emails(text, domain):
    pattern = rf"[a-zA-Z0-9._%+-]+@{re.escape(domain)}"
    return sorted(set(re.findall(pattern, text, flags=re.I)))


def mailto_emails(text, domain):
    found = re.findall(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+)', text, flags=re.I)
    dom = domain.lower()
    return sorted({e for e in found if e.lower().endswith("@" + dom)})


def generic_local(email):
    local = email.split("@")[0].lower()
    return local in {
        "info", "hello", "team", "contact", "contacto", "support", "sales",
        "admin", "office", "hola", "ventures", "invest", "investments",
        "press", "media", "careers", "jobs", "help", "general",
    }


def name_on_page(text, name):
    text_l = unescape(re.sub(r"<[^>]+>", " ", text)).lower()
    text_l = re.sub(r"\s+", " ", text_l)
    for v in name_variants(name):
        if v in text_l:
            return True
    tokens = name_tokens(name)
    if len(tokens) >= 2:
        first, last = tokens[0].lower(), tokens[-1].lower()
        if first in text_l and last in text_l:
            # proximity within ~400 chars
            for m in re.finditer(re.escape(first), text_l):
                start = max(0, m.start() - 200)
                end = min(len(text_l), m.end() + 200)
                if last in text_l[start:end]:
                    return True
    return False


def excerpt_around(text, name, email, width=280):
    plain = unescape(re.sub(r"<[^>]+>", " ", text))
    plain = re.sub(r"\s+", " ", plain)
    idx = plain.lower().find(email.lower())
    if idx < 0:
        for v in name_variants(name):
            idx = plain.lower().find(v)
            if idx >= 0:
                break
    if idx < 0:
        return plain[:width] + "..."
    start = max(0, idx - width // 2)
    return plain[start : start + width].strip()


def analyze_seat(seat):
    domain = domain_from_website(seat["website"])
    path = pick_path(seat["website"])
    seat["path"] = path
    url_pattern = f"{domain}{path}*"
    cdx_url, captures = cdx_lookup(url_pattern)
    checked = [cdx_url]
    result = {
        "item_id": seat["item_id"],
        "name": seat["name"],
        "domain": domain,
        "path": path,
        "cdx_url": cdx_url,
        "captures": len(captures),
        "status": "EMPTY",
        "email": "",
        "source_url": "",
        "excerpt": "",
        "notes": "",
        "snapshots_tried": [],
    }
    if not captures:
        result["notes"] = f"Wayback CDX: no HTTP 200 captures for {domain}{path}*."
        return result

    for cap in captures[:8]:
        ts = cap["timestamp"]
        orig = cap["original"]
        snap = f"https://web.archive.org/web/{ts}/{orig}"
        result["snapshots_tried"].append(snap)
        checked.append(snap)
        try:
            html, _ = fetch(snap)
        except Exception as e:
            continue
        emails = mailto_emails(html, domain) or extract_emails(html, domain)
        person_emails = [e for e in emails if not generic_local(e)]
        if not name_on_page(html, seat["name"]):
            continue
        for em in person_emails:
            # require co-occurrence in a tight window in plain text
            plain = unescape(re.sub(r"<[^>]+>", " ", html))
            plain_l = re.sub(r"\s+", " ", plain).lower()
            em_i = plain_l.find(em.lower())
            if em_i < 0:
                continue
            window = plain_l[max(0, em_i - 350) : em_i + 350]
            ok = False
            for v in name_variants(seat["name"]):
                if v in window:
                    ok = True
                    break
            if not ok:
                tokens = name_tokens(seat["name"])
                if len(tokens) >= 2 and tokens[0].lower() in window and tokens[-1].lower() in window:
                    ok = True
            if ok:
                result["status"] = "FOUND"
                result["email"] = em
                result["source_url"] = snap
                result["excerpt"] = excerpt_around(html, seat["name"], em)
                result["notes"] = f"Archived {path} snapshot: target name and {em} co-occur."
                return result

    result["notes"] = (
        f"Wayback CDX found {len(captures)} capture(s) for {domain}{path}*; "
        f"reviewed {len(result['snapshots_tried'])} snapshot(s) — no target name + person@{domain} co-occurrence."
    )
    result["checked_urls"] = checked
    return result


def main():
    out = []
    for seat in SEATS:
        seat = dict(seat)
        r = analyze_seat(seat)
        out.append(r)
        print(json.dumps(r, indent=2))
    with open("/workspace/mail-finder/wave4/L08/arm-05/evidence/cdx_run.json", "w") as f:
        json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
