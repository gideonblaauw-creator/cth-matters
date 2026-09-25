# Micro-Hand 9/9 — Licensed / semi-open RUES-connected APIs (probe only)

**Desk:** Chamber · Bucaramanga (CCB) · energía cluster enrichment  
**Date:** 2026-09-25  
**Method:** Public documentation only — **no live paid API calls**, no sends, no VPS DB writes.

## Objective

Map **paid or semi-open** APIs that expose Colombia **RUES / Registro Mercantil** data as a candidate path to enrich cluster leads with **matrícula**, **legal representatives**, and **contact hints**, and compare that value against **SECOP** (public procurement) and free registry sources.

## Executive summary

| Question | Answer |
| --- | --- |
| Do RUES resellers reliably deliver matrícula + reps? | **Yes** (by NIT), with normalized JSON — especially “complete” products (`rues-complete`, PlacApi `/api/rues`). |
| Do they deliver **email** for outreach? | **Generally no.** Published Verifik RUES-complete samples show `"email": null`; RUES RM is not an email directory. |
| Cheapest published per-lookup (with data)? | **PlacApi** ~349 COP (~USD 0.09) at minimum pack; **Verifik** catalog ~0.2–0.4 credits per lookup (USD plan-dependent). |
| vs SECOP | SECOP adds **contractor role, process, values, sector**; RUES adds **registry truth** (matrícula state, chamber, CIIU, legal rep name/CC). Complementary, not substitutable. |
| Spend now? | **HITL NO-GO** until goals are fixed: if the goal is **contacts/email**, paid RUES is the wrong primary spend; if the goal is **KYB + rep identity for HITL lookup**, **conditional pilot** after free sandboxes. |

## Target enrichment fields (cluster use case)

| Field | RUES paid APIs | SECOP (Datos Abiertos / API) | Free CCB open data (`wf53-j577`) |
| --- | --- | --- | --- |
| NIT / razón social | Strong | Strong (contractor fields) | Strong |
| Matrícula + estado | Strong | Weak / indirect | Partial (no rep) |
| Cámara de comercio | Strong | Rare | Yes (CCB-focused) |
| CIIU / actividad | Strong | Sometimes (object) | Yes (desc CIIU) |
| Representante legal + documento | Strong (complete tiers) | Uncommon in base datasets | No |
| Email / tel comercial | **Rare / null in docs** | Sometimes in proceso metadata | No |
| “Is active proponent (RUP)” | Verifik categories / PlacApi flag | SECOP-adjacent via contracts | No |

## Provider comparison

### 1. Verifik — `GET /v3/co/rues` and `GET /v3/co/rues-complete`

| Item | Detail |
| --- | --- |
| **Auth** | `Authorization: Bearer <token>` + `Accept: application/json` |
| **Endpoints** | Basic: `https://api.verifik.co/v3/co/rues` — Complete: `https://api.verifik.co/v3/co/rues-complete` |
| **Inputs** | `documentType=NIT`, `documentNumber`, optional `category` ∈ `RM`, `PROP`, `RUNEOL`, `RNT`, `ESAL`, `ESOL`, `JUEGOS`, `EXTRANJERAS` (default `RM`) |
| **Published pricing** | Catalog: **~0.2 credits / 0.3 SmartCheck** (basic), **~0.3 credits / 0.4 SmartCheck** (complete). Subscription bundles from **~USD 490/yr** (Starter tier on marketing site). Per-call USD depends on plan; use `includeCost=true` where supported. |
| **Example fields (docs)** | Basic: `businessName`, `fullNit`, `status`, `registration`, chamber/location, `organizationType`. Complete adds `commercialRegistry` (matrícula, renewal, `registrationStatus`), `legalRepresentatives[]` (name, `documentType`, `documentNumber`, role), `economicActivities[]` (CIIU), `establishmentOwner[]`, optional RUP blocks for `PROP`. |
| **Email in response?** | **Documented as null** in multiple official response examples (`"email": null` in `commercialRegistry`). Not a contact enrichment API. |
| **Sandbox / free sample** | Sandbox base documented for v2 services: `https://api-sandbox.verifik.co/v2/` (no credit burn). Confirm whether v3 RUES routes are mirrored in sandbox before any trial call. |
| **Billing rules (SLA)** | HTTP **200 and 404 charged** for smartCHECK; 403/409/412/422/500 not charged (per SLA). |
| **HITL** | **Required** before production spend — choose basic vs complete; 404 still bills. |

