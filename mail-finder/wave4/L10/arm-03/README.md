# Mail Finder — Wave4 / L10 / Arm 03

**Focus:** Public **CNPJ-class** registries (Brazil, where applicable), **FINRA IAPD**, **SEC EDGAR** (Form D, exhibits, signature blocks), **Canadian securities** (**BCSC** document search), and **DocuSign / ethics / compliance / fund marketing PDFs** on allowlisted public hosts.

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (`CNPJ_IAPD_BCSC_DocuSign_ethics_PDF`)

1. Map seat to firm domain; run **SEC EDGAR EFTS** and pull **Form D / 8-K exhibits** when adviser or issuer links exist.
2. Pull **IAPD** firm record and **Form ADV Part 2A PDF** when CRD maps to the seat (Great North Ventures → CRD **316159**).
3. Search **BCSC** public document portal for firm/name (HTML index; no login).
4. Where Brazil geo applies, sanity-check **CNPJ** public listings — reject wrong-entity matches (unrelated “Valor Capital LTDA” admin shell vs Valor Capital Group VC).
5. Crawl first-party sites for published **ethics / impact / LP** PDFs and **DocuSign-class** signed disclosures when linked on firm domains.
6. **FOUND** only with **display name + exact personal `person@firm`** on the **same page/PDF block**. Generics (`info@`, `careers@`, `community@`, `webmaster@`, IR/third-party broker emails) → **EMPTY**.

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, pattern guessing, SMTP verification, invented emails, paid/authenticated enrichment, **Monday writes**, writes outside `mail-finder/wave4/L10/arm-03/`.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only (empty array this run) |
| `summary.md` | Scorecard |
| `evidence/` | ADV PDF text, SEC exhibit HTML, URL index, negative excerpts |

## Result (this run)

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L10/arm-03/`.

**Branch:** `cursor/mail-finder-wave4-l10-arm03-3291`  
**Processed:** 2026-09-25 (UTC)

Protocol: `mail-finder/protocol/Mail-Finder-Workbench-Strategy.md`.
