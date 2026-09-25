# Mail Finder — Wave 4, Loop L01, Arm 02

Domain hygiene and website backfill for **Potential Investors** seats (Wave 4 L01 Arm 02 input).

## Method

1. **Blank website** — Public web search using firm name + contact; prefer official investment-entity homepage over LinkedIn or personal blogs.
2. **Filled website** — HTTP-check each URL. Flag parked domains (e.g. GoDaddy landers), NXDOMAIN, wrong entity (personal name tied to unrelated company), or redirects to a different live firm domain.
3. **Corrections** — Propose a canonical `https://…` when blank, wrong, or parked. Sniff-test inferences (fetch homepage / team page) before recording.
4. **Email (opportunistic only)** — Record `FOUND` only when a first-party team/people page shows the contact name and a person-specific `mailto:` on the same page. Generics (`info@`, `hello@`, `team@`, etc.) are **not** FOUND.
5. **Prohibited** — No invented emails, no pattern+SMTP, no Hunter/Apollo, no LinkedIn scraping. Name + domain may seed public search only.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat with website status and check log |
| `website-corrections.json` | Corrected URLs (blank / wrong / parked only) |
| `stamp-list.json` | Person-attributed emails for Monday workbench stamping |
| `summary.md` | Scorecard |
| `evidence/` | Short excerpts when Status is `FOUND` |

## Status values

- `WEBSITE_OK` — Current website is the live investment (or employer) entity homepage.
- `WEBSITE_CORRECTED` — Monday URL was blank, wrong, parked, or non-resolving; proposed URL verified.
- `WEBSITE_MAPPED` — Same entity; canonical URL differs (redirect / `www` / path normalization only).
- `DOMAIN_UNRESOLVED` — No reliable firm homepage found after search.
- `FOUND` — Person-specific email on first-party page (replaces website status when applicable).
- `EMPTY` — Reserved; not used when a website verdict applies.
