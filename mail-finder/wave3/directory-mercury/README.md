# Wave3 Arm 4 — `directory_mercury`

Citation-grade **person@firm** discovery using **public directory pages only** (search-seed: name + firm).

## Inputs

- `input.csv` — seat list for this arm (~12 rows), column `method_arm=directory_mercury`

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Full matrix: every seat has `Status`, `Checked_URLs`, `Notes`, `Method` |
| `summary.md` | Human summary and counts |
| `stamp-list.json` | **FOUND only** — empty array `[]` when nothing qualifies |
| `evidence/` | Saved HTML from Mercury, IDB Invest, APG, issuer/nonprofit directories |

## Allowed methods

1. [Mercury Investor Database](https://mercury.com/investor-database) **public profile URLs** (same-page name + Contact Email)
2. IFC / MDB / IDB Invest disclosure or training pages with responsible officers
3. Academic / accelerator / nonprofit investor lists with **name + email on the same page**

## Hard rules

- No Hunter / Apollo / ContactOut / Clearbit
- No pattern guessing, SMTP verify, or invented emails
- No LinkedIn scrape; no paid email finders
- No third-party **bulk** Mercury APIs or scrapers (individual profile fetches OK)
- Profile exists but **no email on page** → `EMPTY`
- Generic inbox on same page (e.g. `info@`, `team@`) without person@firm → `EMPTY`
- Wrong domain vs Monday `Domain` → `EMPTY` (domain gate)

## Regenerate

```bash
python3 build_results.py
```

## Monday

Do **not** write to Monday from this folder; export `stamp-list.json` only for downstream stamping.
