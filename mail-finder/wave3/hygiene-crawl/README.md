# Mail Finder — Wave3 Hygiene Crawl (Arm 5)

Hygiene-gated, search-seed-only first-party email discovery for the Wave3 hygiene batch.

## Contents

| File | Purpose |
|------|---------|
| `input.csv` | Source seats from Monday export |
| `results.csv` | Per-seat Status, Email, Checked_URLs |
| `summary.md` | Run scorecard and notes |
| `stamp-list.json` | FOUND emails only (Monday stamp draft) |
| `website-corrections.json` | Blank Website field corrections (`link_mm7gdv8s`) |
| `evidence/` | Saved first-party HTML + per-seat `crawl_*.json` |
| `scripts/hygiene_crawl.py` | Crawl runner |
| `scripts/finalize_deliverables.py` | Assemble CSV/JSON/MD |

## Re-run

```bash
cd mail-finder/wave3/hygiene-crawl
python3 scripts/hygiene_crawl.py
python3 scripts/finalize_deliverables.py
```

## Rules

- Write path exclusive to this directory.
- No Monday API writes from this arm.
- FOUND requires person name + `mailto:` person@firm on same first-party page.
