#!/usr/bin/env python3
"""Build results.csv, FOUND.md, EMPTY.md, and evidence excerpts from crawl_results.json."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CRAWL = ROOT / "scripts" / "crawl_results.json"
INPUT = ROOT / "input.csv"
EVIDENCE = ROOT / "evidence"

SEAT_NOTES = {
    "13151897907": (
        "bii.co.uk returns Cloudflare 403 on all crawled Team/About/People paths from this "
        "environment; unable to retrieve page-source for Amal-Lee Amin attribution."
    ),
}


def checked_urls_str(checked):
    seen = set()
    out = []
    for entry in checked:
        key = entry.split(" (")[0]
        if key in seen:
            continue
        seen.add(key)
        out.append(entry)
    return " | ".join(out)


def slug(name: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9]+", "-", name.lower()).strip("-")
    return name[:60] or "person"


def main():
    crawl = json.loads(CRAWL.read_text(encoding="utf-8"))
    input_rows = {r["Monday_item_id"]: r for r in csv.DictReader(INPUT.open())}

    results_rows = []
    found_entries = []

    for item in crawl:
        mid = item["Monday_item_id"]
        inp = input_rows[mid]
        hits = item.get("hits") or []
        checked = item.get("checked_urls") or []

        if hits:
            h = hits[0]
            status = "FOUND"
            email = h["email"]
            evidence_url = h["source_url"]
            notes = "Name + person@firm co-occurrence on first-party page (published spelling)."
            excerpt_path = EVIDENCE / f"{slug(item['Contact_name'])}-excerpt.md"
            excerpt_path.write_text(
                "\n".join(
                    [
                        f"# {item['Contact_name']} — {inp.get('Firm', '')}",
                        "",
                        f"**Monday_item_id:** {mid}",
                        f"**Email:** {email}",
                        f"**Evidence URL:** {evidence_url}",
                        "",
                        "## Excerpt",
                        "",
                        h.get("excerpt", ""),
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            found_entries.append(
                {
                    "name": item["Contact_name"],
                    "firm": inp.get("Firm", ""),
                    "domain": item["Domain"],
                    "mid": mid,
                    "email": email,
                    "evidence_url": evidence_url,
                    "excerpt": h.get("excerpt", ""),
                    "excerpt_file": excerpt_path.name,
                }
            )
        elif item.get("linkedin_only_signal"):
            status = "UNCERTAIN"
            email = ""
            evidence_url = ""
            notes = (
                "Name on first-party team/about page with LinkedIn only; "
                "no mailto or published person@firm on same artifact — HOLD (no stamp)."
            )
        else:
            status = "EMPTY"
            email = ""
            evidence_url = ""
            notes = SEAT_NOTES.get(mid) or (
                f"No citation-grade {item['Contact_name']} + person@{item['Domain']} "
                "co-occurrence on crawled Team/About/People/Contact paths."
            )

        results_rows.append(
            {
                "Name": item["Name"],
                "Firm": inp.get("Firm", ""),
                "Domain": item["Domain"],
                "Monday_item_id": mid,
                "Status": status,
                "Email": email,
                "Evidence_URL": evidence_url,
                "Checked_URLs": checked_urls_str(checked),
                "Notes": notes,
            }
        )

    fieldnames = [
        "Name",
        "Firm",
        "Domain",
        "Monday_item_id",
        "Status",
        "Email",
        "Evidence_URL",
        "Checked_URLs",
        "Notes",
    ]
    with (ROOT / "results.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(results_rows)

    found_n = sum(1 for r in results_rows if r["Status"] == "FOUND")
    empty_n = sum(1 for r in results_rows if r["Status"] == "EMPTY")
    uncertain_n = sum(1 for r in results_rows if r["Status"] == "UNCERTAIN")

    found_md = [
        "# MF LI enrich-26 Arm A — FOUND (team person mailto)",
        "",
        f"**Date:** 2026-09-28 | **Seats with FOUND:** {found_n}",
        "",
        "Attribution: Name + person@firm on same first-party Team/About/People/Contact artifact.",
        "",
    ]
    if found_entries:
        for e in found_entries:
            found_md.extend(
                [
                    f"## {e['name']} ({e['firm']})",
                    "",
                    f"- **Monday_item_id:** {e['mid']}",
                    f"- **Domain:** {e['domain']}",
                    f"- **Email:** `{e['email']}`",
                    f"- **Evidence URL:** {e['evidence_url']}",
                    f"- **Excerpt file:** `evidence/{e['excerpt_file']}`",
                    "",
                    "> " + e["excerpt"][:350].replace("\n", " "),
                    "",
                ]
            )
    else:
        found_md.append("_(No FOUND seats in this batch.)_\n")

    (ROOT / "FOUND.md").write_text("\n".join(found_md) + "\n", encoding="utf-8")

    empty_md = [
        "# MF LI enrich-26 Arm A — EMPTY / UNCERTAIN summary",
        "",
        f"**Processed:** {len(results_rows)} seats",
        "",
        "## Counts",
        f"- FOUND: **{found_n}**",
        f"- EMPTY: **{empty_n}**",
        f"- UNCERTAIN: **{uncertain_n}**",
        "",
        "## EMPTY seats",
        "",
    ]
    for r in results_rows:
        if r["Status"] == "EMPTY":
            empty_md.append(
                f"- **{r['Name']}** ({r['Firm']}, `{r['Domain']}`) — {r['Monday_item_id']}"
            )
    empty_md.extend(["", "## UNCERTAIN seats", ""])
    for r in results_rows:
        if r["Status"] == "UNCERTAIN":
            empty_md.append(
                f"- **{r['Name']}** ({r['Firm']}, `{r['Domain']}`) — {r['Monday_item_id']}: {r['Notes']}"
            )
    if uncertain_n == 0:
        empty_md.append("_(none)_")
    empty_md.extend(
        [
            "",
            "## Method",
            "First-party Team / About / People / Contact page-source only; mailto or visible person@firm.",
            "No Hunter/Apollo, pattern+SMTP, LinkedIn scrape, or invented emails.",
            "",
            "**Monday:** No API writes (workbench stamps after HITL review).",
        ]
    )
    (ROOT / "EMPTY.md").write_text("\n".join(empty_md) + "\n", encoding="utf-8")

    print(f"FOUND={found_n} EMPTY={empty_n} UNCERTAIN={uncertain_n}")


if __name__ == "__main__":
    main()
