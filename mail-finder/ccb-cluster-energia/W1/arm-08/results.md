# CCB Clúster Energía — W1 arm-08 Track A (firm contact)

**Method:** Public first-party Contact / Contáctenos / About / Nosotros pages and same-domain contact PDFs only. **FOUND** when a published mailbox appears on the **same first-party page** as the entity (NIT and/or razón social). Tag `email_type` as **ROLE** or **PERSON**. No Hunter/Apollo, LinkedIn scrape, pattern+SMTP, invented emails, or CRM writes.

**Run date:** 2026-09-25 (UTC)

## Summary

| Metric | Count |
|--------|------:|
| Seed rows | 7 |
| **FOUND** | 2 |
| **EMPTY** | 3 |
| **DOMAIN_UNRESOLVED** | 2 |

## FOUND

| NIT | Razón social | Email | Type | Source |
|-----|--------------|-------|------|--------|
| 900935829-6 | ANS ENERGIA SAS | comercial@ansenergia.com.co | ROLE | [contacto.php](https://ansenergia.com.co/contacto.php) |
| 804014489-5 | ANSALL S.A.S. | info@ansall.com | ROLE | [ansall.com](https://www.ansall.com/) |

## EMPTY

| NIT | Razón social | Notes |
|-----|--------------|-------|
| 901828026-4 | ANKARO AUTOMATIZACIONES S.A.S. | Live domain unreachable; no stamped mailbox |
| 900586209-1 | ANSOELEC INGENIERIA S.A.S | No first-party website located |
| 901423337-0 | ANÁLISIS DIGITAL … HIDROCARBUROS S.A.S | No first-party website located |

## DOMAIN_UNRESOLVED

| NIT | Razón social | Candidate domain | Issue |
|-----|--------------|------------------|-------|
| 901626956-1 | AO SOLUCIONES INTEGRALES SAS | aosoluciones.com | Wrong operating entity (web agency) |
| 901391126-4 | AP SOLUCIONES SOSTENIBLES S.A.S. | aypsolucionessustentables.com | Wrong geography / name variant (Mexico Google Site) |

## Deliverables

- `input.csv`, `results.csv`, `results.md`, `stamp-list.json`, `CLOSEOUT.md`, `evidence/`
- **Monday / CRM / Resend:** no writes (`stamp-list.json` lists FOUND only for downstream review)
