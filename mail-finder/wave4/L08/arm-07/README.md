# Mail Finder — Wave4 / L08 / Arm 07

**Focus:** Targeted **Wayback Machine CDX** on a single **`/team`**, **`/about`**, or **`/people`** URL per seat (no broad domain crawl).

## Inputs

- `input.csv` — 5 seats (Monday export).

## Method (`Wayback_CDX_team_about_people`)

1. Eligible seats: **EMPTY** targets with a **non-blank firm website** (all five seeds qualify).
2. Run **at most one** CDX query per seat, scoped to one path (`/team` used for this batch — standard VC team page).
3. If CDX lists `statuscode:200` captures, open **one** snapshot and search archived HTML for the **exact target name** and a **person `@firm` mailto or plaintext email on the same page**.
4. **FOUND** only with citation-grade excerpt from that snapshot (timestamp URL recorded).
5. Name without email, email without name, generics, or CDX rows without snapshot body → **EMPTY**.
6. **Forbidden:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, broad Wayback crawling, authenticated sources, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, non-blank `Checked_URLs`, optional `Email` when FOUND |
| `summary.md` | Scorecard |
| `stamp-list.json` | FOUND seats only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `evidence/` | CDX JSON, Wayback HTML snapshots, URL index, negative excerpts |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L08-arm07) contact@example.com'
EV=mail-finder/wave4/L08/arm-07/evidence
curl -s -A "$UA" \
  'https://web.archive.org/cdx/search/cdx?url=simmacapital.com/team&output=json&limit=10&filter=statuscode:200&collapse=timestamp:8' \
  -o "$EV/cdx-simmacapital_com.json"
curl -sL -A "$UA" -o "$EV/wayback-simmacapital-team-20241012144330.html" \
  'https://web.archive.org/web/20241012144330/https://www.simmacapital.com/team/'
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L08/arm-07/`.
