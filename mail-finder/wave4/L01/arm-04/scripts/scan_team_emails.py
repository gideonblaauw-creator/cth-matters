#!/usr/bin/env python3
"""Scan first-party team URLs for name+mailto co-occurrence."""
import csv
import json
import re
import ssl
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "input.csv"
UA = "Mozilla/5.0 (compatible; MailFinder-Arm04/1.0)"

TEAM_URLS = {
    "13028358775": ["https://www.pcalp.com/team/", "https://www.pcalp.com/news/person/daniela-gomez-ziga/"],
    "13028359182": ["https://www.checkmatecapital.net/team"],
    "13096668277": ["https://www.daluscapital.com/team", "https://www.daluscapital.com/about-us"],
    "13028349815": ["https://circulatecapital.com/team/"],
    "13028336225": ["https://www.greenbondcorporation.com/who-we-are"],
    "13114451141": ["https://onevc.vc/team", "https://onevc.vc/about"],
    "13114460590": ["https://collidecap.com/team", "https://www.collide.capital/team"],
    "13028359480": ["https://acumen.org/about/team/"],
    "13028399382": ["https://glenarapartners.com/team", "https://glenarapartners.com/about"],
    "13028370265": ["https://tech.manacommon.com/team/etienne-gillard/"],
    "13028371139": ["https://www.axel-carbon.com/team", "https://www.axel-carbon.com/about"],
    "13080749061": ["https://www.riverwoodcapital.com/team/"],
    "13100506101": ["https://www.hvcapital.com/team/"],
    "13028371748": ["https://rumbo.ventures/team/", "https://rumbo.ventures/about-us/"],
    "13096680140": ["https://www.canary.com.br/time", "https://www.canary.com.br/en/team"],
    "13028367534": ["https://www.axel-carbon.com/team"],
    "13028371858": ["https://electis.com/about", "https://electis.com/team"],
    "13028358612": ["https://climatealpha.ai/", "https://climatealpha.ai/about"],
    "13100506409": ["https://www.moltenventures.com/team/our-team/"],
}

GENERIC_LOCAL = {"info", "hello", "team", "contact", "support", "general", "investors", "press", "careers", "hr"}


def fetch(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25, context=ctx) as r:
            return r.geturl(), r.read(200000).decode("utf-8", errors="replace")
    except Exception as e:
        return url, f"ERROR: {e}"


def name_tokens(name: str):
    name = re.sub(r"^(Dr\.|Mr\.|Mrs\.|Ms\.)\s+", "", name, flags=re.I)
    name = re.sub(r",.*$", "", name)
    parts = [p for p in re.split(r"\s+", name.strip()) if len(p) > 2]
    return parts


def scan(mid, name, urls):
    tokens = name_tokens(name)
    hits = []
    checked = []
    for url in urls:
        final, html = fetch(url)
        checked.append(final if not html.startswith("ERROR") else f"{url} ({html})")
        if html.startswith("ERROR"):
            continue
        # strip tags for proximity
        text = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.I | re.S)
        text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
        mailtos = re.findall(r'mailto:([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', html, flags=re.I)
        for email in mailtos:
            local = email.split("@")[0].lower()
            if local in GENERIC_LOCAL:
                continue
            # name co-occurrence: mailto near name in html chunk
            for m in re.finditer(re.escape(email), html, flags=re.I):
                chunk = html[max(0, m.start() - 2500) : m.end() + 2500]
                chunk_text = re.sub(r"<[^>]+>", " ", chunk)
                if all(t.lower() in chunk_text.lower() for t in tokens[:2] if tokens):
                    hits.append({"email": email, "source": final})
                    break
    return {"checked": checked, "hits": hits}


def main():
    rows = {r["Monday_item_id"]: r for r in csv.DictReader(INPUT.open())}
    out = {}
    for mid, urls in TEAM_URLS.items():
        row = rows[mid]
        out[mid] = {"name": row["Name"], **scan(mid, row["Name"], urls)}
        print(json.dumps({"id": mid, "hits": out[mid]["hits"]}), flush=True)
    (ROOT / "scripts" / "team_email_scan.json").write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
