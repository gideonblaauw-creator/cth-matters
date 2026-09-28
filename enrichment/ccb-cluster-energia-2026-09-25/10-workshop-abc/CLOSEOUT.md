# Workshop A+B+C — Datathon Climático (2026-10-08)

**Event:** [Datathon Climático socialización](https://luma.com/kdvd65cv) · 8 Oct 2026  
**SSOT (VPS):** `/opt/claude-files/Projects/CCB-Bucaramanga/db/cluster_energia_profile.sqlite`  
**Exports (VPS):** `/opt/claude-files/Projects/CCB-Bucaramanga/exports/workshop-2026-10-08/`  
**Repo mirror:** `enrichment/ccb-cluster-energia-2026-09-25/10-workshop-abc/`  
**Monday:** projection CSVs only — no Monday API / Resend / Gmail.

## Row counts

| Artifact | Rows |
|----------|-----:|
| Profile universe (`companies` with NIT) | 2,113 |
| `secop_proveedor` (A — qmzu-gj57) | 2,113 |
| SECOP proveedor **matched** | 697 |
| With `nombre_representante_legal` (SECOP) | 695 |
| With any SECOP phone (company or rep.) | 694 |
| `secop_contratos_agg` (B — jbjy-vk9h) | 2,113 |
| NITs with ≥1 contract | 343 |
| NITs with non-empty `climate_flags` | 101 |
| `workshop_scorecard` (C) | 2,113 |
| `monday_feed_universe.csv` | 2,113 |
| `monday_feed_pilot60.csv` | 60 (all pilot NITs; 3 not in profile DB) |
| SECOP contract rows pulled (national) | 2,508 |

### Invite tier distribution

| invite_tier | Count |
|-------------|------:|
| Anchor candidate | 228 |
| Ally | 915 |
| Later | 970 |

## Sources

| Hand | Dataset | ID |
|------|---------|-----|
| A Proveedores | SECOP II Proveedores Registrados | `qmzu-gj57` |
| B Contratos | SECOP II Contratos Electrónicos | `jbjy-vk9h` |
| Universe | CCB profile-fit SQLite (`companies`) | wf53-j577-derived CSV load |

**Join:** NIT base before verification digit; strip non-digits from base (`nit_join_key`). SECOP proveedor `nit` uses spaced digits before `-DV`.

**Hygiene:** `No Provisto` / empty → blank. No invented contacts.

## Scorecard heuristic (C)

Documented for reproducibility; tune before live invites.

### `challenge_fit` (one or more, `;`-separated)

- **Eficiencia:** regex on legal name + contract objeto/descripcion + CIIU — eficiencia energética, solar/FV, iluminación/LED, subestaciones, medición/auditoría energética, ISO 50001; default for CIIU `35*` / `43*` when no other signal.
- **Aire:** calidad del aire, emisiones, PM2.5/PM10, HVAC, ventilación, purificación.
- **Circular:** economía circular, residuos, reciclaje, compost, postconsumo, valorización.

### `invite_tier`

- **Anchor candidate:** `is_named_cluster_actor=1`, **or** (≥10 contracts and ≥500M COP total), **or** (core energy CIIU 3511–3514/3520/3530/4322/4661/4730 and (≥3 contracts or SECOP contactable)).
- **Ally:** SECOP proveedor match, **or** ≥1 contract, **or** climate contract flag, **or** CIIU prefix 35/27/43.
- **Later:** remaining profile-fit rows.

### `score_reason`

Short tags joined with `;` (e.g. `named_cluster_actor`, `high_secop_activity`, `climate_contract_signal`, `secop_contactable`, `core_energy_ciiu`, `profile_fit_baseline`). Pilot rows outside profile DB append `pilot_not_in_profile_db`.

### `datathon_status`

Default **`Not invited`** for all rows (Monday projection baseline).

## Refresh

On VPS:

```bash
python3 /opt/claude-files/Projects/CCB-Bucaramanga/db/workshop_abc_enrich.py
```

Proveedores cache: `/opt/claude-files/Projects/CCB-Bucaramanga/db/.cache/qmzu-gj57_by_nit.json` (optional; speeds re-runs).
