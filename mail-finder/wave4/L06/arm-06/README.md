# Mail Finder — Wave4 / L06 / Arm 06

**Focus:** Public **press**, **podcast/show notes**, **conference/speaker** pages, and comparable publisher-controlled HTML — FOUND only when the same page visibly co-locates the target person’s published name and an exact **personal** email or **mailto** (spelling preserved).

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (per seat)

1. Search first-party and publisher pages (press rooms, podcast episode pages, event speaker bios, conference agendas).
2. Require **name + person@domain** (or `mailto:` target) in the same rendered citation unit on one URL.
3. **Generics** (`info@`, `press@`, `comunica@`, `secretary@`, `alliance@`, event info inboxes, etc.) → **EMPTY** unless explicitly attributed to the target on the same block.
4. **Forbidden:** Hunter/Apollo, LinkedIn/Sales Navigator scrape, pattern guessing, SMTP verify, invented emails, paid/authenticated sources, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`), non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | Negative excerpts and optional FOUND snippets |

## Scope

Write **only** under `mail-finder/wave4/L06/arm-06/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l06-arm06-3582`
