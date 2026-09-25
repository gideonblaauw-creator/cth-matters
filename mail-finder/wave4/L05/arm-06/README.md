# Mail Finder — Wave4 / L05 / Arm 06

**Focus:** Public **impact reports**, **LP materials**, **annual reports**, and comparable **PDFs** — **FOUND** only when the seat person’s published name and an exact **person@firm** email appear in the **same** PDF (citation unit).

**Write path:** `mail-finder/wave4/L05/arm-06/` only. **No Monday API writes** from this arm.

## Input

`input.csv` — 5 seats (Monday export).

## Method (`impact_LP_annual_report_PDF`)

1. For each seat, search public first-party and issuer/fund/LP/impact PDFs (annual reports, EIS/IM memos, multilateral impact studies, third-party LP sourcing decks where the firm is cited).
2. Download PDFs when reachable; extract text with `pdftotext` and verify **name + non-generic person@firm** on the **same** document.
3. Record **Source_URL**, page/section where possible, and **Evidence_excerpt** spelling as printed.
4. **Generics** (`info@`, `IR@`, `eis@`, `sales@`, `contact@`, etc.) → **EMPTY** unless the same block attributes the mailbox to the target person (none in this batch).

## Prohibited

Pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, paid/authenticated sources, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, non-blank `Checked_URLs`, optional `Email` when FOUND |
| `stamp-list.json` | FOUND seats only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | PDF copies, extracts, `url-index.md`, `negative-excerpts.md` |

Large issuer PDFs (e.g. Molten FY26 annual report, ERIA Brunei study) are cited by public URL; local repo keeps `pdftotext` extracts only to limit repo size.

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L05-arm06) contact@example.com'
EV=mail-finder/wave4/L05/arm-06/evidence
curl -sL -A "$UA" -o "$EV/molten_eis_im_oct2025.pdf" \
  'https://investors.moltenventures.com/storage/uploads/EIS/Documents/December%202025/Molten%20Ventures%20EIS%20Informantion%20Memorandum%20Issued%20October%202025.pdf'
pdftotext "$EV/molten_eis_im_oct2025.pdf" "$EV/molten_eis_im_oct2025.txt"
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.
