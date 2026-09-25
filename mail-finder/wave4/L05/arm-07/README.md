# Mail Finder — Wave4 / L05 / Arm 07

**Focus:** Public **impact reports**, **LP materials**, **annual reports**, and comparable PDFs where a named person and mailbox co-occur.

## Inputs

- `input.csv` — 5 seats (Monday export).

## Method (`impact_report;LP_materials;annual_report_PDF`)

1. Discover public PDFs from issuers, funds, impact/LAVCA/ecosystem publishers, and investee press releases; treat each PDF as the citation unit.
2. Extract text (`pdftotext`) and search for **display/legal name + non-generic `person@firm` email** on the same document.
3. **FOUND** only when both appear together with citation-grade excerpt (page/section when available).
4. **Generics** (`info@`, `speed@`, regional `@oikocredit.org`, spokesperson inboxes for a different named person) → **EMPTY**.
5. **Forbidden:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, paid/authenticated sources, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, non-blank `Checked_URLs`, optional `Email` when FOUND |
| `summary.md` | Scorecard |
| `stamp-list.json` | FOUND seats only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `evidence/` | PDF snapshots/text, URL index, negative excerpts |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L05-arm07) contact@example.com'
EV=mail-finder/wave4/L05/arm-07/evidence
curl -sL -A "$UA" -o "$EV/endeavor_colombia_informe_2024.pdf" \
  'https://colombia.endeavor.org/wp-content/uploads/2025/03/INFORME-2024_FINAL_04-03-2025_Baja.pdf'
curl -sL -A "$UA" -o "$EV/oikocredit_annual_2024.pdf" \
  'https://www.oikocredit.org/wp-content/uploads/2025/04/Oikocredit-Annual-Report-2024-secured_ENG.pdf'
curl -sL -A "$UA" -o "$EV/bosch_press_kit_ramesohl.pdf" \
  'https://www.bosch-presse.de/pressportal/de/media/pressemappen/press_kit_162950_en.pdf'
pdftotext "$EV/endeavor_colombia_informe_2024.pdf" -
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L05/arm-07/`.
