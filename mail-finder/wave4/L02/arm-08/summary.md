# Wave4 L02 Arm 08 — First-party team/people mailto

**Loop:** Mail Finder Wave4 L02 Arm 08  
**Seats processed:** 3  
**Run date:** 2026-09-25

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 3 |
| UNCERTAIN | 0 |

## Per seat

| Name | Firm | Outcome |
|------|------|---------|
| Andrés Saborido | Wayra (Telefónica) | Team on `/about-us`; contact form only — no person mailto |
| Mark Crawford | Caterpillar Ventures | Live site 403; Wayback ventures page has no team emails |
| Ana Clara Martins | Atlantico | Partner on `/about-us` (listed as Ana Martins); no mailto live or Wayback |

## Deliverables

- `input.csv` — Monday export (3 seats)
- `results.csv` — FOUND/EMPTY + checked URLs
- `stamp-list.json` — empty (no Monday email stamps)
- `evidence/` — HTML snapshots + excerpt notes
- `scripts/crawl_team_mailto.py` — crawl helper (public HTTP)

## Method guardrails

Citation-grade **name + person@firm `mailto:`** on same first-party page only. Generics → not stamped. No Hunter/Apollo/LinkedIn scrape/pattern/SMTP. Website column not modified.
