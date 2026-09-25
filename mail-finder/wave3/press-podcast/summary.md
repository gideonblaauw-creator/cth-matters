# Wave 3 Arm 3 — press / podcast / show-notes (`press_mailto`)

**Run date:** 2026-09-25  
**Input:** 12 P1 seats (`input.csv`)  
**Method:** Search-seed only — industry press, firm newsroom/perspectives, podcast show notes, conference/speaker PDFs where **name and email co-occur** (Citi footnote / mailto class). No pattern guess, Hunter/Apollo, SMTP verify, or LinkedIn scrape.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 12 |
| **HOLD** | 0 |

Baseline context: portfolio ~27/50 overall; this arm adds **no new FOUND** stamps.

## Method notes

- **Generics → EMPTY:** `admin@eclipse.capital`, `info@sumacapital.com`, `info@autotechvc.com`, `founders@autotechvc.com`, `investments@i80group.com`, `info@cim-llc.com`, IDB `requestinformation@idbinvest.org`, etc.
- **LinkedIn-only / calendar links → not FOUND:** Podcast show notes (Keep Cool, FreightCaviar, Auto Remarketing, Logistics of Logistics) point to LinkedIn or firm home — no published mailbox with name.
- **Wrong domain → EMPTY:** Mauricio Rosillo column bylines on Ámbito Jurídico use `mauriciorosillo@gmail.com`; faculty page `rrosillo@javeriana.edu.co` — neither is `@bancolombia.com.co`.
- **BBVA Spark:** Live `bbvaspark.com/en/our-team/` returned **403** from runner; newsroom articles quote Eduardo González without email.

## Seats (all EMPTY)

| Monday_item_id | Name | Domain |
|----------------|------|--------|
| 13114466566 | Agustin De Luca | lendable.io |
| 13028369967 | Aidan Madigan-Curtis | eclipse.capital |
| 13028336649 | Bill Driegert | eclipse.capital |
| 13028359226 | Burak Cendek | autotechvc.com |
| 13114433880 | Eduardo González Montes de Oca | bbvaspark.com |
| 13114467046 | Edward Goldstein | i80group.com |
| 13028336256 | Greg Reichow | eclipse.capital |
| 13114434007 | Jacob Haar | cim-llc.com |
| 13028371978 | Jessica Diaz Nunez | idbinvest.org |
| 13028335946 | Mauricio Rosillo | bancolombia.com.co |
| 13028350024 | Monica Salazar | idbinvest.org |
| 13028359161 | Natalia Medianero Aldaba | sumacapital.com |

## Deliverables

- `results.csv` — full seat rows with `Checked_URLs`
- `stamp-list.json` — FOUND only (empty)
- `evidence/` — URL index + short excerpts
- `README.md` — reproduction hints (search seeds only)

**Monday:** no writes (per brief).
