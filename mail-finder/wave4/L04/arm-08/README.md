# Mail Finder — Wave4 / L04 / Arm 08

**Focus:** SEC EDGAR **exhibits**, **Form D**, and **signature blocks** — discover citation-grade **person@firm** emails with **published local-part spelling** on the same filing artifact as the seat name.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. **SEC EDGAR EFTS** (`efts.sec.gov/LATEST/search-index`) — person name, firm/fund name, `@domain`.
2. **Form D primary XML** — related-person tables and `/s/` signature blocks (disambiguate with firm/target).
3. **Exhibits / registration statements** — 8-K, S-1, 20-F, 13D exhibits when EFTS links issuer to seat firm.
4. **FOUND gate:** name + non-generic `person@firm` in the **same** public filing; record stable archive URL + excerpt (+ page/section when applicable).
5. **Generics** (`info@`, `team@`, IR/PR on unrelated issuers) → **EMPTY**.

## Prohibited

Pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, paid/authenticated sources, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`), `Checked_URLs`, notes |
| `stamp-list.json` | FOUND only — `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | Form D snapshots and negative audit excerpts |

## Scope

Write **only** under `mail-finder/wave4/L04/arm-08/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l04-arm08-5a22`
- Result: **0 FOUND / 5 EMPTY**
