# Mail Finder — Wave4 L04 Arm 02

**Exclusive path:** `mail-finder/wave4/L04/arm-02/`  
**Lane:** Lane B (CTH Matters)  
**Input:** `input.csv` (5 P1 seats)

## Method

Public **SEC EDGAR** filings and exhibits as the primary source family:

1. **EDGAR full-text** search (`efts.sec.gov/LATEST/search-index`) for person name, firm, and `@domain`.
2. Pull **Form D** primary XML, **6-K / 8-K exhibits** (HTML), and **signature blocks** (Form D, Form 4, exhibit POA/signature pages).
3. **FOUND** only when the target person’s **published name** and an exact **person@firm** email appear in the **same** public filing artifact or exhibit (preserve local-part spelling).
4. **EMPTY** for generics (`info@`, `comunicacion.corporativa@`, IR/PR emails on press exhibits not attributed to the target), name-only signature blocks, or email-only blocks without the target name.
5. **Forbidden:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, paid/authenticated sources, Monday writes.

## Deliverables

| File | Description |
|------|-------------|
| `input.csv` | Seed rows (Monday export) |
| `results.csv` | One row per seat; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND-only stamps (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | Filing snapshots and negative excerpts |

## Outcome (this run)

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Re-run (User-Agent required)

```bash
UA='CTH-Matters-MailFinder contact@cth-matters.example'
EV=mail-finder/wave4/L04/arm-02/evidence
curl -s -A "$UA" -o "$EV/i80_form_d_2019.xml" \
  'https://www.sec.gov/Archives/edgar/data/1717048/000171704819000003/primary_doc.xml'
curl -s -A "$UA" -o "$EV/lendable_form_d_2026.xml" \
  'https://www.sec.gov/Archives/edgar/data/1816111/000181611126000001/primary_doc.xml'
```

## Scope

Write **only** under `mail-finder/wave4/L04/arm-02/`.
