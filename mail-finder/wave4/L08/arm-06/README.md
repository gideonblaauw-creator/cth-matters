# Mail Finder — Wave4 / L08 / Arm 06

**Focus:** **Wayback CDX** on firm **`/team`**, **`/about`**, or **`/people`** for promising EMPTY seats with a non-blank firm website.

**Write path:** `mail-finder/wave4/L08/arm-06/` only. **No Monday API writes.**

## Input

- `input.csv` — 5 seats (Monday export).

## Method (`Wayback_CDX_team_about_people`)

1. Require a non-blank **firm website** (all five seats eligible).
2. Pick one path: first live **200** among `/team`, `/about`, `/people` on the firm domain (else default `/team`).
3. Run **at most one CDX API query** per seat scoped to that path (`domain/team` and `www.domain/team` in the same request).
4. Fetch archived snapshots returned by CDX (newest first) until **FOUND** or exhausted.
5. **FOUND** only when archived HTML shows the **target name** and an exact **person@firm** mailto/text on the **same** page.
6. **EMPTY** for generics (`info@`, `hello@`), name without email, email without name, missing captures, or CDX-only metadata.

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, SMTP verification, pattern guessing, invented emails, broad Wayback crawling beyond the single path CDX pass, authenticated sources, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | CDX log, URL index, negative excerpts, optional HTML snapshots |

## Re-run (2026-09-25)

```bash
UA='Mozilla/5.0 (X11; Linux x86_64) MailFinderResearch/1.0 (cth-matters; L08-arm06)'
curl -sL -A "$UA" 'https://web.archive.org/cdx/search/cdx?output=json&filter=statuscode:200&limit=15&url=flybridge.com/team&url=www.flybridge.com/team'
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.
