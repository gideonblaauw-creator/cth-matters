# Mail Finder — Wave4 / L07 / Arm 05

**Focus:** Curated, **openly accessible** investor directories (Mercury-class) that publish structured investor listings — no login, subscription, paywall, or bulk contact-data brokers.

## Input

`input.csv` — 5 seats (Monday CRM export).

## Method

For each seat:

1. Search **Mercury Investor Database** (slug URL + full `investor-database/sitemap.xml` scan).
2. Check Mercury-class public directories: **findfunding.vc**, **investormatch.pro**, **evalyze.ai**, **NFX Signal** (public HTML only).
3. Optionally note **OpenVC** attempts; Cloudflare blocks are **not** used for FOUND.
4. **FOUND** only when **exact target name** + **person@firm** email appear on the **same** directory record, with directory name, stable URL, and citation-grade excerpt.
5. **EMPTY** for missing listings, name-only rows, social/LinkedIn-only links, or **generic** firm mailboxes (`admin@`, `founders@`, `info@`) without person attribution on the same record.
6. **Prohibited:** Hunter, Apollo, RocketReach, ZoomInfo, Lusha, paid databases, LinkedIn/Sales Navigator scraping, SMTP verification, pattern guessing, invented emails, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status`; non-blank `Checked_URLs`; optional `Email` when FOUND |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | Directory HTML snapshots, negative excerpt log |

## Scope

Write **only** under `mail-finder/wave4/L07/arm-05/`. Do not modify other arms or Monday.

## Audit

Negative log: `evidence/negative-excerpts.md`.
