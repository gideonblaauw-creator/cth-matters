# Wave4 L10 Arm 01 — CNPJ / IAPD / Canadian securities + DocuSign / ethics PDF scorecard

**Scope:** 5 seats from `input.csv`  
**Method:** Public **Brazilian CNPJ** (Receita Federal lookup where applicable), **FINRA IAPD**, **Canadian securities** (BCSC search / Form 45-106F1 class), **DocuSign**-class signature blocks in SEC/regulatory text, and **ethics/compliance PDFs**. **FOUND** only when the target **display name** and an exact **personal person@firm** co-occur on the **same public page/PDF**. Generics → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, SMTP verify, invented emails, or Monday writes.

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Per-seat summary

| Monday_item_id | Name | Domain | Outcome |
|----------------|------|--------|---------|
| 13028367182 | Nic Gorini | spin.vc | EMPTY — no SEC/IAPD/CNPJ/BCSC PDF with Gorini + @spin.vc |
| 13100488906 | Niccolò Camerana | stellantis.com | EMPTY — SEC POA exhibits signature only; no email block |
| 13028359863 | Nina Alastruey | demium.com | EMPTY — CNMV FCRE prospectus / BOE sanctions; no Nina + @demium.com |
| 13100506349 | Pat Martin | venture53.com | EMPTY — press PDF quotes Pat; contact is amymack@venture53.com (third party) |
| 13028367036 | Pauline de Valk | abnamro.com | EMPTY — ethics PDF bank-wide inboxes; SIF article uses sif@ generic |

## Notable near-misses

| Seat | Why not FOUND |
|------|----------------|
| Pat Martin | EIN Presswire GenLogs exit PDF: **Pat Martin** quoted; footer **amymack@venture53.com** attributed to Amy Mack, not Pat. |
| Pauline de Valk | Banking-for-better article names **Pauline de Valk** with **sif@abnamro-privateequity.nl** (fund generic, not person@abnamro.com). |
| Nina Alastruey | CNMV prospectus includes **Ana.chaffer@bdo.es** (auditor) only; no Alastruey in document text. |

## Deliverables

- `input.csv`, `results.csv`, `stamp-list.json`, `README.md`, `summary.md`
- `evidence/` — filing/PDF snapshots, excerpts, `url-index.md`, `negative-excerpts.md`

**Processed:** 2026-09-25 (UTC)
