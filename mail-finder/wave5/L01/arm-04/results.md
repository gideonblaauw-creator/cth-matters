# MF W5 L01 Arm 04 — Press / podcast / speaker / conference mailto

**Run:** 2026-09-25 (UTC) · **Seats:** 5 · **Input:** `input.csv`  
**Method:** Public press releases, podcast/show pages, conference speaker bios, and comparable publisher-controlled pages. **FOUND** only when **Contact_name** and a **non-generic personal email** (or `mailto:`) **co-occur on the same artifact**. Generics (`press@`, `info@`, `hello@`, `contact@`, `investors@`, event registration desks, etc.) → **EMPTY**.

## Scorecard

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

**Yield:** 0 / 5 citation-grade personal emails in the press/podcast/speaker lane.

## Per seat

| Monday_item_id | Contact_name | Domain | Outcome |
|----------------|--------------|--------|---------|
| 13028350024 | Monica Salazar | idbinvest.org | **EMPTY** — IDB author/press/LAVCA name Monica; press officer `mplanes@iadb.org` only |
| 13028359161 | Natalia Medianero Aldaba | sumacapital.com | **EMPTY** — team/speaker/conference pages; `info@sumacapital.com` generic |
| 13028349662 | Sergio Díaz | idbinvest.org | **EMPTY** — blog author + byline; no person mailbox on page |
| 13028349457 | Sina Dorner-Müller | apg.nl | **EMPTY** — CS hire / podcast press; no Dorner + personal email on same page |
| 13100496708 | Abe Yokell | congruentvc.com | **EMPTY** — profile + SuperReturn speaker; generics / organizer mail only |

## Hygiene

- No Hunter/Apollo, LinkedIn/Sales Navigator scrape, pattern guessing, SMTP probes, paid sources, or Monday API writes.
- No L01 website hygiene re-run (websites already on file).
- Work confined to `mail-finder/wave5/L01/arm-04/`.

## Artifacts

- `results.csv` — one row per seed seat; non-blank `Checked_URLs`
- `stamp-list.json` — empty (no FOUND)
- `evidence/url-index.md`, `evidence/negative-excerpts.md`, `evidence/*.html` snapshots
