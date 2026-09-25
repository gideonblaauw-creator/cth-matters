# Company websites — public mailto / contact (Micro-Hand 7/9)

Generated: 2026-09-25 (UTC)

## Sources

| ID | Dataset | Use |
|---|---|---|
| `wf53-j577` | EMPRESAS CÁMARA DE COMERCIO DE BUCARAMANGA | Energy-profile NIT allowlist (`desc_ciiu1` + ACTIVO) |
| `qmzu-gj57` | SECOP II — Proveedores Registrados | `sitio_web` joined on NIT (base digits) |

Optional Made in Santander fichas were not merged in this pass (directory is JS-gated; no stable public API without login).

## Allowlist

- wf53 energy-profile NITs: **922**
- SECOP proveedor rows for those NITs: **209**
- Unique domains queued (prioritized, cap **150**): **48**

Priority: named cluster ESP actors → SECOP `esta_activa=Si` → company size → first unique domain per NIT.

## Crawl policy

- User-Agent: `CCB-Cluster-Energia-Research/1.0 (+contact-discovery; polite; no-automation-spam)`
- Rate limit: ~1.25s between sites; robots.txt honored
- Pages tried per site: homepage + common contact paths (`/contacto`, `/contact`, …)
- **Emails are only taken from fetched HTML/mailto** — SECOP `correo` not copied into `enrich.csv`

## Results

| Metric | Count |
|---|---|
| Sites attempted | **48** |
| Sites with ≥1 public email found | **18** |
| Email rows in `enrich.csv` | **26** |
| Attempted, no email on crawled pages | **19** |
| Blocked (robots.txt disallowed) | **11** |
| Fetch/other errors | **0** |

## Output

- `enrich.csv`: columns `nit`, `domain`, `email`, `page_url`, `method` (`mailto` | `contact_page` | `homepage`)

## Notes

- No outbound email/SMS; no VPS database writes.
- Multiple rows per NIT/domain when several distinct published addresses appear.
- Placeholder/template addresses (e.g. `ejemplo@misitio.com`) dropped from `enrich.csv`.
- **150-site cap not reached:** only **48** allowlist NITs had a non-empty SECOP `sitio_web` resolvable to a crawlable domain (209 SECOP rows total for the allowlist).
- One SECOP `sitio_web` pointed at `instagram.com` (NIT `900349430-8`); excluded from crawl queue as a social URL, not an official company domain.

### Sample blocked/error domains

- `robots:essa.com.co`
- `robots:enermas.com.co`
- `robots:ruitoqueesp.com`
- `robots:espigas.com.co`
- `robots:proviservicios.com`
- `robots:lubrigras.net`
- `robots:biocolder.com`
- `robots:centraldebobinados.com`
- `robots:instagram.com`
- `robots:proymelec.com`
- `robots:samatcro.com`
