# Mail Finder — Wave5 / L03 / Arm 08

**Focus:** Public **impact reports**, **DocuSign-adjacent fund filings**, **ethics/adviser materials**, **LP/whitepaper PDFs**, and **fund documents** where a named person and `person@firm` mailbox co-occur in the same artifact.

## Input

- `input.csv` — 5 seats (Monday export).

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`); non-blank `Checked_URLs` |
| `results.md` | Scorecard |
| `stamp-list.json` | FOUND only — not written to Monday from this arm |
| `CLOSEOUT.md` | Counts and run notes |
| `evidence/` | Citations, Form D snapshots, scanned PDFs |

## Scope

Write **only** under `mail-finder/wave5/L03/arm-08/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Result: **0 FOUND / 5 EMPTY**
