# SECOP II Contratos — Micro-Hand 2/9

Generated: 2026-09-25 20:31 UTC

## Datasets

| ID | Title | Role |
|---|---|---|
| `wf53-j577` | EMPRESAS CÁMARA DE COMERCIO DE BUCARAMANGA | Rebuild **energy profile-fit NIT universe** (allowlist). |
| `jbjy-vk9h` | SECOP II - Contratos Electrónicos | Adjudicated **proveedor** activity signal (counts, values, sample proceso URL). |

## Allowlist (wf53-j577)

- CCB rows downloaded: **67,982**
- Energy-profile allowlist (`estado=ACTIVO` + `desc_ciiu1` regex): **890** unique NITs (micro-hand 05 reported **840** with the same rule intent; delta is regex wording / snapshot timing)
- Filter (case-insensitive on `desc_ciiu1`): energía/eléctric/combustibles/solar/hidro/biogas/petróleo/GLP, *gas natural* / *gas licuado*, producción-distribución-comercialización-transmisión de energía/gas, transporte por tuberías.
- Join map: see `nit-map.md`.

## SECOP overlap

| Metric | Count |
|---|---|
| Allowlist NITs with ≥1 adjudicated contract row in SECOP | **99** / 890 |
| Total SECOP contract rows pulled for those NITs | **939** |

Contracts are **national** (all entities); useful for prioritization / recent activity, not jurisdiction-filtered.

## Top NITs by contract count

| NIT | Proveedor (SECOP name) | Contracts | Last firma | Sum valor (COP) |
|---|---|---:|---|---:|
| 900349039-0 | GNVC BUCARAMANGA S.A.S | 98 | 2026-05-12 | 7,991,995,414 |
| 890200951-7 | TRANSPORTES PIEDECUESTA S.A. | 83 | 2026-07-28 | 38,709,634,123 |
| 900456302-1 | DANIEL GARCIA HERNANDEZ E HIJOS S. EN.C.S. | 66 | 2023-06-28 | 937,968,531 |
| 804013578-8 | PROVISERVICIOS SA ESP | 40 | 2026-01-30 | 132,806,035,616 |
| 900971774-2 | EDS EL TRIUNFO | 34 | 2026-03-17 | 6,728,063,309 |
| 804010955-8 | ESTACION DE SERVICIO LA AMERICANA SAS | 34 | 2026-03-19 | 2,425,665,664 |
| 890201230-1 | ELECTRIFICADORA DE SANTANDER S.A. ESP | 32 | 2026-08-12 | 52,973,845,477 |
| 804011800-1 | INGENIERÍA Y SERVICIOS SOCIEDAD ANÓNIMA EMPRESA DE SERVICIOS | 27 | 2026-01-30 | 182,744,410,664 |
| 13923369-0 | Luis Eduardo Moreno Torres | 27 | 2026-01-16 | 302,362,304 |
| 13951565-7 | ESTACION DE SERVICIO SUPER BRIO LOS ARREAYANES | 26 | 2024-10-07 | 647,007,175 |
| 901378311-7 | INFUSO INGENIERIA SAS | 25 | 2026-03-11 | 12,396,156,656 |
| 28098376-7 | piedad yadira vargas martinez - estacion de servicio charala | 25 | 2026-09-02 | 703,229,277 |
| 900734797-6 | ECOFULL | 24 | 2026-06-26 | 428,384,234 |
| 804000035-4 | EDS LA GLORIETA | 22 | 2026-04-23 | 938,350,654 |
| 901156642-7 | ECOENERGY LATIN AMERICA SAS | 20 | 2026-08-25 | 450,869,568 |

## Top NITs by total contract value (valor_del_contrato)

| NIT | Proveedor (SECOP name) | Sum valor (COP) | Contracts | Energy-tagged rows |
|---|---|---:|---:|---:|
| 804011800-1 | INGENIERÍA Y SERVICIOS SOCIEDAD ANÓNIMA EMPRESA DE SERVICIOS | 182,744,410,664 | 27 | 27 |
| 804013578-8 | PROVISERVICIOS SA ESP | 132,806,035,616 | 40 | 40 |
| 890200917-6 | EMPRESA DE TRANSPORTES LEBRIJA LIMITADA | 118,899,092,000 | 9 | 9 |
| 890204814-4 | MANUFACTURAS Y PROCESOS INDUSTRIALES Ltda | 59,555,989,962 | 2 | 2 |
| 890201230-1 | ELECTRIFICADORA DE SANTANDER S.A. ESP | 52,973,845,477 | 32 | 15 |
| 890200951-7 | TRANSPORTES PIEDECUESTA S.A. | 38,709,634,123 | 83 | 45 |
| 804003583-2 | ASOINGENIERIA DEL ORIENTE S.A.S. | 35,974,514,916 | 17 | 10 |
| 900197640-4 | HEGA SA ESP | 23,447,896,152 | 6 | 6 |
| 890207976-2 | EME ING S.A. BIC | 15,027,970,213 | 19 | 12 |
| 804013341-1 | CONELTEC SAS | 12,517,330,100 | 1 | 0 |
| 901378311-7 | INFUSO INGENIERIA SAS | 12,396,156,656 | 25 | 14 |
| 804000551-3 | GAS NATURAL DEL CESAR S.A E.S.P | 9,612,575,155 | 5 | 5 |
| 804002801-9 | GASES DEL SUR DE SANTANDER S.A EMPRESA DE SERVICIOS PUBLICOS | 8,782,036,801 | 6 | 6 |
| 900349039-0 | GNVC BUCARAMANGA S.A.S | 7,991,995,414 | 98 | 92 |
| 900971774-2 | EDS EL TRIUNFO | 6,728,063,309 | 34 | 29 |

## Output

- `enrich.csv` — one row per allowlist NIT with SECOP adjudication history (no invented emails).
- `nit-map.md` — NIT normalization between CCB and SECOP.

## Notes

- Prioritization / activity signal only; primary email enrichment remains Proveedores micro-hands.
- No outbound sends and no VPS database writes.
- `energy_tagged` in `notes` uses UNSPSC/sector/text heuristics; non-energy public contracts still count toward totals.
