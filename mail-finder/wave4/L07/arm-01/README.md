# Mail Finder — Wave4 / L07 / Arm 01

**Focus:** Curated, openly accessible **investor directories** comparable to **Mercury-class** public listings (structured investor/contact tables; no login, subscription, or paywall for the cited record).

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. Search **Mercury Investor Database** (`mercury.com/investor-database`) — slug probe + full investor-database sitemap.
2. Search **Fundraising Fox** (`fundraisingfox.com`) — people + firm investor pages and people sitemaps.
3. Spot-check other Mercury-class surfaces where firm-relevant: **OpenVC** fund profiles, **Private Equity International** institution contact tables, **NFX Signal** (public cards only).
4. **FOUND** only when the **same public directory record/page** shows the **exact target name** and an **exact person@firm** email (preserve published local-part spelling).
5. Profiles with name only, social links, firm, or **generic** mailboxes (`info@`, `team@`, `IR@`, `enquiries@`, masked/paywalled email columns) → **EMPTY**.
6. If directory provenance or whether email is truly public is unclear → **UNCERTAIN** (none this run).

## Prohibited

Hunter, Apollo, RocketReach, ZoomInfo, Lusha, paid contact brokers, LinkedIn/Sales Navigator scraping, SMTP verification, pattern guessing, invented emails, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`); non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | `directory-search-log.json`, `negative-excerpts.md` |

## Scope

Write **only** under `mail-finder/wave4/L07/arm-01/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l07-arm01-1301`
