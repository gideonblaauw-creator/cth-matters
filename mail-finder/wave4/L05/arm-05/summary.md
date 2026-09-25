# Wave4 L05 Arm 05 — Impact / LP / annual-report PDFs

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`)  
**Method:** Public first-party and issuer/fund **PDFs** (impact reports, LP/IR materials, annual reports, cited press PDFs). **FOUND** only when the target **published name** and a **non-generic person@firm** mailbox appear in the **same PDF** (preserve printed spelling). Generics (`press@`, `info@`, `hola@`, etc.) and wrong-firm domains → **EMPTY**. No pattern guessing, Hunter/Apollo, LinkedIn scrape, or Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm / domain | Outcome |
|----------------|------|---------------|---------|
| 13028370265 | Etienne Gillard | Mana Tech / manacommon.com | EMPTY — event PDFs name Gillard; no email in PDF corpus |
| 13028371139 | Federico Giannetti | Axel Carbon / axel-carbon.com | EMPTY — press PDF has Giannetti + **press@axel-carbon.com** only |
| 13080749061 | Federico Storani | Riverwood / riverwoodcapital.com | EMPTY — Endeavor agenda + Vacasa exhibit PDF; no Storani + person@rwcm |
| 13100506101 | Felix Klühr | HV Capital / hvcapital.com | EMPTY — 2020 Heartbeat PDF uses **@hvventures.com** (legacy), not @hvcapital.com |
| 13028371748 | Fernando Lelo de Larrea H | Rumbo / rumbo.ventures | EMPTY — EIN PDF + Form D name only; no person@rumbo.ventures in PDF |

## Deliverables

- `results.csv`, `stamp-list.json` (no FOUND rows), `README.md`, `summary.md`
- `evidence/` — downloaded PDFs, Form D XML, `pdf_search_log.md`
