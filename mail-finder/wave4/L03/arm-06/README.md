# Mail Finder — Wave 4 / L03 / Arm 06

**Focus:** Regulatory / securities **PDF** email discovery (BCSC Form 45-106F1, SEDAR/SEDAR+, SEC EDGAR signature blocks, FINRA/IAPD Form ADV brochures where applicable, Form D / offering memoranda).  
**Write path:** `mail-finder/wave4/L03/arm-06/` only. **No Monday API writes** from this arm.

## Input

`input.csv` — 5 seats (Monday export): Monday_item_id, Name, Contact_name, Firm, Kind, Priority, Status, Website, Domain, LinkedIn.

## Method

1. For each seat, search public **regulatory and securities PDFs** (BCSC eServices / document library patterns, SEDAR+, SEC EDGAR full-text, IAPD firm brochures, issuer offering decks filed or published as PDF).
2. Extract text (`pdftotext`) and require **name + non-generic `person@firm`** on the **same PDF** (team/contact or signature block).
3. **FOUND** → record published spelling in `results.csv` and add row to `stamp-list.json`.
4. **EMPTY** → generics-only, name without person mailbox, or no attributable PDF after reasonable registry pass.
5. LinkedIn URLs in input are **context only** — no scrape.

## Prohibited

Hunter/Apollo, LinkedIn scrape, email pattern invention, SMTP verify, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat FOUND/EMPTY, source URL, checked URLs, notes |
| `stamp-list.json` | FOUND rows for workbench Monday email stamp |
| `summary.md` | Scorecard |
| `evidence/` | PDF copies and excerpts for FOUND (and selected EMPTY checks) |

## Result statuses

| Status | Meaning |
|--------|---------|
| `FOUND` | Citation-grade person email from public regulatory/securities PDF |
| `EMPTY` | No attributable person@firm in PDF lane for this wave |
