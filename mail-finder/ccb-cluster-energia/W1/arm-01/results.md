# MF CCB Clúster Energía — W1 arm-01 Track A (firm contact)

**Method:** First-party Contact / Contáctenos / About / Nosotros (+ same-domain PDFs).  
**Run date:** 2026-09-25  
**Seeds:** 8 (from `input.csv`)

## Summary

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 0 |
| UNCERTAIN | 0 |
| DOMAIN_UNRESOLVED | 8 |

## Findings

No seed had a **verified first-party firm website** with a published mailbox co-occurring with **NIT and/or razón social** on the same page. Commercial directories (InformaColombia, eInforma, Empresite) list phones and addresses but are not first-party firm contact pages and were not stamped.

Several **near-name domains** were sniff-tested and rejected (wrong entity or no NIT match), including:

- `cablesas.com.co` (CABLESAS — not Cables de Santander S.A.S.)
- `hasolutions.com.co` (HA Solutions IT — NIT 800.035.776-1)
- `www.3elementos.co` (3 Elementos SAS — not 3ED S.A.S.)
- `369.net.co` (369 Ingeniería Col — Barranquilla)
- `gironesp.com` (Girón municipal ESP)

## Deliverables

| File | Description |
|------|-------------|
| `input.csv` | Seed copy |
| `results.csv` | One row per seed; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only (`[]`) |
| `evidence/` | Registry HTML captures, `url-index.md`, `negative-excerpts.md` |
| `CLOSEOUT.md` | Handoff notes |

## Monday / CRM

No CRM writes. No `stamp-list` entries (zero FOUND).

**Stamp-list (FOUND only):** include `nit`, `razon_social`, `crm_id`, `email`, `email_type`, `source_url`, `excerpt`, `city`, `domain`, and **`contact_name`** when a named person appears on the same first-party page as the mailbox (Monday Contact name `text_mm7hkeme`). Blank/`""` for ROLE-only with no person named.

| FOUND with `contact_name` | FOUND without `contact_name` |
|---------------------------:|-----------------------------:|
| 0 | 0 |
