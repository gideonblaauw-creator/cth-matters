# Wave4 L10 Arm 06 — CNPJ / IAPD / BCSC / DocuSign & ethics PDF scorecard

**Scope:** 5 seats from `input.csv`  
**Method:** Public **CNPJ-class registry** checks where geo applies, **FINRA IAPD** / **SEC EDGAR EFTS**, **BCSC** document search, and **DocuSign / ethics / compliance PDFs** (`pdftotext`). FOUND only when the **same public page or PDF** co-locates the target person’s name and an exact **personal** `person@firm` mailbox.  
**Prohibited:** Hunter/Apollo, LinkedIn scrape, pattern/SMTP, invented emails, paid directories, **Monday writes**.  
**Write path:** `mail-finder/wave4/L10/arm-06/` only.

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## FOUND

None.

## Notable near-misses (not stamped)

| Seat | Why not FOUND |
|------|----------------|
| Erika Marcucci | United Way/FBD **DocuSign ethics PDF** validates **Fernando Cortés McAllister** + `fcortes@fundacionbd.org`, not Erika. Startuplinks `emarcucci@fundacionbd.org` is a **directory** hit (Wave4 L07 arm-02), outside this arm’s registry/PDF lane. |
| CrossBoundary | MIGA ESRS lists **Ifeoma Dike** + `ifeoma.dike@crossboundary.com`, but Monday row is a **firm seat** with no `Contact_name` — no attributable target person for FOUND gate. |
| Maersk Growth | Prior regulatory PDF pass: segment mention + **IR@maersk.com** / **growth@maersk.com** generics only. |
| Norfund | **post@norfund.no** in issuer PDFs; annual report extract has no person mailboxes. |
| Blink VC | **blink.vc** domain inactive/for-sale pattern; Brazilian CNPJ “BLINK” entities are unrelated; no person `@blink.vc` in registry/PDF lane. |

## Evidence

- `evidence/` — downloaded PDFs and HTML snapshots for this pass  
- `evidence/negative-excerpts.md` — citation-grade negative notes  
- `evidence/url-index.md` — per-seat URL audit list  

## Run metadata

- Processed: 2026-09-25 (UTC)  
- Branch: `cursor/mail-finder-wave4-l10-arm06-c588`
