# Mail Finder — Wave4 / L03 / Arm 03

**Focus:** **Regulatory / securities PDF** email discovery for 5 Potential Investors seats (`input.csv`).

## Method

Public regulatory corpora only (no Hunter/Apollo, no LinkedIn scrape, no pattern+SMTP, no invented emails):

- SEC EDGAR + **EFTS** full-text (`efts.sec.gov`)
- **Form D** / amendment XML and signature blocks
- SEC **IAPD** Form ADV Part 2A PDFs (`reports.adviserinfo.sec.gov`)
- **BCSC** document search (Form 45-106F1 and related exempt-market reports)
- **SEDAR+** / other national filing indexes via public web search when EDGAR is thin
- FINRA/IAPD-class adviser brochures where the seat maps to a registered adviser

**FOUND gate:** display name and **person@firm** (non-generic) must **co-occur in the same public PDF/filing** using published spelling. Role/generic inboxes (`info@`, `admin@`, fund contact lines without person attribution) → **EMPTY**.

## Input

`input.csv` — Monday_item_id, Name, Contact_name, Firm, Kind, Priority, Status, Website, Domain, LinkedIn.

## Forbidden

- Hunter, Apollo, LinkedIn scrape, pattern guessing, SMTP verify, invented emails
- Monday API writes (workbench imports `stamp-list.json` only)
- Writes outside `mail-finder/wave4/L03/arm-03/`

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat Status, Checked_URLs, Notes |
| `stamp-list.json` | FOUND emails only (`email_mm7ffmz4` workbench import) |
| `summary.md` | Scorecard |
| `evidence/` | Regulatory negative cites; person-email PDF snapshots when FOUND |
| `README.md` | This file |

## Result (this run)

**0 FOUND / 5 EMPTY** — see `summary.md` and `evidence/empty-rationale.md`.

Protocol: `mail-finder/protocol/Mail-Finder-Workbench-Strategy.md`.
