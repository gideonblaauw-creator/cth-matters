# RUES public enrichment — CCB Clúster Energía (2026-09-25)

Desk: Chamber · Bucaramanga · Micro-hand 3/9 · HITL / read-only

## Executive summary

| Question | Answer |
|----------|--------|
| **Bulk open export / API without login?** | **NO** for nationwide matrícula + status at scale |
| **Public citizen path** | **YES** — interactive search at [rues.org.co](https://www.rues.org.co/) (no account) |
| **Sample hit-rate (n=25)** | **24/25 (96%)** with matrícula + estado on hits |
| **Recommendation** | **HITL semi-automated extract** (paced UI or licensed API), not unattended bulk scrape |

## Bulk feasibility (open / no paywall)

### Citizen portal (`www.rues.org.co`)

- Free **basic** Registro Mercantil lookup by NIT, razón social, or matrícula (Confecámaras [guía usuario público](https://app-antiguoprd.rues.org.co/GuiaUsuarioPublico/index.html)).
- **No** self-service CSV/JSON export for arbitrary NIT lists.
- Paid **certificados** are separate from basic lookup (not used in this hand).

### Entity / official bulk (`entidades.rues.org.co`)

- CSV/TXT **aggregated reports** are documented for **registered public-policy / academic / utility entities**, with token login — not an anonymous open bulk feed ([entidades.rues.org.co](https://entidades.rues.org.co/)).

### Machine API

| Endpoint | Auth | Result (2026-09-25) |
|----------|------|---------------------|
| `GET https://pruebasruesapi.rues.org.co/api/ConsultasRUES/TipoRegistro` | None | **200** — metadata only |
| `POST …/ConsultaNIT?usuario=…&nit=…` (pruebas host) | Required | **401** for public `usuario` guesses |
| `https://ruesapi.rues.org.co/` | Credentials | **403** from this environment |

**Conclusion:** There is **no** confirmed **login-free, unrestricted national bulk export** of matrícula + status. Production enrichment must treat RUES as **controlled lookup** (UI or credentialed API), aligned with third-party summaries of Colombia company data ([companiesdata.cloud/open-company-data-colombia.html](https://companiesdata.cloud/open-company-data-colombia.html)).

## Sample design (wf53 energy allowlist)

**Note:** The `wf53` energy profile-fit allowlist file was **not present** in the Lane B parking repo or Drive search on this worker (expected SoT: VPS `/opt/claude-files/…`).

**Proxy universe (same desk intent):** SECOP II Proveedores on [datos.gov.co](https://www.datos.gov.co/) dataset `qmzu-gj57`, filtered to **Santander / Norte de Santander** providers whose name or UNSPSC category text matches energy/electrical keywords (~118 NITs). From that pool:

1. **Forced includes** (cluster actors): `890203703`, `804007332`, `900304878`
2. **Random fill** to **n=25** (SECOP rows; NIT normalized to base number for RUES search)

Evidence JSON: `sample_results.json` (browser citizen searches, 2–3 s spacing).

## Sample results

| Metric | Value |
|--------|-------|
| NITs queried | 25 |
| RUES hits | 24 |
| Misses | 1 (`1090385959` — “No se encontraron resultados”) |
| Status on hits | 24/24 **Activa** |
| Matrícula on hits | 24/24 |

**Chambers (hits):** Bucaramanga 12 · Cúcuta 8 · Barrancabermeja 4.

### Public fields observed (citizen RM search)

Typical on result / detail:

- Identificación (NIT)
- Razón social (+ sigla when applicable)
- **Matrícula mercantil** (+ número de inscripción)
- **Estado** (e.g. Activa)
- **Cámara de Comercio**
- Categoría / tipo sociedad / tipo organización
- Actividad económica (CIIU list when detail opened)
- Municipio / departamento (in UI)

Not retrieved (by design): certificados PDF, representación legal completa, RUP/RNT unless other register selected.

### Cluster anchor checks

| NIT | Entity | Matrícula | Estado | Cámara |
|-----|--------|-----------|--------|--------|
| 890203703 | ELECTROORIENTE S.A.S. | 1355 | Activa | Bucaramanga |
| 804007332 | CONSULTORIA Y MEDIO AMBIENTE S.A. | 74047 | Activa | Bucaramanga |
| 900304878 | RYCTEL S.A.S. | 172682 | Activa | Bucaramanga |

Deliverable rows: `enrich.csv`.

## Recommendation — HITL bulk extract

1. **Do not** run high-volume scraping against authenticated API or bypass paywalls/certificates.
2. **Short term (HITL):** Operator paced searches on [rues.org.co](https://www.rues.org.co/) or chamber portals; export `enrich.csv` columns; cap ~25–50 NITs/session; log `source_url` + timestamp.
3. **Medium term:** If CCB / CTH qualifies, request **entidad** access on [entidades.rues.org.co](https://entidades.rues.org.co/) for semicolon-separated CSV reports (policy-compliant bulk).
4. **Licensed path:** Confecámaras / RUES API credentials for `ConsultaNIT` (hand 9/9 licensed probe — separate micro-hand).
5. **QA:** Reconcile SECOP NIT formatting (DV suffix) before RUES lookup; treat “not found” as data-quality flag (see `1090385959`).

## Artifacts

| File | Purpose |
|------|---------|
| `enrich.csv` | Sample enrichment rows |
| `sample_results.json` | Structured browser evidence |
| `REPORT.md` | This assessment |

No sends · No VPS DB writes.
