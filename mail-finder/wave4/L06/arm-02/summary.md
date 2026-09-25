# Wave4 L06 Arm 02 — Press / podcast / speaker + mailto co-occurrence

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`).  
**Method:** Public press releases, podcast/show notes, conference and speaker pages; **FOUND** only when the seat’s published name and an exact **non-generic personal email** (or `mailto:`) co-occur on the same public page or linked publisher speaker deck. Generics (`info@`, `contacto@`, `atencioncliente@`, etc.) → **EMPTY**.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 1 |
| **EMPTY** | 4 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Outcome |
|----------------|------|---------|
| 13028366698 | Karen Sheffield | EMPTY — multiple speaker pages; no person mailbox on same page |
| 13028367969 | Klaus Hergett | EMPTY — press/blog name Klaus; only generic contacto@ |
| 13028367167 | Kärt Klein | EMPTY — EstVCA press + info@estvca.ee generic on same page |
| 13114435457 | Lucas de la Vega | EMPTY — Actyus team/press; generic atencioncliente@ only |
| 13028358136 | Lucía Gaitán Sánchez | **FOUND** — UNEP FI webinar speaker PDF: `l.gaitan@finance-in-motion.com` |

## Deliverables

- `results.csv`, `stamp-list.json` (1 FOUND), `README.md`, `summary.md`, `evidence/` (URL index, negative excerpts, Lucia excerpt + PDF text)

**No Monday writes** from this folder.
