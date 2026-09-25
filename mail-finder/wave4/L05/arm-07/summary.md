# Wave4 L05 Arm 07 — Impact / LP / annual-report PDFs

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`)  
**Method:** Public first-party and industry PDFs (impact reports, LP/ecosystem materials, annual reports, issuer press kits). **FOUND** only when the target person’s published name and an exact `person@firm` email co-occur in the **same PDF**. Generics and third-party contact blocks → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, SMTP verify, invented emails, or Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm | Outcome |
|----------------|------|------|---------|
| 13028358383 | Humberto Matsuda | Overboost | EMPTY — no qualifying PDF; site generic speed@overboost.me not person-bound |
| 13114411690 | Igor Piquet | Endeavor Catalyst | EMPTY — Colombia informe + LAVCA PDFs name Piquet without @endeavor.org on same PDF |
| 13100506451 | Ingo Ramesohl | Bosch Ventures / RBVC | EMPTY — Bosch press kit pairs Ramesohl with spokesperson email, not person@rbvc.com |
| 13100503653 | J.P. Keating | proChain Ventures | EMPTY — no Form D / LP PDF with Keating + @prochain.vc |
| 13028358308 | James Todd, CFA | Oikocredit | EMPTY — annual/impact/VZW PDFs: Todd named or quoted without person@oikocredit.org |

## Artifacts

- `results.csv`, `stamp-list.json` (empty), `README.md`, `evidence/` (PDF text extracts, `url-index.md`, `negative-excerpts.md`, EDGAR query JSON where applicable)
