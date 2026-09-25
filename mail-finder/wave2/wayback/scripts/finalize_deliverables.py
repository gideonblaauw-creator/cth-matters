#!/usr/bin/env python3
"""Write results.md and first-found-evidence.md from results.csv."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results.csv"


def main():
    rows = list(csv.DictReader(RESULTS.open(encoding="utf-8")))
    counts = {}
    for r in rows:
        counts[r["Status"]] = counts.get(r["Status"], 0) + 1

    md = f"""# Mail Finder Wave2 — Wayback CDX arm

Board **18425305222** · Input: `input.csv` ({len(rows)} deep50 EMPTY seats).

**Primary method:** Internet Archive CDX API on each seat `Domain` for paths matching `/team`, `/about`, `/people`, `/leadership`, `/contact`, `/our-team` (and equivalents); fetch `id_` snapshots; parse HTML source for `mailto:` + name co-occurrence. Generics → EMPTY; no live deep-crawl except one retry when snapshot truncated.

Hard rules: citation-grade only; no Hunter/Apollo/LinkedIn scrape/pattern guessing.

## Status counts

| Status | Count |
|--------|------:|
"""
    for st in ("FOUND", "EMPTY", "HOLD", "UNCERTAIN", "DOMAIN_UNRESOLVED"):
        if counts.get(st):
            md += f"| {st} | {counts[st]} |\n"

    found = [r for r in rows if r["Status"] == "FOUND"]
    md += "\n## FOUND (stamp list)\n\n"
    if found:
        for r in found:
            md += f"- **{r['Name']}** — `{r['Email']}` — [{r['Source_URL']}]({r['Source_URL']})\n"
    else:
        md += "_None this pass — no citation-grade name + person@firm on archived team/about pages._\n"

    md += """
## Per-seat summary

| Monday_item_id | Name | Domain | Status | Notes (abbrev.) |
|----------------|------|--------|--------|-----------------|
"""
    for r in rows:
        note = (r["Notes"] or "")[:120].replace("|", "/")
        md += f"| {r['Monday_item_id']} | {r['Name']} | {r['Domain']} | {r['Status']} | {note}… |\n"

    md += """
## Artifacts

- `results.csv` — all input seats
- `found-for-monday.csv` — FOUND rows only (empty if none)
- `first-found-evidence.md` — evidence blocks for FOUND
- `html/` — saved Wayback snapshot sources reviewed this pass
- `scripts/run_wayback_cdx.py` — CDX + snapshot parser

CDX queries logged in each row `Checked_URLs` (first entry is the CDX API URL for the seat domain).
"""

    (ROOT / "results.md").write_text(md, encoding="utf-8")

    ev = [
        "# Wave2 Wayback — first-found evidence",
        "",
        "No **FOUND** rows in this arm. No Monday stamp list entries.",
        "",
        "Reviewed snapshots with only generic firm mailto (examples):",
        "- `congruentvc.com` contact snapshots — `info@`, `investors@`",
        "- `mourocapital.com` contact-us — `info@mourocapital.com`",
        "- `turn8.co` contact — `contact@turn8.co`",
        "- `crossboundary.com` advisory/contact — generic `contact@` pattern on live; archived our-team fragments without person mailto",
        "",
        "**HOLD** (LinkedIn-primary on team listing, no archived person mailto):",
    ]
    for r in rows:
        if r["Status"] == "HOLD":
            ev.append(f"- {r['Name']} ({r['Domain']}) — {r['Notes'][:200]}")
    ev.append("")
    (ROOT / "first-found-evidence.md").write_text("\n".join(ev), encoding="utf-8")
    print(counts)


if __name__ == "__main__":
    main()
