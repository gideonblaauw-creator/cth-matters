# Wave5 L04 Arm 01 — Regulatory with mailbox (scorecard)

**Method:** Public regulatory filings / registries / adviser disclosures with mailboxes (SEC EDGAR exhibits & Form D, IAPD Form ADV, FCA MIFIDPRU-class PDFs, IFC project disclosures). **FOUND** only when **Contact_name** and exact **person@firm** e-mail appear in the **same** public regulatory artifact.

**Run date (UTC):** 2026-09-25  
**Seats:** 5

| Status | Count |
|--------|------:|
| FOUND | 1 |
| EMPTY | 4 |
| UNCERTAIN | 0 |

| Monday_item_id | Contact_name | Firm | Status | Email (if FOUND) |
|----------------|--------------|------|--------|------------------|
| 13132419392 | Dayna Grayson | Construct Capital | EMPTY | — |
| 13132420194 | Francesco Filia | Fasanara Capital | EMPTY | — |
| 13132447865 | Hemant Taneja | General Catalyst | FOUND | htaneja@generalcatalyst.com |
| 13132419461 | Itai Tsiddon | LGVP | EMPTY | — |
| 13132419984 | Jaime Zunzunegui | Nazca | EMPTY | — |

## Acceptance

- Every seed row appears exactly once in `results.csv`.
- All rows have non-blank `Checked_URLs`.
- One FOUND row with matching `stamp-list.json` entry and citation excerpt under `evidence/`.
- No Monday writes.
