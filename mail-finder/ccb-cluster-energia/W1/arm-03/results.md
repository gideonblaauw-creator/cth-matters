# CCB Clúster Energía — W1 arm-03 Track A (firm contact)

**Method:** First-party Contact / Contáctenos / Nosotros (+ same-domain contact blocks). ROLE inboxes allowed when co-published with entity legal name on the same page.

**Batch:** 8 seed rows (`input.csv`)

## Scorecard

| Status | Count |
|--------|------:|
| FOUND | 1 |
| EMPTY | 0 |
| UNCERTAIN | 0 |
| DOMAIN_UNRESOLVED | 7 |

## FOUND

| NIT | Razón social | Email | Type | Source |
|-----|--------------|-------|------|--------|
| 805027872-3 | ABONO VERDE COMPOSTING LIMITADA | info@avcomposting.com | ROLE | [Wayback Quienes somos](https://web.archive.org/web/20240304205955/https://www.avcomposting.com/nosotros/quienes-somos) |

Live `avcomposting.com` serves a parking lander; citation is from archived first-party pages (`evidence/abono-verde-found-excerpt.md`).

## DOMAIN_UNRESOLVED (7)

No citation-grade first-party domain to crawl, or candidate domain could not be tied to the seed NIT/razón social:

- A&G Imperial Inversiones SAS  
- A.B CIVITOP S.A.S.  
- ABELLA CARDENAS YOVANNY (natural person)  
- Aceites Chicamocha SAS  
- Acevedo & Lopez Ingenieria SAS (`acevedoingenieria.com` not verified)  
- ACOSTA CORREA CARLOS ANDRES (natural person)  
- Actividades de Consultoria Construccion y Servicios de Ingenieria SAS (ACTSI)

## Monday / CRM

**No Monday or CRM writes.** Workbench may import `stamp-list.json` after HITL review.

`stamp-list.json` includes `contact_name` (maps to Monday `text_mm7hkeme`) when a person is co-published with the mailbox; blank for this batch’s ROLE-only FOUND (`info@avcomposting.com`).
