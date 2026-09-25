# Wave4 L07 Arm 04 — Curated public investor directories (Mercury-class)

**Run date:** 2026-09-25 (UTC)  
**Input:** 5 seats (`input.csv`).  
**Method:** Open, curated investor directories comparable to the **Mercury Investor Database** (structured public listings with direct contact fields). Also checked **Gaebler.com VC Database**, **Mindmaps** firm records, and **Private Equity International** institution contacts where relevant. Excluded Hunter/Apollo/RocketReach/ZoomInfo/Lusha, LinkedIn scraping, pattern guessing, and firm-site-only crawls (other L07 arms).

**FOUND gate:** Exact target person name and exact `person@firm` email on the **same** public directory record, with citation-grade excerpt.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm / domain | Outcome |
|----------------|------|---------------|---------|
| 12737044089 | Norrsken VC | norrsken.vc | EMPTY — firm seat; no Norrsken listing in Mercury sitemap (295 profiles) or Gaebler/Mindmaps with name+person@ |
| 12736993459 | 574 Invest / SNCF·GEODIS | 574invest.sncf.fr | EMPTY — Mindmaps shows `contact@574invest.sncf.fr` only (generic); no Mercury profile |
| 12736959331 | Michelin Ventures | michelin.com | EMPTY — no Mercury-class directory hit for CVC contact with person@michelin.com |
| 12727972972 | Rhenus Group | rhenus.com | EMPTY — no directory record with named contact + person@rhenus.com |
| 13130192673 | Felipe Cortés | fundacionbd.org | EMPTY — Felipe Cortés not in Mercury corpus; PEI lists other names with masked emails |

## Corpora searched

- Mercury Investor Database index + full sitemap (`evidence/mercury-investor-database-sitemap.xml`; per-profile text scan)
- Gaebler.com VC Database search
- Mindmaps.ai-ecosystem.org (574 Invest firm id 133638)
- PEI institution profile (Fundación Bolívar Davivienda)
- The CVC directory search URLs (connection failed from environment; see `evidence/negative-excerpts.md`)

## Deliverables

- `results.csv`, `stamp-list.json` (empty), `README.md`, `summary.md`, `evidence/` (`directory_search.json`, negative excerpts, Mercury sitemap)

**No Monday writes** from this folder.
