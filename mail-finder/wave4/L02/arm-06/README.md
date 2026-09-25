# Mail Finder — Wave 4 / L02 / Arm 06

**Focus:** First-party team/people **`mailto:`** discovery (name + person@firm co-occurrence).  
**Write path:** `mail-finder/wave4/L02/arm-06/` only. **Website column already set** — no website backfill in this arm.

## Input

`input.csv` — 4 seats (Monday export): Monday_item_id, Name, Contact_name, Firm, Kind, Priority, Status, Website, Domain, LinkedIn.

## Method

1. Crawl **firm domain only** (public HTTP) from the Monday Website origin.
2. Seed paths: `/`, `/team`, `/people`, `/about`, `/about-us`, `/our-team`, `/leadership`, `/contact`, plus limited BFS on team-like internal links.
3. Parse page source for `mailto:` links; require **non-generic** local part on **firm domain** and **name co-occurrence** on the same page/nearby block.
4. **FOUND** → record email + source URL in `results.csv` and `stamp-list.json`.
5. **EMPTY** → no email; generics (`info@`, `hello@`, `enquiries@`, `IR@`, etc.) do not qualify.

## Prohibited

Hunter/Apollo, LinkedIn scrape, email pattern invention, SMTP verify, Monday API writes from this arm.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat FOUND/EMPTY, checked URLs, notes |
| `stamp-list.json` | FOUND rows for workbench Monday email stamp (empty if none) |
| `summary.md` | Scorecard |
| `evidence/` | HTML snapshots and `crawl_report.json` |
| `scripts/crawl_team_mailto.py` | Crawl runner |

## Re-run

```bash
python3 scripts/crawl_team_mailto.py
```

Then adjudicate hits manually if the crawler flags candidates (this batch: 0 FOUND).
