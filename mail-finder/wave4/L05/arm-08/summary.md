# Wave4 L05 Arm 08 — Impact / LP / annual-report PDF scorecard

**Scope:** 5 seats from `input.csv`  
**Method:** Public impact reports, LP materials, annual reports, and comparable issuer/fund PDFs. **FOUND** only when the target person’s printed name and an exact `person@firm` mailbox appear in the **same PDF** with citation-grade excerpt. Generics (`impact@`, `communications@`, `contact@`, etc.) excluded.  
**Prohibited:** Pattern guessing, SMTP, Hunter/Apollo, LinkedIn scrape, Monday writes. **No Monday API writes** from this arm.

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 1 |
| EMPTY | 4 |
| UNCERTAIN | 0 |

## FOUND

| Monday_item_id | Name | Email | Source |
|----------------|------|-------|--------|
| 13028366289 | Jean-Marc Champagne | jmchampagne@senecaimpact.earth | [WWF GEF TNFD MTR report PDF](https://files.worldwildlife.org/wwfcmsprod/files/Publication/file/2ons9eh7ip_GEF_TNFD_MTR_report_final_plus_mgmt_response.pdf) (p. 48, evaluation team block) |

## Notable near-misses

| Seat | Why not FOUND |
|------|----------------|
| Jonathan Duarte | CrossBoundary Aug 2025 partner press PDF names Duarte; contact is `communications@crossboundary.com` only. |
| Josep Oriol | Okavango privacy PDF lists `j.oriol@okavango-capital.com` without printing *Josep Oriol*. |
| Jason Sydow | N47 CDN “Intelligence on Tap” and other linked PDFs — no Sydow + `@n47` / `@next47` person mailbox. |
| Juan Franck | latinamericafund.com has no public PDF corpus; SBIA/LatAm brochure PDFs not retrievable here. |

## Evidence

- `evidence/13028366289-jean-marc-champagne-excerpt.md`
- `evidence/pdfs/GEF_TNFD_MTR_report_final_plus_mgmt_response.pdf`
- `evidence/url-index.md`, `evidence/negative-excerpts.md`, `evidence/pdf_scan_audit.json`
