# Micro-Hand 8/9 — OpenCorporates + GLEIF (CCB Clúster Energía sample)

**Desk:** Chamber · Bucaramanga  
**Date:** 2026-09-25  
**Run:** `bc-9cfdd700-a2d7-5922-9f38-53d98146cbbb`  
**Mode:** Read-only enrichment probe (no sends, no VPS DB writes)

## Objective

Test whether **OpenCorporates** (and **GLEIF** LEI mapping where useful) adds officers, registry URLs, or emails for a ≤20 company sample aligned with the CCB **Clúster Energía** / Santander energy-profile universe.

## Sample (n=19)

No shared `ccb-cluster-energia` master file was present in the parking repo at run time (parallel micro-hands 1–7 still running). Sample was built from **public SECOP Proveedores del Estado** (`datos.gov.co` dataset `jbjy-vk9h`):

- **Santander department**, names matching **E.S.P. / electric / energy / gas / solar / hydro / term** filters (deduped by NIT), plus
- **National energy-chain majors** commonly present in Santander cluster conversations (Ecopetrol, Celsia, Enel, EPM, Isagen, GEB, XM, CHEC), and
- **Two public-sector energy buyers** (Departamento de Santander, Municipio de Bucaramanga) as negative controls.

Full rows: `enrich.csv`.

## OpenCorporates

| Check | Result |
|--------|--------|
| API (`api.opencorporates.com/v0.4/...`) | **No usable key** in environment. Anonymous calls return `Invalid Api Token` (OC now expects a token even for search). |
| Public web search (`/companies?jurisdiction_code=co&q=…`) | **19/19 `no_results`** for NIT and legal-name queries (including Ecopetrol, Bancolombia-style sanity checks). |
| Direct company URLs (`/companies/co/{number}`) | **HTTP 403** after repeated automated access (rate/bot protection). |
| Officers on OC | **0/19** (no company pages resolved). |
| Emails on OC | **0/19** |
| Registry deep links (RUES/Cámara) via OC | **None** — no Colombia company records surfaced in this sample. |

**Interpretation:** For this Bucaramanga/Santander energy-profile slice, **OpenCorporates Colombia coverage is effectively empty** (not merely sparse). OC is **not** a substitute for RUES, CCB/Made in Santander, SECOP, or SSPD sources used in sibling micro-hands.

## GLEIF LEI

Public API: `https://api.gleif.org/api/v1/lei-records` (no key required).

| Metric | Count |
|--------|------:|
| Sample rows | 19 |
| LEI found (name or `registeredAs` match) | **6** |
| LEI for Santander municipal/regional ESPs (ESSA, CENS, AMB, etc.) | **0** |
| Officers | **0** (GLEIF does not publish officers) |
| Emails | **0** |

LEI hits were limited to **large, nationally visible** utilities/energy corporates (Ecopetrol, Celsia Colombia, Enel Colombia, EPM, Isagen, Grupo Energía Bogotá). Regional Bucaramanga/Santander ESPs in the sample had **no LEI**.

**NIT ↔ LEI caveat:** GLEIF `registeredAs` matched sample NIT for 5/6 hits. Grupo Energía Bogotá LEI maps to `899999082-3` in GLEIF, not the `860035827-4` string used in some legacy lists — verify in RUES before merging.

## Coverage verdict — email enrichment

### **Useful for email enrichment: NO**

- No OC company pages → no officer names, no registry emails.
- GLEIF adds LEI identifiers only; no contact fields.
- Even where LEI exists, entities are **holding/utility scale** — not cluster SME decision-makers.

## What it *is* good for (limited)

1. **LEI crosswalk** for national-tier energy companies when you already have a correct legal name/NIT (6/19 here).
2. **Parent / group identification** downstream (GLEIF → Bloomberg/refinitiv-style graphs), not implemented in this hand.
3. **Negative filter:** if OC `jurisdiction_code=co` returns nothing, route the row to **RUES / SECOP / SSPD / CCB directory** (hands 1–7) instead of spending quota on OC.

## Recommended stack (this cluster)

| Need | Prefer |
|------|--------|
| Email / named contact | RUES (hand 3/9), company sites (7/9), SECOP contratos (2/9), SSPD (5/9) |
| Legal name + NIT hygiene | SECOP proveedores + RUES |
| Officers / board | RUES filings, Superintendencia documents — **not OC Colombia** |
| LEI for large utilities | GLEIF (this hand) |

## Artifacts

- `enrich.csv` — one row per sample company: `nit`, `name`, `oc_url`, `lei`, `officers_summary`, `email_if_any`, `notes`

## Re-run notes

- Set `OPENCORPORATES_API_KEY` if the desk obtains a free OC token; re-test API search before bulk web scraping.
- Throttle OC web requests (403 observed) or use licensed API to avoid bot blocks.
- Replace sample with the shared cluster master CSV when micro-hand 1 publishes `enrichment/ccb-cluster-energia-2026-09-25/`.
