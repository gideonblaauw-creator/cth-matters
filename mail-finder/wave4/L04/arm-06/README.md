# Mail Finder — Wave4 / L04 / Arm 06

**Focus:** SEC EDGAR **exhibits**, **Form D** (and amendments), and **signature blocks** — require published **name + person@firm email** on the same public filing artifact (preserve exact local-part spelling).

**Write path:** `mail-finder/wave4/L04/arm-06/` only. **No Monday API writes** from this arm.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. **SEC EDGAR EFTS** — phrase and domain searches; disambiguate with firm / fund legal name (e.g. Atlantico Partners, Endeavor Catalyst).
2. **Form D primary docs** — `https://www.sec.gov/Archives/edgar/data/{CIK}/{accession}/xslFormDX01/primary_doc.xml`; review Item 3 related persons and signature tables.
3. **Exhibits** — 8-K / registration / M&A exhibits when EFTS links fund or person to a filing set.
4. **Signature without email** → **EMPTY** (not UNCERTAIN).
5. **Generic mailboxes** (`info@`, `IR@`, `press@`, etc.) → **EMPTY**.

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, email pattern guessing, SMTP verification, invented addresses, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Every seed row once; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND rows only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | Citation-grade excerpts; `evidence/formd/` optional Form D snapshots |

## FOUND gate

Record email only when the **same SEC filing or exhibit** attributes a **person@firm** address to **that named person** (exact published spelling).

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l04-arm06-dfb6`
