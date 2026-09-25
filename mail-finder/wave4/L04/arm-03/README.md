# Mail Finder — Wave4 L04 Arm 03

**Method:** Public **SEC EDGAR** filings — Form D / A, exhibits (8-K, F-1, SC 13, loan agreements), and filing signature / related-person blocks. Use firm and target name to disambiguate.

**Exclusive path:** `mail-finder/wave4/L04/arm-03/` only.

## HARD rules (summary)

- **FOUND** only when the target person’s published name and an exact `person@firm` email appear in the **same** public filing or exhibit. Preserve local-part spelling exactly.
- Record stable filing URL + citation-grade excerpt (page/section when applicable).
- Generic mailboxes (`info@`, `legal@`, `monitor@iadb.org`, etc.) → **EMPTY**.
- Forbidden: pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn scrape, paid sources, **Monday writes**.

## Workflow

1. Query [SEC EDGAR full-text search](https://efts.sec.gov/LATEST/search-index) for person, firm, and `@domain`.
2. Open Form D `primary_doc.xml` and relevant exhibits; extract related-person / signature blocks.
3. Classify **FOUND | EMPTY | UNCERTAIN**; populate `Checked_URLs` for every seat (non-blank).
4. Append **FOUND** rows to `stamp-list.json` with `Evidence_excerpt`.

## Deliverables

| File | Purpose |
|------|---------|
| `input.csv` | Monday seed (5 seats) |
| `results.csv` | Per-seat status, notes, checked URLs |
| `stamp-list.json` | FOUND only — `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | Optional filing snapshots and negative excerpts |

## This run

All five seats **EMPTY** under the SEC EDGAR gate. See `summary.md` and `evidence/url-index.md`.

**No Monday API writes** from this agent.
