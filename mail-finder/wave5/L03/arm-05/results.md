# Wave5 L03 Arm 05 — Impact / DocuSign / ethics PDFs scorecard

**Run:** 2026-09-25 · **Seats:** 5 · **Input:** `input.csv`  
**Method:** Public impact reports, DocuSign-class artifacts, ethics materials, LP/fund disclosures (PDF or HTML). **FOUND** only when exact `Contact_name` and a non-generic `person@firm` mailbox co-occur in the same public artifact.

## Results

| Status | Count |
|--------|------:|
| FOUND | 1 |
| EMPTY | 4 |
| UNCERTAIN | 0 |

**Yield:** 1 / 5 citation-grade personal emails.

## Per seat

| Monday_item_id | Contact_name | Firm / domain | Outcome |
|----------------|--------------|---------------|---------|
| 13028365776 | Scot Bryson | impactful.capital | **EMPTY** — team/impact pages and Climate Bonds agriculture criteria name Scot Bryson without person@impactful.capital |
| 13096674688 | Scott Sobel | Valor Capital Group | **FOUND** — `scott.sobel@valorcapitalgroup.com` on IDB Invest EWS Valor Opportunity Fund I LP contact block |
| 13028360221 | Simon SDG | sdgglobalgroup | **EMPTY** — no artifact with exact "Simon SDG" + personal email; SDG materials use info@sdgglobalgroup.com or Simon Littlewood without person mailbox |
| 13028366345 | Son Nguyen | iixglobal.com | **EMPTY** — IIX impact PDFs/RFP use info@ / impactpartners@ / iixvietnam@ generics only |
| 13114451331 | Susana Garcia-Robles | capria.vc | **EMPTY** — Capria impact PDFs impact@capria.vc; ethics pages grievance@capria.vc |

## Hygiene

- No Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP validation, or Monday writes.
- Role/generic inboxes (`info@`, `impact@`, `impactpartners@`, `grievance@`, `iixvietnam@`) → **EMPTY**.

## Artifacts

- `evidence/scott-sobel-ews-excerpt.md` + `evidence/ews-valor-opportunity-fund-i.html` (FOUND)
- `stamp-list.json` — Scott Sobel only
