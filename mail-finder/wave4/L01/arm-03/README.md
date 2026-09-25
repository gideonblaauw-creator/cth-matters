# Mail Finder — Wave4 / L01 / Arm 03

**Domain hygiene + Website backfill** for the Potential Investors slice (input: `input.csv`).

## Rules (this arm)

1. **Website blank:** resolve live **investment-entity** homepage via public web search (firm + contact). Prefer official firm site over LinkedIn or personal blogs.
2. **Website filled:** HTTP-check; flag parked (`/lander`, GoDaddy for-sale), NXDOMAIN/404, wrong entity, or redirects to a different live firm domain.
3. **Proposals:** suggest canonical `https://…` when blank, wrong, or parked; sniff-test noisy domain inferences before proposing.
4. **Email (opportunistic):** record **FOUND** only when a first-party team/people page shows **display name + person@firm mailto** on the same page. Generics (`info@`, `hello@`, `team@`, `contact@`) are not FOUND.
5. **Forbidden:** invented emails, pattern+SMTP, Hunter/Apollo, LinkedIn scrape. LinkedIn URLs in CSV are context only.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat hygiene status + checked URLs |
| `website-corrections.json` | Monday Website stamp candidates (wrong/blank/parked) |
| `stamp-list.json` | FOUND emails only (Monday email column) |
| `summary.md` | Scorecard |
| `evidence/` | Excerpts for any FOUND (empty this run) |

## Status values (`results.csv`)

- **WEBSITE_OK** — Current URL live and correct for the investment entity (or documented operating affiliation).
- **WEBSITE_CORRECTED** — Live canonical URL differs from Monday value (redirect, www, or wrong parked domain replaced).
- **WEBSITE_MAPPED** — Monday domain alias redirects to a different live registrable domain (same entity).
- **DOMAIN_UNRESOLVED** — Cannot establish a crawlable investment-entity homepage.
- **FOUND** — Citation-grade personal email (none this arm).
- **EMPTY** — Not used as website outcome in this arm when a hygiene status applies.

Protocol reference: `mail-finder/protocol/Mail-Finder-Workbench-Strategy.md`.
