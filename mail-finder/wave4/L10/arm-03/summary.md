# Wave4 L10 Arm 03 — CNPJ / IAPD / Canadian securities + DocuSign / ethics PDF scorecard

**Scope:** 5 seats from `input.csv` (P2)  
**Method:** Public **Brazilian CNPJ-class** lookups where relevant, **FINRA IAPD** (firm/ADV), **SEC EDGAR** (Form D, exhibits), **BCSC** document search, and **ethics/compliance/press PDF** lanes. **FOUND** only when the seat **name** and a **non-generic `person@firm`** co-occur on the **same public page or PDF**. Generics → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, or invented emails.

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Per seat

| Monday_item_id | Name | Domain | Result |
|----------------|------|--------|--------|
| 13114431023 | Robert Weber | greatnorthventures.com | EMPTY — Form D + IAPD ADV name-only; 0 EDGAR @domain |
| 13028358897 | Ryan Martin | enduringplanet.com | EMPTY — not on Form D; no regulatory person@ |
| 13028365776 | Scot Bryson | impactful.capital | EMPTY — no filings; site/podcast without @impactful.capital person cite |
| 13096674688 | Scott Sobel | valorcapitalgroup.com | EMPTY — EX-99.1 names Scott; email block is Doug Smith CFO |
| 13028360221 | Simon SDG | sdgglobalgroup.com | EMPTY — press uses info@ generic; no Simon SDG + person@ on same source |

## Notable near-misses

- **Scott Sobel:** [Valor Latitude EX-99.1](https://www.sec.gov/Archives/edgar/data/1843091/000095010321009266/dp153096_ex9901.htm) — Scott Sobel listed as director; `Doug.smith@valorcapitalgroup.com` is CFO contact only.
- **Robert Weber:** [Great North Capital Fund II Form D/A](https://www.sec.gov/Archives/edgar/data/1849375/000184937526000001/0001849375-26-000001.txt) — signer/promoter without email field.
- **Simon SDG:** [Green Economy Media](https://greeneconomy.media/tip-one-partnership-with-sdg-to-raise-global-impact-funds-to-invest-in-africa/) — Simon Littlewood quote + `info@sdgglobalgroup.com`.

## Deliverables

- `input.csv`, `results.csv`, `stamp-list.json`, `README.md`, `summary.md`
- `evidence/` — IAPD ADV extract, SEC exhibit snapshot, URL index, negative excerpts

**Processed:** 2026-09-25 (UTC)
