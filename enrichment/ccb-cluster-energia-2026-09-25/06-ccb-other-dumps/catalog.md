# datos.gov.co catalog — CCB Bucaramanga / territorial Santander (hand 6/9)

Scanned **2026-09-25** via [datos.gov.co](https://www.datos.gov.co) catalog API and Socrata metadata (`/api/views/{id}.json`, `/resource/{id}.json?$select=count(*)`). Baseline already in use: **wf53-j577**.

**Energy-profile NITs** for join tests: **334** rows from wf53-j577 where `desc_ciiu1` matches (case-insensitive) any of: `ENERG`, `ELECTRIC`, `GAS NATURAL`, `COMBUSTIB`, `PETROLE`, `SOLAR`. (wf53 has description-only CIIU, no numeric CIIU column.)

Legend: **email?** / **phone?** / **nit?** / **matrícula?** from column names + spot checks. **Join usefulness** vs energy-profile NITs on wf53.

| Dataset ID | Title | Publisher | Rows | Columns (summary) | email? | phone? | nit? | matrícula? | Join usefulness |
|---|---|---|---:|---|:---:|:---:|:---:|:---:|---|
| [wf53-j577](https://www.datos.gov.co/d/wf53-j577) | EMPRESAS CÁMARA DE COMERCIO DE BUCARAMANGA | CCB Bucaramanga | 67,982 | `nit`, `razon_social`, `tipo_juridico`, `estado`, `fecha_matricula`, `desc_ciiu1`, `ciudad`, `departamento`, `tamano_empresa` | N | N | Y | Y (`fecha_matricula` only) | **HIGH** (primary key; no contact) |
| [2i2b-mnag](https://www.datos.gov.co/d/2i2b-mnag) | Vista - Bucaramanga - Tamaños de empresas | CCB Bucaramanga | 0 | `message` (broken derived view) | N | N | N | N | **NONE** |
| [mmza-t6y4](https://www.datos.gov.co/d/mmza-t6y4) | Registro de Activos de Información (transparencia) | CCB Bucaramanga | 41 | metadata inventory fields | N | N | N | N | **NONE** |
| [peuz-jfbb](https://www.datos.gov.co/d/peuz-jfbb) | Índice información clasificada/reservada | CCB Bucaramanga | 10 | legal/transparency index | N | N | N | N | **NONE** |
| [y57r-fz8q](https://www.datos.gov.co/d/y57r-fz8q) | Vista - Historia - Bucaramanga - Tamaño de empresa | Alcaldía Bucaramanga | — | API **403** on row count; metadata present | — | — | — | — | **LOW** (inaccessible via open API from this run) |
| [xbft-sj66](https://www.datos.gov.co/d/xbft-sj66) | **Depuración Registro Mercantil** | **Cámara de Comercio de Valledupar (Cesar)** — not Bucaramanga | 4,697 | `matr_cula`, `nombre`, `organizaci_n_juridica`, `ultanoren`, `tipo`, `libro`, `registro`, `acto` | N | N | N | Y | **NONE** for Santander energy NITs (wrong chamber; depuration log; no NIT/CIIU/contact) |
| [tt89-nvfs](https://www.datos.gov.co/d/tt89-nvfs) | Empresas Santander | SUPER (servicios públicos) | 513 | `nombre`, `servicio`, `direccion`, `telefono`, `email`, … (no `nit`) | Y | Y | N | N | **LOW** (name-only join; 0 rows with `servicio=ENERGIA`; mostly acueducto/aseo/alcantarillado) |
| [8pbk-y8cn](https://www.datos.gov.co/d/8pbk-y8cn) | Empresas Santander | SUPER | 513 | Same schema as tt89-nvfs (duplicate) | Y | Y | N | N | **LOW** (duplicate of tt89-nvfs) |
| [jnzr-x9ww](https://www.datos.gov.co/d/jnzr-x9ww) | Registro Único de Prestadores SSP — Santander | SUPER | 570 | **`nit`**, `nombre`, `servicio`, `telefono`, `email`, `direccion`, … | Y | Y | Y | N | **MED** (3 energy-profile NITs with contact via `nit`; 0 electricity merchants in `servicio`; multi-utility overlap) |
| [tf5y-j9kn](https://www.datos.gov.co/d/tf5y-j9kn) | Acueductos Santander | SUPER | 145 | Same as tt89 without `nit` | Y | Y | N | N | **LOW** (subset of SSP; no NIT) |
| [7zcc-jcja](https://www.datos.gov.co/d/7zcc-jcja) | empresas de servicios públicos en Colombia | SUPER | 13,110 | National SSP; contact fields; no `nit` | Y | Y | N | N | **LOW** (filter Santander possible; no NIT key) |
| [bedu-5uzi](https://www.datos.gov.co/d/bedu-5uzi) | EMPRESAS MUNICIPIO DE GIRON | Alcaldía Girón (metro) | 6,737 | `documento`, `correo_electronico_notificaciones`, `numero_de_telefono_notificaciones`, addresses | Y | Y | Y* | N | **HIGH** (25/334 energy NITs; join `documento` = NIT base without check digit) |
| [5z34-e3ws](https://www.datos.gov.co/d/5z34-e3ws) | Vista EMPRESAS GIRON (NIT filter) | Alcaldía Girón | 6,737 | `documento`, `razon_social`, addresses (no contact) | N | N | Y | N | **MED** (address only; same entities as bedu-5uzi) |
| [96mx-6n3n](https://www.datos.gov.co/d/96mx-6n3n) | Grandes Contribuyentes Municipio de Giron | Alcaldía Girón | 92 | `numero_de_documento`, `correo_de_notificaciones`, `numero_de_notificaciones` | Y | partial | Y* | N | **MED** (1 energy NIT overlap; small list) |
| [ryfe-5k95](https://www.datos.gov.co/d/ryfe-5k95) | PYMES CAMARA BARRANCABERMEJA | CCB Barrancabermeja | 454 | `razon_social`, `ciiu_1`, `ciiu_2`, `tam_empresa`, matricula dates (no NIT column) | N | N | N | Y | **LOW** (CIIU text; 0 name overlap with energy profile in test) |
| [yisd-d6ns](https://www.datos.gov.co/d/yisd-d6ns) | NITs + actividad económica | CCB Barrancabermeja | 12,986 | `nit`, `mun_comercial`, `ciiu_1`…`ciiu_4` (numeric CIIU in text) | N | N | Y | N | **MED** for CIIU refinement elsewhere; **LOW** for energy cluster (0 NIT overlap with wf53 energy slice) |
| [9v9c-htja](https://www.datos.gov.co/d/9v9c-htja) | EMPLEADOS POR EMPRESA CCB Barrancabermeja | CCB Barrancabermeja | 11,303 | `nit`, `matricula`, `email_comercial`, `ciiu_1`, `personal`, … | Y | N | Y | Y | **MED** regional (email+matricula+NIT); **LOW** for Bucaramanga energy slice (0 overlap tested) |
| [3pfh-yj57](https://www.datos.gov.co/d/3pfh-yj57) | EMPRESAS VENTA VEHÍCULOS USADOS | CCB Barrancabermeja | 58 | `nit`, `matricula`, `dir_comercial` | N | N | Y | Y | **NONE** for energy |
| [gxmq-aa4t](https://www.datos.gov.co/d/gxmq-aa4t) | BD recicladoras CCBarrancabermeja | CCB Barrancabermeja | (not counted) | recycler registry | N | N | — | — | **NONE** for energy |
| [xf9q-25zn](https://www.datos.gov.co/d/xf9q-25zn) | EMPRESAS ACELERADAS - AVANZA BGA | IMEFE Bucaramanga | 80 | entrepreneurship survey (no NIT) | N | N | N | N | **NONE** |
| [wwhc-kpg6](https://www.datos.gov.co/d/wwhc-kpg6) | CARACTERIZACIÓN EMPRENDEDORES SANTANDER | Gobernación Santander | 501 | survey fields | N | N | N | N | **NONE** |

\* Girón `documento` / `numero_de_documento` are NIT without verification digit; join uses base-9 match to wf53 `nit`.

## CCB Bucaramanga open data conclusion

Under publisher **“Cámara de Comercio de Bucaramanga, Santander”**, datos.gov.co exposes **only one** empresa registry with NIT (`wf53-j577`). **No** CCB Bucaramanga dataset on the portal includes `correo`, `teléfono`, or numeric CIIU. Contact enrichment for the energy cluster must come from **territorial** publishers (Girón, SUPER SSP) or other Santander chambers (Barrancabermeja) with jurisdiction overlap limits.

## Explicit: xbft-sj66

Catalog title matches “Depuración Registro Mercantil”, but attribution is **Valledupar (Cesar)**. It is a depuration/cleanup log (`tipo=DEPURADO`), not a Bucaramanga empresa directory. **Not useful** for joining Bucaramanga/Santander energy NITs; included only because the ID appears in broader “Cámara de Comercio” searches.
