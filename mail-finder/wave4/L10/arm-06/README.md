# Mail Finder — Wave4 / L10 / Arm 06

**Focus:** Public **Brazilian CNPJ** (where applicable), **FINRA IAPD** / **SEC EDGAR**, **Canadian securities (BCSC)**, **DocuSign** audit trails, and **ethics / compliance PDFs** on issuer or multilateral disclosure sites.

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (per seat)

1. Map seat to jurisdiction; run **CNPJ/OpenCorporates-class** registry pass when Brazil-linked.
2. Search **IAPD** firm brochures and **SEC EDGAR EFTS** full-text for `@firm` + target name co-occurrence.
3. Search **BCSC** public document search for Form **45-106F1**-class filings when Canadian nexus exists.
4. Download public **ethics / ESG / compliance PDFs** (including **DocuSign** certificate pages); extract with `pdftotext`.
5. **FOUND** → target **name + person@firm** on the **same URL/PDF** → `results.csv` + `stamp-list.json`.
6. **EMPTY** → generics-only, name without person mailbox, wrong entity, or no attributable document after reasonable pass.
7. **UNCERTAIN** → ambiguous attribution only.

## Prohibited

Hunter/Apollo, LinkedIn scrape, email pattern invention, SMTP verify, paid/authenticated sources, **Monday API writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`), non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | PDFs, negative excerpts, URL index |

## Scope

Write **only** under `mail-finder/wave4/L10/arm-06/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l10-arm06-c588`
