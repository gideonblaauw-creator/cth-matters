# Mail Finder — Wave 4, Loop L01, Arm 01

Domain hygiene and **Website** backfill for **Potential Investors** only.

## Scope

- **Write path:** `mail-finder/wave4/L01/arm-01/` (exclusive).
- **Input:** `input.csv` (Monday export; do not write back to Monday from this arm).
- **Out of scope:** Other arms, Monday API, email pattern guessing, SMTP verification, Hunter/Apollo, LinkedIn scraping.

## Method (per seat)

1. **Blank Website** — Public web search (firm + contact). Prefer official investment-entity homepage over LinkedIn or personal sites.
2. **Filled Website** — HTTP-check: flag parked landers, NXDOMAIN, wrong entity, or redirect to a *different* firm’s domain.
3. **Proposals** — Suggest corrected `https://…` when blank, wrong, or parked; sniff-test before recording.
4. **Email (opportunistic)** — If a first-party team/people page shows **display name + person@firm `mailto:`** on the same page, record `FOUND` with `Source_URL`. Generics (`info@`, `hello@`, `team@`, `admin@`, etc.) are **not** FOUND.
5. **Search seeds** — Name/domain may guide public search only. **Never invent emails.**

## Deliverables

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat with website status and checked URLs |
| `website-corrections.json` | Monday website stamps for blank/wrong/parked only |
| `stamp-list.json` | FOUND emails only (workbench → Monday) |
| `summary.md` | Counts |
| `evidence/` | Excerpts for any FOUND (empty this run) |

## Status values (`results.csv`)

- `WEBSITE_OK` — Current URL is live and matches the investment entity.
- `WEBSITE_MAPPED` — Was blank; homepage mapped via search.
- `WEBSITE_CORRECTED` — Was wrong/parked/retail redirect; proposed URL in `Proposed_Website`.
- `DOMAIN_UNRESOLVED` — No reliable public investment-entity homepage.
- `FOUND` — Person-specific email with first-party evidence.
- `EMPTY` — Reserved; not used when website outcome is one of the `WEBSITE_*` states above.

## Run metadata

- **Date:** 2026-09-25 (UTC)
- **Agent:** Cloud domain-hygiene pass (Composer 2.5)
