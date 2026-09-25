# Wave4 L07 Arm 07 — Curated public investor directories (Mercury-class)

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`)  
**Method:** Curated, openly accessible investor directories (Mercury Investor Database, ImpactAssets IA50, GIIN member profiles, Signal NFX firm/investor listings, Fundraising Fox where public). **FOUND** only when the seat **name** and an exact **person@firm** email appear on the **same** directory record/page. Generics, masked “reveal” broker fields, social-only profiles, and cross-record joins → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, SMTP verify, invented emails, or Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm | Outcome |
|----------------|------|------|---------|
| 13114434007 | Jacob Haar | Community Investment Management (CIM) | EMPTY — no Mercury slug; GIIN/Fox list org or bio without person@cim-llc.com |
| 13028371978 | Jessica Diaz Nunez | IDB Invest | EMPTY — no Mercury profile; GIIN/IDB staff directory pages without name+@idbinvest.org |
| 13028336447 | Kevin Bone | Lightrock | EMPTY — absent from Mercury sitemap; Signal NFX firm roster omits Bone; Fox masks emails |
| 13028357441 | Klaus Prebensen | Impact Fund Denmark | EMPTY — no Mercury/GIIN person-level mailbox (first-party site generic only) |
| 12727972974 | Kuehne+Nagel / Reefknot | Reefknot | EMPTY — firm seat; directory pages only generic info@ or masked team emails |

## Directory access notes

- **Mercury** (`mercury.com/investor-database/*`): Sitemap scanned (296 profiles); none of the five targets appear. Direct slug URLs return 404.
- **ImpactAssets IA50**: `/ia50/` redirects to login; `fund.php?id=…` returns 404 from this environment (could not re-verify historical IA50 contact blocks).
- **OpenVC**: Search endpoints returned 403 to automated fetch — not used for FOUND.
- **Fundraising Fox**: Investor/people pages often show **masked** emails with “reveal” — treated as broker-style, excluded from FOUND (same gate as Hunter/Apollo-class sources).

## Artifacts

- `results.csv`, `stamp-list.json` (empty), `README.md`, `evidence/` (`url-index.md`, `negative-excerpts.md`, `directory_search.json`, HTML snapshots)