**Docs:** [Colombia RUES v3](https://docs.verifik.co/business-validation/colombia-rues-v3/) · [RUES complete v3](https://docs.verifik.co/business-validation/rues-complete-v3/)

---

### 2. PlacApi — `POST /api/rues` (registro mercantil)

| Item | Detail |
| --- | --- |
| **Auth** | Header `x-api-key: pk_live_…` |
| **Endpoint** | `POST https://placapi.com/api/rues` |
| **Inputs** | JSON: `documento` (NIT/CC, normalized), or `nombre` / `termino`, optional `offset`, `refresh` |
| **Published pricing** | **1 credit** per lookup **with data**; credits from **349 COP** (≥30 credits, min purchase ~10.470 COP). Volume down to **99 COP/credit** at 50k+. **Zero-hit searches can still charge** (docs: valid charged result). Signup: **1 free query** (FAQ). |
| **Example fields (docs)** | `razonSocial`, `matricula`, `camaraComercio`, `estadoMatricula`, `tipoSociedad`, `organizacionJuridica`, `ciiuPrincipal`/`Secundario`, matrícula/renovación/cancelación dates, `ultimoAnoRenovado`, `representanteLegal`, `documentoRepresentanteLegal`, `inscritaComoProponente` |
| **Email in response?** | **Not listed** in documented schema. |
| **Sandbox / free sample** | **1 free consultation** on account creation (FAQ); doc response example uses `"mode": "live"` with fictional empresa — cite only as `EXAMPLE_NOT_LIVE`. |
| **HITL** | **Required** — Colombian COP prepay; clarify 404/charging policy before bulk NIT pass. |

**Docs:** [Registro mercantil](https://placapi.com/docs/registro-mercantil) · [Pricing](https://placapi.com/api-rues-colombia) · [llms.txt](https://placapi.com/llms.txt)

---

### 3. Apitude — `rues-co` and `identity-business-co`

| Item | Detail |
| --- | --- |
| **Auth** | `x-api-key` + async pattern: `POST https://apitude.co/api/v1.0/requests/rues-co/` then poll returned `url` / `request_id` |
| **Inputs** | e.g. `{"document_number": "899999068-1"}` |
| **Published pricing** | **Not public** on service page; platform is credit/partner-based. **500 responses not charged**; 404/200 behavior documented. Some services need **extra partner contract** (FAQ). |
| **Example fields (docs)** | RM-style: `numero_de_matricula`, `camara_de_comercio`, `estado_de_la_matricula`, `tipo_de_sociedad`, `actividad_economica`, `ultimo_ano_renovado`, dates, `representante_legal` / related blocks in extended services. **`identity-business-co`** adds **`phone_number`**, `formatted_address`, geocode, `actividades_economicas` — partner-sourced, not pure RUES. |
| **Email in response?** | **Not in core `rues-co` sample**; business identity service may include phone, not email in published example. |
| **Sandbox / free sample** | Account + API key; contract-gated services may error until sales enables. |
| **HITL** | **Required** — sales/pricing + partner contract status before relying on for pipeline. |

**Docs:** [rues-co](https://www.apitude.co/en/docs/services/rues-co/) · [identity-business-co](https://apitude.co/es/docs/services/identity-business-co/) · [FAQ](https://apitude.co/en/faq/)

---

### 4. AnySite — `POST /api/rues/companies`

| Item | Detail |
| --- | --- |
| **Auth** | Header `access-token` |
| **Published pricing** | **1 credit** per request (OpenAPI description). Plans from **USD 49/mo** (15k credits); **7-day trial, 1,000 credits** on Starter (marketing). **412 / empty may still charge** on most endpoints (plans doc). |
| **Example fields** | Typed `RuesCompany` schema in OpenAPI (NIT/matrícula-focused registry record). |
| **Email** | **Not positioned** as email source. |
| **HITL** | **Required** — USD subscription; confirm RUES endpoint coverage vs scraping stability. |

**Docs:** [RUES companies](https://docs.anysite.io/api-reference/rues/ruescompanies) · [API pricing](https://anysite.io/pricing/api/)

---

### 5. CoreSoft — API RUES (marketing / demo UI)

| Item | Detail |
| --- | --- |
| **Auth** | API key (exact header not fully documented on landing page) |
| **Published pricing** | **Not published** on landing; claims **free demo** without card |
| **Example fields** | `nit`, `razon_social`, `matricula`, `camara`, `estado`, `actividad` |
| **Email** | **No** |
| **Note** | Private aggregator, not official chamber; treat as **low-trust until SLA/pricing documented**. |
| **HITL** | **Required** — do not spend until contract + DPA clear. |

**Docs:** [CoreSoft API RUES](https://coresoft.solutions/api-rues.html)

---

### 6. Truora — `type=company`, `country=CO` (Checks API)

| Item | Detail |
| --- | --- |
| **Auth** | Header `Truora-API-Key`; POST `https://api.checks.truora.com/v1/checks` |
| **Nature** | **Not a dedicated RUES API** — KYB/background **company check** aggregating datasets (`business_background`, `legal_background`, `criminal_record`, etc. for CO). |
| **Published pricing** | **Enterprise/sales** — not listed per lookup on dev docs. |
| **RUES-like fields** | May surface company name/status via `business_background`; **not a substitute** for structured matrícula/rep JSON. |
| **Email** | **No** |
| **HITL** | **Required** — only if compliance/KYB budget exists; poor fit for bulk energía cluster enrichment. |

**Docs:** [Company check guide](https://dev.truora.com/guides/check_type_company_guide/index.md)

---

### 7. Semi-open official RUES API (not a commercial SKU)

| Item | Detail |
| --- | --- |
| **Access** | Public token flow described in community docs: `POST https://ruesapi.rues.org.co/WEB2/api/Token/ObtenerToken` then authenticated calls e.g. `BusquedaAvanzadaRM`. Help page lists `ConsultaNIT`, `ConsultaMatricula`, etc. ([help](https://pruebasruesapi.rues.org.co/Help)). |
| **Pricing** | **No published fee** — effectively free at point of use; subject to **ToS, rate limits, captcha, and operational risk**. Some routes reference `usuario=` (possible chamber credential). |
| **Email** | **No** |
| **HITL** | **Required for automation policy** — legal/compliance review before production scraping; not “licensed” in the commercial sense. |

**Reference (community):** [RUES NIT gist](https://gist.github.com/cdiaz/a48dc7cbb4fb3dbfa555e016a5aae1dd)

---

### 8. Free reference (not in scope for spend, but sets the bar)

- **CCB open data:** [EMPRESAS CÁMARA DE COMERCIO DE BUCARAMANGA (`wf53-j577`)](https://www.datos.gov.co/resource/wf53-j577.json) — bulk NIT, razón social, CIIU, ciudad; **no legal rep**.
- **RUES web portal:** Public consult at `ruesfront.rues.org.co` (CCB states nine registries, no citizen fee).

## SECOP vs paid RUES — what we gain

**SECOP** (Colombia Compra Eficiente / Datos Abiertos contratos) answers: *Who sold to the state, in which sector, for how much, under which process?* It is the right signal for **energía-sector commercial traction** and sometimes **process contact fields**, but it does **not** replace chamber registry for:

- Matrícula **ACTIVA/CANCELADA** and **último año renovado**
- **Representante legal** + identification for HITL or identity cross-check
- Multi-establishment structure (Verifik `establishmentOwner`)
- RUP/proponent status (Verifik `PROP`, PlacApi `inscritaComoProponente`)

**Paid RUES APIs** answer: *Is this NIT a real, registered legal entity, who represents it, and what is its declared economic activity?* They do **not** answer: *What is their procurement email?*

Recommended stack logic:

1. **SECOP / cluster list** → NIT candidates + sector proof  
2. **RUES enrichment** → validate entity + rep identity  
3. **Separate contact path** (public web, SECOP proceso, manual HITL) → email/phone  

## Go / no-go for spend

| Scenario | Recommendation |
| --- | --- |
| Primary KPI = **verified matrícula + legal rep** for CCB energía cluster | **Conditional GO** — pilot **one** provider after free tier (PlacApi 1 free query and/or Verifik sandbox if v3 available), compare hit rate on known NITs. |
| Primary KPI = **email/contact completion** | **NO-GO** on RUES spend — docs show **no reliable email**; budget should go to contact-specific sources (not probed here). |
| Large batch (10k+ NITs) | **NO-GO until** pricing negotiated — PlacApi volume ~99–349 COP/query; AnySite ~USD 0.03–0.05/query at scale; Verifik credit math needs plan quote. |
| Compliance-heavy KYB | Consider **Verifik complete** (signed payload) or **Truora** — different budget line than cluster marketing enrichment. |

**HITL decision needed:** Approve **(a)** provider choice, **(b)** max monthly lookups, **(c)** acceptance of **404 billing**, **(d)** confirmation that **rep personal data** processing is allowed under internal policy (CC numbers from registry).

## Free sandbox / docs-only samples (safe to cite)

| Provider | Free path cited in docs |
| --- | --- |
| Verifik | Sandbox host `api-sandbox.verifik.co` (v2; verify v3 RUES coverage before use) |
| PlacApi | 1 free query on registration |
| AnySite | 7-day trial, 1,000 credits (requires trial activation; **do not start without HITL**) |
| Apitude | API key signup; pricing/partner gates unknown |
| CoreSoft | Demo UI claimed |

## Probe constraints (this run)

- No paid endpoints invoked.  
- No email sends.  
- No VPS DB writes.  
- `enrich.csv` contains **documentation examples only**, tagged `EXAMPLE_NOT_LIVE`.

## Sources

- Verifik: [colombia-rues-v3](https://docs.verifik.co/business-validation/colombia-rues-v3/), [rues-complete-v3](https://docs.verifik.co/business-validation/rues-complete-v3/), [SLA billing](https://docs.verifik.co/legal/service-level-agreement/), [Enroll sandbox note](https://docs.verifik.co/services/verifik-enroll-code-solution-via-api/full-api-tutorial/)
- PlacApi: [registro-mercantil](https://placapi.com/docs/registro-mercantil), [FAQ](https://placapi.com/preguntas-frecuentes)
- Apitude: [rues-co](https://www.apitude.co/en/docs/services/rues-co/), [identity-business-co](https://apitude.co/es/docs/services/identity-business-co/)
- AnySite: [rues/companies](https://docs.anysite.io/api-reference/rues/ruescompanies), [pricing](https://anysite.io/pricing/api/)
- CoreSoft: [api-rues](https://coresoft.solutions/api-rues.html)
- Truora: [company checks](https://dev.truora.com/guides/check_type_company_guide/index.md)
- CCB / datos: [CCB datos abiertos](https://www.camaradirecta.com/institucional/ley-de-transparencia/datos-abiertos), [wf53-j577](https://www.datos.gov.co/resource/wf53-j577.json)
- RUES API help: [pruebasruesapi Help](https://pruebasruesapi.rues.org.co/Help)
