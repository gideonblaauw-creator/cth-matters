# Mail Finder — Wave4 / L09 / Arm 01

**Focus:** Deferred **high-yield** retry on L01–L03 EMPTY seats using public **press**, **podcast/show notes**, **conference**, and **speaker** pages where the target person’s name and an exact **personal email** or **`mailto:`** co-occur on the same published page.

These five seats were previously processed under impact/LP PDF in `mail-finder/wave4/L05/arm-05/` (all EMPTY) with domain corrections from `mail-finder/wave4/L01/arm-04/`.

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (per seat)

1. Search publisher-controlled press, event, speaker, and podcast pages (first-party or reputable host).
2. Require **display name + exact personal mailbox** (or `mailto:` target) on the **same page**; capture spelling exactly as rendered.
3. Generics (`press@`, `info@`, `hello@`, `team@`, `contact@`, role press contacts not tied to the person, etc.) → **EMPTY**.
4. Legacy or wrong domains vs seed firm website → **EMPTY** (not UNCERTAIN unless page is ambiguous about firm affiliation).
5. Do not infer from patterns, paid contact databases, or other people’s pages.

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, pattern guessing, SMTP verification, invented emails, paid/authenticated sources, broad crawl, **Monday writes**, writes outside `mail-finder/wave4/L09/arm-01/`.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | URL index, negative excerpts, selected HTML snapshots |

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L09/arm-01/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l09-arm01-f731`
