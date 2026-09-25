# CLOSEOUT — Wave5 L03 Arm 08

## Run

- **Branch:** `cursor/mf-w5-l03-arm08-impact-pdf-f531`
- **Exclusive path:** `mail-finder/wave5/L03/arm-08/`
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

For each seat, enumerated first-party and SEC public artifacts in the impact / LP / fund-document / Form ADV lane:

- Firm team and contact HTML (avenuegp.com, nxtp.vc, qedinvestors.com, crosslinkcapital.com)
- SEC Form D primary documents for Avenue and NXTP funds
- SEC Form ADV Part 1 PDFs (Avenue CRD 315296, Crosslink CRD 109948, QED CRD 284908)
- QED Webflow CDN impact/LP PDFs (pdftotext scan)
- EDGAR full-text index queries for name + domain / e-mail co-occurrence

No qualifying artifact bound any target `Contact_name` to a non-generic personal `@firm` mailbox in the same document block.

## Deliverables

| File | Status |
|------|--------|
| `input.csv` | Copied from upload |
| `results.csv` | Complete |
| `results.md` | Complete |
| `stamp-list.json` | Empty (`items: []`) — no FOUND |
| `CLOSEOUT.md` | This file |
| `evidence/` | URL index, negative excerpts, Form D / PDF / ADV snapshots |

## Notes

- IAPD Part 2A brochure PDFs (e.g. Crosslink brochure ID 283599) returned 403/404 from automated fetch; Form ADV Part 1 text layers contained no e-mail addresses for any target.
- Role/generic inboxes observed (`hello@avenuegp.com`, `info@nxtp.vc`, `moffer@crosslinkcapital.com`) were not stamped per arm rules.
- **Monday API:** not called.
