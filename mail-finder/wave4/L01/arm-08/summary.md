# Wave4 L01 Arm 08 — Domain hygiene scorecard

**Scope:** 13 seats (Potential Investors) from `input.csv`  
**Method:** HTTP checks + public web search + first-party team/about sniff (no Hunter/Apollo, no SMTP guess, no LinkedIn scrape)

## Status counts

| Status | Count |
|--------|------:|
| WEBSITE_OK | 10 |
| WEBSITE_CORRECTED | 3 |
| WEBSITE_MAPPED | 0 |
| DOMAIN_UNRESOLVED | 0 |
| FOUND | 0 |
| EMPTY | 0 |

## Website corrections (Monday Website field)

| Monday_item_id | Firm | Proposed URL |
|----------------|------|--------------|
| 12737022231 | Manutara Ventures | https://manutaraventures.com/ |
| 12736993459 | 574 Invest / SNCF·GEODIS | https://www.574invest.com/ |
| 12727972972 | Rhenus Group | https://www.rhenus.group/ |

## Email (FOUND)

None. Generics observed (not stamped): `hello@extantia.com`, `investments@norrsken.vc`, `IR@congruencecapital.com`, `contact@goodwell.nl`, regional `enquiries.*@redribbon.co`.

## Canonical www notes (no Monday change required)

Several apex domains redirect to `www` on the same entity (Earlybird, Red Ribbon, Extantia, Norrsken, Michelin, Blue Action Accelerator). Proposed_Website records canonical `https://www…` where useful for workbench; status remains WEBSITE_OK.
