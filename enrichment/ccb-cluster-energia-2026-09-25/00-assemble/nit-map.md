# NIT normalization — Wave 0 assemble

Canonical join key for all micro-hand `enrich.csv` files in this wave.

## Rule

1. Trim whitespace on the raw `nit` string.
2. If the string contains `-`, take the segment **before the first hyphen** as the NIT base (verification digit / DV is dropped for joining).
3. Strip all non-digit characters from the base (`re.sub(r"\D", "", base)`).
4. Empty result → row skipped for join (logged in assemble inventory if present).

## Display `nit` column in outputs

- Prefer the **first seen** formatted value from `01-secop-proveedores/enrich.csv` (includes DV when CCB provides it).
- If a NIT appears only in satellite arms (e.g. `02-secop-contratos`), use that arm’s formatted `nit` string.

## Cross-source maps

| Source | Field | Join |
|--------|--------|------|
| CCB wf53-j577 / Hands outputs | `nit` | `{base}-{dv}` → join on `base` digits |
| SECOP qmzu-gj57 | `documento_proveedor` | numeric body = join key |
| SECOP jbjy-vk9h contracts | `documento_proveedor` | same as proveedores |

Same rule as `02-secop-contratos/nit-map.md` and `01-secop-proveedores/build_enrichment.py` (`nit_join_key`).
