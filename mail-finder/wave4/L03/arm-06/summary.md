# Wave4 L03 Arm 06 — regulatory / securities PDF scorecard

**Run:** 2026-09-25 · **Seats:** 5 · **Input:** `input.csv`  
**Method:** Public-web discovery of **BCSC Form 45-106F1–class**, **SEDAR/SEDAR+**, **SEC EDGAR / IAPD**, **Form D**, and other **national securities / offering PDFs**. **FOUND** only when the seat **name** and a **non-generic `person@firm`** co-occur in the **same public PDF** (published spelling). Generics → **EMPTY**.

## Results

| Status | Count |
|--------|------:|
| FOUND | 1 |
| EMPTY | 4 |

**Yield:** 1 / 5 citation-grade personal emails.

## Per seat

| Name | Domain | Outcome |
|------|--------|---------|
| Stefanie Hauer | nature-re.com | **FOUND** — `s.hauer@nature-re.com` in Fair Finance Institute NatureRe deck (Partner & Board Member) |
| William Prescott | redribbon.co | Fund PDFs only `redribbonrerise@redribbon.co`; no Prescott + person@redribbon.co in EDGAR/regulatory PDFs |
| Jeff Stoike | blueactionaccelerator.com | Speaker PDF bio only; no person@ on firm domain in filings PDFs searched |
| Mikayla Hart | congruencecapital.com | Congruence SEC 13F / IAPD path — no Hart + person@congruencecapital.com in accessible regulatory PDFs |
| David García Acero | bbvaspark.com (BBVA Spark) | No securities PDF with name + person@bbvaspark.com |

## Hygiene

- No Hunter/Apollo, LinkedIn scrape, pattern guessing, or SMTP validation.
- Generic inboxes (`redribbonrerise@`, `IR@`, `team@`, `enquiries@`) → **EMPTY**.
- **No Monday API writes** — workbench uses `stamp-list.json` after review.

## Artifacts

- `evidence/naturere-fair-finance-deck-2025-10-21.pdf` + `stefanie-hauer-excerpt.md` (FOUND)
- Supporting EMPTY checks: Red Ribbon investor deck, OIP speakers PDF (Jeff Stoike, no email)
