# Mail Finder — Wave4 / L04 / Arm 05

**Focus:** SEC EDGAR **exhibits**, **Form D** filings, and **signature blocks** — preserve published local-part spelling.

## Input

`input.csv` — 5 seats (Monday CRM export: item_id, name, contact_name, firm, website, etc.).

## Method

For each seat:

1. Query **SEC EDGAR EFTS** full-text (`https://efts.sec.gov/LATEST/search-index`) for the person name, firm, and `@domain`.
2. Open candidate **Form D** `primary_doc.xml`, **exhibits** (HTML/TXT), and **signature blocks**; disambiguate using firm / fund name.
3. **FOUND** only when the target **name** and a **non-generic person@firm** email co-occur in the **same public filing artifact**, with citation-grade excerpt (and page/section when applicable).
4. **EMPTY** for generics (`info@`, `ir@`, `pr@`, etc.), signature without email, email without target name, or no qualifying EDGAR hit.
5. **Prohibited:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn scraping, paid/authenticated sources, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`); non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND rows only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | Archived filings + negative/positive excerpts |

## Scope

- Write **only** under `mail-finder/wave4/L04/arm-05/`.
- Do **not** modify other arms or Monday.

## Audit

Search log: `evidence/edgar_search.json`.  
SEC requests use a descriptive User-Agent per SEC fair-access policy.
