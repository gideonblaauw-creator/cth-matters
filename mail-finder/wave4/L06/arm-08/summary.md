# Wave4 L06 Arm 08 — Press / podcast / speaker mailto scorecard

**Loop:** Mail Finder Wave4 L06 Arm 08  
**Seats processed:** 5  
**Run date:** 2026-09-25 (UTC)

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Method

Public **press releases**, **podcast/show pages**, **conference/speaker listings**, and comparable publisher-controlled HTML. **FOUND** only when the seat **display name** and an exact **non-generic person@firm** email (or `mailto:` target) **co-occur on the same page**. Generics (`info@`, `hello@`, `team@`, `support@`, `ventures@`, `tech@`, `contact@`, publisher support inboxes, speaker-agency mailboxes) → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP verify, or invented emails.

## Per-seat outcomes

| Monday_item_id | Name | Firm | Outcome |
|----------------|------|------|---------|
| 13028366345 | Son Nguyen | IIX | EMPTY — Vietcetera ESG panel + alumni bio; no person@iixglobal.com |
| 13114451331 | Susana Garcia-Robles | Capria Ventures | EMPTY — ImpactAlpha podcast + Capria bio/PDF; generics only |
| 13100496537 | Séverine Grégoire | ZEBOX Ventures | EMPTY — ventures@ze-box.io generic beside manager name |
| 13028372158 | Tiffany Chen | Carbon Equity | EMPTY — team/press paths; support@ generic only |
| 13100506407 | Tim Rehder | Earlybird | EMPTY — member + EUVC podcast + Medium press; tech@/info@ generics |

## Deliverables

- `input.csv` — Monday export (5 seats)
- `results.csv` — all seats with non-blank `Checked_URLs`
- `stamp-list.json` — no FOUND rows (`[]`)
- `evidence/` — HTML snapshots + negative excerpt log
- `README.md` — arm specification

**Monday:** no writes (workbench review only).
