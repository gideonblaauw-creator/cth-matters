# Wave2 filings-edgar — results summary

**Arm:** SEC EDGAR (Form D/exhibits), Canadian/regulatory PDF search, impact-finance & IFC-style disclosure PDFs. No Hunter/Apollo; no pattern guessing; generics excluded.

## Counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 24 |
| UNCERTAIN | 0 |
| DOMAIN_UNRESOLVED | 1 |
| **Total seats** | **25** |

## Yield notes

- **Zero FOUND** this pass: VC/CVC seats rarely publish person emails in Form D; most hits were name-only signature blocks or generic firm inboxes (`info@`, `investors@`, `legal@`, `comunciacion@`) excluded by protocol.
- **Strongest near-misses (still EMPTY):** Congruent Form D filings with Abraham E. Yokell (address/phone, no email); Valor Latitude SEC PR with Scott Sobel named but contact email belongs to CFO Doug Smith; EIF Ship2B press with Maite Fibla quoted and comms inbox only.
- **DOMAIN_UNRESOLVED:** Fernando Lelo (`rumbo.vc` Monday domain vs `rumbo.ventures` operating site); EDGAR Rumbo SPV CIK 2093599 has no person mailbox.
- **Non-person rows:** Rabobank Partnerships, CrossBoundary (firm) — no named individual to bind to person@firm on filings.

## Method

Primary queries: `efts.sec.gov/LATEST/search-index` per person and `@domain`, plus `filetype:pdf` web targets (BCSC 45-106F1 pattern, IFC/EIF impact disclosures, issuer PDF footers).
