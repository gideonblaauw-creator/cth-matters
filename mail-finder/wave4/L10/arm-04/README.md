# Mail Finder — Wave4 / L10 / Arm 04

**Focus:** Registry and compliance **PDF** lane — public **Brazilian CNPJ** (where entity geography applies), SEC **IAPD** Form ADV, **Canadian securities** (BCSC search / 45-106F1 class), **DocuSign** and **ethics/compliance** PDFs on firm or fund sites.

**Write path:** `mail-finder/wave4/L10/arm-04/` only. **No Monday API writes** from this arm.

## Input

- `input.csv` — 5 seats (Monday export): Son Nguyen (IIX), Susana Garcia-Robles (Capria), Séverine Grégoire (ZEBOX), Tiffany Chen (Carbon Equity), Tim Rehder (Earlybird).

## Method (per seat)

1. **IAPD** — firm search → download Form ADV PDF → `pdftotext`; look for target name + `person@firm` on same document.
2. **SEC EDGAR** full-text — `"Name"`, `@domain`, Form D / adviser filings where relevant.
3. **BCSC** — site search for issuer/fund strings; follow public `.pdf` links when present.
4. **CNPJ / national registry PDFs** — when seat firm maps to a Brazilian (or other) registry publication with contact blocks.
5. **Ethics / impact / DocuSign PDFs** — firm-hosted or fund compliance PDFs; require name + non-generic mailbox co-occurrence.
6. **Generics** (`info@`, `impact@`, `ventures@`, `grievance@`, `support@`, desk inboxes) → **EMPTY** for attribution.

## Forbidden

Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP verify, invented emails, paid sources, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat Status (FOUND \| EMPTY \| UNCERTAIN), non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND rows only for HITL Monday patch |
| `summary.md` | Scorecard |
| `README.md` | This arm spec |
| `evidence/` | ADV extracts, impact PDF text, negative excerpts |

## FOUND gate

Record email only when the **same public page or PDF** attributes a **person@firm** address to **that named person** (published spelling).

Protocol: `mail-finder/protocol/Mail-Finder-Workbench-Strategy.md`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l10-arm04-f0cb`
