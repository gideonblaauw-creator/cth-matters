# Mail Finder — Wave4 / L03 / Arm 05

**Focus:** Regulatory and securities **PDF** email discovery (Potential Investors). Uses public filings and signature blocks — not firm-site team crawls (see Wave4 L02 Arm 05 for mailto lane).

## Input

`input.csv` — columns: Monday_item_id, Name, Contact_name, Firm, Kind, Priority, Status, Website, Domain, LinkedIn.

**Seats:** 5 (Wave4 L03 Arm 05 batch).

## Method

For each seat:

1. Search **BCSC** Form **45-106F1** and related exempt-distribution filings (BCSC document viewer / EDER).
2. Attempt **SEDAR+** / national registers where entity jurisdiction suggests filings (**CNMV** for Spanish gestoras, **AFM** register for Dutch AIFMs, **SEC EDGAR** Form D / full-text for US fund vehicles, **FINRA IAPD** where applicable).
3. Download or view public **PDFs** (or BCSC-rendered filing PDFs); extract text and scan for **seat display name + non-generic `person@firm`** in the same block (certification, signature, contact table).
4. **FOUND** only with citation-grade co-attribution in one public PDF (published spelling).
5. Generics (`info@`, `hello@`, `contacto@`, `support@`, `invest@`, etc.) → **EMPTY** for this arm.
6. **Prohibited:** Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP verify, invented emails. LinkedIn URLs in input are human context only.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat FOUND/EMPTY, checked URLs, notes |
| `stamp-list.json` | FOUND emails for Monday workbench stamp (after review) |
| `summary.md` | Scorecard |
| `evidence/` | PDFs and excerpts supporting FOUND or key EMPTY adjudication |
| `README.md` | This spec |

## Result statuses

| Status | Meaning |
|--------|---------|
| `FOUND` | Citation-grade person email in a regulatory/securities PDF |
| `EMPTY` | No qualifying name + person@firm co-occurrence in filings searched this wave |

## Scope guardrails

- Write **only** under `mail-finder/wave4/L03/arm-05/`.
- Do **not** modify other arms or Monday.

## Regenerate evidence text (optional)

```bash
pip install pypdf --break-system-packages
python3 - <<'PY'
from pypdf import PdfReader
p = "evidence/bcsc-autotech-fund-ii-45-106f1.pdf"
print(PdfReader(p).pages[0].extract_text())
PY
```
