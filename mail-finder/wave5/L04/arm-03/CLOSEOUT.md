# Wave5 L04 Arm 03 — CLOSEOUT

**Title hint:** MF W5 L04 arm-03 regulatory mailbox  
**Branch:** `cursor/mf-w5-l04-arm03-regulatory-mailbox-af7f`  
**Path:** `mail-finder/wave5/L04/arm-03/` only

## Counts

| Metric | Value |
|--------|------:|
| Input seats | 5 |
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |
| stamp-list entries | 0 |

## Method summary

Primary sources only: SEC IAPD Form ADV PDFs (CRD 277131, 284908, 305587), SEC Form D primary XML for Quona / Lachy Groom / QED / Accial entities, EDGAR EFTS full-text (`@domain`, name+`@` boolean), IAPD search API (firm/individual). Did **not** use Form D / ADV Part 1 name-only rows as FOUND evidence. Did not use Hunter/Apollo, LinkedIn scrape, pattern guessing, or Monday API.

## Blockers / environment

- Standalone IAPD brochure PDF URLs (`/Brochure/{id}.pdf`) returned **403** from this environment; combined ADV PDF downloads (200) were used instead.
- BCSC search URLs referenced in prior waves returned **404** here; no BCSC 45-106F1 artifact with mailbox was retrieved for these seats.
- Colombia SFC agent registry portal is login-gated; no public HTML/PDF with Lawrence Chua + personal email was obtained.

## Deliverables

- [x] `input.csv` (5 seats)
- [x] `results.csv` (5 rows, all `Checked_URLs` non-blank)
- [x] `results.md`
- [x] `stamp-list.json` (empty — no FOUND)
- [x] `evidence/` (URL index, negative excerpts, ADV/Form D samples, `edgar_search.json`)
- [x] Draft PR (not merged)

## Monday

No Monday writes performed.
