# Wave4 L09 Arm 04 — Deferred high-yield (L01–L03 closeout leads)

**Run:** 2026-09-25 (UTC) · **Seats:** 5 · **Input:** `input.csv`  
**Method:** Use **L01 / L02 / L03 closeouts as hints only**; fetch each lead URL plus **one same-domain expand** (WP media index, cited PDF, or L03-class impact/regulatory PDF). **FOUND** only with independent verification of **printed name + exact person@firm** in the same document or HTML block. Generics → **EMPTY**.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 1 |
| **EMPTY** | 4 |
| **UNCERTAIN** | 0 |

## FOUND

| Monday_item_id | Name | Email | Source |
|----------------|------|-------|--------|
| 13028366289 | Jean-Marc Champagne | jmchampagne@senecaimpact.earth | [WWF GEF TNFD MTR report PDF](https://files.worldwildlife.org/wwfcmsprod/files/Publication/file/2ons9eh7ip_GEF_TNFD_MTR_report_final_plus_mgmt_response.pdf) |

## EMPTY (high-yield paths checked)

| Seat | Why EMPTY |
|------|-----------|
| Jason Sydow | L01 n47 team lead — no person@n47 / @next47 on team HTML or CDN PDF |
| Jonathan Duarte | L01 people page; L03 PLANETA PDF + L03 arm-02 FLII2025 — name only or generics |
| Josep Oriol | L01 team page; privacy PDF `j.oriol@` without *Josep Oriol* in same block |
| Juan Franck | L01 latinamericafund site — no PDF corpus; SoftBank brochure URLs unreachable; no SEC bind |

## Hygiene

- No Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP checks, invented emails, or Monday writes.
- Writes confined to `mail-finder/wave4/L09/arm-04/`.

## Evidence

- `evidence/leads-from-L01-L03.md` — hint index  
- `evidence/13028366289-jean-marc-champagne-excerpt.md` — FOUND snippet  
- `evidence/url-index.md`, `evidence/negative-excerpts.md`, fetched HTML/PDF under `evidence/`
