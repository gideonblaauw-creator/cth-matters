# Mail Finder — Wave4 / L03 / Arm 04

**Focus:** Regulatory and securities **PDF** email discovery (BCSC Form 45-106F1 class, SEDAR+/provincial filings where searchable, SEC EDGAR full-text, FINRA/IAPD Form ADV, CNMV FCRE prospectuses, UK Companies House PDFs, signature/certification blocks).

## Input

`input.csv` — 5 seats: Monday_item_id, Name, Contact_name, Firm, Kind, Priority, Status, Website, Domain, LinkedIn.

## Method

For each seat:

1. Query **SEC EDGAR** full-text (`efts.sec.gov/LATEST/search-index`) for `"Name"`, `@domain`, and firm strings.
2. Search **BCSC** / `filetype:pdf` dorks for 45-106F1-style certification blocks (name + email + signature).
3. Pull **national registry PDFs** where the entity appears (CNMV for Demium funds, Companies House for UK cos.).
4. Extract text with **`pdftotext`**; require **name + person@firm** on the **same document** (published spelling).
5. **Generics** (`info@`, `hello@`, `legal@`, `admin@`, role inboxes) → **EMPTY** for attribution.

## Forbidden

- Hunter, Apollo, LinkedIn scrape, pattern guessing, SMTP verify, invented emails
- Monday API writes (workbench consumes `stamp-list.json` only)
- Writes outside `mail-finder/wave4/L03/arm-04/`

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat Status, Source_URL, Checked_URLs, Notes, Method |
| `stamp-list.json` | FOUND emails for Monday email column (HITL) |
| `summary.md` | Scorecard |
| `README.md` | This arm spec |
| `evidence/` | PDF excerpts / saved filings (FOUND or negative cite) |

## Status values

- **FOUND** — Citation-grade person@firm from a public regulatory/securities PDF with name co-occurrence
- **EMPTY** — No qualifying PDF cite for this arm

Protocol: `mail-finder/protocol/Mail-Finder-Workbench-Strategy.md`.
