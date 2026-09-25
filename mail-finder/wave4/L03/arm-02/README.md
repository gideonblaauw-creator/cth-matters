# Mail Finder — Wave4 L03 Arm 02 (regulatory / securities PDF)

**Exclusive path:** `mail-finder/wave4/L03/arm-02/`  
**Lane:** Lane B (CTH Matters)  
**Input:** `input.csv` (5 seats)

## Method

Public-web discovery and PDF text extraction focused on regulatory and securities sources:

- SEC EDGAR full-text (`efts.sec.gov`) and Form D issuer filings
- FINRA IAPD Form ADV PDF (Eclipse CRD 255789)
- Hyatt investor / GRI / ethics PDFs
- Impact/regulatory PDFs (e.g. FLII2025 report for Angel Ventures speaker roster)
- BCSC / SEDAR+ / CNMV-oriented searches where applicable

**FOUND** requires citation-grade co-occurrence of the target person’s published name and an exact `person@firm` email in the **same public PDF** (or equivalent regulatory filing text). Generics (`info@`, `impact@`, `ethics@`, `admin@`, etc.) do not qualify.

## Deliverables

| File | Description |
|------|-------------|
| `input.csv` | Seed rows (Monday export) |
| `results.csv` | One row per seat; `Checked_URLs` documents sources searched |
| `stamp-list.json` | FOUND-only Monday stamps (empty this run) |
| `summary.md` | Scorecard |

## Outcome (this run)

All five seats **EMPTY** after regulatory PDF lane — no qualifying person@firm cites. No Monday API writes.

## Forbidden (not used)

Hunter/Apollo, LinkedIn scrape/Sales Nav/PhantomBuster, pattern guessing, SMTP verification, invented emails, non-public/authenticated sources.
