# Mail Finder — Wave4 / L09 / Arm 04

**Focus:** **Deferred high-yield** pass using **L01–L03 closeout URLs and evidence notes as leads only** (re-verify every FOUND).

**Write path:** `mail-finder/wave4/L09/arm-04/` only.

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (`deferred_high_yield_L01_L03_leads`)

1. Map each seat to URLs recorded in **L01 / L02 / L03** closeouts (`results.csv`, team crawls, cited PDF URLs in L03 evidence).
2. Fetch each lead; allow **one same-domain expand** (e.g. Seneca WP media JSON, CrossBoundary PDF cited in L03 Amazon guide extracts, FLII2025 class from L03 arm-02).
3. For impact principals, check **public evaluation / roster PDFs** when L03 established that lane (GEF TNFD MTR, FLII2025).
4. **FOUND** only when target **name** and **person@firm** (non-generic) co-occur in the same artifact, with stable URL + excerpt saved under `evidence/`.
5. **Generics** (`impact@`, `communications@`, `PLANETA@`, role-only inboxes) → **EMPTY**.
6. **Forbidden:** Hunter/Apollo, LinkedIn/Sales Navigator scraping, pattern/SMTP verification, invented emails, Monday writes, broad crawl beyond lead + one expand.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`); non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only |
| `summary.md` | Scorecard |
| `evidence/` | Snapshots, excerpts, lead index |

## Result (2026-09-25)

**1 FOUND / 4 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L09/arm-04/`. Do not modify other wave4 arms.
