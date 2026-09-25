# Mail Finder — Wave4 / L07 / Arm 04

**Focus:** Curated, openly accessible **investor directories** (Mercury-class): structured public listings that publish investor names and contact emails. No login, paywall, or bulk contact-data brokers.

## Inputs

- `input.csv` — 5 seats (Monday export).

## Method (`curated_public_investor_directories;Mercury;Gaebler;Mindmaps`)

1. Search **Mercury Investor Database** (`mercury.com/investor-database`) using the public sitemap (295 investor profile URLs as of 2026-09-21) and text scan for seat names / firms.
2. Cross-check **Gaebler.com Venture Capital Database** search for firm names.
3. Check other Mercury-class firm/person tables when indexed (e.g. **Mindmaps** investor firm pages, **PEI** institution contact tables when public fields are unmasked).
4. **FOUND** only when the seat target’s **exact name** and an exact **person@firm** email appear on the **same** directory record, with a stable URL and citation-grade excerpt saved under `evidence/`.
5. Directory rows with only firm name, generic mailbox (`info@`, `contact@`), or social links → **EMPTY**. Masked/paywalled email placeholders → **EMPTY** (not UNCERTAIN unless directory access itself is unclear).
6. **Forbidden:** Hunter, Apollo, RocketReach, ZoomInfo, Lusha, paid databases, LinkedIn/Sales Navigator scraping, SMTP verification, pattern guessing, invented emails, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, non-blank `Checked_URLs`, optional `Email` when FOUND |
| `stamp-list.json` | FOUND seats only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | Sitemap, directory audit JSON, negative excerpts |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L07-arm04) contact@example.com'
EV=mail-finder/wave4/L07/arm-04/evidence
curl -sL -A "$UA" -o "$EV/mercury-investor-database-sitemap.xml" \
  'https://mercury.com/investor-database/sitemap.xml'
curl -sL -A "$UA" -o "$EV/mindmaps-574.html" \
  'https://mindmaps.ai-ecosystem.org/mind-map/firms/133638/'
```

## Result

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L07/arm-04/`.
