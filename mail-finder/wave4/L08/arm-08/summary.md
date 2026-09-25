# Wave4 L08 Arm 08 — Scorecard

**Method:** One targeted Wayback CDX lookup per seat on `/team` (or `/about` for domains configured in run script), then a single archived HTML fetch from the best-matching capture in that CDX response.

**Run:** 2026-09-25 (UTC) · **Branch:** `cursor/mail-finder-wave4-l08-arm08-ec49`

| Monday_item_id | Name | Firm | Domain | Path | Status | Outcome |
|----------------|------|------|--------|------|--------|---------|
| 13028336225 | Dr. Luke Kirke | — | greenbondcorp.com | `/team` | EMPTY | CDX returned no HTTP 200 captures for `greenbondcorp.com/team` |
| 13114451141 | Eduardo Brennand Campos | OneVC | onevc.vc | `/team` | EMPTY | Archived `…/team/eduardo-campos` lists Partner bio + LinkedIn; no `@onevc.vc` mailto or text on same page |
| 13114460590 | Elias Mufarech | Collide Capital | collide.capital | `/team` | EMPTY | CDX returned no HTTP 200 captures for `collide.capital/team` |
| 13028359480 | Elvia Gomez | — | acumen.org | `/team` | EMPTY | Archived `…/team/elvia-gomez/` has full bio; no `@acumen.org` personal mailto/text co-located |
| 13028399382 | Emma Haight | — | glenarapartners.com | `/team` | EMPTY | CDX returned no HTTP 200 captures for `glenarapartners.com/team` |

## Totals

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Notes

- **FOUND gate:** archived page must show the seat holder’s name and an exact personal `person@firm` email (or mailto) on the **same** snapshot — not CDX metadata alone.
- **stamp-list.json:** empty (no FOUND seats).
