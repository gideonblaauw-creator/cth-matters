# Wave4 L03 Arm 05 — Regulatory / securities PDF scorecard

**Loop:** Mail Finder Wave4 L03 Arm 05 (BCSC Form 45-106F1, SEDAR/SEDAR+, FINRA/IAPD, CNMV/AFM-class national filings, signature blocks)  
**Seats processed:** 5  
**Run date:** 2026-09-25

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |

## Method

For each seat, search public regulatory and securities PDFs (and BCSC HTML-rendered 45-106F1 filings) for **display name + non-generic person@firm** co-occurrence in the same document block (signature, Item 10 certification, or equivalent). Generics (`info@`, `contacto@`, `support@`, `invest@`, firm-wide inboxes) → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guessing, or SMTP verify.

## Highlights

| Name | Domain | Regulatory pass |
|------|--------|-----------------|
| Tiffany Chen | carbonequity.com | AFM-licensed AIFM; no person-specific cite in filings searched |
| Alfredo Neila | plasticrepairsystem.com | Not CNMV fund issuer; PRS PDFs lack person email block |
| Lucía Gaitán Sánchez | gawa-capital.com | CNMV gestora reg. 167; no PDF with her + person@gawacapital.com |
| Mau Messina | sf500.vc | No BC/CNMV securities PDF with person email |
| Burak Cendek | autotechvc.com | BCSC 45-106F1 cites **Quin Garcia** / qg@autotechvc.com only (see `evidence/`) |

## Deliverables

- `input.csv` — 5-seat batch
- `results.csv` — per-seat EMPTY with checked URLs
- `stamp-list.json` — no FOUND emails (`[]`)
- `evidence/` — BCSC Autotech PDF + search log (+ PRS sample PDF)
- `README.md` — arm spec

**Monday:** no writes (workbench review only).
