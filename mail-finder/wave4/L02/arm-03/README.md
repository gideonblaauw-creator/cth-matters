# Mail Finder — Wave4 / L02 / Arm 03

**Focus:** First-party **team/people mailto discovery** (Website already set in Monday — no Website backfill in this arm).

## Input

`input.csv` — 4 seats: Monday_item_id, Name, Contact_name, Firm, Kind, Priority, Status, Website, Domain, LinkedIn.

## Method

For each seat:

1. Crawl the firm **Website** and standard paths: `/team`, `/people`, `/about`, `/our-team`, `/leadership` (and same-domain team subpages discovered from HTML).
2. Scan **page source** for `mailto:` (and visible firm-domain emails) with **display-name co-occurrence** in the same HTML block/window.
3. Record **FOUND** only for citation-grade **person@firm** (non-generic) cites. Generics → treat as **EMPTY** for email purposes.
4. Follow same-domain person profile links when slug/name appears in team HTML.

## Forbidden

- Hunter, Apollo, LinkedIn scrape, pattern guessing, SMTP verify, invented emails
- Monday API writes (workbench uses `stamp-list.json` only)
- Writes outside `mail-finder/wave4/L02/arm-03/`

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat Status, Checked_URLs, Notes |
| `stamp-list.json` | FOUND emails for Monday email column (HITL) |
| `summary.md` | Scorecard |
| `evidence/` | HTML snapshots + excerpts (FOUND or negative cite) |
| `scripts/crawl_team_mailto.py` | Automated path crawl + mailto scan (audit trail) |

## Status values (`results.csv`)

- **FOUND** — Person email with first-party name co-occurrence
- **EMPTY** — No citation-grade person email on crawled first-party pages

Protocol: `mail-finder/protocol/Mail-Finder-Workbench-Strategy.md`.
