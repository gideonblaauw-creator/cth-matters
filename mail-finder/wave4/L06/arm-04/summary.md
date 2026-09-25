# Wave4 L06 Arm 04 — press / podcast / speaker + mailto scorecard

**Run:** 2026-09-25 (UTC) · **Seats:** 5 · **Input:** `input.csv`  
**Method:** Public **press releases**, **podcast/show notes**, **conference/speaker pages**, and comparable publisher pages. **FOUND** only when the seat **name** and a **non-generic personal email** (or `mailto:`) **co-occur on the same page**. Generics (`press@`, `info@`, `contact@`, `impact@`, etc.) → **EMPTY**.

## Results

| Status | Count |
|--------|------:|
| FOUND | 1 |
| EMPTY | 4 |
| UNCERTAIN | 0 |

**Yield:** 1 / 5 citation-grade personal emails in the press/podcast/speaker lane.

## Per seat

| Monday_item_id | Name | Domain | Outcome |
|----------------|------|--------|---------|
| 13028367245 | Michal Lasocki | eecventures.com | **EMPTY** — team/speaker pages; only `contact@eecventures.com` or third-party organizer mailboxes |
| 13028372212 | Miheer Chanrai | climate.capital | **EMPTY** — site + summit/speaker listings; no Chanrai + `person@climate.capital` |
| 13100511303 | Monica Saggioro Leal | maya.capital | **EMPTY** — team + podcast/webinar pages name Monica; no personal email on page |
| 13028366958 | Nathalie Couët | senecaimpact.com | **FOUND** — `nathalie@couet-strategy.com` on [WiGH speaker profile](https://women-in-green-hydrogen.net/nathalie-couet/) (Seneca site has no Couët + person email) |
| 13052203004 | Netradyne (strategic / bolt-on) | netradyne.com | **EMPTY** — press footers cite PR contact Sarah Duckett; generics on contact page |

## Hygiene

- No Hunter/Apollo, LinkedIn/Sales Navigator scrape, pattern guessing, SMTP validation, or Monday writes.
- Work confined to `mail-finder/wave4/L06/arm-04/`.
- Evidence cache: `evidence/fetched/` (134 HTML snapshots) + `evidence/research-notes.md`.

## Artifacts

- `evidence/nathalie-couet-wigh-excerpt.txt` — FOUND snippet
- `evidence/netradyne-leadership-pr.html` — sample press release (media contact block)
