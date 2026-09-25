# Mail Finder — Wave4 / L05 / Arm 05

**Focus:** Public **impact reports**, **LP / investor materials**, **annual reports**, and comparable **PDFs** where a named person and mailbox co-occur.

## Input

`input.csv` — 5 seats (Monday CRM export).

## Method

For each seat:

1. Search public PDFs (firm site assets, fund press/impact PDFs, event agendas, cited LP materials).
2. Open each candidate PDF; extract text (`pdftotext`) and verify **name + person@firm** on the same document.
3. **FOUND** only with citation-grade excerpt (URL, page/section when available, printed spelling).
4. **EMPTY** for generics, name-only, email-only, or legacy/wrong domains vs seed firm website.
5. **Prohibited:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn scraping, paid/authenticated sources, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status`; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | PDFs, negative log, SEC artifacts |

## Scope

Write **only** under `mail-finder/wave4/L05/arm-05/`. Do not modify other arms or Monday.

## Audit

Search log: `evidence/pdf_search_log.md`.  
SEC requests use descriptive User-Agent per SEC fair-access policy.
