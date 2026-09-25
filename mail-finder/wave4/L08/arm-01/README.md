# Mail Finder — Wave4 / L08 / Arm 01

**Focus:** **Wayback CDX** on firm **`/team`**, **`/about`**, or **`/people`** (one targeted lookup per seat).

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (`Wayback_CDX_team_about_people`)

1. For each **EMPTY** seat with a **non-blank firm website**, run **one** CDX query on the chosen team/about/people URL (wildcard suffix allowed for that path only).
2. If CDX returns HTTP **200** captures, fetch **one** snapshot and inspect HTML for **display name + exact personal `@domain` or `mailto:`** on the **same page**.
3. **FOUND** only with citation-grade co-occurrence on that snapshot (record timestamp URL + excerpt).
4. Generics, name-only, email-only, stale unrelated pages, and **CDX rows without body review** → **EMPTY**.
5. **Forbidden:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, broad Wayback crawling beyond the single path, authenticated sources, **Monday writes**.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | CDX JSON, Wayback HTML, URL index, negative excerpts |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L08-arm01)'
EV=mail-finder/wave4/L08/arm-01/evidence
curl -sS -A "$UA" "https://web.archive.org/cdx/search/cdx?url=congruentvc.com/team*&output=json&filter=statuscode:200&limit=10" -o "$EV/cdx-congruentvc-team.json"
curl -sS -A "$UA" -o "$EV/wayback-congruentvc-team.html" "https://web.archive.org/web/20231201224020/https://www.congruentvc.com/team"
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L08/arm-01/`.
