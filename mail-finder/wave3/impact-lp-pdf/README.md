# Mail Finder — Wave3 / Impact–LP–PDF arm

Exclusive deliverable path for **method_arm = `impact_lp_pdf`**.

## Contents

| File | Purpose |
|------|---------|
| `input.csv` | Monday export (12 seats) |
| `results.csv` | Full arm output: `Status`, `Checked_URLs`, `Notes`, `Method=impact_lp_pdf` |
| `summary.md` | Human scorecard |
| `stamp-list.json` | **FOUND only** (empty when no citation-grade hits) |
| `evidence/` | Downloaded PDFs + text extracts supporting EMPTY/UNCERTAIN calls |

## Rules (hard)

- Search seeds only: `"Name" "Firm"` / domain + `filetype:pdf`, impact report, annual report, SFDR, DFI disclosure, etc.
- **FOUND** only when full name and person@firm email co-occur on the same public PDF (published spelling).
- Shared inboxes (`contact@`, `info@`, `press@`, `impact@`, …) → **EMPTY**.
- No Monday API writes from this folder.

## Evidence PDFs

- `lightrock_mifidpru_2025.pdf` — Kevin Bone listed; no email in body
- `lightrock_modern_slavery_2025.pdf` — Kevin Bone signature; no email
- `ifu_ar_2024.pdf` — IFU annual report 2024
- `impactfund_sdg_fund_2024.pdf` — Danish SDG Investment Fund impact report 2024 (`contact@impactfund.dk` footer only)
- `molten_ar_2026.pdf`, `molten_sustainability_2026.pdf` — George Chalmers named; generic firm emails only
- `reefknot_sustainability.pdf` — `info@reefknotinvestments.com` only
- `crossboundary_ia50.pdf`, `crossboundary_carbon_playbook.pdf` — firm/program contacts only
- `seneca_seaweed.pdf` — `info@senecaimpact.earth` in About section

See `evidence/extracts.md` for quoted snippets.
