# Wave4 L02 Arm 03 — First-party team/people mailto discovery

**Batch:** 4 seats (P2)  
**Method:** Public HTTP crawl of firm Website plus standard team paths (`/team`, `/people`, `/about`, `/our-team`, `/leadership`, page source) for **display name + person@firm `mailto:`** co-occurrence. Generics (`info@`, `hello@`, `team@`, `admin@`, etc.) → not FOUND. No Hunter/Apollo/LinkedIn scrape/pattern/SMTP/invented emails. Monday Website column untouched (pre-set in input).

## Scorecard

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 4 |

## Per seat

| Name | Domain | Outcome |
|------|--------|---------|
| Andrii Hordiichuk | biosingularity.world | Team + leadership roster; no person email in source |
| Matteo Scalabrino | rfcatalytic.org | No name on site; generic admin inbox only |
| Elvia Gomez | acumen.org | Team profile live; no person mailto |
| Emma Haight | glenarapartners.com | Team page lists role; no mailto |

## Monday stamping

`stamp-list.json` is empty (no citation-grade FOUND). Route EMPTY seats to ReachGate per protocol.

## Evidence

Short excerpts and saved HTML under `evidence/` for each seat (negative cites).

## Audit

Regenerate crawl JSON: `python3 scripts/crawl_team_mailto.py` (urllib; Acumen may 403 — manual Chrome-UA fetch documented in evidence for Elvia Gomez).
