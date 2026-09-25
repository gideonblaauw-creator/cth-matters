# Mail Finder — Wave4 Loop L01 Arm 08

Domain hygiene and Website backfill for **Potential Investors** seats only.

## Input

- `input.csv` — Monday export (`Monday_item_id`, `Name`, `Contact_name`, `Firm`, `Kind`, `Priority`, `Status`, `Website`, `Domain`, `LinkedIn`)

## Method (per seat)

1. **Blank Website** — resolve live investment-entity homepage via public web search (firm + contact). Prefer official firm site over LinkedIn or personal blogs.
2. **Filled Website** — HTTP-check: flag parked pages, NXDOMAIN, wrong entity, or redirects to a different live firm domain.
3. **Propose** corrected `https://…` when blank, wrong, or parked; sniff-test noisy inferences before proposing.
4. **Email (opportunistic)** — record **FOUND** only when a first-party team/people page shows **name + person@firm mailto** co-occurrence. Generics (`info@`, `hello@`, `team@`, `IR@`, regional `enquiries@`) are **not** FOUND.
5. **Never** invent emails, pattern+SMTP, Hunter/Apollo, or LinkedIn scrape. Name+domain may seed search only.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | All seats with hygiene status, URLs checked, optional FOUND email |
| `website-corrections.json` | Monday Website updates (blank/wrong/parked only) |
| `stamp-list.json` | FOUND emails for workbench Monday stamps |
| `summary.md` | Scorecard |
| `evidence/` | Excerpts for any FOUND row |

## Status values (`results.csv`)

- `WEBSITE_OK` — current (or canonical www) URL matches live investment entity
- `WEBSITE_CORRECTED` — propose new homepage URL in `Proposed_Website`
- `WEBSITE_MAPPED` — blank Website filled from search
- `DOMAIN_UNRESOLVED` — no verified live entity homepage
- `FOUND` — person-attributed email on first-party page
- `EMPTY` — reserved; not used when website is resolved but email absent (use `WEBSITE_OK` / `WEBSITE_CORRECTED` instead)

## Run metadata

- Processed: 2026-09-25 (UTC)
- Repo path: `mail-finder/wave4/L01/arm-08/` (exclusive; do not edit other arms or Monday)
