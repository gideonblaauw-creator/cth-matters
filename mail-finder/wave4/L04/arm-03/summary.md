# Wave4 L04 Arm 03 — scorecard

**Lane:** L04 (SEC EDGAR exhibits / Form D / signature blocks)  
**Arm:** 03  
**Seats:** 5  
**Run date:** 2026-09-25  

## Results

| Monday_item_id | Name | Firm | Status |
|----------------|------|------|--------|
| 13114434007 | Jacob Haar | Community Investment Management (CIM) | EMPTY |
| 13028371978 | Jessica Diaz Nunez | IDB Invest | EMPTY |
| 13028336447 | Kevin Bone | Lightrock | EMPTY |
| 13028357441 | Klaus Prebensen | Impact Fund Denmark | EMPTY |
| 12727972974 | Kuehne+Nagel / Reefknot | Kuehne+Nagel / Reefknot | EMPTY |

**FOUND:** 0  
**EMPTY:** 5  
**UNCERTAIN:** 0  

## Method notes

- Primary corpus: SEC EDGAR full-text (EFTS `search-index`), Form D primary XML, and transaction exhibits (8-K, F-1, loan agreements).
- **FOUND gate:** target name + exact person `@firm` email in the **same** public filing artifact; preserve published local-part spelling.
- CIM Form D family confirms Jacob Haar as signer/related person but EDGAR Form D XML carries **no email fields** for these issuers.
- Lightrock appears in Lilium/Qell exhibits with **generic** `umur@lightrock.com` / `legal@lightrock.com` only — excluded.
- IDB Invest / Danish Impact Fund / Reefknot venture: no indexed EDGAR artifacts pairing seat holders with person-domain emails.

## Deliverables

- `input.csv`, `results.csv`, `stamp-list.json` (`[]`), `README.md`, `summary.md`
- `evidence/` — Form D snapshots, excerpts, `url-index.md`, `edgar_search.json`

**Monday:** no API writes (workbench imports `stamp-list.json` when FOUND exists).
