# Mail Finder — Wave4 / L07 / Arm 07

**Focus:** Curated **Mercury-class** public investor directories — structured listings with direct contact fields, no login/paywall, no bulk contact brokers.

## Inputs

- `input.csv` — 5 seats (Monday export).

## Method (`Mercury_investor_database;ImpactAssets_IA50;GIIN_member_directory;Signal_NFX;FundraisingFox`)

1. Search **Mercury Investor Database** (slug URLs + full `investor-database/sitemap.xml` scan + `?q=` landing).
2. Check **ImpactAssets IA50** fund/listing pages when publicly reachable.
3. Check **GIIN** member search and firm member profile pages.
4. Check **Signal NFX** firm and investor slugs (public HTML only; no Gmail intro unlock).
5. Check **Fundraising Fox** investor/people listings when openly published — **exclude** masked “reveal” email brokers.
6. **FOUND** only when the seat **published name** and exact **person@firm** email co-occur on the **same** directory record/page, with citation-grade excerpt.
7. **Generics** (`info@`, `contact@`, `press@`, shared inboxes) → **EMPTY**.
8. **Forbidden:** Hunter, Apollo, RocketReach, ZoomInfo, Lusha, paid DBs, LinkedIn/Sales Navigator scraping, SMTP verification, pattern guessing, invented emails, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, non-blank `Checked_URLs`, optional `Email` when FOUND |
| `summary.md` | Scorecard |
| `stamp-list.json` | FOUND seats only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `evidence/` | URL index, negative excerpts, directory search log, HTML snapshots |

## Re-run (2026-09-25)

```bash
UA='Mozilla/5.0 (X11; Linux x86_64) MailFinderResearch/1.0 (cth-matters; L07-arm07)'
EV=mail-finder/wave4/L07/arm-07/evidence
curl -sL -A "$UA" -o "$EV/mercury-investor-sitemap.xml" https://mercury.com/investor-database/sitemap.xml
curl -sL -A "$UA" -o "$EV/mercury-shruti-control.html" https://mercury.com/investor-database/shruti-gandhi
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L07/arm-07/`.
