# CLOSEOUT — MF Wave5 L04 Arm 04 (regulatory with mailbox)

## Counts

| Metric | Value |
|---|---|
| Input seats | 5 |
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |
| Stamp-list entries | 0 |

## Work path

Exclusive path: `mail-finder/wave5/L04/arm-04/`

## Summary

All five seats were researched against public regulatory sources (FINRA/IAPD Form ADV PDFs, SEC EDGAR EFTS and Form D XML, Czech ARES and obchodní rejstřík for Lighthouse Ventures GP s.r.o.). Several targets appear on IAPD Schedule D control-person tables (Lee Fixel, Mark Simmer, Mikayla Hart) or Form D signature blocks (Mark Simmer), but **none** of the qualifying artifacts co-publish a personal `person@firm` mailbox bound to the seat name. Form D name-only rows were not stamped. Generic/role addresses and non-regulatory web contacts were excluded per arm rules.

## Deliverables

- [x] `input.csv`
- [x] `results.csv` (5/5 rows, unique Monday_item_id)
- [x] `results.md`
- [x] `stamp-list.json` (empty — no FOUND)
- [x] `evidence/` (negative regulatory excerpts + URL index)

## Monday

No Monday API writes performed.
