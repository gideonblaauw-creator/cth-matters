# Mail Finder — Wave4 / L05 / Arm 08

**Focus:** Public **impact reports**, **LP materials**, **annual reports**, and comparable **PDFs** where a named person and `person@firm` mailbox co-occur in the same document.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. Enumerate first-party PDFs (issuer/fund site, WP media API, sitemap HTML hrefs).
2. Pull comparable public PDFs (e.g. WWF/GEF evaluation reports naming Seneca advisors).
3. Extract text with `pdftotext`; require **printed name + exact person@firm email** in the same PDF block.
4. Record stable PDF URL, page/heading when available, and verbatim excerpt.
5. **Generics** (`impact@`, `communications@`, `info@`, role-only inboxes) → **EMPTY**.

## Prohibited

Pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, paid/authenticated sources, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`); non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only — `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | PDF snapshots and excerpts |

## Scope

Write **only** under `mail-finder/wave4/L05/arm-08/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l05-arm08-2235`
- Result: **1 FOUND / 4 EMPTY**
