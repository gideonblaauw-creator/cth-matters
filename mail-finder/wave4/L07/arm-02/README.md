# Mail Finder — Wave4 / L07 / Arm 02

**Exclusive path:** `mail-finder/wave4/L07/arm-02/`  
**Lane:** Lane B (CTH Matters)  
**Focus:** Curated, openly accessible **investor directories** (Mercury-class): structured public listings with direct contact fields — no login, subscription, paywall, or bulk contact-data brokers.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (`curated_public_investor_directory;Mercury_class_DB`)

1. Search **Mercury Investor Database** (index + full `investor-database/sitemap.xml` slug pass).
2. Search **Gaebler.com Venture Capital Database** firm/VC profile pages (VentureDeal-sourced public tables).
3. Search **Startuplinks** LATAM institution profiles where applicable.
4. **FOUND** when the directory record shows **exact target name** + **exact personal `person@firm` email** together (visible block or citation-grade schema on the same URL).
5. **EMPTY** when directories list names only, social links, firm-only rows, or **generic** mailboxes (`info@`, `contact@`, `post@`) without person co-attribution on the same record.
6. **Excluded:** Hunter, Apollo, RocketReach, ZoomInfo, Lusha, Private Equity List subscription emails, LinkedIn/Sales Navigator scraping, SMTP verification, pattern guessing, invented emails, Monday API writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; non-blank `Checked_URLs`; `Status` ∈ FOUND \| EMPTY \| UNCERTAIN |
| `stamp-list.json` | FOUND seats only |
| `summary.md` | Scorecard |
| `evidence/` | FOUND excerpts + negative directory notes + URL index |

## Result (this run)

**1 FOUND / 4 EMPTY** — see `summary.md`.

## Re-run

```bash
UA='MailFinderResearch/1.0 (cth-matters; L07-arm02) contact@example.com'
EV=mail-finder/wave4/L07/arm-02/evidence
curl -sL -A "$UA" -o "$EV/startuplinks_fundacion_bd.html" \
  'https://www.startuplinks.world/instituciones-de-inversion/fundacion-bolivar-davivienda'
curl -sL -A "$UA" -o "$EV/mercury_idb_sitemap.xml" \
  'https://mercury.com/investor-database/sitemap.xml'
```

## Scope

Write **only** under `mail-finder/wave4/L07/arm-02/`.
