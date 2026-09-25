# Mail Finder — Wave4 L02 Arm 01

First-party **team/people mailto** lane: crawl the seat’s `Website` (plus standard team paths) and stamp only citation-grade `person@firm` emails where the **contact name co-occurs** on the same first-party page.

## Inputs

- `input.csv` — Monday export (4 seats)

## Outputs

| File | Purpose |
|---|---|
| `results.csv` | All seats with `Status`, `Checked_URLs`, notes |
| `stamp-list.json` | FOUND rows only (Monday stamp payload) |
| `summary.md` | Scorecard |
| `evidence/` | HTML/text excerpts for FOUND (empty when no FOUND) |

## Reproduce

```bash
python3 crawl_arm01.py
```

Public HTTP only. Forbidden: Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP verify, invented emails.

## This run

- **0 FOUND / 4 EMPTY** — see `summary.md`.
- No Monday writes; stamp-list is `[]`.
