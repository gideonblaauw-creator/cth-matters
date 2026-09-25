# Wave4 L01 Arm 01 — Domain hygiene scorecard

**Input:** 18 Potential Investor seats (`input.csv`)  
**Method:** HTTP checks + public web search for blank websites; opportunistic team-page mailto scan (no Hunter/Apollo/pattern SMTP).

| Status | Count |
|--------|------:|
| WEBSITE_OK | 15 |
| WEBSITE_MAPPED | 1 |
| WEBSITE_CORRECTED | 1 |
| DOMAIN_UNRESOLVED | 1 |
| FOUND | 0 |
| EMPTY | 0 |

**Website corrections for Monday:** 2 entries in `website-corrections.json` (1 map-from-blank, 1 wrong-entity redirect fix).

**Emails stamped:** 0 (`stamp-list.json` is `[]`).

**Notes**
- BBVA Spark and Lendable return intermittent bot/captcha responses on some paths; apex domains verified as live investment entities.
- Victoria But (Sun East family office): no authoritative public homepage — left `DOMAIN_UNRESOLVED`.
- No first-party pages found with **person name + non-generic mailto** co-occurrence for any seat.
