# Mail Finder — Wave 4 / L01 / Arm 06

**Scope:** Potential Investors board seats from `input.csv` (domain hygiene + website backfill).  
**Write path:** `mail-finder/wave4/L01/arm-06/` only (no Monday API writes).

## Method

1. **Blank Website** — Resolve the live investment-entity homepage via public web search (firm name + contact). Prefer official firm sites over LinkedIn or personal blogs.
2. **Filled Website** — HTTP-check (redirects, NXDOMAIN, parking, wrong corporate root vs. venture unit, wrong entity).
3. **Proposals** — Suggest canonical `https://…` when blank, wrong, parked, or non-resolving; sniff-test before proposing.
4. **Email (opportunistic)** — Record **FOUND** only when a first-party team/people page shows **name + person@firm `mailto`** co-occurrence. Generics (`info@`, `hello@`, `team@`, fund inboxes) are **not** FOUND.
5. **Prohibited** — No invented emails, pattern+SMTP, Hunter/Apollo, or LinkedIn scrape. Name+domain may seed public search only.

## Status values (`results.csv`)

| Status | Meaning |
|--------|---------|
| `WEBSITE_OK` | Current URL live and matches the investment entity (canonical `www`/path noted in Notes when applicable). |
| `WEBSITE_CORRECTED` | Monday URL wrong, parked, NXDOMAIN, or parent corporate root; `Proposed_Website` set. |
| `WEBSITE_MAPPED` | Website was blank; mapped to resolved firm homepage. |
| `DOMAIN_UNRESOLVED` | No live firm homepage verified after search + checks. |
| `FOUND` | Citation-grade personal email on first-party page. |
| `EMPTY` | Website hygiene complete; no personal email found. |

## Outputs

- `results.csv` — all seats
- `website-corrections.json` — corrections for blank/wrong/parked only
- `stamp-list.json` — FOUND emails for workbench Monday stamps
- `summary.md` — scorecard
- `evidence/` — excerpts for FOUND rows (empty if none)
