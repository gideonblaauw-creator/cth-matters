#!/usr/bin/env python3
import json, urllib.parse, urllib.request, sys

UA = "cth-matters mail-finder contact@example.com"

queries = [
    "783partners.com",
    '"Alistair Langer"',
    '"783 Partners"',
    "endeavor.org",
    '"Allen Taylor" AND Endeavor',
    '"Endeavor Catalyst"',
    "regeneraventures.com",
    '"Regenera Ventures"',
    '"Alma Catalina Gutierrez"',
    "angelventures.vc",
    '"Amaya Balino"',
    '"Angel Ventures"',
    "atlantico.vc",
    '"Ana Clara Martins"',
    '"Atlantico Partners"',
]

results = {}
for q in queries:
    url = (
        "https://efts.sec.gov/LATEST/search-index?q="
        + urllib.parse.quote(q)
        + "&dateRange=custom&startdt=2000-01-01&enddt=2026-09-25"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    hits = data.get("hits", {}).get("hits", [])
    total = data.get("hits", {}).get("total", {}).get("value", 0)
    results[q] = {"total": total, "hits": []}
    for h in hits[:10]:
        s = h["_source"]
        results[q]["hits"].append(
            {
                "id": h["_id"],
                "file_date": s.get("file_date"),
                "form": s.get("form_type"),
                "entity": (s.get("display_names") or [""])[0],
            }
        )
    print(f"{q!r}: {total}")
    for row in results[q]["hits"][:3]:
        print(" ", row)

with open("/workspace/mail-finder/wave4/L04/arm-06/evidence/efts_search.json", "w") as f:
    json.dump(results, f, indent=2)
