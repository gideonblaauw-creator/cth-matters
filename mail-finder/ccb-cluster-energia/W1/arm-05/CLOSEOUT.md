# Arm 05 Track A — CLOSEOUT

Date: 2026-09-25  
Path: `mail-finder/ccb-cluster-energia/W1/arm-05/`

## Acceptance checklist

- [x] `input.csv` copied from operator upload (7 seed rows)
- [x] `results.csv` — one row per seed; FOUND cited with `email_type`, `source_url`, `evidence_excerpt`
- [x] `results.md`, `stamp-list.json`, `evidence/` present
- [x] No Monday / CRM / Resend writes
- [x] Draft PR opened (do not merge)

## Scorecard

- **FOUND:** 1 (ALTURAS — gerencia@alturasingenieria.com, ROLE)
- **EMPTY:** 4 (two personas naturales + ALLPRO + ALQUILAB — no first-party mailbox)
- **DOMAIN_UNRESOLVED:** 2 (Alexis Vega dead domain / non-firm-domain Wayback mail; Altus no verified site)

## Operator notes

- Alexis Vega: consider separate website-stamp pass if `alexisvegaingenieros.com` is re-registered.
- Altus: do not use `altusingenieria.com` (Venezuela homonym) or national Altus brands for this NIT.

## Monday workbench (Gideon addendum)

- **Contact name column:** `text_mm7hkeme`
- **`stamp-list.json`:** include `contact_name` when a **named person** is published on the **same first-party page as the mailbox** (exact published spelling). Leave blank for ROLE-only inboxes. Never invent names.
- This run: sole FOUND is `gerencia@alturasingenieria.com` (ROLE) → `contact_name` is intentionally blank.
