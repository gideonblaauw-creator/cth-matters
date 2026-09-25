# Mail Finder — Wave4 / L10 / Arm 07

**Focus:** Public **CNPJ** (Brazilian registry, when the seat maps to a BR entity), **FINRA/IAPD** Form ADV PDFs, **Canadian securities** (**BCSC** document search), **SEC EDGAR/EFTS**, **DocuSign** references in filed agreements, and **ethics/compliance PDFs** — require **display name + exact person@firm** on the **same public page/PDF**.

**Write path:** `mail-finder/wave4/L10/arm-07/` only. **No Monday API writes** from this arm.

## Input

- `input.csv` — 5 seats (Monday export). This batch has **blank `contact_name`** on all rows (firm-level items).

## Method (per seat)

1. **CNPJ** — public Brazilian CNPJ APIs / registry when jurisdiction suggests a BR vehicle (negative for this batch’s primary domains).
2. **IAPD** — `api.adviserinfo.sec.gov` firm search; download Form ADV / brochure PDFs from `reports.adviserinfo.sec.gov`; extract text for name + `@domain` co-occurrence.
3. **BCSC** — `https://www.bcsc.bc.ca/search-results?query=…` for exempt-market / issuer documents when geo suggests Canada.
4. **SEC EDGAR / EFTS** — full-text index (`efts.sec.gov`) for firm name, `@domain`, Form D signature blocks, ethics exhibits.
5. **DocuSign** — EFTS search for DocuSign + firm (execution clauses only count if a **named person** and **person@firm** appear in the same citation block).
6. **Ethics/compliance PDFs** — first-party ethics charters, ICM policies, code-of-conduct PDFs linked from issuer sites.

## FOUND gate

Record email only when the **same public regulatory or compliance document** attributes a **person@firm** address to **that named person**. Generics (`info@`, `proparco@`, `complaints@`, `acumen-america@`, department inboxes) → **EMPTY**. Name without email or email without name → **EMPTY**. Ambiguous attribution → **UNCERTAIN**.

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, email pattern guessing, SMTP verification, invented addresses, paid/authenticated contact brokers, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seed; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND rows only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | URL index, negative excerpts, IAPD/PDF snapshots |

## Result (this run)

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Re-run (examples)

```bash
UA='CTH Matters MailFinder mailfinder@cth-matters.io'
EV=mail-finder/wave4/L10/arm-07/evidence
curl -sS -A "$UA" "https://efts.sec.gov/LATEST/search-index?q=%22%40proparco.fr%22" -o "$EV/efts_at_proparco.json"
curl -sS -A "$UA" -o "$EV/acumen_adv_174380.pdf" "https://reports.adviserinfo.sec.gov/reports/ADV/174380/PDF/174380.pdf"
curl -sS -A "$UA" -L -o "$EV/proparco_icm_policy.pdf" "https://proparco.fr/sites/proparco/files/2026-04/2026_icm-policy.pdf"
```

## Scope

Write **only** under `mail-finder/wave4/L10/arm-07/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l10-arm07-6080`
