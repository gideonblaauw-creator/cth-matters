# Mail Finder — Wave4 / L05 / Arm 04

**Focus:** Public **impact reports**, **LP materials**, **annual reports**, and comparable **PDFs** — require **name + person@firm email** in the **same PDF** (exact published spelling). Each PDF is the citation unit.

**Write path:** `mail-finder/wave4/L05/arm-04/` only. **No Monday API writes** from this arm.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. **First-party PDF discovery** — annual/impact/LP pages, `/wp-content/uploads/`, sitemaps, press/IR PDF attachments.
2. **Comparable public PDFs** — fund Form D only when published as downloadable PDF/XML with email fields; statutory filings (e.g. UK LLP accounts) when relevant.
3. **Third-party conference / ecosystem PDFs** when they clearly reference the seat’s fund and person.
4. **Extract text** — confirm name and mailbox co-occur in the same PDF block (page/heading when possible).
5. **Generic mailboxes** (`info@`, `hello@`, `investors@`, `ab@`, role-only) → **EMPTY**.
6. **Name without email** or **email without target name** in the same PDF → **EMPTY**.

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, email pattern guessing, SMTP verification, invented addresses, paid/authenticated sources, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Every seed row once; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND rows only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | URL index, negative excerpts, optional FOUND snippets |

## FOUND gate

Record email only when the **same public PDF** attributes a **person@firm** address to **that named person** (not a firm-wide contact block elsewhere in the document).

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l05-arm04-21c3`
