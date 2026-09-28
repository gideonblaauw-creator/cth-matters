#!/usr/bin/env python3
"""Generate results.csv, summary.md, stamp-list.json for wave3 directory-mercury arm."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "input.csv"
OUT_CSV = ROOT / "results.csv"
OUT_SUMMARY = ROOT / "summary.md"
OUT_STAMP = ROOT / "stamp-list.json"

ROWS = [
    {
        "Monday_item_id": "13028349662",
        "Name": "Sergio Díaz",
        "Firm": "",
        "Domain": "idbinvest.org",
        "Priority": "P1",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/sergio-diaz | https://idbinvest.org/en/blog/author/sergio-diaz | https://idbinvest.org/en/idb-invest-caribbean-impact-manager-training-series | idbinvest.org PDF/disclosure search (no Sergio+@idbinvest.org co-occurrence)",
        "Status": "EMPTY",
        "Notes": "Mercury slug 404/error page. IDB author bio lists posts only; IFC/MDB training pages name other speakers — no same-page Sergio Díaz + person@idbinvest.org.",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13028349457",
        "Name": "Sina Dorner-Müller",
        "Firm": "",
        "Domain": "apg.nl",
        "Priority": "P1",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/sina-dorner-muller | https://apg.nl/en/press-and-media/ | https://apg.nl/mediarelaties/",
        "Status": "EMPTY",
        "Notes": "Mercury profile not found. APG press page lists named spokespeople with @apg.nl (base64 obfuscated) but Sina Dorner-Müller not among them; no Sina+@apg.nl public directory hit.",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13028364943",
        "Name": "Abhinav Sinha",
        "Firm": "",
        "Domain": "bii.co.uk",
        "Priority": "P2",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/abhinav-sinha | https://www.bii.co.uk/en/people/abhinav-sinha/ | Mercury investor-database browse (no BII match in SSR slice)",
        "Status": "EMPTY",
        "Notes": "Mercury slug 404. Official BII people profile has bio only — no contact email on same page.",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13100506386",
        "Name": "Adriana Saman",
        "Firm": "",
        "Domain": "clocktowerventures.com",
        "Priority": "P2",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/adriana-saman | https://mercury.com/investor-database/ben-savage | https://www.lavca.org/people/adriana-saman/",
        "Status": "EMPTY",
        "Notes": "No Mercury profile for Adriana Saman (slug 404). Mercury lists Ben Savage (Clocktower GP) with ben@clocktowerventures.com — different person. LAVCA nonprofit investor directory has name/firm only, no email.",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13028360241",
        "Name": "Alfredo Neila",
        "Firm": "",
        "Domain": "plasticrepairsystem.com",
        "Priority": "P2",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/alfredo-neila | https://www.plasticrepair.eu/prs-nombra-co-director-general-a-alfredo-neila/",
        "Status": "EMPTY",
        "Notes": "Mercury slug 404. PRS press page quotes Alfredo Neila but contact block is generic info@plasticrepair.eu only (not person@plasticrepairsystem.com co-attributed).",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13028372613",
        "Name": "Alistair Langer",
        "Firm": "",
        "Domain": "783capital.com",
        "Priority": "P2",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/alistair-langer | https://www.783partners.com/team",
        "Status": "EMPTY",
        "Notes": "Mercury slug 404. 783 Partners team page names Alistair Langer; only generic info@783partners.com (domain gate vs seat domain 783capital.com).",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13114396029",
        "Name": "Allen Taylor",
        "Firm": "Endeavor Catalyst",
        "Domain": "endeavor.org",
        "Priority": "P2",
        "Email": "",
        "Email_type": "",
        "Confidence": "MEDIUM",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/allen-taylor | https://endeavor.org/about-us/allen-taylor/ (Cloudflare block from runner) | https://endeavor.org/2025-endeavor-catalyst-annual-report/ | https://www.kauffmanfellows.org/fellows/allen-taylor",
        "Status": "EMPTY",
        "Notes": "Mercury slug 404. Endeavor Catalyst annual report page lists jackie.carmel@endeavor.org (fundraising IR) — not Allen Taylor. Kauffman Fellows nonprofit directory: bio only, no email.",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13028350632",
        "Name": "Amaya Baliño Sanz",
        "Firm": "",
        "Domain": "angelventures.vc",
        "Priority": "P2",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/amaya-balino-sanz | https://idbinvest.org/en/idb-invest-caribbean-impact-manager-training-series",
        "Status": "EMPTY",
        "Notes": "Mercury slug 404. IDB Invest Caribbean Impact Manager training series lists Amaya Baliño (Angel Ventures) as speaker — no email on same page.",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13114466721",
        "Name": "Ana Clara Martins",
        "Firm": "Atlantico",
        "Domain": "atlantico.vc",
        "Priority": "P2",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/ana-clara-martins | https://www.atlantico.vc/about-us | https://www.lavca.org/ (search seed — no Atlantico profile with email)",
        "Status": "EMPTY",
        "Notes": "Mercury slug 404. Atlantico about page lists Ana Martins among team — no mailto/email on page.",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13028336707",
        "Name": "Andrés Salazar González",
        "Firm": "",
        "Domain": "bavaria.co",
        "Priority": "P2",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/andres-salazar-gonzalez | Mercury browse/search (no profile)",
        "Status": "EMPTY",
        "Notes": "Mercury investor-database: no profile for Andrés Salazar González / Bavaria Colombia seat. No IFC/MDB or nonprofit investor-list page with name+@bavaria.co on same source.",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13100509893",
        "Name": "Aquilino Peña",
        "Firm": "",
        "Domain": "kiboventures.com",
        "Priority": "P2",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/aquilino-pena | https://www.kiboventures.com/team",
        "Status": "EMPTY",
        "Notes": "Mercury slug 404. Kibo team page confirms role; no person@kiboventures.com on same page (firm hello@ only on third-party summaries — not stamped).",
        "Method": "directory_mercury",
    },
    {
        "Monday_item_id": "13028370676",
        "Name": "Asia Agnelli",
        "Firm": "",
        "Domain": "tmv.com",
        "Priority": "P2",
        "Email": "",
        "Email_type": "",
        "Confidence": "HIGH",
        "Source_URL": "",
        "Checked_URLs": "https://mercury.com/investor-database/asia-agnelli | https://www.tmv.vc/team/azzi-agnelli | https://mercury.com/investor-database/soraya-darabi",
        "Status": "EMPTY",
        "Notes": "Mercury slug 404 for Asia/Azzi Agnelli. TMV team page (Azzi Agnelli) shows team@tmv.vc generic footer — not person@tmv.com. Soraya Darabi Mercury profile has no contact email published.",
        "Method": "directory_mercury",
    },
]

FIELDS = [
    "Monday_item_id",
    "Name",
    "Firm",
    "Domain",
    "Priority",
    "Email",
    "Email_type",
    "Confidence",
    "Source_URL",
    "Checked_URLs",
    "Status",
    "Notes",
    "Method",
]


def main():
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for row in ROWS:
            w.writerow(row)

    found = [r for r in ROWS if r["Status"] == "FOUND"]
    stamp = [
        {
            "Monday_item_id": r["Monday_item_id"],
            "Name": r["Name"],
            "Email": r["Email"],
            "Source_URL": r["Source_URL"],
            "Domain": r["Domain"],
        }
        for r in found
    ]
    OUT_STAMP.write_text(json.dumps(stamp, indent=2) + "\n", encoding="utf-8")

    empty = sum(1 for r in ROWS if r["Status"] == "EMPTY")
    summary = f"""# Mail Finder Wave3 — Arm 4: directory-mercury

