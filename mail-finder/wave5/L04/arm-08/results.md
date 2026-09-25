# Mail Finder — Wave5 L04 Arm 08 — Regulatory with mailbox

**Method:** Public regulatory filings / registries / adviser disclosures that contain mailboxes (SEC EDGAR & IAPD, BCSC, CVM/CNPJ, CNMV, comparable primary HTML/PDF). **FOUND** only when **Contact_name** and exact **person@firm** email co-occur in the **same** regulatory artifact.

| Metric | Count |
|--------|------:|
| Seats | 5 |
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Per-seat

| Monday_item_id | Contact_name | Firm | Status | Notes |
|----------------|--------------|------|--------|-------|
| 13132419415 | Steven Lambe | Trinity Capital | EMPTY | No EDGAR/BCSC artifact binds Lambe to a non-generic trincap/trinity mailbox |
| 13132447195 | Tiago Wigman | L4 Venture Builder | EMPTY | CNPJ/CVM name present; no personal email on same regulatory record |
| 13132420166 | Will Poole | Capria Ventures | EMPTY | Form D / IAPD ADV — officer names without person emails |
| 13132423031 | William A. Mejia | Arrebol Capital | EMPTY | No EDGAR/IAPD/BCSC regulatory hit with name + personal email |
| 13132447354 | Bobby Aitkenhead | IDC Ventures | EMPTY | No CNMV/SEC regulatory artifact with name + personal email |

## Artifacts

- `input.csv` — seed export (5 seats)
- `results.csv` — full run log with `Checked_URLs`
- `stamp-list.json` — empty (no FOUND)
- `evidence/` — negative audit notes

**Processed:** 2026-09-25 (UTC)
