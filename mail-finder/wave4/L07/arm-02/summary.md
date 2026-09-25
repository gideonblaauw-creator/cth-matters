# Wave4 L07 Arm 02 — Curated public investor directories (Mercury-class)

**Run date:** 2026-09-25 (UTC)  
**Input:** 5 seats (`input.csv`)  
**Method:** Open, curated investor directories comparable to Mercury’s public investor database (Mercury Investor Database, Gaebler Venture Capital Database, Startuplinks LATAM institution profiles). **FOUND** only when the target person’s exact published name and an exact `person@firm` email appear on the **same** directory record/page. Generics, paywalled broker tables, and cross-record joins → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, SMTP verify, invented emails, or Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 1 |
| **EMPTY** | 4 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm | Outcome |
|----------------|------|------|---------|
| 13080769456 | Blink VC | Blink VC | EMPTY — Mercury DB miss; Gaebler “Blink” is blinkcv.com generic, not blink.vc person email |
| 13080768682 | CrossBoundary | CrossBoundary | EMPTY — Gaebler names only or generic contact@; PE List paywalled |
| 13092847178 | Erika Marcucci | Fundación Bolívar Davivienda | **FOUND** — Startuplinks: Erika Marcucci Núñez + emarcucci@fundacionbd.org |
| 12737016921 | Maersk Growth | Maersk Growth | EMPTY — Gaebler “Email Not Recorded”; no Mercury slug |
| 13080768999 | Norfund | Norfund | EMPTY — generic post@norfund.no; team emails behind paid PE List |

## Artifacts

- `results.csv`, `stamp-list.json` (1 FOUND), `README.md`, `evidence/` (Startuplinks excerpt, URL index, negative excerpts)
