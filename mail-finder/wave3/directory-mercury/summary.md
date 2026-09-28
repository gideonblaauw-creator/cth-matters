# Mail Finder Wave3 — Arm 4: directory-mercury

**method_arm:** `directory_mercury`  
**Seats:** 12  
**Run date:** 2026-09-25 (UTC)

## Counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 12 |

## Method (allowed sources only)

- Mercury Investor Database public profile pages (manual slug browse + firm/name search seeds; no bulk Mercury API)
- IFC / IDB Invest MDB training & disclosure pages
- Academic / accelerator / nonprofit investor directories (e.g. LAVCA, Kauffman Fellows, Endeavor Catalyst report)

**Forbidden paths not used:** Hunter/Apollo/ContactOut/Clearbit, pattern guessing, SMTP verify, LinkedIn scrape, paid finders, third-party Mercury scrapers.

## FOUND (stamp list)

_None this arm._

## Notable near-misses (not stamped)

- **Adriana Saman** — Mercury has [Ben Savage / Clocktower](https://mercury.com/investor-database/ben-savage) with `ben@clocktowerventures.com`; different individual.
- **Allen Taylor** — [2025 Endeavor Catalyst annual report](https://endeavor.org/2025-endeavor-catalyst-annual-report/) lists `jackie.carmel@endeavor.org` for fund IR, not Allen Taylor.
- **Asia Agnelli** — TMV profile page uses generic `team@tmv.vc` alongside Azzi Agnelli name.

## Evidence

HTML snapshots under `evidence/` (Mercury attempts, IDB/APG/BII/Kibo/Atlantico/TMV/783/PRS pages).

## Baseline

Wave3 cumulative baseline referenced in brief: **27/50** prior to this arm; **+0 FOUND** here → still **27/50** unless other arms add stamps.
