# Mail Finder — Wave3 Arm 1 (regulatory_pdf)

Search-seed only arm for 12 Teclogi VC/CVC seats (`input.csv`).

## Method

Public regulatory corpora only (no pattern guessing, no Hunter/Apollo, no LinkedIn scrape):

- SEC EDGAR + EFTS full-text (`efts.sec.gov`)
- SEC IAPD Form ADV brochures (`reports.adviserinfo.sec.gov`)
- Form D / EX-10 signature blocks
- BCSC document search (HTML)
- CVM public fund/participant listings (`cvmweb.cvm.gov.br`)
- CNMV entity portal (Telefónica/BBVA)

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat status and checked URLs |
| `summary.md` | Counts + FOUND table |
| `stamp-list.json` | Monday workbench import (`email_mm7ffmz4`) — FOUND only |
| `evidence/` | Negative or partial regulatory excerpts |

## Result

**0 FOUND** — no citation-grade person@firm from regulatory sources for this seed list in this pass.

## Monday

Do **not** stamp from this agent; hand `stamp-list.json` to workbench when FOUND rows exist.
