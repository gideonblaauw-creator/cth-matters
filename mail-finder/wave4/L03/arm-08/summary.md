# Wave4 L03 Arm 08 — Regulatory / securities PDF scorecard

**Scope:** 5 seats from `input.csv`  
**Method:** Public regulatory corpora — SEC EDGAR EFTS, Form D / Form 4 XML, FINRA IAPD Form ADV, BCSC document search (HTML). PDF text via `pdftotext` where downloadable.  
**Prohibited:** Hunter/Apollo, LinkedIn scrape, pattern+SMTP, invented emails. **No Monday writes** from this arm.

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
| Greg Reichow | Enovix EX-99.1 names Reichow; emails on page are Enovix IR/PR (`canderson@enovix.com`, etc.), not `@eclipse.capital`. |
| Ana Clara Martins | Atlantico Form D related persons / signatures are Julio Vasconcellos only. |
| Iñaki García Llorente | Lendable Form D entities on EDGAR; no name + `@lendable.io` in filing XML. |

## Evidence

Audit excerpts under `evidence/` (negative regulatory pass; no FOUND rows).

## Prior arms

These seats were also **EMPTY** on first-party team/mailto in Wave4 L02 Arm 08 (`mail-finder/wave4/L02/arm-08/`).
