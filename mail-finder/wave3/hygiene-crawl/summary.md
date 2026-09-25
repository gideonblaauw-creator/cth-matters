# Wave3 Arm 5 — Hygiene-gated first-party crawl

**method_arm:** `team_html_hygiene`  
**Run date:** 2026-09-25  
**Seats:** 12 (input `wave3-hygiene-crawl.csv`)

## Scorecard

| Metric | Count |
|--------|------:|
| FOUND (person@firm mailto + name co-occurrence) | 1 |
| EMPTY | 11 |
| Baseline reference | 27/50 (prior wave aggregate) |

## Method (this arm)

1. Verify live firm domain (flag parked/NXDOMAIN; note `website-corrections.json` for blank Monday Website only).
2. **One** first-party pass: `/team`, `/about`, `/people`, `/contact`, sitemap-discovered team URLs, plus optional search-seed (`site:domain` + person name) on firm domain only.
3. Optional Wayback on `/team|/about|/people` only when team 403 or mailto signal without attribution.
4. No third HTML pass; EMPTY seats escalate to regulatory/impact PDF in a later arm.

## Forbidden (observed)

No pattern guessing, SMTP verify, Hunter, LinkedIn scrape, or generic stamping.

## Domain hygiene

- **Christel Piron:** Monday `psvfoundry.com` is NXDOMAIN → live **psv.xyz** (`/foundry`, `/people`).
- **Dennis Zaidi:** Monday `checkmatecap.com` is parked → live **checkmatecapital.net**.

## FOUND summary

- **Christel Piron** — `cp@psv.xyz` — [https://www.psv.xyz/people](https://www.psv.xyz/people)

## EMPTY / escalate

- **Blink VC** (13080769456): blink.vc team/home crawled; no person mailto on first-party HTML.
- **Bryony Parker** (13028370683): savia.vc team paths; Bryony Parker listed without mailto.
- **Chip Hazard** (13114411688): flybridge.com/team lists Chip Hazard; Squarespace team page has no mailto links.
- **Christopher Gottschalk** (13100505949): mourocapital.com team sitemap + /team/christopher-gottschalk/; bio pages without personal mailto (info@mourocapital.com generic only elsewhere).
- **Clete Brewer** (13100511323): newroadcp.com/team and /team/clete-brewer/; no person@newroadcp.com mailto co-occurrence.
- **Daniel Blandón** (13028370003): simmacapital.com/team lists Daniel Blandón with LinkedIn only.
- **Dennis Zaidi** (13028359182): checkmatecapital.net our-team crawled on live domain; no Dennis Zaidi person mailto.
- **Dondi Hananto** (13028349815): circulatecapital.com team; Dondi Hananto without mailto (esg@ generic on contact).
- **Eduardo Brennand Campos** (13114451141): onevc.vc/team/eduardo-campos first-party bio; LinkedIn only, no email.
- **Etienne Gillard** (13028370265): manatechmiami.com team/about paths; no person mailto.
- **Federico Storani** (13080749061): riverwoodcapital.com/team returns Cloudflare challenge (403-class); no person mailto captured on first-party pass.
