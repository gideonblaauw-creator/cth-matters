# Mail Finder — Wave4 / L06 / Arm 01

**Focus:** Public **press**, **podcast/show notes**, **conference**, and **speaker** pages where the target person’s name and an exact **personal email** or **`mailto:`** co-occur on the same published page.

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (per seat)

1. Search publisher-controlled press/event/speaker/podcast pages (first-party or reputable host).
2. Require **display name + exact personal mailbox** (or `mailto:` target) on the **same page**; capture spelling exactly as rendered.
3. Generics (`press@`, `info@`, `hello@`, `team@`, `contact@`, `bookings@`, etc.) → **EMPTY**.
4. Do not infer from patterns, other people’s pages, or paid contact databases.

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, pattern guessing, SMTP verification, invented emails, paid/authenticated sources, **Monday writes**, writes outside `mail-finder/wave4/L06/arm-01/`.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seed; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | PDF/HTML snapshots, excerpts, URL index |

## Scope

Write **only** under `mail-finder/wave4/L06/arm-01/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l06-arm01-5946`
