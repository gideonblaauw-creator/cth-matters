# Wave4 L07 Arm 03 — Curated public investor directories (Mercury-class)

**Run date:** 2026-09-25  
**Input:** 5 firm seats (`input.csv`)  
**Method:** Open, curated investor directories comparable to the [Mercury Investor Database](https://mercury.com/investor-database): structured public listings with direct contact fields. **Excluded:** Hunter, Apollo, RocketReach, ZoomInfo, Lusha, LinkedIn/Sales Navigator scraping, paid/bulk contact brokers, login-gated email fields, pattern guessing, SMTP verification, invented emails, Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm | Outcome |
|----------------|------|------|---------|
| 12727933614 | Proparco | Proparco | **EMPTY** — PEI names staff; person emails paywalled; generic `proparco@proparco.fr` only |
| 13080749096 | Rabobank Partnerships | Rabobank Partnerships | **EMPTY** — not in Mercury DB; PEI masks person `@rabobank.com` |
| 12737016236 | Acumen | Acumen | **EMPTY** — OpenVC/GIIN/PEI/LAVCA attempts; no open name + `person@acumen.org` |
| 12736995257 | Goodwell Investments | Goodwell Investments | **EMPTY** — PEI names partners; emails paywalled; generic `contact@goodwell.nl` |
| 12737022231 | Manutara Ventures | Manutara Ventures | **EMPTY** — Private Equity List paywalls team emails; generic `info@manutaravc.com` only |

## Artifacts

- `results.csv`, `stamp-list.json` (empty), `README.md`, `input.csv`
- `evidence/` — HTML snapshots, `mercury_investor_sitemap.xml`, `negative-excerpts.md`, `url-index.md`

## Calibration

Mercury positive control (not a seat): [Shruti Gandhi profile](https://mercury.com/investor-database/shruti-gandhi) exposes `shruti@array.vc` on the same page as the investor name — this is the citation bar applied to each seat.
