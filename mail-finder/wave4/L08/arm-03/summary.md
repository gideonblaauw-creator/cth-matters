# Wave4 L08 Arm 03 — Wayback CDX on /team, /about, or /people

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`).  
**Method:** One targeted **Wayback CDX** lookup per seat on a single **/team**, **/about**, or **/people** path (or exact equivalent) on the Monday firm website. **FOUND** only when an archived page shows the seat person’s name and an exact **person@firm** email (or `mailto:`) **together**. CDX metadata alone is not evidence. No pattern guess, SMTP verify, Hunter/Apollo, LinkedIn scrape, broad Wayback crawl, or Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm / domain | CDX path | Outcome |
|----------------|------|---------------|----------|---------|
| 13028365646 | Ana Lucía Rodhas Alcántara | Hyatt (`hyatt.com`) | `/about` | EMPTY — CDX `[]` |
| 13028359995 | Andrii Hordiichuk | BioSingularity (`biosingularity.world`) | `/team` | EMPTY — CDX `[]` |
| 13028358627 | Andrés Méndez | Colaborativo (`colaborativo.io`) | `/about` | EMPTY — CDX `[]` |
| 13100509887 | Andrés Saborido | Wayra / Telefónica (`telefonica.com`) | `/en/about-us` | EMPTY — snapshots exist; 2022-10-06 page has no Saborido + personal email |
| 13028336707 | Andrés Salazar González | Bavaria (`bavaria.co`) | `/nosotros` | EMPTY — CDX `[]` |

## Deliverables

- `results.csv`, `stamp-list.json`, `README.md`, `summary.md`, `evidence/` (CDX JSON, Telefónica snapshot, negative excerpts)

**No Monday writes** from this folder.
