#!/usr/bin/env python3
"""Build results.csv, stamp-list.json, results.md, CLOSEOUT.md from crawl_results.json."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CRAWL = ROOT / "scripts" / "crawl_results.json"
INPUT = ROOT / "input.csv"
METHOD = "wave5-L02-arm04-team-mailto"

NOTES = {
    "13114460590": (
        "collidecap.com/teams lists Elias Mufarech (Principal) with LinkedIn link only; "
        "footer mailto is generic general@collidecap.com — excluded, not name-co-attributed."
    ),
    "13028359480": (
        "acumen.org/team/elvia-gomez/ (200) shows Elvia Gómez bio; no mailto and no "
        "person@acumen.org in page source. acumen.org/team/ index likewise has no personal mailto."
    ),
    "13028399382": (
        "glenarapartners.com/Team/ lists Emma Haight (Managing Partner) with bio modal; "
        "no mailto and no @glenarapartners.com in HTML."
    ),
    "13028370265": (
        "tech.manacommon.com/team/etienne-gillard/ (200) bio for Etienne Gillard; "
        "about-us/ and contact-us/ have no person mailto. No @tech.manacommon.com mailto on crawled paths."
    ),
    "13028371139": (
        "www.axel-carbon.com homepage lists Federico Giannetti (Co-founder & general partner); "
        "LinkedIn icon only — no mailto and no @axel-carbon.com on crawled first-party paths."
    ),
}


def checked_urls_str(checked):
    seen = set()
    out = []
    for entry in checked:
        if "oembed" in entry or "wp-json" in entry:
            continue
        key = entry.split(" (")[0]
        if key in seen:
            continue
        seen.add(key)
        out.append(entry)
    return " | ".join(out)


def main():
    crawl = json.loads(CRAWL.read_text(encoding="utf-8"))
    input_rows = {r["Monday_item_id"]: r for r in csv.DictReader(INPUT.open())}

    results_rows = []
    stamps = []

    for item in crawl:
        mid = item["Monday_item_id"]
        inp = input_rows[mid]
        hits = item.get("hits") or []
        checked = item.get("checked_urls") or []
        if hits:
            h = hits[0]
            status = "FOUND"
            email = h["email"]
            source_url = h["source_url"]
            notes = f"First-party page: {h.get('excerpt', '')[:280]}"
            stamps.append(
                {
                    "monday_item_id": mid,
                    "email": email,
                    "source_url": source_url,
                    "excerpt": h.get("excerpt", "")[:500],
                }
            )
        else:
            status = "EMPTY"
            email = ""
            source_url = ""
            notes = NOTES.get(mid) or (
                f"No citation-grade {item['Contact_name']} + person@{item['Domain']} "
                f"co-occurrence on crawled Team/About/People/Contact paths."
            )

        results_rows.append(
            {
                "Monday_item_id": mid,
                "Name": item["Name"],
                "Contact_name": item["Contact_name"],
                "Firm": inp.get("Firm", ""),
                "Domain": item["Domain"],
                "Priority": item.get("Priority", inp.get("Priority", "")),
                "Email": email,
                "Email_type": "work" if email else "",
                "Confidence": "HIGH" if email else "",
                "Source_URL": source_url,
                "Checked_URLs": checked_urls_str(checked),
                "Status": status,
                "Notes": notes,
                "Method": METHOD,
            }
        )

    fieldnames = [
        "Monday_item_id",
        "Name",
        "Contact_name",
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
    with (ROOT / "results.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(results_rows)

    (ROOT / "stamp-list.json").write_text(
        json.dumps(stamps, indent=2), encoding="utf-8"
    )

    found = sum(1 for r in results_rows if r["Status"] == "FOUND")
    empty = sum(1 for r in results_rows if r["Status"] == "EMPTY")
    uncertain = sum(1 for r in results_rows if r["Status"] == "UNCERTAIN")

    md = [
        "# Mail Finder Wave5 L02 Arm 04 — Team person mailto",
        "",
        "Method: first-party Team / About / People / Contact pages and firm bios.",
        "",
        "## Counts",
        f"- Seats: **{len(results_rows)}**",
        f"- FOUND: **{found}**",
        f"- EMPTY: **{empty}**",
        f"- UNCERTAIN: **{uncertain}**",
        "",
        "## Per seat",
        "",
        "| Monday_item_id | Contact_name | Domain | Status | Email |",
        "| --- | --- | --- | --- | --- |",
    ]
    for r in results_rows:
        md.append(
            f"| {r['Monday_item_id']} | {r['Contact_name']} | {r['Domain']} | "
            f"{r['Status']} | {r['Email'] or '—'} |"
        )
    if stamps:
        md.extend(["", "## FOUND evidence", ""])
        for s in stamps:
            md.append(f"- **{s['email']}** — [{s['source_url']}]({s['source_url']})")
            md.append(f"  - Excerpt: {s['excerpt'][:200]}…")
    else:
        md.extend(["", "## FOUND evidence", "", "_(none)_"])
    md.extend(["", "**Monday:** No API writes (`stamp-list.json` for HITL only)."])
    (ROOT / "results.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    closeout = [
        "# CLOSEOUT — Wave5 L02 Arm 04",
        "",
        f"- Processed: {len(results_rows)} / 5 seats",
        f"- FOUND: {found}",
        f"- EMPTY: {empty}",
        f"- UNCERTAIN: {uncertain}",
        "",
        "## Notes",
        "- Exclusive path: `mail-finder/wave5/L02/arm-04/`",
        "- No Monday writes performed.",
        "- Generics (`general@`, `info@`, etc.) excluded per protocol.",
    ]
    if empty == len(results_rows):
        closeout.append(
            "- All seats lack first-party name + personal mailto co-occurrence on "
            "crawled team/about/contact paths (consistent with prior Wave4 L02 passes "
            "on overlapping names where applicable)."
        )
    (ROOT / "CLOSEOUT.md").write_text("\n".join(closeout) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
