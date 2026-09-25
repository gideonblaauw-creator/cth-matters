# Wave4 L03 Arm 03 — Regulatory / securities PDF email discovery

**Batch:** 5 seats (4× P2, 1× P1)  
**Method:** Public regulatory corpora — SEC EDGAR EFTS full-text, Form D / signature blocks, SEC IAPD Form ADV PDFs, BCSC document search, SEDAR+ (web), national securities filing indexes. **FOUND** only when **display name + person@firm** co-occur in the **same** public PDF/filing text (published spelling). Generics → **EMPTY**.

## Scorecard

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |

## Per seat

| Name | Domain | Outcome |
|------|--------|---------|
| Andrii Hordiichuk | biosingularity.world | No SEC/BCSC regulatory PDF with name + firm email |
| Matteo Scalabrino | rockefellerfoundation.org | No EDGAR PDF with name + person@firm (RFCC / Foundation) |
| Elvia Gomez | acumen.org | No SEC/SEDAR+ securities PDF for Acumen.org seat |
| Emma Haight | glenarapartners.com | UK LLP; no securities PDF; SEC Glenara hits wrong entity |
| Alejandro Arenas | cim-llc.com | CIM Form D/ADV name roster without Arenas; no person emails in ADV |

## Monday stamping

`stamp-list.json` is empty (no citation-grade FOUND). Route EMPTY seats to ReachGate per protocol. **No Monday writes** from this agent.

## Evidence

Negative regulatory audit trail under `evidence/` (Form D / ADV excerpts, EFTS query log). No FOUND rows — no person-email PDF snapshots required.

## Cross-lane note

L02 Arm 03 (team/mailto crawl) on the same four P2 names also returned 0 FOUND; this arm applies the regulatory PDF gate independently (includes P1 Alejandro Arenas / CIM).
