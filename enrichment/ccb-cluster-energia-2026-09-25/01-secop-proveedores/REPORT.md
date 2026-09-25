# SECOP II Proveedores → CCB energy NIT universe

## Sources
- CCB empresas: `https://www.datos.gov.co/resource/wf53-j577.json` (dataset `wf53-j577`)
- SECOP proveedores: `https://www.datos.gov.co/Estad-sticas-Nacionales/SECOP-II-Proveedores-Registrados/qmzu-gj57` (dataset `qmzu-gj57`)

## Universe filters (Hands allowlist)
- `departamento` = SANTANDER (case-insensitive)
- `estado` ≠ CANCELADO
- `desc_ciiu1` in energy profile-fit title allowlist (mapped to CIIU codes below)

## Title → CIIU code map used

- **0510** — Extracción De Hulla (Carbón De Piedra) (7 empresas in universe)
- **0520** — Extracción De Carbón Lignito (2 empresas in universe)
- **0610** — Extracción De Petróleo Crudo (0 empresas in universe)
- **0620** — Extracción De Gas Natural (2 empresas in universe)
- **0910** — Actividades De Apoyo Para La Extracción De Petróleo Y De Gas Natural (13 empresas in universe)
- **1910** — Fabricación De Productos De Hornos De Coque (0 empresas in universe)
- **1921** — Fabricación De Productos De La Refinación Del Petróleo (16 empresas in universe)
- **2513** — Fabricación De Generadores De Vapor, Excepto Calderas De Agua Caliente Para Calefacción Central (2 empresas in universe)
- **2711** — Fabricación De Motores, Generadores Y Transformadores Eléctricos (2 empresas in universe)
- **2711** — Fabricación De Motores, Turbinas, Y Partes Para Motores De Combustión Interna (3 empresas in universe)
- **2712** — Fabricación De Aparatos De Distribución Y Control De La Energía Eléctrica (7 empresas in universe)
- **2720** — Fabricación De Pilas, Baterías Y Acumuladores Eléctricos (4 empresas in universe)
- **2733** — Fabricación De Hilos Y Cables Eléctricos Y De Fibra Óptica (1 empresas in universe)
- **2740** — Fabricación De Equipos Eléctricos De Iluminación (6 empresas in universe)
- **2790** — Fabricación De Otros Tipos De Equipo Eléctrico N.C.P. (6 empresas in universe)
- **3314** — Mantenimiento Y Reparación Especializado De Equipo Eléctrico (76 empresas in universe)
- **3511** — Generación De Energía Eléctrica (37 empresas in universe)
- **3512** — Transmisión De Energía Eléctrica (0 empresas in universe)
- **3513** — Distribución De Energía Eléctrica (3 empresas in universe)
- **3514** — Comercialización De Energía Eléctrica (7 empresas in universe)
- **3520** — Producción De Gas Distribución De Combustibles Gaseosos Por Tuberías (25 empresas in universe)
- **3520** — Producción De Gas; Distribución De Combustibles Gaseosos Por Tuberías (0 empresas in universe)
- **3530** — Suministro De Vapor Y Aire Acondicionado (7 empresas in universe)
- **4322** — Instalaciones Eléctricas (452 empresas in universe)
- **4661** — Comercio Al Por Mayor De Combustibles Sólidos, Líquidos, Gaseosos Y Productos Conexos (43 empresas in universe)
- **4730** — Comercio Al Por Menor De Combustible Para Automotores (194 empresas in universe)
- **4930** — Transporte Por Tuberías (3 empresas in universe)
- **7112** — Actividades De Ingeniería Y Otras Actividades Conexas De Consultoría Técnica (1021 empresas in universe)
- **7120** — Ensayos Y Análisis Técnicos (72 empresas in universe)

## Row counts
| Metric | Count |
|--------|------:|
| Universe NITs (profile-fit) | 2011 |
| CCB rows scanned (Santander, non-CANCELADO) | 63123 |
| SECOP proveedor rows downloaded | 1615063 |
| Universe NITs matched in SECOP | 643 (32.0%) |
| Universe NITs with any email (correo or rep. legal) | 642 (31.9%) |
| enrich.csv data rows | 2011 |

## Outputs
- `enrich.csv` — one row per universe NIT
- `universe_nits.txt` — original NIT strings (with DV when present)

## Join logic
- Join key: NIT base before verification digit (strip `-` DV punctuation); digits only on base.
- Emails only from SECOP fields; `No Provisto` treated as empty (never invented).
