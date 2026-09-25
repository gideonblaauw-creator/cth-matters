# Mail Finder — Wave4 / L07 / Arm 08

**Focus:** Curated, **openly accessible** investor directories (Mercury-class): structured public listings that may publish **display name + person@firm email** on the same record.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. **Mercury Investor Database** — slug probe + full sitemap profile corpus keyword scan.
2. **Comparable public directories** — e.g. LAVCA women investor lists, GRI Institute member profiles, Signal (NFX) firm pages, inClimate company rosters, EasyVC/OpenVC/Foundersuite when reachable without auth.
3. **FOUND gate** — exact seat name and exact personal `person@firm` email on the **same** public directory record/page, with directory name, stable URL, and citation-grade excerpt.
4. **EMPTY** — profile with name only, social link, firm, or generic mailbox (`info@`, press/IR); do not join across records or infer from domain patterns.
5. **UNCERTAIN** — directory access or provenance unclear (not used this run once negative paths were documented).

## Prohibited

Hunter, Apollo, RocketReach, ZoomInfo, Lusha, paid databases, LinkedIn/Sales Navigator scraping, SMTP verification, pattern guessing, invented emails, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`); non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only — `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | Audit notes and Mercury scan metadata |

## Scope

Write **only** under `mail-finder/wave4/L07/arm-08/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l07-arm08-e390`
- Result: **0 FOUND / 5 EMPTY**
