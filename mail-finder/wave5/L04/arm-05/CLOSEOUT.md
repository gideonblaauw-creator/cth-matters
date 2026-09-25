# CLOSEOUT — Mail Finder Wave5 L04 Arm-05

**Lane:** Regulatory with mailbox  
**Exclusive path:** `mail-finder/wave5/L04/arm-05/`  
**Seats:** 5  
**Run date:** 2026-09-25 (relaunch after infra error)

## Counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Deliverables

- [x] `input.csv` (5 seed rows)
- [x] `results.csv` (5 rows, all `Checked_URLs` non-blank)
- [x] `results.md` (scorecard)
- [x] `stamp-list.json` (empty — no FOUND)
- [x] `evidence/` (URL index, negative excerpts, Form D / ADV snapshots)

## Method summary

Primary sources: SEC EDGAR EFTS, Form D primary XML/HTML, FINRA IAPD Form ADV PDF (Spark CRD 161231), CMF Chile AFIP manager search for 30N. Skipped Form D / ADV Part 1 name-only rows without mailboxes. No Hunter/Apollo, SMTP guessing, LinkedIn scrape, or Monday writes.

## Outcome notes

- Relaunch completed full regulatory pass; prior infra failures (SEC 404/403 on bad accession paths) resolved with corrected archive URLs and rate-limited fetches.
- **0 FOUND** — no seat had target name and personal `@firm` email in the same public regulatory artifact.
- Near-miss: Cometa IV Form D binds **Jose Luis Bolanos Flores** to GP role but omits email; Spark Wayfair DRS binds **alex@sparkcapital.com** to Finkelstein, not Hyatt.

## PR

Draft PR opened; **not merged**.
