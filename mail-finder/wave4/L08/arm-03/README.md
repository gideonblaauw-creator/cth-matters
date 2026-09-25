# Mail Finder — Wave4 / L08 / Arm 03

**Focus:** One targeted **Wayback CDX** check per seat on the firm’s **/team**, **/about**, or **/people** path (or equivalent exact path).

## Inputs

- `input.csv` — 5 seats (Monday export).

## Method (`Wayback_CDX_team_about_people`)

1. Eligible seats: **EMPTY** seeds with a non-blank firm **website** (all five in this batch).
2. Choose **one** path per domain among `/team`, `/about`, `/people` (or locale equivalent, e.g. `/nosotros` for Bavaria).
3. Run **one** CDX query, e.g.  
   `https://web.archive.org/cdx/search/cdx?url={domain}{path}&output=json&filter=statuscode:200&limit=15`
4. If CDX returns captures, fetch **at most one** representative archived HTML snapshot from that CDX result and search for **target name** + **person@firm** / `mailto:` on the **same page**.
5. **FOUND** only when both co-occur on that snapshot; record timestamp URL and excerpt in `stamp-list.json` + `evidence/`.
6. **EMPTY** when CDX is empty, or archived page lacks name+personal email together (including generic-only or name-only pages).
7. **Forbidden:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn/Sales Navigator scraping, **broad** Wayback crawling, authenticated sources, Monday writes.

## CDX paths used (this run)

| Seat | CDX `url=` parameter |
|------|------------------------|
| Hyatt | `hyatt.com/about` |
| BioSingularity | `biosingularity.world/team` |
| Colaborativo | `colaborativo.io/about` |
| Telefónica (Wayra) | `telefonica.com/en/about-us` |
| Bavaria | `bavaria.co/nosotros` |

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, non-blank `Checked_URLs`, optional `Email` when FOUND |
| `summary.md` | Scorecard |
| `stamp-list.json` | FOUND seats only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `evidence/` | CDX JSON, snapshot HTML, negative excerpts |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L08-arm03) contact@example.com'
EV=mail-finder/wave4/L08/arm-03/evidence
curl -s -A "$UA" -o "$EV/cdx-telefonica-about-us.json" \
  'https://web.archive.org/cdx/search/cdx?url=telefonica.com/en/about-us&output=json&filter=statuscode:200&limit=15'
curl -sL -A "$UA" -o "$EV/telefonica-about-us-20221006014248.html" \
  'https://web.archive.org/web/20221006014248id_/https://www.telefonica.com/en/about-us/'
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L08/arm-03/`.
