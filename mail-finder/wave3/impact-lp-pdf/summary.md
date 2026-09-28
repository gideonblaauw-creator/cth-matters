# Wave3 Arm 2 — `impact_lp_pdf` (search-seed only)

**Run:** 2026-09-25  
**Input:** 12 seats (`input.csv`)  
**Method:** Public impact/LP/SFDR/annual/DFI PDFs via `"Name" "Firm" … filetype:pdf` search seeds only (no pattern guess, Hunter/Apollo, SMTP verify, or LinkedIn scrape).

## Scorecard

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 11 |
| UNCERTAIN | 1 |
| HOLD | 0 |

**Day baseline context:** 27/50 overall program; this arm adds **0** citation-grade stamps.

## FOUND

None. `stamp-list.json` is empty (Monday stamps deferred to workbench).

## UNCERTAIN

| Monday_item_id | Name | Issue |
|----------------|------|--------|
| 13028366958 | Nathalie Couët | Board domain `senecaimpact.com` / Seneca Impact Advisors, but public profiles show Couët Strategic Advisors & HYDGEN — not listed on Seneca team; no PDF name+email co-occurrence under Seneca. |

## Method notes

- **Generics not stamped:** `contact@impactfund.dk`, `info@reefknotinvestments.com`, `info@congruentvc.com`, `impact@senecaimpact.earth`, `contact@crossboundary.com`, `press@lightrock.com`, `cosec@molten.vc`, etc.
- **PDFs harvested** under `evidence/` (Lightrock MIFID + modern slavery; IFU AR 2024; IFU SDG Fund impact 2024; Molten AR + sustainability FY26; Reefknot sustainability paper; CrossBoundary IA50 + carbon playbook; Seneca seaweed research).
- **Ship2B / Maite Fibla:** BSocial impact report referenced in press; direct `ship2bventures.com/...Informe...pdf` URL returned HTML (not a PDF) — no name+person@firm in a PDF.

## Per-seat summary

All seats documented in `results.csv` with `Checked_URLs` and `Status`.
