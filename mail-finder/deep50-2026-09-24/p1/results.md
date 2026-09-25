# P1 deep hunt — results summary (2026-09-24)

**Arm:** Cursor Hands P1 deep hunt  
**Input:** 22 P1 seats (`input.csv`)  
**Goal:** citation-grade `person@firm` toward Deep-50 desk target  

## Counts

| Status | Count |
|--------|------:|
| **FOUND** | 2 |
| **EMPTY** | 20 |
| **UNCERTAIN** | 0 |
| **DOMAIN_UNRESOLVED** | 0 |

## FOUND (citation-grade)

| Monday_item_id | Name | Firm | Email | Source |
|----------------|------|------|-------|--------|
| 13114431052 | Marc Helwani | i80 Group | healing@i80group.com | [SEC EDGAR hlco_ex1018.htm](https://www.sec.gov/Archives/edgar/data/1441082/000147793222007571/hlco_ex1018.htm) |
| 13028335949 | Fernando Cortes McAllister | Fundación Bolívar Davivienda | fcortes@fundacionbd.org | [United Way Colombia ethics PDF](https://unitedwaycolombia.org/wp-content/uploads/2024/12/Codigo-de-Etica-y-Buen-Gobierno-firmado.pdf) |

## Methods used (seat-level)

- Firm `/team`, `/about`, profile pages + page source (mailto, JSON-LD, RSC payloads)
- Wayback CDX for `lendable.io/team`, `bbvaspark.com`
- Public PDFs (Lendable impact report, IDB Invest factsheets, United Way / DIAN registry)
- SEC EDGAR full-text + exhibit cache (i80 Group)
- Press / podcast HTML via web discovery (no paid finders, no LinkedIn scrape)

## Notes

- Generics only (`info@`, `contact@`, `admin@`, `investments@`, etc.) recorded as **EMPTY** per brief.
- BBVA Spark live site returned **403** from this environment; Wayback homepage cached; no name+email co-occurrence found for Spark Colombia seats.
- Eclipse, Lightrock, CIM, Lendable LatAm, IDB Invest equity/mezzanine, and APG seats: team/bio pages confirmed identity but no public person-level mailbox with co-occurring citation.

**Deliverables:** `results.csv`, `found-for-monday.csv`, `first-found-evidence.md`, `html/` cache.
