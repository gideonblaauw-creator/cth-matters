# Mail Finder — Wave4 / L03 / Arm 08

**Focus:** Regulatory and securities **PDF / filing text** for **name + person@firm** co-occurrence (published spelling).

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. **SEC EDGAR / EFTS** — full-text and indexed search; Form D, Form 4, 8-K exhibits, proxy/definitive materials where relevant.
2. **FINRA IAPD** — Form ADV brochures for adviser entities tied to the seat’s firm domain.
3. **BCSC** — document search portal (HTML) for Canadian exempt-distribution / 45-106F1-class filings when firm geo suggests.
4. **Signature blocks** — related-person tables in Form D XML; no email → cannot FOUND.
5. **Generics** (`info@`, `careers@`, `admin@`, IR/PR inboxes on unrelated issuer docs) → **EMPTY**, not UNCERTAIN.

## Prohibited

Hunter/Apollo, LinkedIn scrape, email pattern guessing, SMTP verify, invented addresses, **Monday writes**.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat Status, Checked_URLs, Notes |
| `stamp-list.json` | FOUND emails only (Monday workbench `email_mm7ffmz4`) |
| `summary.md` | Scorecard |
| `evidence/` | Excerpts for FOUND rows; this run includes negative audit notes |

## FOUND gate

Store email only when the **same public regulatory document** attributes a **person@firm** address to **that named person** (not a third-party issuer IR contact, not IAPD “do not list employee emails” boilerplate alone).

## Scope

Write **only** under `mail-finder/wave4/L03/arm-08/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l03-arm08-da2c`
