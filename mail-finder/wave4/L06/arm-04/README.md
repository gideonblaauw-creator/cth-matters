# Mail Finder — Wave4 / L06 / Arm 04

**Focus:** Public **press releases**, **podcast/show notes**, **conference/speaker pages**, and reputable **media pages** — require **target name + personal email or `mailto:`** co-occurring on the **same page** (exact published spelling).

**Write path:** `mail-finder/wave4/L06/arm-04/` only. **No Monday API writes** from this arm.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. Discover **first-party or publisher-controlled** press, newsroom, speaker, and podcast pages (plus ecosystem conference listings when they cite the seat).
2. **FOUND** when the contact **display name** and a **non-generic** `person@domain` (or `mailto:`) appear together on one page; capture excerpt + URL.
3. **Generics** (`press@`, `info@`, `hello@`, `team@`, `contact@`, `bookings@`, `impact@`, etc.) → **EMPTY**.
4. Do **not** use an email attributed to a **different person** on the same page (e.g. media contact for another executive) when researching a named person or unrelated firm seat.
5. Contact forms, social handles, and role inboxes without person attribution → **EMPTY**.

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, email pattern guessing, SMTP verification, invented addresses, paid/authenticated sources, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Every seed row once; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND rows only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | Research notes, fetched HTML, FOUND excerpts |

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l06-arm04-b90f`
