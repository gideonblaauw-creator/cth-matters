# Mail Finder — Wave4 / L03 / Arm 07

**Focus:** Regulatory and national-securities **PDF / filing text** — BCSC Form 45-106F1, SEC EDGAR (Form D, 6-K, exhibits), FINRA/IAPD, signature blocks.

## Inputs

- `input.csv` — 5 seats (Monday export).

## Method (`regulatory_PDF`)

1. Query **SEC EDGAR full-text** (`efts.sec.gov/LATEST/search-index`) for person name, firm, and `@domain`.
2. Pull **Form D / exhibit / 6-K** primary documents; extract text (XML/HTML/PDF via `pypdf` where needed).
3. Search **BCSC** public search / 45-106F1 pattern for Canadian exempt distributions (negative for this batch).
4. **FINRA IAPD** firm/individual search when adviser registration applies (i80 Group seat).
5. **FOUND** only when a **public PDF or filing block** cites **that person’s name** and a **non-generic person `@firm` email** together (published spelling).
6. **Generics** (`info@`, `ir@`, `investors@`, corporate comms inboxes) → **EMPTY**.
7. **Forbidden:** Hunter/Apollo, LinkedIn scrape, pattern+SMTP, invented emails.
8. **No Monday writes** from this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, `Checked_URLs`, optional `Email` when FOUND |
| `summary.md` | Scorecard |
| `stamp-list.json` | FOUND seats only (for downstream stamping) |
| `evidence/` | Filing snapshots, negative excerpts, URL index, EDGAR hit JSON |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; regulatory-pdf) contact@example.com'
EV=mail-finder/wave4/L03/arm-07/evidence
curl -s -A "$UA" -o "$EV/amplifica_form_d_2021.xml" \
  'https://www.sec.gov/Archives/edgar/data/1852706/000185270621000001/primary_doc.xml'
curl -s -A "$UA" -o "$EV/congruent_form_d_2017.xml" \
  'https://www.sec.gov/Archives/edgar/data/1694110/000169411017000002/primary_doc.xml'
curl -s -A "$UA" -o "$EV/factorial_exhibit8.htm" \
  'https://www.sec.gov/Archives/edgar/data/2049662/000160548426000052/Exhibit8.htm'
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L03/arm-07/`.
