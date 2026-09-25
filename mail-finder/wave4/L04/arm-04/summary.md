# Wave4 L04 Arm 04 — SEC EDGAR exhibits / Form D / signature blocks

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`) — P1 outreach batch (Bancolombia, IDB Invest ×2, Suma Capital, APG).  
**Method:** Public SEC EDGAR full-text search, Form D / 6-K / DSTRBRPT / loan exhibits, and signature blocks. **FOUND** only when the seat’s published name and an exact person `@firm` email appear in the **same** filing artifact. Generics (`asamblea@`, `treasury@iadb.org`, `InvestorRelations@iadb.org`, etc.) → **EMPTY**. No pattern guessing, Hunter/Apollo, LinkedIn, or invented emails.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Domain | Outcome |
|----------------|------|--------|---------|
| 13028335946 | Mauricio Rosillo | bancolombia.com.co | EMPTY — 6-K contact phone-only; generic `asamblea@`; POA signature without email |
| 13028350024 | Monica Salazar | idbinvest.org | EMPTY — no EDGAR name+email; Merqueo exhibits IDB Invest lender only |
| 13028359161 | Natalia Medianero Aldaba | sumacapital.com | EMPTY — zero EDGAR name hits; Suma listed in AMG EX-21 without people |
| 13028349662 | Sergio Díaz | idbinvest.org | EMPTY — IDB board rep name collision; IDB treasury/IR generics only |
| 13028349457 | Sina Dorner-Müller | apg.nl | EMPTY — zero EDGAR hits for name or `@apg.nl` |

## Deliverables

- `results.csv` — one row per seed seat  
- `stamp-list.json` — empty (no FOUND)  
- `evidence/` — `edgar_search.json`, `negative-excerpts.md`, `url-index.md`, filing snapshots  
- **No Monday writes**
