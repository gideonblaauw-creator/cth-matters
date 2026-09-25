# Wave4 L04 Arm 06 — SEC EDGAR exhibits / Form D / signature blocks

**Scope:** 5 seats from `input.csv`  
**Method:** Public SEC EDGAR — EFTS full-text search, Form D / Form D/A primary documents (`xslFormDX01`), filing exhibits and signature blocks. **FOUND** only when the target person’s published name and an exact **person@firm** email appear in the **same** filing artifact.  
**Prohibited:** Pattern guessing, SMTP verify, Hunter/Apollo, LinkedIn scrape, invented emails, **Monday writes**.

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## FOUND

None.

## Notable near-misses (not stamped)

| Seat | Why not FOUND |
|------|----------------|
| Allen Taylor | Form D signature block names Allen Taylor (`/s/ Allen Taylor`) but Form D has **no email field**; EFTS `"Endeavor Catalyst" AND @` = 0. |
| Ana Clara Martins | Atlantico Partners Form D related persons / signers are **Julio Vasconcellos** only. |
| Amaya Baliño Sanz | EDGAR “Angel Ventures” hits are other legal entities (US fund LP; Pacific Alliance fund in Swvl docs), not `angelventures.vc` + Amaya. |

## Evidence

Negative audit notes and Form D excerpts under `evidence/`. Local Form D HTML snapshots under `evidence/formd/`.

## Prior arms

These seats were also **EMPTY** on non-SEC passes in Wave4 L02/L03 (team mailto / broader regulatory PDF arms). This arm confirms no SEC Form D / exhibit path to FOUND under the co-occurrence gate.
