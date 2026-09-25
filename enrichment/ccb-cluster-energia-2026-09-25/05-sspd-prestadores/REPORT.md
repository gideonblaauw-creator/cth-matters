# SSPD / Prestadores servicios públicos — Micro-Hand 5/9

Generated: 2026-09-25 20:20 UTC

## Datasets used

| ID | Title | Role |
|---|---|---|
| `wf53-j577` | EMPRESAS CÁMARA DE COMERCIO DE BUCARAMANGA | CCB registry; **energy profile allowlist** derived from `desc_ciiu1` (activo + energy/gas/electricity/combustibles/solar-related CIIU descriptions). |
| `jnzr-x9ww` | Registro Único de Prestadores de Servicios Públicos — **Santander** | Pulled in full; **no electricity/gas rows** in this view (services present: ACUEDUCTO, ALCANTARILLADO, ASEO). |
| `4qkq-csdn` | Registro Único de Prestadores de Servicios Públicos — **RUPS (national)** | Source for **ENERGIA ELECTRICA**, **GAS NATURAL**, **GAS LICUADO DEL PETROLEO** prestadores and official contact fields. |

Santander-focused prestadores de energía/gas were taken from `4qkq-csdn` with `departamento_domicilio = SANTANDER` (33 service rows). The Santander slice `jnzr-x9ww` does not currently expose energy/gas services on datos.gov.co.

## Allowlist (wf53-j577)

- CCB rows downloaded: **67,982**
- Energy-profile allowlist (ACTIVO + energy-related `desc_ciiu1`): **840** unique NITs
- Filter: case-insensitive regex on `desc_ciiu1` for energía/eléctric/gas/GLP/combustibles/solar/hidro/biogas/petróleo and related distribution/generation wording (same rule documented for parallel cluster hands).

## SSPD energy/gas pull

- National RUPS energy/gas rows (`4qkq-csdn`): **606**
- Santander domicilio subset: **33** rows

## Overlap with profile NITs

| Metric | Count |
|---|---|
| Intersection rows (profile NIT × SSPD energy/gas record) | **23** |
| Unique profile NITs with ≥1 SSPD energy/gas match | **19** / 840 allowlist |
| Allowlist NITs with no SSPD energy/gas row | **821** |

## Contact coverage (intersection rows; unique NITs)

| Field | NITs with value |
|---|---|
| Email | **19** / 19 (100.0%) |
| Teléfono | **19** / 19 |
| Dirección | **19** / 19 |

## Output

- `enrich.csv`: inner join **CCB energy allowlist** ∩ **SSPD energy/gas** on `nit` (one row per NIT × servicio). Emails/phones/addresses are **only** values present in SSPD — none invented.

## Notes

- No outbound email/SMS and no VPS database writes.
- Multiple SSPD rows per NIT are expected when a prestador registers more than one gas/electricity service.
