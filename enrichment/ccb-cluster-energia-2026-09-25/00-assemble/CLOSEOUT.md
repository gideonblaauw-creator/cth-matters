# Wave 0 assemble — CLOSEOUT

Date: 2026-09-25

## Acceptance checklist

- [x] `00-assemble/` outputs present (`union.csv`, `email_blank.csv`, `resend_stage.csv`, `mailfinder_pilot_candidates.csv`, `REPORT.md`, `nit-map.md`)
- [x] Input inventory with non-zero row counts in `REPORT.md`
- [x] `union.csv` row count = with_email + blank (documented in `REPORT.md`)
- [x] `resend_stage.csv` — non-blank sourced emails only; **no Resend API / no send**
- [x] `mailfinder_pilot_candidates.csv` — ≤80 rows, all from blank-email pool
- [x] Hands **3 (RUES public)** and **4 (Made in Santander)** marked **ABSENT** in `REPORT.md`
- [x] Draft PR: https://github.com/gideonblaauw-creator/cth-matters/pull/134

## Operator notes

- Re-run: `python3 enrichment/ccb-cluster-energia-2026-09-25/00-assemble/assemble_wave0.py`
- Track A: `email_type=ROLE` rows in `resend_stage.csv` are acceptable for a later Resend import (not executed in Wave 0).
