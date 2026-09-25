# Mail Finder — Wave4 / L09 / Arm 08

**Focus:** **Deferred high-yield URL follow-ups** — fetch URLs queued in **L01–L03 closeouts and evidence notes**, then **one same-domain expand** (team/contact/about or filing-history) per seat. Require **display name + non-generic `person@firm`** (or valid firm-seat attribution) on the **same page/document**.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (`wave4_L09_arm08_deferred_highyield_urls`)

1. Build per-seat queue from **L01** domain-hygiene URLs, **L02** team/mailto crawls, and **L03** regulatory/filing hints documented in prior arms (see `evidence/deferred-url-queue.md`).
2. Fetch each queued URL; expand once on the Monday **Website** domain (no broad crawl).
3. **FOUND** only after independent verification of **name + person@firm** co-occurrence (published spelling); capture `Source_URL` + excerpt.
4. **Generics** (`contact@`, `info@`, `press@`, `impact@`, etc.) → **EMPTY**.
5. Do not promote a **different person’s** mailbox (e.g. media contact on a firm bolt-on seat) unless the seat name matches.

## Prohibited

Hunter/Apollo, LinkedIn scrape, email pattern guessing, SMTP verification, invented emails, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Every seat once; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND rows only |
| `summary.md` | Scorecard |
| `evidence/` | URL index, deferred queue, excerpts |

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L09/arm-08/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l09-arm08-d312`
