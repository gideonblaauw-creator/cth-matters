# CLOSEOUT — Wave5 L04 Arm 07 (regulatory with mailbox)

**Exclusive path:** `mail-finder/wave5/L04/arm-07/`  
**Method:** Public regulatory filings / registries / adviser disclosures (SEC Form D, IAPD Form ADV Part 1 PDF, EDGAR EFTS; CVM cadastro probe)  
**Seats:** 5  

## Counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

**Input rows:** 5  
**`results.csv` rows:** 5 (1:1)

## Run notes

- All five targets appear on SEC Form ADV Part 1 and/or Form D related-person tables, but none of the retrieved **qualifying** artifacts bind the target `Contact_name` to a non-generic personal `@firm` mailbox on the same document block (Form D / ADV Part 1 name-only lesson applied).
- IAPD Form ADV **Part 2A brochure** PDF endpoints returned 403 from automated fetch; Part 1 PDF text layers contained **no** e-mail addresses for any firm in this arm.
- Kaszek MELI SPAC EX-99.1 lists `pr@kaszek.com` (press) without Santiago Fossatti on the same contact block — treated as generic/role, not FOUND.
- Sam Altman seat: registered adviser entity is **Altman Capital Management, LLC** (CRD 312632); Part 1 does not list Sam/Samuel Altman as control person.
- BCSC document search URLs returned 404 in this environment; CVM cadastro HTML search did not surface a Fossatti + personal e-mail regulatory PDF.
- **Monday:** not written (per arm rules).
- **PR:** draft only; not merged.

## Deliverables

| File | Status |
|------|--------|
| `input.csv` | From upload |
| `results.csv` | Complete |
| `results.md` | Complete |
| `stamp-list.json` | Empty (no FOUND) |
| `CLOSEOUT.md` | This file |
| `evidence/` | URL index, negative excerpts, ADV PDFs, Form D / filing captures |
