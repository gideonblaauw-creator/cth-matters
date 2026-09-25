#!/usr/bin/env python3
"""Generate Wave4 L01 Arm05 deliverables from input CSV + manual verification."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INPUT = Path("/home/ubuntu/.cursor/projects/workspace/uploads/wave4-l01-arm05_3eae.csv")

# Seat outcomes from HTTP checks + public web verification (2026-09-25).
SEATS = {
    "13028367214": {
        "Status": "WEBSITE_OK",
        "Proposed_Website": "https://www.arxus.eu/en-BE/",
        "Notes": "Live Arxus (Cronos Group IT services) site; locale redirect from apex. Seat is employer site, not a standalone fund vehicle.",
        "Checked_URLs": "https://www.arxus.eu/ (200→/en-BE/)",
    },
    "13028358383": {
        "Status": "WEBSITE_CORRECTED",
        "Proposed_Website": "https://overboost.me/",
        "Notes": "overboost.vc NXDOMAIN; official Overboost VC site is overboost.me (Humberto Matsuda listed on team).",
        "Checked_URLs": "https://overboost.vc (NXDOMAIN); https://overboost.me/ (200)",
    },
    "13114411690": {
        "Status": "WEBSITE_MAPPED",
        "Proposed_Website": "https://endeavor.org/catalyst/",
        "Notes": "endeavor.org parent org live but Cloudflare 403 to automated clients; Igor Piquet is Endeavor Catalyst LATAM — catalyst subsite is the investment entity homepage.",
        "Checked_URLs": "https://endeavor.org (403 bot challenge); https://endeavor.org/catalyst/ (403 bot challenge, public index OK); https://endeavor.org/about-us/global-team/ (public roster cites Igor Piquet)",
    },
    "13100506451": {
        "Status": "WEBSITE_OK",
        "Proposed_Website": "https://bosch.ventures/",
        "Notes": "Bosch Ventures official domain resolves; team page live.",
        "Checked_URLs": "https://bosch.ventures (200); https://bosch.ventures/team/ingo-ramesohl/ (200, no person mailto)",
    },
    "13100503653": {
        "Status": "WEBSITE_CORRECTED",
        "Proposed_Website": "https://www.prochain.vc/",
        "Notes": "prochain.ventures NXDOMAIN; proChain Ventures official site is prochain.vc.",
        "Checked_URLs": "https://prochain.ventures (NXDOMAIN); https://www.prochain.vc/ (200)",
    },
    "13028358308": {
        "Status": "WEBSITE_MAPPED",
        "Proposed_Website": "https://www.oikocredit.org/",
        "Notes": "James Todd, CFA is Oikocredit investment staff; oikocredit.org 301→www and Cloudflare 403 to bots — canonical public homepage is www.oikocredit.org.",
        "Checked_URLs": "https://oikocredit.org (301→www, 403 bot); https://www.oikocredit.org/ (403 bot challenge, entity verified publicly)",
    },
    "13100511350": {
        "Status": "WEBSITE_MAPPED",
        "Proposed_Website": "https://www.n47.com/",
        "Notes": "next47.com 301 redirects to n47.com (Siemens next47 rebrand); live investment firm homepage.",
        "Checked_URLs": "https://next47.com (301→https://www.n47.com/ 200); https://www.n47.com/team (200)",
    },
    "13028366289": {
        "Status": "WEBSITE_OK",
        "Proposed_Website": "https://senecaimpact.earth/",
        "Notes": "Seneca Impact Advisors official site; Jean-Marc Champagne MD/co-founder verified publicly.",
        "Checked_URLs": "https://senecaimpact.earth/ (200); https://senecaimpact.earth/about-us/ (generic mailto only)",
    },
    "13028367050": {
        "Status": "WEBSITE_OK",
        "Proposed_Website": "https://crossboundary.com/",
        "Notes": "CrossBoundary Advisory official site; Jonathan Duarte people page live.",
        "Checked_URLs": "https://crossboundary.com (200); https://crossboundary.com/people/jonathan-duarte/ (200, no mailto)",
    },
    "13028393225": {
        "Status": "WEBSITE_OK",
        "Proposed_Website": "https://www.okavango-capital.com/",
        "Notes": "Okavango Capital Partners official site; Josep Oriol managing partner on team page.",
        "Checked_URLs": "https://www.okavango-capital.com/ (200); https://www.okavango-capital.com/our-team.html (200, no person mailto)",
    },
    "13028372274": {
        "Status": "WEBSITE_CORRECTED",
        "Proposed_Website": "https://gairaconsulting.com/",
        "Notes": "edtechhublatam.org is a regional EdTech community hub, not Juan Aparicio's firm; founder/CEO site is Gaira Consulting (angel/EdTech investor).",
        "Checked_URLs": "https://edtechhublatam.org (200); https://gairaconsulting.com/ (200); https://gairaconsulting.com/nosotros/ (founder Juan Manuel Aparicio)",
    },
    "13100503497": {
        "Status": "WEBSITE_OK",
        "Proposed_Website": "https://www.latinamericafund.com/",
        "Notes": "SoftBank Investment Advisers Latin America Fund public site; matches Firm field.",
        "Checked_URLs": "https://www.latinamericafund.com/ (200, SoftBank Latin America Fund branding)",
    },
    "13114458098": {
        "Status": "WEBSITE_MAPPED",
        "Proposed_Website": "https://www.atlantico.vc/",
        "Notes": "atlantico.vc redirects to www.atlantico.vc; Atlantico VC official homepage.",
        "Checked_URLs": "https://atlantico.vc (301→https://www.atlantico.vc/ 200); https://www.atlantico.vc/about-us (200, Julio Vasconcellos on page)",
    },
    "13028367329": {
        "Status": "WEBSITE_CORRECTED",
        "Proposed_Website": "https://jambaar-capital.com/",
        "Notes": "jambaar.com is parked (/lander redirect, 114-byte stub); Jambaar Capital official site is jambaar-capital.com.",
        "Checked_URLs": "https://jambaar.com (200→/lander parked); https://jambaar-capital.com/ (200)",
    },
    "13028372637": {
        "Status": "WEBSITE_MAPPED",
        "Proposed_Website": "https://www.lichen.vc/",
        "Notes": "lichen.vc redirects to www.lichen.vc; Lichen Ventures climate-hard-tech fund homepage.",
        "Checked_URLs": "https://lichen.vc (301→https://www.lichen.vc/ 200); https://www.lichen.vc/about (200)",
    },
    "13028359258": {
        "Status": "WEBSITE_OK",
        "Proposed_Website": "https://andeshorizoncapital.com/",
        "Notes": "Andes Horizon Capital investment boutique; Kai Christian Buhofer founding partner on about page.",
        "Checked_URLs": "https://andeshorizoncapital.com/ (200); https://andeshorizoncapital.com/en/nosotros/ (200)",
    },
    "13028349951": {
        "Status": "WEBSITE_OK",
        "Proposed_Website": "https://turn8.co/",
        "Notes": "TURN8 official site; Kamal Hassan founder profile page live (generic info@ only).",
        "Checked_URLs": "https://turn8.co (200); https://turn8.co/kamal-hassan/ (200, mailto:info@turn8.co only)",
    },
    "13028366698": {
        "Status": "WEBSITE_MAPPED",
        "Proposed_Website": "https://www.pachamamavc.com/",
        "Notes": "pachamamavc.com redirects to www.pachamamavc.com; Pachamama Ventures fund site.",
        "Checked_URLs": "https://pachamamavc.com (301→https://www.pachamamavc.com/ 200); https://www.pachamamavc.com/ (200)",
    },
    "13028367969": {
        "Status": "WEBSITE_CORRECTED",
        "Proposed_Website": "https://www.urbanfarmerspro.com/",
        "Notes": "workvivo.com is unrelated employee-engagement SaaS; Klaus Hergett is co-founder/CEO of Urban Farmers Pro (impact/agtech investor-operator).",
        "Checked_URLs": "https://workvivo.com (301→www.workvivo.com 200, wrong entity); https://www.urbanfarmerspro.com/ (200)",
    },
}

FIELDNAMES = [
    "Status",
    "Monday_item_id",
    "Name",
    "Firm",
    "Current_Website",
    "Proposed_Website",
    "Domain",
    "Notes",
    "Checked_URLs",
    "Email",
    "Source_URL",
]


def main() -> None:
    rows_in = list(csv.DictReader(INPUT.open()))
    results = []
    corrections = []

    for row in rows_in:
        mid = row["Monday_item_id"]
        meta = SEATS[mid]
        status = meta["Status"]
        proposed = meta["Proposed_Website"]
        current = row["Website"].strip()

        out = {
            "Status": status,
            "Monday_item_id": mid,
            "Name": row["Name"],
            "Firm": row["Firm"],
            "Current_Website": current,
            "Proposed_Website": proposed if proposed.rstrip("/") != current.rstrip("/") else "",
            "Domain": row["Domain"],
            "Notes": meta["Notes"],
            "Checked_URLs": meta["Checked_URLs"],
            "Email": "",
            "Source_URL": "",
        }
        results.append(out)

        if status == "WEBSITE_CORRECTED":
            corrections.append(
                {
                    "Monday_item_id": mid,
                    "Corrected_URL": proposed,
                    "Why": meta["Notes"],
                }
            )

    with (ROOT / "results.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        w.writerows(results)

    (ROOT / "website-corrections.json").write_text(
        json.dumps(corrections, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (ROOT / "stamp-list.json").write_text("[]\n", encoding="utf-8")

    counts = {}
    for r in results:
        counts[r["Status"]] = counts.get(r["Status"], 0) + 1

    summary_lines = [
        "# Wave4 L01 Arm05 — Domain hygiene scorecard",
        "",
        f"Seats processed: **{len(results)}**",
        "",
        "| Status | Count |",
        "| --- | ---: |",
    ]
    for status in sorted(counts):
        summary_lines.append(f"| {status} | {counts[status]} |")
    summary_lines.extend(
        [
            "",
            "## Notes",
            "",
            "- No first-party team/people pages exposed a non-generic `mailto:` co-occurring with a seat name; **FOUND = 0**.",
            "- Corrections written to `website-corrections.json` (parked/NXDOMAIN/wrong-entity only).",
            "- Redirect mappings (e.g. next47→n47.com) are recorded as `WEBSITE_MAPPED` in `results.csv`.",
        ]
    )
    (ROOT / "summary.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
