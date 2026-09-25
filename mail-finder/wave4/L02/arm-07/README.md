# Mail Finder — Wave4 / L02 / Arm 07

**Focus:** First-party team / people **mailto** discovery on seats that already have Website set.

## Inputs

- `input.csv` — 3 seats (Monday export).

## Method (`firm_team_mailto`)

1. Crawl the firm **Website** from Monday plus common team paths: `/team`, `/people`, `/about`, `/our-team`, `/leadership`.
2. Inspect **page source** for `mailto:` links where the **display name** and **person `@firm`** appear on the same page/block.
3. **FOUND** only when citation-grade (name-attributed person email).
4. **Generics** (`info@`, `hello@`, `investors@`, `team@`, etc.) → **EMPTY**.
5. **Public HTTP only** — no Hunter/Apollo, LinkedIn scrape, pattern guess, SMTP verify, or invented emails.
6. **No Monday writes** from this directory. Do not change Website column.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, `Checked_URLs`, optional `Email` when FOUND |
| `summary.md` | Scorecard |
| `stamp-list.json` | FOUND seats only (for downstream stamping) |
| `evidence/` | URL index, excerpts, HTML snapshots |

## Re-run (2026-09-25)

```bash
UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
EV=mail-finder/wave4/L02/arm-07/evidence
curl -sL -A "$UA" -o "$EV/amplifica_aboutus.html" https://www.amplifica.capital/aboutus
curl -sL -A "$UA" -o "$EV/congruent_abe-yokell.html" https://www.congruentvc.com/team/abe-yokell
curl -sL -A "$UA" -o "$EV/stellantis_home.html" https://www.stellantis.ventures/
```

## Result

**0 FOUND / 3 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L02/arm-07/`.
