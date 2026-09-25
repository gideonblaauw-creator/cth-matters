# Wave4 L08 Arm 01 — Wayback CDX (`/team`, `/about`, `/people`)

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`).  
**Method:** One **Wayback CDX** lookup per eligible seat (non-blank firm website), scoped to a single **team / about / people** path; review at most one archived snapshot when CDX returns captures. **FOUND** only when target name and exact **person@firm** (or `mailto:`) co-occur on that snapshot. CDX metadata alone is not evidence.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm / domain | Path checked | Outcome |
|----------------|------|---------------|--------------|---------|
| 13100496708 | Abe Yokell | Congruent Ventures (`congruentvc.com`) | `/team` | EMPTY — Abe named on archive; no person email on same record |
| 13028364943 | Abhinav Sinha | BII (`bii.co.uk`) | `/about/our-people` | EMPTY — name in directory only; no `@bii.co.uk` on page |
| 13100506386 | Adriana Saman | Clocktower Ventures (`clocktowerventures.com`) | `/team` | EMPTY — CDX 0 captures |
| 13028336231 | Alethia Wong | Zenani Capital (`zenanicapital.com`) | `/team` | EMPTY — target absent; no person email |
| 13028360241 | Alfredo Neila | Plastic Repair System (`plasticrepairsystem.com`) | `/about` | EMPTY — CDX 0 captures |

## Deliverables

- `results.csv`, `stamp-list.json`, `README.md`, `summary.md`, `evidence/` (CDX JSON, Wayback HTML, `url-index.md`, `negative-excerpts.md`)

**No Monday writes** from this folder.
