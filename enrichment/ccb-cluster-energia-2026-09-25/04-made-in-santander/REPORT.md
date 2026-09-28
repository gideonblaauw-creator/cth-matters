# Made in Santander — Clúster Energía / Energía (2026-09-25)

## Scope

Sources requested:

| Source | URL | Role |
|--------|-----|------|
| Directorio Clúster | https://madeinsantander.co/directorio-cluster/ | Landing / mapa del ecosistema (sin fichas en HTML estático) |
| Tag clúster energía | https://madeinsantander.co/listing-tag/cluster-energia/ | Taxonomía WP `job_listing_tag` id **574** |
| Filtro capacidad Energía | https://madeinsantander.co/amenity/energia-es/ | Archivo por amenity/capacidad «Energía» |
| Ficha conocida | https://madeinsantander.co/empresa/essi/ | Validación manual |

## Listings found

### `listing-tag/cluster-energia/`

- Página carga con título **Cluster Energia | Made in Santander** (término `term-574`).
- Grid de listados WP Job Manager renderizado en HTML con mensaje: **«No hay listados que coincidan con tu búsqueda.»**
- **0 empresas** asociadas al tag `cluster-energia` en el directorio en el momento del scrape.
- Enlace REST expuesto en `<head>`: `wp-json/wp/v2/job_listing_tag/574` (no usable vía `curl`; ver Cloudflare).

### `amenity/energia-es/`

- Tras pasar verificación Cloudflare en navegador y esperar carga JS/AJAX del grid: **1 resultado**.
- Única ficha enlazada: **ESSI** → https://madeinsantander.co/empresa/essi/
- Paginación adicional (`/page/2/` …) no aportó más slugs en pruebas con sesión válida.

### `directorio-cluster/`

- Contenido promocional del Directorio Clúster (café, turismo, tecnología, salud, construcción, **energía**).
- Sin listado embebido de empresas ni URLs `/empresa/...` en el cuerpo estático; el acceso al clúster energía en footer apunta al tag `cluster-energia` (vacío).

### Total extraído para `enrich.csv`

| # | Empresa | Origen listing |
|---|---------|----------------|
| 1 | Empresa de Soluciones, Servicios e Innovación ESSI SAS | `amenity/energia-es` (capacidad **Energía** en ficha) |

**Nota:** Otras empresas del directorio mencionan energía eléctrica en la descripción (p. ej. Electro Software, Vásquez & Rodríguez) pero **no** aparecen en el tag `cluster-energia` ni en el filtro `amenity/energia-es`; no se incluyeron para no mezclar búsqueda general con listados energía/clúster.

## Cloudflare / automation

| Método | Resultado |
|--------|-----------|
| `curl` / scripts sin navegador | **HTTP 403**, página «Just a moment…», `cf-mitigated: challenge` |
| `WebFetch` (empresa individual) | OK para fichas `/empresa/{slug}/`; **no** devuelve cards del grid (listados vía JS) |
| `WebFetch` (tag / amenity / wp-json) | Shell estático o error; sin listados |
| Playwright headless | Intermitente: a menudo bloqueado en tag/amenity |
| Playwright / Chrome con UI (`headless: false`) | Pasó Turnstile con espera ~8–20 s; necesario para contar resultados en `amenity/energia-es` |
| RSS `listing-tag/cluster-energia/feed/` | 403 con `curl` |

**Ray IDs observados (ejemplos):** `a40cb77b4be07af9`, `a40cc1e97f88e605`, `a40cc1d12bdc8080`.

**Recomendación operativa:** una URL a la vez, cookies de sesión tras challenge, scroll para disparar AJAX del Job Manager; no confiar en API REST pública sin sesión.

## Campos por ficha (ESSI)

Publicados en https://madeinsantander.co/empresa/essi/:

- **Email:** monica.zambrano@essi.com.co  
- **Teléfono:** 304 2117205  
- **Web:** http://essi.com.co/  
- **LinkedIn (empresa):** https://www.linkedin.com/company/essilatinoamerica/  
- **NIT:** no publicado en la ficha  
- **Capacidades:** Energía; Industria Lactea  

Contactos del sitio (CCB / Made in Santander: marco.vasquez@camaradirecta.com, +57 (607) 6527000) **excluidos** del CSV de empresa.

## Join tips → registro CCB (NIT)

1. **Prioridad de match:** razón social exacta de la ficha → variantes sin sufijo (`ESSI`, `ESSI SAS`) → dominio `essi.com.co` → email `@essi.com.co`.
2. **NIT ausente en MiS:** usar RUES / CCB por NIT o búsqueda por nombre en el universo CCB; no inferir NIT desde contactos.
3. **Tag vacío:** el clúster energía está creado en WordPress (tag 574) pero sin empresas etiquetadas; futuras altas en `cluster-energia` deberían re-ejecutar este brazo.
4. **Deduplicación:** cruzar con otros brazos del enrichment por `source_url` y por NIT cuando aparezca en otra fuente.
5. **Señal débil energía:** solo incluir filas adicionales si aparecen en `amenity/energia-es` o recuperan el tag `cluster-energia`, no solo por keywords en descripción.

## Artefactos

- `enrich.csv` — 1 fila (ESSI), columnas: name, nit, email, phone, website, linkedin, source_url
