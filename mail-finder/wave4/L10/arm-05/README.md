# Mail Finder — Wave 4 / L10 / Arm 05

**Focus:** Public **Brazilian CNPJ**, **IAPD**, **Canadian securities** (incl. **BCSC**), **DocuSign**, and **ethics/compliance PDFs** — citation-grade **name + person@firm** on the same public page/PDF.  
**Write path:** `mail-finder/wave4/L10/arm-05/` only. **No Monday API writes** from this arm.

## Input

`input.csv` — 5 seats (Monday export): `item_id`, `name`, `contact_name`, `firm`, `website`, …

## Method (per seat)

1. **CNPJ** — public registry/consulta listings; require seat name + non-generic `person@` on the same published record/PDF (reject unrelated homonym entities).
2. **IAPD** — FINRA/SEC adviser search + Form ADV Part 2A PDF text when retrievable; individual CRD only when it maps to the seat person at the seat firm.
3. **Canadian securities / BCSC** — BCSC document/search patterns; Form 45-106F1-class and offering-memorandum PDFs where relevant.
4. **DocuSign** — public signed ethics/compliance PDFs with certificate/audit trail showing name + mailbox.
5. **Ethics/compliance PDFs** — corporate codes of conduct, impact/governance PDFs on issuer or firm sites.

**FOUND** → record email + source URL in `results.csv` and `stamp-list.json`.  
**EMPTY** → generics-only, name without person mailbox, wrong-person registry hit, or parent-domain email that does not match the seat website domain.  
**UNCERTAIN** → ambiguous co-occurrence only.

## Prohibited

Hunter/Apollo, LinkedIn scrape, email pattern invention, SMTP verify, invented addresses, Monday writes, paid enrichment sources.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat FOUND/EMPTY/UNCERTAIN, Checked_URLs, notes |
| `stamp-list.json` | FOUND rows only (Monday workbench `email_mm7ffmz4`) |
| `summary.md` | Scorecard |
| `evidence/` | PDFs, registry JSON, negative excerpts |

## FOUND gate

Store email only when the **same public document** in the lanes above attributes a **non-generic `person@firm`** to **that named person** (seat website domain unless the document explicitly uses a verified affiliate domain on the same attributed block).

## Scope

Write **only** under `mail-finder/wave4/L10/arm-05/`. Do not modify other arms.

## Run metadata

- Branch: `cursor/mail-finder-l10-arm05-7ebc`
- Batch result: **0 FOUND** (5 EMPTY)
