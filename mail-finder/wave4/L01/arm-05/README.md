# Mail Finder — Wave4 Loop L01 Arm05

Domain hygiene and **Website** backfill for **Potential Investors** seats (Monday board input).

## Input

- Source CSV: `uploads/wave4-l01-arm05.csv` (columns: Monday_item_id, Name, Contact_name, Firm, Kind, Priority, Status, Website, Domain, LinkedIn).
- This arm processed **19** seats from the attached batch.

## Method (primary)

For each seat:

1. **Blank Website** — resolve the live investment-entity homepage via public web search (firm + contact). Prefer official firm sites over LinkedIn or personal blogs.
2. **Filled Website** — HTTP-check for NXDOMAIN, parking (`/lander`, registrar parking), wrong entity, or redirect to a different live firm domain.
3. **Propose** canonical `https://…` when blank, wrong, parked, or when a clearer entity homepage exists. Sniff-test noisy inferences before proposing.
4. **Opportunistic email** — only when a first-party team/people page shows **name + person@firm** `mailto` co-occurrence. Generics (`info@`, `hello@`, `team@`) do **not** qualify as FOUND.
5. **Never** invent emails, pattern-guess, SMTP-verify, or use Hunter/Apollo/LinkedIn scrape. LinkedIn URLs in input are context only.

## Output artifacts

| File | Purpose |
| --- | --- |
| `results.csv` | One row per seat with status, websites, notes, checked URLs |
| `website-corrections.json` | Monday Website patch list (blank/wrong/parked) |
| `stamp-list.json` | FOUND emails only (may be `[]`) |
| `summary.md` | Scorecard counts |
| `evidence/` | Short excerpts for any FOUND (empty when none) |

## Result statuses

| Status | Meaning |
| --- | --- |
| `WEBSITE_OK` | Current URL live and matches the investment entity (or acceptable employer site noted) |
| `WEBSITE_CORRECTED` | Replaced blank/wrong/parked/NXDOMAIN URL |
| `WEBSITE_MAPPED` | Live redirect or canonical URL on a different hostname (e.g. rebrand) |
| `DOMAIN_UNRESOLVED` | Could not establish a live firm homepage |
| `FOUND` | Person email with first-party co-occurrence cite |
| `EMPTY` | No website and no resolution (none in this arm — all rows had Website values) |

## Regenerate

```bash
python3 mail-finder/wave4/L01/arm-05/build_results.py
```
