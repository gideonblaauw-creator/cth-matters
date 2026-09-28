#!/usr/bin/env python3
"""Build Wave3 hygiene-crawl deliverables from crawl_results.json."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CRAWL = ROOT / "crawl_results.json"
INPUT = ROOT / "input.csv"

WEBSITE_CORRECTIONS = [
    {
        "Monday_item_id": "13028403427",
        "Name": "Christel Piron",
        "Monday_Domain": "psvfoundry.com",
        "corrected_website": "https://www.psv.xyz/foundry",
        "reason": "psvfoundry.com does not resolve (NXDOMAIN). PSV Foundry first-party site is psv.xyz.",
        "link_mm7gdv8s_note": "blank Website only — stamp https://www.psv.xyz/foundry",
    },
    {
        "Monday_item_id": "13028359182",
        "Name": "Dennis Zaidi",
        "Monday_Domain": "checkmatecap.com",
        "corrected_website": "https://www.checkmatecapital.net/",
        "reason": "checkmatecap.com redirects to parked /lander; operating firm site is checkmatecapital.net.",
        "link_mm7gdv8s_note": "blank Website only — stamp https://www.checkmatecapital.net/",
    },
]

ROW_NOTES = {
    "13080769456": "blink.vc team/home crawled; no person mailto on first-party HTML.",
    "13028370683": "savia.vc team paths; Bryony Parker listed without mailto.",
    "13114411688": "flybridge.com/team lists Chip Hazard; Squarespace team page has no mailto links.",
    "13100505949": "mourocapital.com team sitemap + /team/christopher-gottschalk/; bio pages without personal mailto (info@mourocapital.com generic only elsewhere).",
    "13100511323": "newroadcp.com/team and /team/clete-brewer/; no person@newroadcp.com mailto co-occurrence.",
    "13028370003": "simmacapital.com/team lists Daniel Blandón with LinkedIn only.",
    "13028349815": "circulatecapital.com team; Dondi Hananto without mailto (esg@ generic on contact).",
    "13114451141": "onevc.vc/team/eduardo-campos first-party bio; LinkedIn only, no email.",
    "13028370265": "manatechmiami.com team/about paths; no person mailto.",
    "13080749061": "riverwoodcapital.com/team returns Cloudflare challenge (403-class); no person mailto captured on first-party pass.",
    "13028359182": "checkmatecapital.net our-team crawled on live domain; no Dennis Zaidi person mailto.",
}


def main():
    crawl_rows = {r["Monday_item_id"]: r for r in json.loads(CRAWL.read_text())}
    input_rows = list(csv.DictReader(INPUT.open()))

    results_fields = [
        "Monday_item_id",
        "Name",
        "Firm",
        "Domain",
        "Priority",
        "Email",
        "Email_type",
        "Status",
        "Source_URL",
        "Checked_URLs",
        "Method",
        "Notes",
    ]

    results = []
    stamp = []

    for row in input_rows:
        mid = row["Monday_item_id"]
        c = crawl_rows.get(mid, {})
        status = c.get("Status", "EMPTY")
        email = c.get("Email", "")
        source = c.get("Source_URL", "")
        checked = c.get("Checked_URLs", [])
        if isinstance(checked, list):
            checked_s = " | ".join(dict.fromkeys(checked))
        else:
            checked_s = checked

        notes = c.get("Notes") or ROW_NOTES.get(mid, "")
        if mid in ROW_NOTES and status == "EMPTY":
            notes = ROW_NOTES[mid]
        if status == "FOUND" and mid == "13028403427":
            notes = (
                "mailto:cp@psv.xyz co-occurring with Christel Piron on psv.xyz/people "
                "(Monday domain psvfoundry.com NXDOMAIN; crawled live psv.xyz)."
            )

        if status == "FOUND" and email:
            stamp.append(
                {
                    "Monday_item_id": mid,
                    "Name": row.get("Name") or row.get("Firm"),
                    "Email": email,
                    "Source_URL": source,
                    "method_arm": "team_html_hygiene",
                }
            )

        results.append(
            {
                "Monday_item_id": mid,
                "Name": row.get("Name", ""),
                "Firm": row.get("Firm", ""),
                "Domain": row.get("Domain", ""),
                "Priority": row.get("Priority", "P2"),
                "Email": email,
                "Email_type": "person@firm" if status == "FOUND" else "",
                "Status": status,
                "Source_URL": source,
                "Checked_URLs": checked_s,
                "Method": "team_html_hygiene",
                "Notes": notes,
            }
        )

    with (ROOT / "results.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=results_fields)
        w.writeheader()
        w.writerows(results)

    found = sum(1 for r in results if r["Status"] == "FOUND")
    empty = sum(1 for r in results if r["Status"] == "EMPTY")
    summary = f"""# Wave3 Arm 5 — Hygiene-gated first-party crawl

**method_arm:** `team_html_hygiene`  
**Run date:** 2026-09-25  
**Seats:** {len(results)} (input `wave3-hygiene-crawl.csv`)

## Scorecard

| Metric | Count |
|--------|------:|
| FOUND (person@firm mailto + name co-occurrence) | {found} |
| EMPTY | {empty} |
| Baseline reference | 27/50 (prior wave aggregate) |

## Method (this arm)

1. Verify live firm domain (flag parked/NXDOMAIN; note `website-corrections.json` for blank Monday Website only).
2. **One** first-party pass: `/team`, `/about`, `/people`, `/contact`, sitemap-discovered team URLs, plus optional search-seed (`site:domain` + person name) on firm domain only.
3. Optional Wayback on `/team|/about|/people` only when team 403 or mailto signal without attribution.
4. No third HTML pass; EMPTY seats escalate to regulatory/impact PDF in a later arm.

## Forbidden (observed)

No pattern guessing, SMTP verify, Hunter, LinkedIn scrape, or generic stamping.

## Domain hygiene

- **Christel Piron:** Monday `psvfoundry.com` is NXDOMAIN → live **psv.xyz** (`/foundry`, `/people`).
- **Dennis Zaidi:** Monday `checkmatecap.com` is parked → live **checkmatecapital.net**.

## FOUND summary

"""
    for r in results:
        if r["Status"] == "FOUND":
            summary += f"- **{r['Name']}** — `{r['Email']}` — [{r['Source_URL']}]({r['Source_URL']})\n"
    if found == 0:
        summary += "- (none)\n"

    summary += """
## EMPTY / escalate

"""
    for r in results:
        if r["Status"] != "FOUND":
            summary += f"- **{r['Name'] or r['Domain']}** ({r['Monday_item_id']}): {r['Notes'][:200]}\n"

    (ROOT / "summary.md").write_text(summary, encoding="utf-8")
    (ROOT / "stamp-list.json").write_text(json.dumps(stamp, indent=2), encoding="utf-8")
    (ROOT / "website-corrections.json").write_text(
        json.dumps(WEBSITE_CORRECTIONS, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
