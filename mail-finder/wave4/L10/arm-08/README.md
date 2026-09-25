# Mail Finder — Wave4 / L10 / Arm 08

**Focus:** Public **CNPJ** (Brazilian corporate registry listings), **FINRA IAPD**, **Canadian securities** filings (incl. **BCSC** document search), **DocuSign**-style signed PDFs when published, and **ethics/compliance** PDFs on firm or foundation sites.

**Write path:** `mail-finder/wave4/L10/arm-08/` only. **No Monday API writes** from this arm.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. **IAPD** — `api.adviserinfo.sec.gov` firm/individual search when US adviser registration may apply.
2. **BCSC / Canadian securities** — public document search portal for exempt-distribution / 45-106-class patterns.
3. **CNPJ** — public Brazilian registry mirrors; **reject wrong-entity** homonyms that do not match the seat domain/firm.
4. **Ethics / compliance / impact PDFs** — download first-party PDFs; extract with `pdftotext`.
5. **DocuSign** — include only when a public signed PDF attributes a named person and mailbox on the same document.
6. **FOUND gate:** printed **target name** + **person@firm** on the **same public page or PDF block**. Generics → **EMPTY**. Name without email or email without target name → **EMPTY**. Ambiguous → **UNCERTAIN**.

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, email pattern guessing, SMTP verification, invented addresses, paid/authenticated contact brokers, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only — `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | PDF snapshots, URL index, negative excerpts |

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l10-arm08-8a82`
- Result: **0 FOUND / 5 EMPTY**
