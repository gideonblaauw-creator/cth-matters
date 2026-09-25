# Mail Finder — Wave4 / L04 / Arm 04

**Arm:** SEC EDGAR exhibits, Form D, and filing **signature blocks** (preserve published local-part spelling).  
**Write path:** `mail-finder/wave4/L04/arm-04/` only.

## Inputs

- `input.csv` — 5 seats exported from Monday (website column pre-filled).

## Method (hard rules)

1. Query **SEC EDGAR full-text** (`efts.sec.gov/LATEST/search-index`) and pull primary documents / exhibits (Form D, 6-K, DSTRBRPT, EX-10 loan agreements, EX-24 POA, etc.).
2. Disambiguate using **firm / domain** and filing entity (e.g. Bancolombia CIK 1071371, IDB CIK 311670).
3. **FOUND** only when the target person’s published name and a **non-generic** person `@firm` email appear together in the same public filing with citation-grade excerpt + stable URL.
4. **Generics** (`info@`, `asamblea@`, treasury/IR, investor relations) → **EMPTY**.
5. **Forbidden:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator, paid/authenticated sources, Monday API writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Full attribution row per seat (`Status`, non-blank `Checked_URLs`) |
| `stamp-list.json` | FOUND seats only (Monday workbench import) |
| `summary.md` | Batch scorecard |
| `evidence/` | EDGAR search JSON, URL index, negative excerpts, filing snapshots |

## Re-run (discovery)

```bash
UA='MailFinderResearch/1.0 (cth-matters; wave4-L04-arm04) contact@example.com'
curl -s -A "$UA" 'https://efts.sec.gov/LATEST/search-index?q=%22Mauricio%20Rosillo%22'
```

See `evidence/url-index.md` for per-seat filing URLs archived in this run.

## Result (2026-09-25)

**0 FOUND / 5 EMPTY** — see `summary.md`.
