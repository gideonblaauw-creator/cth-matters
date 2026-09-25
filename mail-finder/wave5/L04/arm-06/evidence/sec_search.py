#!/usr/bin/env python3
import json, urllib.parse, urllib.request, re

UA = "MailFinderResearch/1.0 (cth-matters; regulatory-mailbox) contact@example.com"

def efts(q, size=10):
    url = "https://efts.sec.gov/LATEST/search-index?q=" + urllib.parse.quote(q) + f"&from=0&size={size}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="replace")

queries = [
    '"Rachel Holt"',
    '"Rachel Holt" AND "Construct"',
    '"@construct.capital"',
    '"Construct Capital" AND "Form D"',
    '"Roy Bahat"',
    '"Roy Bahat" AND "@bloombergbeta"',
    '"@bloombergbeta.com"',
    '"Bloomberg Beta"',
    '"Rafa de la Guia"',
    '"Rafa de la Guia" AND "@quona"',
    '"@quona.com"',
    '"Quona Capital" AND "Form D"',
    '"Rodolfo Elias Dieck"',
    '"Rodolfo Dieck"',
    '"@proezaventures.com"',
    '"Proeza Ventures"',
    '"Rodrigo Velasco" AND "BBVA"',
    '"@bbvaspark.com"',
    '"BBVA Spark"',
]

for q in queries:
    try:
        d = efts(q, 8)
        total = d.get("hits", {}).get("total", {})
        hits = d.get("hits", {}).get("hits", [])
        print(f"\n=== {q} === total={total}")
        for h in hits[:5]:
            src = h.get("_source", {})
            print(
                src.get("file_date"),
                src.get("form"),
                src.get("adsh"),
                (src.get("display_names") or [""])[0][:80],
            )
    except Exception as e:
        print(f"\n=== {q} === ERROR {e}")
