# Wave4 L04 Arm 01 — Scorecard

**Method:** Public SEC EDGAR exhibits, Form D filings, and filing signature / related-person blocks (preserve published local-part spelling).

**Run date (UTC):** 2026-09-25  
**Seats:** 5 (all P1)

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

| Monday_item_id | Name | Domain | Status | Notes |
|----------------|------|--------|--------|-------|
| 13114466566 | Agustin De Luca | lendable.io | EMPTY | Lendable Form D directors; no De Luca; 0× `@lendable.io` in EDGAR |
| 13028369967 | Aidan Madigan-Curtis | eclipse.capital | EMPTY | Portfolio Form D names Director; no email; 0× `@eclipse.capital` |
| 13114444514 | Alejandro Arenas | cim-llc.com | EMPTY | CIM Form D Haar/Hokenson; Oportun EX-99.1 URL-only CIM mention |
| 13028336649 | Bill Driegert | eclipse.capital | EMPTY | 0× `"Bill Driegert"`; Eclipse Form D/ADV silent |
| 13028359226 | Burak Cendek | autotechvc.com | EMPTY | Autotech Fund IV Form D lists Cendek; no person email in artifact |

## Acceptance

- Every seed row appears exactly once in `results.csv`.
- All rows have non-blank `Checked_URLs`.
- No FOUND rows → `stamp-list.json` is empty `[]`.
- Artifacts saved under `evidence/` for negative audit.
