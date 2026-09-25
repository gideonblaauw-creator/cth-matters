# CCB Clúster Energía W1 arm-08 — CLOSEOUT (Track A firm contact)

## Counts

| Metric | Value |
|--------|------:|
| Input seeds | 7 |
| **FOUND** | 2 |
| **EMPTY** | 3 |
| **DOMAIN_UNRESOLVED** | 2 |
| `stamp-list.json` entries | 2 |

## Method compliance

- First-party contact surfaces only (no SECOP correo copy, no Hunter/Apollo, no LinkedIn scrape, no pattern/SMTP).
- Every seed row appears once in `results.csv`.
- FOUND rows include published spelling, `email_type`, `source_url`, and excerpt; evidence under `evidence/`.
- **No Monday, CRM, or Resend API writes.**

## Outcomes

1. **ANS ENERGIA SAS** — `comercial@ansenergia.com.co` (ROLE) on `contacto.php` with ANS ENERGIA S.A.S. branding.
2. **ANSALL S.A.S.** — `info@ansall.com` (ROLE) on official SPA site with ANSALL S.A.S. legal branding.
3. **ANKARO** — domain identified but live site down/unreachable here → EMPTY (Wayback reference kept, not stamped).
4. **ANSOELEC / ANÁLISIS DIGITAL** — no first-party web presence → EMPTY.
5. **AO SOLUCIONES INTEGRALES / AP SOLUCIONES SOSTENIBLES** — candidate domains map to different entities → DOMAIN_UNRESOLVED.

## Artifacts

| File | Purpose |
|------|---------|
| `input.csv` | Seed copy from arm-08 upload |
| `results.csv` | Full disposition per NIT |
| `results.md` | Human summary |
| `stamp-list.json` | FOUND-only downstream stamps |
| `evidence/` | HTML/JS snapshots, excerpts, URL index |

**PR:** draft only — do not merge.
