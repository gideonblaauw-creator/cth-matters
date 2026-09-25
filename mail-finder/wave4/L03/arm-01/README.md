# Mail Finder — Wave4 L03 Arm 01 (regulatory / securities PDF)

Lane B parking arm. **Exclusive write path:** this directory only.

## Input

- `input.csv` — 5 seats (Wave4 L03 batch `db01`).

## Method

Public-web discovery and PDF text search only:

- SEC EDGAR + EFTS (`efts.sec.gov`)
- Form D / Form D/A XML and submission `.txt`
- Public coalition/regulatory-style PDFs hosted on seat domains (e.g. AIC reports on amazoninvestor.org)
- Issuer annual report PDFs where relevant (Maersk)
- BCSC / FCA / Companies House **search** (no authenticated scrapers)

**Hard gate:** FOUND only when the same public PDF contains both the target person’s published name and an exact `person@firm` email. Generics (`info@`, `growth@`, `IR@`, `secretary@`, etc.) → EMPTY.

**Forbidden:** Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP verify, invented emails.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat status + non-blank `Checked_URLs` |
| `stamp-list.json` | Monday import (`email_mm7ffmz4`) — FOUND only |
| `summary.md` | Scorecard |
| `evidence/` | Negative / near-miss excerpts |
| `pdfs/` | Downloaded source PDFs (audit) |

## Result

**0 FOUND / 5 EMPTY** for this pass.

Do **not** write to Monday from this agent; hand `stamp-list.json` to the workbench when FOUND rows exist.
