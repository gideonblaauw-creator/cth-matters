# Wave4 L07 Arm 05 — Curated public investor directories (Mercury-class)

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`)  
**Method:** Open, curated investor directories comparable to Mercury’s public investor database — **Mercury Investor Database**, **findfunding.vc**, **Investor Match (investormatch.pro)**, **Evalyze.ai**, and **NFX Signal** (public profile pages only). **Excluded:** Hunter, Apollo, RocketReach, ZoomInfo, Lusha, paid/bulk brokers, LinkedIn scraping, SMTP/pattern guessing, Monday writes.

**FOUND** only when the **exact target name** and **person@firm** email co-occur on the **same** public directory record/page with citation-grade excerpt.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm / domain | Outcome |
|----------------|------|---------------|---------|
| 13114466566 | Agustin De Luca | Lendable / lendable.io | EMPTY — no Mercury listing; no Lendable rows on findfunding/investormatch |
| 13028369967 | Aidan Madigan-Curtis | eclipse.capital | EMPTY — named on findfunding; only `admin@eclipse.capital` generic |
| 13114444514 | Alejandro Arenas | CIM / cim-llc.com | EMPTY — no Mercury-class directory with name+email |
| 13028336649 | Bill Driegert | eclipse.capital | EMPTY — no Mercury profile; no person email on directory records |
| 13028359226 | Burak Cendek | autotechvc.com | EMPTY — named on findfunding; only `founders@autotechvc.com` generic |

## Deliverables

- `input.csv`, `results.csv`, `stamp-list.json` (`items: []`), `README.md`, `summary.md`
- `evidence/` — Mercury sitemap + 404 captures, findfunding/investormatch/evalyze/NFX HTML, `negative-excerpts.md`

**Monday:** No writes (`stamp-list.json` empty).
