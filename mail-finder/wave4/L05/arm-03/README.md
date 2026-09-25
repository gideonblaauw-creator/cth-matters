# Mail Finder — Wave4 / L05 / Arm 03

**Focus:** Public **impact reports**, **LP / offering PDFs**, **annual-report-style disclosures**, and comparable issuer/fund PDFs. **FOUND** only when the same PDF contains the target person’s printed name and an exact **person@firm** email binding that mailbox to that person.

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (per seat)

1. **First-party & fund PDF discovery** — DuckDuckGo `filetype:pdf`, firm `wp-content/uploads`, BMV/DFC/JICA-style LP summaries, impact newsletters.
2. **Text extraction** — `pypdf` on downloaded PDFs; verify name + non-generic mailbox on the **same** document.
3. **Regulatory adjunct** — IAPD Form ADV PDF when domain maps to a registered adviser (no employee emails when absent).
4. **Generics excluded** — `press@`, `investorrelations@`, PR-agency contacts, and third-party mailboxes not tied to the target name → **EMPTY**.

## Prohibited

Pattern guessing, SMTP verification, Hunter/Apollo, LinkedIn scrape, invented emails, paid/authenticated sources, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`), `Checked_URLs`, notes |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | PDF copies, excerpts, `url-index.md`, `negative-excerpts.md` |

## Scope

Write **only** under `mail-finder/wave4/L05/arm-03/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l05-arm03-b887`
