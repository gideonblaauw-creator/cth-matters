# Mail Finder — Wave4 / L08 / Arm 08

**Focus:** **Wayback CDX** — one targeted lookup per promising EMPTY seat with a firm website, limited to **`/team`**, **`/about`**, or **`/people`** (prefix on that path only).

## Input

- `input.csv` — 5 seats (Monday export).

## Method (`wave4_L08_arm08_wayback_cdx_team_about_people`)

1. Require a **non-blank firm website**; derive registrable domain.
2. Run **one** CDX API query: `url={domain}{path}` with `matchType=prefix`, `filter=statuscode:200`, `collapse=urlkey` (path default `/team`; `acumen.org` uses `/team` for staff permalinks).
3. From that single CDX response, pick the capture whose URL best matches the seat name (e.g. `…/team/eduardo-campos`), then fetch **one** Wayback `id_` snapshot.
4. **FOUND** only if the archived HTML shows the **target name** and a **non-generic** `person@firm` mailto or visible email on the same page/block.
5. **EMPTY** — no CDX captures, name absent, name without email, generic inboxes, or email without the target name.

## Prohibited

Pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, broad domain Wayback crawls (beyond the one path prefix query), authenticated sources, **Monday writes**, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status` = `FOUND` \| `EMPTY` \| `UNCERTAIN`; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only — `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | CDX JSON, Wayback HTML snapshots, audit notes |

## Re-run

```bash
cd mail-finder/wave4/L08/arm-08
python3 evidence/run_cdx.py
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L08/arm-08/`.
