# Mail Finder — Wave4 L10 Arm 02 — Summary

**Processed:** 2026-09-25 (UTC)  
**Seats:** 5 (P2)  
**Method:** Public **Brazilian CNPJ**, **FINRA/IAPD**, **Canadian securities (BCSC document search)**, **SEC EDGAR**, **DocuSign** co-search on EDGAR, and **ethics/compliance PDFs**.  
**FOUND gate:** Target **name + exact personal `person@firm`** on the **same public page or PDF**. Generics, name-without-email, email-without-name, or third-party contacts → **EMPTY**.

## Scorecard

| Result | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Per seat

| Monday_item_id | Name | Firm | Status | Rationale |
|----------------|------|------|--------|-----------|
| 13100506291 | Philipp Emig | Leitmotif | EMPTY | IAPD ADV (CRD 329025): no Emig + @leitmotif.vc; SEC/BCSC/DocuSign negative |
| 13100511582 | Philippe Schlumpf | Itaú Ventures | EMPTY | CNPJ generic judicial email; Form D lists Schlumpf without email |
| 13100506303 | Quennie Co | Shell Ventures | EMPTY | Shell Ethics & Compliance Manual PDF: no Co, no person@shell.com |
| 13114433932 | Rafael Barbalat | Prosus Ventures | EMPTY | Regulatory/press PDFs quote Barbalat; no person@prosus.com on same doc |
| 13028365736 | Ricardo Politi | AIC | EMPTY | COP-27 PDF: Politi named; Jonah@ is another person's contact |

## Notes

- **IAPD Part 2A brochure** fetch via `firm/brochures` API returned 403 from this environment; Form ADV PDF + firm search API used for Leitmotif seat.
- **No Monday API writes.** Evidence under `evidence/`.
