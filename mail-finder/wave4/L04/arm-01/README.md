# Mail Finder — Wave4 / L04 / Arm 01

**Focus:** SEC EDGAR **exhibits**, **Form D** filings, and **signature / related-person blocks** — FOUND only when the same public artifact contains the target person’s published name and an exact **person@firm** email (local-part spelling preserved).

## Input

- `input.csv` — 5 P1 seats (Monday export).

## Method (per seat)

1. **SEC EFTS** — phrase and domain searches to locate filing families tied to the firm / person.
2. **Form D XML / submission text** — `relatedPersonsList`, issuer identity, `signatureName` blocks (Form D rarely includes email; exhibits may).
3. **8-K / other exhibits** — when EFTS domain hits occur, open the exhibit and verify name + non-generic mailbox co-occurrence.
4. **IAPD Form ADV PDF** — secondary check when adviser CRD maps to seat domain (no individual employee emails when absent from brochure text).
5. **Generics** (`info@`, `ir@`, PR agency domains, etc.) → **EMPTY**.

## Prohibited

Pattern guessing, SMTP verification, Hunter/Apollo, LinkedIn scrape, invented emails, paid/authenticated sources, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`), `Checked_URLs`, notes |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | Downloaded Form D / exhibit snippets; `sec-efts-query-log.json` |

## Scope

Write **only** under `mail-finder/wave4/L04/arm-01/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l04-arm01-bff9`
