# Mail Finder — Wave4 / L10 / Arm 01

**Focus:** Public **Brazilian CNPJ**, **IAPD**, **Canadian securities** (incl. BCSC), **DocuSign**-class signature blocks, and **ethics/compliance PDFs**.

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (`regulatory_compliance_PDF`)

1. **SEC EDGAR full-text** (`efts.sec.gov/LATEST/search-index`) for person, firm, domain, and `@` local-parts.
2. **FINRA IAPD** firm/individual search when the seat maps to a US registered adviser (`api.adviserinfo.sec.gov`).
3. **BCSC** public document search portal for Canadian exempt-distribution / 45-106F1-class filings.
4. **Brazilian CNPJ** — Receita Federal public CNPJ consultation when seat geo or firm suggests a Brazil entity (negative for this batch).
5. **DocuSign / signature blocks** — inspect SEC exhibits and regulatory PDFs for co-located name + email (not LinkedIn or press-only pages).
6. **Ethics / compliance PDFs** — e.g. bank Code of Conduct; generics (`conduct@`, `info@`, `sif@`, `whistle@`) do not qualify.
7. **FOUND** only when the **same public PDF/page** cites **that person’s name** and a **non-generic person@firm** (published spelling).
8. **Forbidden:** Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP verification, invented emails, paid/authenticated sources, **Monday writes**.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | PDF/HTML snapshots, excerpts, URL index |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L10-arm01) contact@example.com'
EV=mail-finder/wave4/L10/arm-01/evidence
curl -sS -A "$UA" -o "$EV/factorial_exhibit8.htm" \
  'https://www.sec.gov/Archives/edgar/data/2049662/000160548426000052/Exhibit8.htm'
curl -sS -A "$UA" -o "$EV/genlogs_exit_pr.pdf" \
  'https://0e190a550a8c4c8c4b93-fcd009c875a5577fd4fe2f5b7e3bf4eb.ssl.cf2.rackcdn.com/EINPresswire-889760480-venture-53-exits-genlogs-as-the-freight-intelligence-innovator-enters-its-next-phase-of-growth-2.pdf'
curl -sS -A "$UA" -o "$EV/abnamro_code_of_conduct.pdf" \
  'https://assets.ctfassets.net/1u811bvgvthc/41lBW0oknzRdlD32ggd8MN/b5bcd991e044489d88ed42cc0daa84df/Code_of_Conduct.pdf'
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L10/arm-01/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l10-arm01-86ad`
