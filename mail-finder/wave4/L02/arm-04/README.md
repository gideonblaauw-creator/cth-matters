# Mail Finder — Wave4 / L02 / Arm 04

**Arm:** First-party firm website — team/people **mailto:** + name co-occurrence  
**Write path:** `mail-finder/wave4/L02/arm-04/` only  

## Inputs

- `input.csv` — 4 seats exported from Monday (Website column pre-filled; not modified here)

## Method (hard rules)

- Public HTTP GET only on firm domain paths
- Stamp **only** when a `mailto:` (or Cloudflare `data-cfemail` decoding to mailto-equivalent) on the same page/block co-occurs with the seat’s display name and is **not** a generic inbox (`info@`, `hello@`, etc.)
- No Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP checks, or invented emails
- No Monday API writes from this arm

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Full attribution row per seat |
| `stamp-list.json` | Post-review stamp intents (email column only when FOUND) |
| `summary.md` | Batch yield summary |
| `evidence/` | HTML snapshots, crawl JSON, text excerpts |
| `crawl_arm04.py` | Reproducible crawler for this arm |

## Re-run

```bash
cd mail-finder/wave4/L02/arm-04
python3 crawl_arm04.py
```

Then refresh seat-specific notes in `results.csv` / excerpts if manual review adds context.
