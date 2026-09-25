#!/usr/bin/env python3
"""Build results.csv, results.md, stamp-list.json, CLOSEOUT.md from crawl_results.json."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "input.csv"
CRAWL = ROOT / "scripts" / "crawl_results.json"
METHOD = "wave5_L02_arm08_team_mailto"

NOTES = {
    "13100503497": (
        "latinamericafund.com/team (Gatsby): Juan Franck in team page-data roster; "
        "no mailto or @latinamericafund.com in team/about HTML or page-data."
    ),
    "13114458098": (
        "atlantico.vc/about-us lists Julio Vasconcellos (Partner); zero mailto in page source."
    ),
    "13028359258": (
        "andeshorizoncapital.com/nosotros lists Kai Christian Buhofer; no mailto on site crawl."
    ),
    "13028349951": (
        "turn8.co/about + /kamal-hassan bio; only generic mailto info@turn8.co (footer/contact)."
    ),
    "13028367969": (
        "urbanfarmerspro.com: Klaus Hergett not on nosotros/home; contacto@ only on /contacto (generic)."
    ),
}

EXTRA_CHECKED = {
    "13100503497": [
        "https://www.latinamericafund.com/page-data/team/page-data.json",
    ],
    "13028359258": [
        "https://andeshorizoncapital.com/nosotros/",
    ],
    "13028349951": [
        "https://turn8.co/kamal-hassan/",
    ],
    "13028367969": [
        "https://www.urbanfarmerspro.com/nosotros",
        "https://www.urbanfarmerspro.com/contacto",
    ],
}


def main():
    crawl = json.loads(CRAWL.read_text(encoding="utf-8"))
    rows_out = []
    found = 0
    empty = 0
    uncertain = 0

    for row in csv.DictReader(INPUT.open(encoding="utf-8")):
        mid = row["Monday_item_id"]
        c = crawl[mid]
        checked = list(c["checked"])
        for u in EXTRA_CHECKED.get(mid, []):
            if u not in checked:
                checked.append(u)
        checked_str = " | ".join(checked)
        hits = c.get("hits") or []
        if hits:
            status = "FOUND"
            found += 1
            h = hits[0]
            email = h["email"]
            source_url = h["source_url"]
        else:
            status = "EMPTY"
            empty += 1
            email = ""
            source_url = ""

        rows_out.append(
            {
                "Monday_item_id": mid,
                "Name": row["Name"],
                "Contact_name": row.get("Contact_name", row["Name"]),
                "Firm": row.get("Firm", ""),
                "Kind": row.get("Kind", ""),
                "Priority": row.get("Priority", ""),
                "Website": row["Website"],
                "Domain": row.get("Domain", ""),
                "Email": email,
                "Source_URL": source_url,
                "Checked_URLs": checked_str,
                "Status": status,
                "Notes": NOTES.get(mid, ""),
                "Method": METHOD,
            }
        )

    fieldnames = [
        "Monday_item_id",
        "Name",
        "Contact_name",
        "Firm",
        "Kind",
        "Priority",
        "Website",
        "Domain",
        "Email",
        "Source_URL",
        "Checked_URLs",
        "Status",
        "Notes",
        "Method",
    ]
    with (ROOT / "results.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_out)

    stamps = []
    for r in rows_out:
        if r["Status"] != "FOUND":
            continue
        # placeholder — no FOUND in this run
        pass

    (ROOT / "stamp-list.json").write_text(
        json.dumps(stamps, indent=2) + "\n", encoding="utf-8"
    )

    md = [
        "# Wave5 L02 Arm 08 — Team person mailto scorecard",
        "",
        f"**Method:** {METHOD}",
        f"**Seats:** {len(rows_out)}",
        "",
        "## Status counts",
        "",
        "| Status | Count |",
        "|--------|------:|",
        f"| FOUND | {found} |",
        f"| EMPTY | {empty} |",
        f"| UNCERTAIN | {uncertain} |",
        "",
        "## Per seat",
        "",
        "| Contact_name | Firm / domain | Status | Notes |",
        "|--------------|---------------|--------|-------|",
    ]
    for r in rows_out:
        firm = r["Firm"] or r["Domain"]
        note = r["Notes"][:80] + ("…" if len(r["Notes"]) > 80 else "")
        md.append(
            f"| {r['Contact_name']} | {firm} | {r['Status']} | {note} |"
        )
    md.extend(
        [
            "",
            "## Deliverables",
            "",
            "- `input.csv` — Monday export (5 seats)",
            "- `results.csv` — one row per seat",
            "- `stamp-list.json` — FOUND only (empty this run)",
            "- `evidence/` — HTML snapshots + excerpt notes",
            "- `CLOSEOUT.md` — run summary",
        ]
    )
    (ROOT / "results.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    closeout = [
        "# CLOSEOUT — Mail Finder Wave5 L02 Arm 08",
        "",
        "## Counts",
        "",
        f"- **FOUND:** {found}",
        f"- **EMPTY:** {empty}",
        f"- **UNCERTAIN:** {uncertain}",
        f"- **Total seats:** {len(rows_out)}",
        "",
        "## Notes",
        "",
        "- First-party Team/About/People/Contact (and firm bios) only; no Hunter/Apollo/LinkedIn scrape.",
        "- Generic inboxes (`info@turn8.co`, `contacto@urbanfarmerspro.com`) not stamped.",
        "- Juan Franck confirmed on SBLA `/team/` via Gatsby page-data; site publishes no person mailto.",
        "- Julio Vasconcellos on Atlantico `/about-us` without mailto (consistent with prior Wave4 L02 arm-08 Atlantico checks).",
        "- No Monday writes performed.",
        "",
        "## Artifacts",
        "",
        "- Crawl log: `scripts/crawl_results.json`",
        "- Crawl helper: `scripts/crawl_team_mailto.py`",
    ]
    (ROOT / "CLOSEOUT.md").write_text("\n".join(closeout) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
