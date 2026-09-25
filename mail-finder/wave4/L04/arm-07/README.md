# Mail Finder — Wave4 / L04 / Arm 07

**Focus:** Public **SEC EDGAR** exhibits, **Form D** filings, and **signature blocks**; preserve published local-part spelling.

## Inputs

- `input.csv` — 5 seats (Monday export).

## Method (`SEC_EDGAR_exhibits;SEC_EDGAR_Form_D;signature_blocks`)

1. Query **SEC EDGAR full-text** (`efts.sec.gov/LATEST/search-index`) for person name, firm, website domain, and `@domain` strings; scope by issuer **CIK** when useful (Hyatt `1468174`, Telefónica `81052`, AmBev/AB InBev for Bavaria chain).
2. Pull **Form D**, **20-F/6-K**, and **exhibit** primary documents; extract text from HTML/XML (archived under `evidence/`).
3. **FOUND** only when a filing/exhibit cites **that person’s name** and a **non-generic person `@firm` email** together (exact published local-part).
4. **Generics** (`info@`, `ir@`, `amv@`, corporate comms, etc.) → **EMPTY** unless name-attributed on the same block (none in this batch).
5. **Forbidden:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, paid/authenticated sources, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, non-blank `Checked_URLs`, optional `Email` when FOUND |
| `summary.md` | Scorecard |
| `stamp-list.json` | FOUND seats only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `evidence/` | EDGAR query log, URL index, negative excerpts, filing snapshots |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L04-arm07) contact@example.com'
EV=mail-finder/wave4/L04/arm-07/evidence
curl -s -A "$UA" -o "$EV/hyatt_ex141_2016.htm" \
  'https://www.sec.gov/Archives/edgar/data/1468174/000146817416000152/a123115exhibit141.htm'
curl -s -A "$UA" -o "$EV/0000814052-25-000036-index.htm" \
  'https://www.sec.gov/Archives/edgar/data/81052/000081405225000036/0000814052-25-000036-index.htm'
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L04/arm-07/`.
