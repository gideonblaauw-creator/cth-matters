#!/usr/bin/env python3
"""Fetch SEC EFTS search-index JSON for L10 arm-05 seats."""
import json
import urllib.parse
import urllib.request

UA = "cth-matters-mail-finder gideon@example.com"
QUERIES = {
    "ulrich_thiem_porsche": '"Ulrich Thiem" porsche',
    "at_porsche_ventures": "@porsche.ventures",
    "yair_reem_extantia": '"Yair Reem" extantia',
    "at_extantia": "@extantia.com",
    "william_prescott_redribbon": '"William Prescott" redribbon',
    "at_redribbon": "@redribbon.co",
    "jeff_stoike_blueaction": '"Jeff Stoike" "Blue Action"',
    "at_blueaction": "@blueactionaccelerator.com OR @blueaction.eco",
    "mikayla_hart_congruence": '"Mikayla Hart" congruence',
    "at_congruence": "@congruencecapital.com",
    "ulrich_thiem_email": '"Ulrich Thiem" @',
    "porsche_ventures_formd": "porsche ventures Form D",
}


def fetch(q: str) -> dict:
    params = urllib.parse.urlencode(
        {
            "q": q,
            "dateRange": "custom",
            "startdt": "2000-01-01",
            "enddt": "2026-12-31",
        }
    )
    url = f"https://efts.sec.gov/LATEST/search-index?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode())


def main() -> None:
    out = {}
    for key, q in QUERIES.items():
        try:
            data = fetch(q)
            total = data.get("hits", {}).get("total", {})
            out[key] = {"query": q, "total": total, "hits": []}
            for hit in data.get("hits", {}).get("hits", [])[:15]:
                src = hit.get("_source", {})
                out[key]["hits"].append(
                    {
                        "score": hit.get("_score"),
                        "file_date": src.get("file_date"),
                        "form": src.get("root_forms"),
                        "display_names": src.get("display_names"),
                        "file_id": hit.get("_id"),
                    }
                )
        except Exception as e:
            out[key] = {"query": q, "error": str(e)}
    path = "/workspace/mail-finder/wave4/L10/arm-05/evidence/edgar_search_summary.json"
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    print("wrote", path)


if __name__ == "__main__":
    main()
