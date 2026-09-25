# Workshop A+B+C — Monday feed pack (desk mirror)

Desk copy of the VPS-generated CCB cluster energía workshop enrichment (SECOP proveedor + contratos + scorecard → Monday projection CSVs).

## VPS SSOT

- Database and scripts: `/opt/claude-files/Projects/CCB-Bucaramanga/db/`
- Full export bundle: `/opt/claude-files/Projects/CCB-Bucaramanga/exports/workshop-2026-10-08/`

## What is in this folder

| File | Purpose |
|------|---------|
| `monday_feed_pilot60.csv` | 60-row pilot slice for Monday review |
| `workshop_abc_stats.json` | Row-count sanity check vs VPS run |
| `PILOT60_PREVIEW.md` | Human-readable pilot summary |
| `CLOSEOUT.md` | Workshop A+B+C closeout (sources, heuristics, refresh) |

## Not in this PR

- **`monday_feed_universe.csv`** (2,113 rows) — remains on VPS exports only for this pack; not attached here due to size / review scope.

## Operations

- **No Monday API writes** from this pack (projection CSVs and docs only).
- No Resend / Gmail / SECOP re-pull from this repo path.

## Branch naming

Preferred desk branch: `cursor/workshop-abc-enrich-desk` (cloud agent may use `-b887` suffix).
