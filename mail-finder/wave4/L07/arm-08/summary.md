# Wave4 L07 Arm 08 — Curated public investor directories (Mercury-class)

**Run date:** 2026-09-25 (UTC)  
**Input:** 5 seats (`input.csv`) — same P1 batch as Wave4 L04 Arm 04 (Bancolombia, IDB Invest ×2, Suma Capital, APG).  
**Method:** Open, curated investor directories comparable to the **Mercury Investor Database** (structured public listings with direct contact fields). No login-gated email, no paywall brokers (Hunter/Apollo/RocketReach/ZoomInfo/Lusha), no LinkedIn scrape, no pattern guessing, no Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Domain | Outcome |
|----------------|------|--------|---------|
| 13028335946 | Mauricio Rosillo | bancolombia.com.co | EMPTY — no Mercury profile; LAVCA/other directories without person email |
| 13028350024 | Monica Salazar | idbinvest.org | EMPTY — LAVCA listing name-only; IDB author page without mailbox |
| 13028359161 | Natalia Medianero Aldaba | sumacapital.com | EMPTY — inClimate gated; Suma `info@` generic only |
| 13028349662 | Sergio Díaz | idbinvest.org | EMPTY — GRI + IDB pages name-only |
| 13028349457 | Sina Dorner-Müller | apg.nl | EMPTY — no Mercury/Signal directory email for seat |

## Mercury corpus

- Sitemap: 295 public investor profiles scanned (`evidence/mercury_profile_scan.json`).
- **Zero** profiles mention seed names or firm keywords (Bancolombia, IDB Invest, Suma Capital, APG).

## Deliverables

- `results.csv` — one row per seed seat  
- `stamp-list.json` — empty (no FOUND)  
- `evidence/` — Mercury scan JSON, `negative-excerpts.md`, `url-index.md`  
- **No Monday writes**
