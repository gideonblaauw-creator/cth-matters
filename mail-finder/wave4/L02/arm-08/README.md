# Mail Finder — Wave4 / L02 / Arm 08

**Focus:** First-party firm website crawl for **display name + person@firm `mailto:`** co-occurrence (team / people / about paths + page source).

## Input

- `input.csv` — 3 seats with Monday Website already set (no website backfill in this arm).

## Method

1. Crawl each seat’s **Website** domain over standard team paths (`/team`, `/people`, `/about`, `/about-us`, `/our-team`, `/leadership`, `/contact`, …).
2. Parse HTML for `mailto:` links on `@firm` domain; require **name tokens** near the mailto in the same page block.
3. Treat generic locals (`info@`, `hello@`, `team@`, `contact@`, …) as **non-FOUND** (EMPTY for this method).
4. If live crawl blocked (403), one **Wayback** fetch of the Monday Website URL when available.
5. Save snapshots under `evidence/` for audit.

## Prohibited

Hunter/Apollo, LinkedIn scrape, email pattern guessing, SMTP verify, invented addresses, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat Status, Checked_URLs, Notes |
| `stamp-list.json` | FOUND emails only (Monday workbench) |
| `summary.md` | Scorecard |
| `evidence/` | HTML + excerpt notes |

## Scope

Write **only** under `mail-finder/wave4/L02/arm-08/`.
