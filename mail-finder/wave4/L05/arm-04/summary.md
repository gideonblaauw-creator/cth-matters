# Wave4 L05 Arm 04 — impact / LP / annual-report PDF scorecard

**Run:** 2026-09-25 (UTC) · **Seats:** 5 · **Input:** `input.csv`  
**Method:** Public **impact reports**, **LP materials**, **annual reports**, and comparable **PDFs** (plus statutory accounts where published as PDF). **FOUND** only when the seat **name** and a **non-generic `person@firm`** co-occur in the **same PDF** with citation-grade excerpt. Generics → **EMPTY**.

## Results

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

**Yield:** 0 / 5 citation-grade personal emails in the PDF lane.

## Per seat

| Monday_item_id | Name | Domain | Outcome |
|----------------|------|--------|---------|
| 13028336225 | Dr. Luke Kirke | greenbondcorp.com | **EMPTY** — GBC/éthica HTML only; generic `hello@ethica.capital`; no qualifying PDF |
| 13114451141 | Eduardo Brennand Campos | onevc.vc | **EMPTY** — ONEVC Form D + site; no Eduardo + person@onevc.vc in public PDF |
| 13114460590 | Elias Mufarech | collide.capital | **EMPTY** — Collide letter/team HTML; no PDF with person@collidecap.com |
| 13028359480 | Elvia Gomez | acumen.org | **EMPTY** — Acumen annual/impact/audit PDFs checked; no Gomez + person@acumen.org |
| 13028399382 | Emma Haight | glenarapartners.com | **EMPTY** — CH accounts PDF names Haight; no email in PDF |

## Hygiene

- No Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP validation, or Monday writes.
- Generic inboxes (`hello@`, `ab@`, `investors@`, `media@`, etc.) → **EMPTY**.
- Work confined to `mail-finder/wave4/L05/arm-04/`.

## Artifacts

- `evidence/url-index.md` — PDF URLs checked per seat
- `evidence/negative-excerpts.md` — exclusion rationale
- `evidence/glenara-llp-accounts-excerpt.txt` — Companies House PDF text sample (Emma Haight, no `@`)
- `evidence/acumen_pdf_probe.json` — automated Acumen PDF path probe log
