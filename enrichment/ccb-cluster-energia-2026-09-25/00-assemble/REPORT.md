# Wave 0 assemble — REPORT

Generated: 2026-09-25 20:36 UTC

## Input inventory (`enrich.csv`)

| Path | Data rows | REPORT.md |
|------|----------:|:---------:|
| `01-secop-proveedores/enrich.csv` | 2011 | yes |
| `02-secop-contratos/enrich.csv` | 99 | yes |
| `05-sspd-prestadores/enrich.csv` | 23 | yes |
| `06-ccb-other-dumps/enrich.csv` | 26 | yes |
| `07-company-websites/enrich.csv` | 26 | yes |
| `08-opencorporates-gleif/enrich.csv` | 19 | yes |
| `09-licensed-rues-apis/enrich.csv` | 7 | yes |

### Absent micro-hands (not merged)

- **ABSENT:** Hand 3 — RUES public — no folder on `main` at assemble time
- **ABSENT:** Hand 4 — Made in Santander — no folder on `main` at assemble time

`09-licensed-rues-apis/enrich.csv` contains **0** non-example live rows (doc samples only); excluded from email priority per Wave 0 spec.

## Universe

| Metric | Count |
|--------|------:|
| SECOP proveedores universe (01 spine) | 2011 |
| Distinct NIT join keys in `union.csv` | 2029 |
| With non-blank email after priority merge | 659 |
| Blank email (`email_blank.csv`) | 1370 |
| `02-secop-contratos` NITs with contract signal | 99 |

Reference: CCB VPS energy profile cited in hand docs ~922 wf53 allowlist / **2011** SECOP-universe NITs in `01-secop-proveedores`; broader VPS ~2115 not used as assemble spine.

## Email source contribution (winning arm)

| source_arm | NITs |
|------------|-----:|
| `01-secop-proveedores` | 642 |
| `06-ccb-other-dumps` | 10 |
| `05-sspd-prestadores` | 7 |

## Email type (chosen email)

| email_type | Count |
|------------|------:|
| PERSON | 551 |
| ROLE | 63 |
| UNKNOWN | 45 |

## Outputs

| File | Rows |
|------|-----:|
| `union.csv` | 2029 |
| `email_blank.csv` | 1370 |
| `resend_stage.csv` | 659 |
| `mailfinder_pilot_candidates.csv` | 80 |

## Merge rules

1. Join key: see `nit-map.md`.
2. Email priority: `01-secop-proveedores` (correo before rep. legal) → `07-company-websites` (mailto &lt; contact page &lt; homepage) → `05-sspd-prestadores` → `06-ccb-other-dumps` → `08-opencorporates-gleif`.
3. No invented emails; empty stays empty.
4. Resend: staged only — **no API send**.

## Mail Finder pilot (≤80)

From `email_blank.csv`, sort by Santander/Bucaramanga metro city match (desc), then rows with domain/`website` hint, then `razon_social`. Cap **80**.
