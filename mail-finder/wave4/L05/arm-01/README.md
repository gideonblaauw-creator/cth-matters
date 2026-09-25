# Mail Finder — Wave4 / L05 / Arm 01

**Focus:** Public **impact reports**, **LP materials**, **annual reports**, and comparable PDFs — FOUND only when the same PDF contains the target person’s published name and an exact **person@firm** email (spelling preserved).

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (per seat)

1. Search issuer / fund / impact PDFs (including cross-fund reports such as FLII2025).
2. Crawl first-party sites for `.pdf` links (impact, LP, annual report, ethics decks).
3. Download candidate PDFs and extract text; require **name + person@firm email** on the same citation unit.
4. Generics (`info@`, `contacto@`, `soporte@`, `infocolombia@`, role inboxes without person attribution) → **EMPTY**.
5. HTML pages, Substack posts, and third-party directories are noted in `Checked_URLs` but do **not** satisfy FOUND unless equivalent public PDF evidence exists.

## Prohibited

Pattern guessing, SMTP verification, Hunter/Apollo, LinkedIn scrape, invented emails, paid/authenticated sources, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`), non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | Downloaded PDFs, `pdf-search-log.json`, negative excerpts |

## Scope

Write **only** under `mail-finder/wave4/L05/arm-01/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l05-arm01-369b`
