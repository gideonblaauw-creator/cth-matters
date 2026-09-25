# Wave4 L01 Arm 03 — Domain hygiene + Website backfill

**Batch:** Potential Investors (19 seats)  
**Method:** HTTP check, parked-domain detection, public web search for live investment-entity homepages; opportunistic first-party team-page mailto scan (no pattern guessing, no Hunter/Apollo, no LinkedIn scrape).

## Scorecard

| Status | Count |
|--------|------:|
| WEBSITE_OK | 4 |
| WEBSITE_CORRECTED | 12 |
| WEBSITE_MAPPED | 1 |
| DOMAIN_UNRESOLVED | 2 |
| FOUND | 0 |

## Highlights

- **Parked / for-sale domains corrected:** `savia.vc` → `https://saviaventures.com/`; `blink.vc` → `https://blinkimpact.com/` (GoDaddy for-sale landers).
- **Redirect canonicalization:** Kibo, Flybridge, Mouro, Angel Ventures, Epic Angels, Centry, Climate Club, SIMMA, BEV FO, Greenbull (www + EN entry).
- **Domain alias:** `dibanka.com` → `https://dibanka.co/`.
- **Unresolved:** `carbonsul.com` (404 / wrong-entity sniff); `sdginvestors.com` (hosting suspended page).
- **Emails:** No citation-grade `person@firm` mailto co-occurrence on first-party pages; `stamp-list.json` empty.

## Monday Website stamps (workbench)

Use `website-corrections.json` for rows where `Proposed_Website` differs from Monday `Current_Website` (skip if Monday Website already filled and matches live canonical — HITL per protocol).
