# Mail Finder — Wave4 / L01 / Arm 07

**Focus:** Domain hygiene + website backfill (Potential Investors only).

## Method

1. **Blank Website** — Public web search on firm + contact; prefer official investment-entity homepage over LinkedIn or personal sites.
2. **Filled Website** — HTTP-check for NXDOMAIN, parking (GoDaddy for-sale landers), wrong entity (personal name → unrelated corp), or redirects to a different live firm domain.
3. **Proposals** — Suggest corrected `https://…` when blank, wrong, or parked; sanity-check inferences before writing to `results.csv`.
4. **Opportunistic email** — Only when a **first-party** team/people page shows **display name + person@firm `mailto:`** on the same page. Generics (`info@`, `hello@`, `team@`, `ventures@`, grievance inboxes) are **not** FOUND.
5. **Prohibited** — No invented emails, pattern+SMTP, Hunter/Apollo, LinkedIn scrape. Name+domain may seed search only.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat website status, URLs checked, optional FOUND email |
| `website-corrections.json` | Corrections for blank/wrong/parked only |
| `stamp-list.json` | FOUND emails for Monday workbench stamping |
| `summary.md` | Scorecard |
| `evidence/` | Short excerpts for FOUND rows |
| `input.csv` | Source Monday export for this arm |

## Status values

- `WEBSITE_OK` — Current URL is the live investment entity (or acceptable canonical).
- `WEBSITE_CORRECTED` — Wrong/generic/parked; `Proposed_Website` set.
- `WEBSITE_MAPPED` — Parent URL valid; mapped to specific fund/ventures subsite.
- `DOMAIN_UNRESOLVED` — Could not verify a live entity homepage.
- `FOUND` — Citation-grade person email on first-party page.
- `EMPTY` — Reserved; not used when a website status applies.

## Scope guardrails

- Write **only** under `mail-finder/wave4/L01/arm-07/`.
- Do **not** modify other arms or Monday.
