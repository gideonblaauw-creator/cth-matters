# Wave4 L04 Arm 05 — SEC EDGAR exhibits / Form D / signature blocks

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`)  
**Method:** Public SEC EDGAR — EFTS full-text search, Form D primary XML, exhibits, and filing signature blocks. **FOUND** only when the target **published name** and an exact **person@firm** email appear in the **same** filing artifact (preserve local-part spelling). Generics and signature-only / email-only rows → **EMPTY**. No pattern guessing, Hunter/Apollo, LinkedIn scrape, or Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm / domain | Outcome |
|----------------|------|---------------|---------|
| 13100496708 | Abe Yokell | Congruent Ventures / congruentvc.com | EMPTY — Form D related person + `/s/ Abraham Yokell`; no `@congruentvc.com` |
| 13028364943 | Abhinav Sinha | bii.co.uk | EMPTY — 0 EDGAR hits for person; BII cited in ReNew exhibit without target email |
| 13100506386 | Adriana Saman | Clocktower Ventures / clocktowerventures.com | EMPTY — not on Clocktower Form D; 0 domain hits |
| 13028336231 | Alethia Wong | zenanicapital.com | EMPTY — Zenani Form D lists Lauer; Wong absent; no domain emails |
| 13028360241 | Alfredo Neila | plasticrepairsystem.com | EMPTY — no EDGAR presence for person or firm |

## Deliverables

- `results.csv`, `stamp-list.json` (no FOUND items), `README.md`, `summary.md`
- `evidence/` — archived Form D XML, `edgar_search.json`, per-seat excerpt notes
