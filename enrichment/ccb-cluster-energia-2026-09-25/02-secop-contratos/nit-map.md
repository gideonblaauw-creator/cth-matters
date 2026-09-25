# NIT join map — CCB (wf53-j577) ↔ SECOP II (jbjy-vk9h)

| Source | Field | Format | Notes |
|--------|--------|--------|--------|
| wf53-j577 | `nit` | `{base}-{dv}` e.g. `890201230-1` | CCB Bucaramanga registry key |
| jbjy-vk9h | `documento_proveedor` | numeric body only e.g. `890201230` | Match `split('-')[0]` on CCB `nit` |
| jbjy-vk9h | `tipodocproveedor` | often `NIT` for juridical persons | Not filtered (CCB set is all juridical NITs) |

**Allowlist rebuild:** `estado = ACTIVO` and `desc_ciiu1` matches energy CIIU regex (documented in `REPORT.md`).

**Energy contract tagging (volume prioritization only):** sector / objeto / descripción / UNSPSC (`codigo_de_categoria_principal`) matched against energy keywords and UNSPSC segments 26, 71, 14, 25.
