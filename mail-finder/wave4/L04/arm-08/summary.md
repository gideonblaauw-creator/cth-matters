# Wave4 L04 Arm 08 — Scorecard

**Method:** Public **SEC EDGAR** exhibits, **Form D**, and filing **signature blocks** — **FOUND** only when the seat **name** and **exact published person@firm** co-occur in the **same public filing artifact**. Generics and name/email split across documents → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, SMTP verify, or Monday writes.

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Per seat

| Monday_item_id | Name | Firm | Status | Notes |
|----------------|------|------|--------|-------|
| 13100496455 | Anna Raptis | Amplifica Capital | EMPTY | Form D signer; no email in XML |
| 13100509893 | Aquilino Peña | Kibo Ventures | EMPTY | No Kibo Ventures issuer on EDGAR |
| 13028370676 | Asia Agnelli | TMV | EMPTY | Form D lists other GPs; Agnelli absent; no @tmv.vc |
| 13028372799 | Belkacem Hammoulhadj | Greenbull Group | EMPTY | 0 EDGAR hits for name/domain |
| 13028366580 | Benjamin Radomski | BEV Family Office | EMPTY | 0 EDGAR hits for name/domain |

## Artifacts

- `input.csv` — 5 seats (Monday export)
- `results.csv` — all seats, non-blank `Checked_URLs`
- `stamp-list.json` — empty (`items: []`)
- `evidence/` — Form D XML copies + search audit notes

**Processed:** 2026-09-25 (UTC)
