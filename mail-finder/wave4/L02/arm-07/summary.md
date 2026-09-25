# Wave4 L02 Arm 07 — first-party team / people mailto

**Run date:** 2026-09-25  
**Input:** 3 P2 seats (`input.csv`)  
**Method:** `firm_team_mailto` — crawl firm Website plus `/team`, `/people`, `/about`, `/our-team`, `/leadership`, and page HTML for **display name + person `@firm` mailto** co-occurrence. Public HTTP only.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 3 |

## Per seat

| Monday_item_id | Name | Firm | Outcome |
|----------------|------|------|---------|
| 13100496455 | Anna Raptis | Amplifica Capital | EMPTY — `/aboutus` name + LinkedIn; contact `info@` generic |
| 13100496708 | Abe Yokell | Congruent Ventures | EMPTY — profile + team list; footer `info@` / `investors@` only |
| 13100488906 | Niccolò Camerana | Stellantis Ventures | EMPTY — live site 403 (Akamai); no team HTML retrieved |

## Method notes

- **Generics → EMPTY:** `info@amplificacapital.com`, `info@congruentvc.com`, `investors@congruentvc.com`.
- **LinkedIn-only on team pages** does not satisfy citation gate.
- **Stellantis Ventures:** bot wall on all probed paths; no Wayback pass in this arm (website crawl only).
- **No Monday writes** from this folder.

## Deliverables

- `results.csv`, `stamp-list.json`, `README.md`, `summary.md`, `evidence/` (HTML snapshots + excerpts)