**method_arm:** `directory_mercury`  
**Seats:** {len(ROWS)}  
**Run date:** 2026-09-25 (UTC)

## Counts

| Status | Count |
|--------|------:|
| FOUND | {len(found)} |
| EMPTY | {empty} |

## Method (allowed sources only)

- Mercury Investor Database public profile pages (manual slug browse + firm/name search seeds; no bulk Mercury API)
- IFC / IDB Invest MDB training & disclosure pages
- Academic / accelerator / nonprofit investor directories (e.g. LAVCA, Kauffman Fellows, Endeavor Catalyst report)

**Forbidden paths not used:** Hunter/Apollo/ContactOut/Clearbit, pattern guessing, SMTP verify, LinkedIn scrape, paid finders, third-party Mercury scrapers.

## FOUND (stamp list)

"""
    if found:
        for r in found:
            summary += f"- **{r['Name']}** — `{r['Email']}` — {r['Source_URL']}\n"
    else:
        summary += "_None this arm._\n"

    summary += """
## Notable near-misses (not stamped)

- **Adriana Saman** — Mercury has [Ben Savage / Clocktower](https://mercury.com/investor-database/ben-savage) with `ben@clocktowerventures.com`; different individual.
- **Allen Taylor** — [2025 Endeavor Catalyst annual report](https://endeavor.org/2025-endeavor-catalyst-annual-report/) lists `jackie.carmel@endeavor.org` for fund IR, not Allen Taylor.
- **Asia Agnelli** — TMV profile page uses generic `team@tmv.vc` alongside Azzi Agnelli name.

## Evidence

HTML snapshots under `evidence/` (Mercury attempts, IDB/APG/BII/Kibo/Atlantico/TMV/783/PRS pages).

## Baseline

Wave3 cumulative baseline referenced in brief: **27/50** prior to this arm; **+0 FOUND** here → still **27/50** unless other arms add stamps.
"""
    OUT_SUMMARY.write_text(summary, encoding="utf-8")
    print(f"Wrote {OUT_CSV}, {OUT_SUMMARY}, {OUT_STAMP} ({len(found)} FOUND)")


if __name__ == "__main__":
    main()
