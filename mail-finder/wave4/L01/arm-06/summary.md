# Arm 06 — Domain hygiene scorecard

**Run:** 2026-09-25 · **Seats:** 19 · **Input:** `input.csv`

## Status counts

| Status | Count |
|--------|------:|
| WEBSITE_OK | 13 |
| WEBSITE_CORRECTED | 6 |
| WEBSITE_MAPPED | 0 |
| DOMAIN_UNRESOLVED | 0 |
| FOUND | 0 |
| EMPTY | 0 |

## Website hygiene

| Verdict | Seats |
|---------|-------|
| NXDOMAIN / legacy alias | Lucía (gawa-capital.com → gawacapital.com), Nathalie (senecaimpact.com → senecaimpact.earth) |
| Wrong corporate root | Maersk Growth, Caterpillar Ventures, Stellantis Ventures |
| Wrong entity / unit | Matteo Scalabrino (Rockefeller Foundation → RF Catalytic Capital) |
| Live OK (no correction) | Kärt Klein (EstVCA), Lucas de la Vega (Actyus), Maite Fibla (Ship2B), Marcus Behrendt (BMW i Ventures), Mau Messina (SF500), Michal Lasocki (EEC Ventures), Miheer Chanrai (Climate Capital), Monica Saggioro (Maya Capital), Netradyne, Nic Gorini (Spin Ventures), Nina Alastruey (Demium/Mission on demium.com), Norfund, Pat Martin (Venture 53) |

## Email

No first-party **name + person@firm** mailto co-occurrence on team/people pages. Generics only (e.g. `info@`, `impact@`, `stellantisventures@`, `contact@`). **`stamp-list.json` is empty.**

## Environment notes

Direct `curl` to `maersk.com`, `caterpillar.com`, and apex `maersk.com/growth` timed out from the runner; Maersk Growth and Caterpillar Ventures URLs were verified via alternate fetch and public documentation. All other seats were HTTP-checked from the runner.
