# CLOSEOUT — Wave5 L04 Arm 06

## Run

- **Branch:** `cursor/mf-w5-l04-arm06-regulatory-1ac0`
- **Exclusive path:** `mail-finder/wave5/L04/arm-06/`
- **Date (UTC):** 2026-09-25

## Seat counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

**Input rows:** 5  
**`results.csv` rows:** 5 (1:1 with input)

## Method summary

For each seat, searched public regulatory corpora for artifacts that bind the target person to a non-generic firm-domain mailbox:

- SEC EDGAR EFTS (name + `@domain` co-occurrence queries)
- Form D `primary_doc.xml` for Construct, Quona, and Bahat-related issuers
- IAPD Form ADV Part 1 PDF text (Construct CRD 310594, Quona CRD 277131)
- BBVA parent 6-K (BBVA Spark organizational reference)
- Proeza-related SEC 8-K (Dila Capital) and XOS/NextGen board disclosure text
- Form C crowdfunding primary doc (Inside.com — Bahat mention not in contact fields)

No qualifying artifact paired any target `Contact_name` with a personal `person@firm` email in the same document block. Form D / ADV Part 1 name-only rows were not promoted (W2 lesson).

## Deliverables

| File | Status |
|------|--------|
| `input.csv` | Copied from upload |
| `results.csv` | Complete |
| `results.md` | Complete |
| `stamp-list.json` | Empty (`items: []`) — no FOUND |
| `CLOSEOUT.md` | This file |
| `evidence/` | URL index, negative excerpts, Form D/ADV snapshots |

## Notes

- IAPD Part 2A brochure PDF endpoints returned 403 to automated fetch; Part 1 layers contained no person-level employee emails for targets.
- Generic/role addresses observed in adjacent filings (BBVA IR, law-firm emails on SPAC docs, Quona firm social handles) were excluded per arm rules.
- **Monday API:** not called.
