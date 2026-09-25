# Mail Finder — Wave4 L10 Arm 02

**Exclusive path:** `mail-finder/wave4/L10/arm-02/`  
**Lane:** Lane B (CTH Matters)  
**Input:** `input.csv` (5 P2 seats)

## Method

Public regulatory and compliance corpora only:

1. **Brazilian CNPJ** — public registry APIs/pages (e.g. `publica.cnpj.ws`) for fund entities tied to the seat.
2. **FINRA IAPD** — firm/individual search and Form ADV PDF text where the adviser maps to the seat domain.
3. **Canadian securities** — **BCSC** public document search (incl. exempt-market / 45-106F1-class patterns when applicable).
4. **SEC EDGAR EFTS** — Form D/A and full-text queries for name + `@firm` co-occurrence.
5. **DocuSign** — EDGAR full-text discovery for DocuSign-tagged filings referencing the seat’s firm (no public envelope PDFs with person emails found this run).
6. **Ethics / compliance PDFs** — issuer ESG/ethics manuals and first-party event PDFs (Shell E&C Manual, AIC COP materials, law-firm alert PDFs for Prosus deals).

**FOUND** only when **display name + personal `person@firm` email** appear on the **same public page or PDF**.  
**EMPTY** for generics, name-only, email-only, or third-party contacts on the same block.  
**UNCERTAIN** when attribution is ambiguous.

## Prohibited

Hunter/Apollo, LinkedIn scrape, email pattern guessing, SMTP verification, invented emails, paid contact brokers, Monday writes, writes outside this directory.

## Deliverables

| File | Description |
|------|-------------|
| `input.csv` | Seed rows |
| `results.csv` | One row per seat; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only |
| `summary.md` | Scorecard |
| `evidence/` | URL index + negative excerpts + downloaded PDFs/XML |

## Outcome (this run)

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Re-run (User-Agent)

```bash
UA='CTH-Matters-MailFinder/1.0 (wave4-L10-arm02; regulatory)'
EV=mail-finder/wave4/L10/arm-02/evidence
curl -s -A "$UA" 'https://publica.cnpj.ws/cnpj/32864313000184' -o "$EV/cnpj_ws_itau.json"
curl -sL -A "$UA" -o "$EV/leitmotif_adv.pdf" \
  'https://reports.adviserinfo.sec.gov/reports/ADV/329025/PDF/329025.pdf'
curl -sL -A "$UA" -o "$EV/shell_ethics_manual.pdf" \
  'https://www.shell.com/investors/environmental-social-and-governance/_jcr_content/root/main/section/simple_913716519/list_1995953506/list_item_copy.multi.stream/1653374782393/82914f4065a9cf72bfd7bef87df5c80bf3d596d4/shell-ethics-and-compliance-manual-march-2021.pdf'
```

## Scope

Write **only** under `mail-finder/wave4/L10/arm-02/`.
