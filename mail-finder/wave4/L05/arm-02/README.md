# Mail Finder — Wave4 L05 Arm 02

**Exclusive path:** `mail-finder/wave4/L05/arm-02/`  
**Lane:** Lane B (CTH Matters)  
**Input:** `input.csv` (5 P2 seats)

## Method

Public **impact reports, LP materials, annual reports**, and comparable first-party PDFs:

1. Discover PDFs via firm sites (WP media APIs, sitemaps), issuer annual reports (e.g. MongoDB ARS), and impact conferences (e.g. FLII report).
2. Text-extract each PDF (PyMuPDF) or regulatory HTML proxy; search for **target person name** and **`person@firm`** in the same artifact.
3. **FOUND** only when published name spelling and exact non-generic mailbox co-occur in that PDF—not firm-wide contact blocks.
4. **EMPTY** for generics (`info@`, `hello@`), name-only bios, email-only footers, or name hits on unrelated persons.
5. **Forbidden:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, paid/authenticated sources, Monday writes.

## Deliverables

| File | Description |
|------|-------------|
| `input.csv` | Seed rows (Monday export) |
| `results.csv` | One row per seat; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND-only stamps (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | PDF snapshots, negative excerpts, URL index |

## Outcome (this run)

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Re-run (User-Agent required)

```bash
UA='CTH-Matters-MailFinder contact@example.com'
EV=mail-finder/wave4/L05/arm-02/evidence
curl -sL -A "$UA" -o "$EV/flii2025_report.pdf" \
  'https://flii.org/wp-content/uploads/2025/04/FLII2025_Report_web.pdf'
curl -sL -A "$UA" -o "$EV/mongodb_ars_2026.htm" \
  'https://www.sec.gov/Archives/edgar/data/1441816/000162828026036431/ars.htm'
```

## Scope

Write **only** under `mail-finder/wave4/L05/arm-02/`.
