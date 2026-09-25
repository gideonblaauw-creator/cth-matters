# MF Wave5 L04 Arm 04 — Regulatory with mailbox

**Method:** Public regulatory filings / registries / IAPD Form ADV and SEC EDGAR artifacts that may co-publish a legal name with a personal firm mailbox. **FOUND** only when `Contact_name` and `person@firm` appear in the **same** citation artifact. Form D / ADV Part 1 name-only rows skipped when no mailbox present. Role/generic mailboxes → EMPTY.

| Monday_item_id | Contact_name | Firm | Status | Email | Citation |
|---|---|---|---|---|---|
| 13132451596 | Lee Fixel | Addition | EMPTY | — | IAPD ADV 309075 names Fixel; no @addition.com in filing |
| 13132447815 | Mark Simmer | Clear Haven Capital Management | EMPTY | — | IAPD ADV 149165 + Form D signer; no person@clearhaven.com |
| 13132451948 | Michal Zalesak | Lighthouse Ventures | EMPTY | — | CZ ARES/rejstřík + SEC 0; no regulatory name+mailbox bind |
| 13028367829 | Mikayla Hart | (Congruence Capital) | EMPTY | — | IAPD ADV 328559 Partner listing; no @congruencecapital.com |
| 13132412518 | Mike Packer | QED Investors | EMPTY | — | IAPD ADV 284908; Packer absent; EDGAR 0 for person@ |

## Scorecard

| Status | Count |
|---|---|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |
| **Total seats** | **5** |

## Notes

- IAPD full Form ADV PDFs downloaded for Addition (309075), Clear Haven (149165), QED (284908), and Congruence (328559); extracted text contains **zero** `@firm` employee addresses (consistent with ADV instruction not to supply individual employee emails).
- BCSC document search endpoints returned 404 from this environment; primary pass relied on SEC IAPD/EDGAR and Czech public registers.
- No Monday writes; `stamp-list.json` empty (FOUND-only).
