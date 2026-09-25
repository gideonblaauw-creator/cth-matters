# Mail Finder — Wave4 Loop L02 Arm 02

**Focus:** First-party firm website crawl for **name + person@firm `mailto:`** co-occurrence (team / people / about paths).

## Input

- `input.csv` — Monday export (`Monday_item_id`, `Name`, `Contact_name`, `Firm`, `Kind`, `Priority`, `Status`, `Website`, `Domain`, `LinkedIn`)

## Method (this arm)

1. **Public HTTP only** — fetch Monday `Website` and standard team paths: `/`, `/team`, `/people`, `/about`, `/our-team`, `/leadership`, plus seat-specific paths when discovered (e.g. Seneca `/about-us/the-team/`).
2. **FOUND** — citation-grade `person@firm` where the same first-party HTML block/page shows the contact **display name** and a **non-generic** `mailto:` (or visible `@domain` email) together.
3. **Generics → not FOUND** — `info@`, `hello@`, `team@`, `impact@`, `infocolombia@`, regional inboxes, etc. without person co-occurrence → treat seat as **EMPTY** for this arm.
4. **Website column** — read-only; note NXDOMAIN/parked only (this batch: all seeds already had live URLs).
5. **Prohibited** — no Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP verify, invented emails, or Monday API writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `FOUND` / `EMPTY` / `UNCERTAIN`, checked URLs, notes |
| `stamp-list.json` | FOUND emails for workbench Monday stamp (empty this run) |
| `summary.md` | Scorecard |
| `evidence/` | HTML/text excerpts for FOUND rows only |
| `scripts/scan_team_emails.py` | Reproducible crawl + co-occurrence scan |
| `scripts/team_email_scan.json` | Machine-readable crawl log |

## Run metadata

- Processed: 2026-09-25 (UTC)
- Repo path: `mail-finder/wave4/L02/arm-02/` (exclusive write path)
