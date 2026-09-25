# Mail Finder — Wave4 / L06 / Arm 08

**Focus:** Public **press**, **podcast/show notes**, **conference**, and **speaker** pages where a named person and a visible personal email or `mailto:` co-occur on the **same page**.

## Input

- `input.csv` — 5 seats (Monday export: `Monday_item_id`, name, firm, website, priority).

## Method (per seat)

1. Discover publisher-controlled pages: firm press/news, syndicated media quoting the person, podcast episode listings, conference speaker rosters, speaker-bureau profiles (when they publish a direct mailbox — not agency-only contact forms).
2. Fetch HTML (or transcript/show-notes when embedded in HTML) and inspect for `mailto:` and plain-text `@firm` addresses on the same document as the seat name.
3. **FOUND** only with citation-grade **name + exact non-generic person@firm** co-occurrence.
4. **Generics** (`press@`, `info@`, `hello@`, `team@`, `support@`, `ventures@`, `tech@`, `contact@`, `bookings@`, publisher/podcast support inboxes, speaker-agency mailboxes) → **EMPTY**.
5. **Prohibited:** Hunter/Apollo, LinkedIn/Sales Navigator scraping, pattern guessing, SMTP verification, invented emails, paid/authenticated sources, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`); non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only — `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | HTML snapshots and negative excerpt notes |

## Scope

Write **only** under `mail-finder/wave4/L06/arm-08/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l06-arm08-4971`
- Result: **0 FOUND / 5 EMPTY**
