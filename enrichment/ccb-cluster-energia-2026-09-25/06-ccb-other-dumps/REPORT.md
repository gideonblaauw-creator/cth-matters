# Hand 6/9 — Other CCB / territorial datos.gov dumps

**Desk:** Chamber · Bucaramanga · **Date:** 2026-09-25  
**Scope:** Open datasets on datos.gov.co beyond wf53-j577 that could add email, phone, matrícula, or better CIIU for the **energy-profile** company set.

## Executive summary

| Finding | Detail |
|---|---|
| CCB Bucaramanga on datos.gov.co | Single empresa table **wf53-j577** (67,982 rows). No correo/teléfono columns. |
| xbft-sj66 | **Misleading ID in search:** Valledupar depuration log, 4,697 rows, matrícula + name only — **not** Bucaramanga, **no** NIT join. |
| Empresas Santander (SUPER) | **tt89-nvfs** / **8pbk-y8cn**: 513 rows, email+phone but **no NIT**; zero `ENERGIA` service rows. |
| Best territorial contact dump | **bedu-5uzi** (Alcaldía Girón): municipal notification email/phone; **25** energy-profile NITs joined. |
| Best NIT+contact (SSP) | **jnzr-x9ww**: **3** energy-profile NITs (utilities with energy-related CIIU in wf53). |
| Barrancabermeja CCB | **9v9c-htja** has `email_comercial` + `matricula` + `nit` but **0** overlap with wf53 energy slice; **yisd-d6ns** adds numeric CIIU text for Barrancabermeja jurisdiction only. |
| enrich.csv | **26** unique NITs with at least one of email/telephone from non-wf53 dumps (see below). |

No emails invented; no outbound contact; no VPS DB writes.

## Energy-profile definition (join denominator)

Because prior hand artifacts are not in this repo, the profile was reconstructed from wf53-j577:

- Filter: `desc_ciiu1` ILIKE any of `%ENERG%`, `%ELECTRIC%`, `%GAS NATURAL%`, `%COMBUSTIB%`, `%PETROLE%`, `%SOLAR%`
- **334 NITs** (all chambers/jurisdictions present in wf53, mostly Bucaramanga metro)

wf53 columns do **not** include numeric CIIU codes — only `desc_ciiu1` text — so “better CIIU” from open data must come from other tables (e.g. yisd-d6ns, ryfe-5k95, 9v9c-htja) with geographic/jurisdiction caveats.

## Join methodology → enrich.csv

| Source | Join key | Matches (unique NIT) | Notes |
|---|---|---:|---|
| bedu-5uzi | `documento` (NIT base 9) = wf53 `nit` sans check digit | 25 | Girón metro; notification fields |
| 96mx-6n3n | same base-9 | 1 (also in bedu) | Grandes contribuyentes subset |
| jnzr-x9ww | exact `nit` | 3 | SSP registry; duplicate rows per service collapsed in export |
| tt89-nvfs | exact `razon_social` | subset of jnzr | Not used separately (weaker; no NIT) |

When the same NIT appears in multiple sources, **email/phone priority:** bedu-5uzi → 96mx-6n3n → jnzr-x9ww.

**Coverage:** 26 / 334 energy-profile NITs (**7.8%**) gain at least one contact field from these dumps. Remaining **308** have no joinable open contact in scanned sets.

## Recommendations for later hands

1. **Do not spend join cycles on xbft-sj66** for Bucaramanga — wrong chamber and schema.
2. **wf53-j577 remains SoT** for NIT + estado + descriptive CIIU + matricula date; no parallel CCB Bucaramanga dump beats it on datos.gov.co.
3. **Girón municipal data (bedu-5uzi)** is the highest-yield open contact layer for metro energy/combustibles/fuels NITs already in wf53.
4. **jnzr-x9ww** is worth keeping for **NIT-keyed** SSP contacts but skews to multi-service utilities (acueducto/aseo), not pure generation/commercialization merchants.
5. **Barrancabermeja 9v9c-htja** is promising for **regional** Santander oil/gas hub firms if the energy profile is expanded to Barrancabermeja NITs not present in wf53 slice (0 overlap today).
6. **2i2b-mnag** / **y57r-fz8q**: broken or blocked views — no data via public API in this run.

## Artifacts

- `catalog.md` — full dataset matrix
- `enrich.csv` — 26 rows, columns: `nit`, `razon_social`, `desc_ciiu1`, `ciudad`, `email`, `telefono`, `source_datasets`, `join_method`

## API references

- CCB empresas: https://www.datos.gov.co/d/wf53-j577  
- Girón empresas: https://www.datos.gov.co/d/bedu-5uzi  
- RUPS Santander: https://www.datos.gov.co/d/jnzr-x9ww  
- xbft-sj66 (Valledupar): https://www.datos.gov.co/d/xbft-sj66  
