# Wave4 L03 Arm 07 — regulatory / securities PDF

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`) — 3 overlap prior L02 arm-07 team-mailto batch plus 2 P1 seats (BBVA Spark, i80 Group).  
**Method:** Public-web discovery + PDF/filing text — BCSC Form 45-106F1 pattern, SEC EDGAR (Form D, 6-K, exhibits), FINRA/IAPD firm lookup, national securities signature blocks. **FOUND** only when **display/legal name + person `@firm` email** co-occur on the **same public PDF/filing block**. Generics → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, or invented emails.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |

## Per seat

| Monday_item_id | Name | Firm | Outcome |
|----------------|------|------|---------|
| 13100496455 | Anna Raptis | Amplifica Capital | EMPTY — Form D signer, no email; BCSC negative; ecosystem PDF name-only |
| 13100496708 | Abe Yokell | Congruent Ventures | EMPTY — Form D related person; no `@congruentvc.com` in filings |
| 13100488906 | Niccolò Camerana | Stellantis Ventures | EMPTY — 13D POA signature; no email |
| 13114433880 | Eduardo González Montes de Oca | BBVA Spark | EMPTY — BBVA 6-K generic corporate email only |
| 13114467046 | Edward Goldstein | i80 Group | EMPTY — not on Form D; EDGAR/IAPD negative |

## Method notes

- **Form D XML** carries names/signatures but typically **no person email** for these issuers — still searched and archived under `evidence/`.
- **Generics excluded:** `info@amplificacapital.com`, `info@`/`investors@congruentvc.com`, `comunicacion.corporativa@bbva.com`, `investments@`/`ir@i80group.com`, `stellantisventures@stellantis.com`.
- **IAPD PDF brochure** endpoint returned AccessDenied from this environment; HTML ADV snapshot blocked — firm/individual **search API** used instead for Edward Goldstein seat.
- **No Monday writes** from this folder.

## Deliverables

- `results.csv`, `stamp-list.json`, `README.md`, `summary.md`, `evidence/` (filings, excerpts, `edgar_search.json`, `url-index.md`)
