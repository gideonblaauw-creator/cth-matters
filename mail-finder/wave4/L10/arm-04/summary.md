# Mail Finder — Wave4 / L10 / Arm 04 — Summary

**Processed:** 2026-09-25 (UTC)  
**Branch:** `cursor/mail-finder-wave4-l10-arm04-f0cb`  
**Seats:** 5  
**Method lane:** Public CNPJ (where applicable), SEC **IAPD** Form ADV, **BCSC**-class Canadian securities search, **DocuSign / ethics / compliance PDFs**, plus EDGAR full-text where relevant.

## Scorecard

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

| Monday_item_id | Name | Firm | Status |
|----------------|------|------|--------|
| 13028366345 | Son Nguyen | IIX | EMPTY |
| 13114451331 | Susana Garcia-Robles | Capria Ventures | EMPTY |
| 13100496537 | Séverine Grégoire | ZEBOX / CMA CGM | EMPTY |
| 13028372158 | Tiffany Chen, CFA | Carbon Equity | EMPTY |
| 13100506407 | Tim Rehder | Earlybird | EMPTY |

## Notes

- **IAPD:** Capria (CRD 284129) and Earlybird GmbH (CRD 341941) ADV PDFs list target names on Schedule A but contain **no extractable person@firm emails**.
- **Generics excluded:** `impact@capria.vc`, `grievance@capria.vc`, `ventures@ze-box.io`, `info@earlybird.com`, `iixvietnam@iixglobal.com`, etc. do not qualify under the FOUND gate.
- **CNPJ:** No Brazil-entity PDF tied these seats to a CNPJ publication with name + person@firm.
- **Prior arms:** Press/team methods (L06 arm-08, L03 arm-05) already EMPTY for the same Monday IDs; this arm adds registry/PDF lane coverage without upgrading any seat to FOUND.

## Artifacts

- `results.csv` — full per-seat audit trail  
- `stamp-list.json` — empty (no FOUND)  
- `evidence/negative-excerpts.md` — citation-grade negatives  
- `evidence/url-index.md` — checked URL index  
- `evidence/iapd_adv_alt_*.txt` — Form ADV text extracts  
