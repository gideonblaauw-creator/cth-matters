# Mail Finder — Wave4 / L06 / Arm 03

**Focus:** Public **press releases**, **podcast/show notes**, **conference/speaker pages**, and comparable publisher-controlled pages — **FOUND** only when the target name and an exact **personal** email or `mailto:` visibly co-occur on the **same page**.

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (per seat)

1. Search public press, podcast notes, event/speaker bios, and reputable media pages tied to the seat (prefer first-party or publisher-controlled URLs).
2. Require **display name + person@firm** (or personal non-generic mailbox) in the same rendered page / citation unit; capture `mailto:` or visible text exactly as published.
3. Generics (`press@`, `info@`, `contacto@`, `comunciacion@`, `admin@`, comms desks without person attribution) → **EMPTY**.
4. Forbidden: Hunter/Apollo, LinkedIn/Sales Navigator scrape, pattern guessing, SMTP verification, invented emails, paid/authenticated sources, **Monday writes**.

## Prohibited paths

Writes **only** under `mail-finder/wave4/L06/arm-03/`.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`), non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | URL index and negative excerpts |

## Result (this run)

**0 FOUND / 5 EMPTY** — see `summary.md` and `evidence/`.

Protocol: `mail-finder/protocol/Mail-Finder-Workbench-Strategy.md`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l06-arm03-9195`
