# Mail Finder — Wave4 / L07 / Arm 03

**Focus:** **Curated, openly accessible investor directories** (Mercury-class): public listings that publish direct contact details without login, subscription, or paywall.

## Input

`input.csv` — 5 firm-level Potential Investors seats (Monday export).

## Method (`curated_public_investor_directory`)

Primary reference: [Mercury Investor Database](https://mercury.com/investor-database) (free profile pages with name + contact email when listed).

Also searched comparable public directory surfaces where the firm appears:

- Mercury sitemap + full profile scan (`mercury.com/investor-database/sitemap.xml`)
- [OpenVC](https://www.openvc.app/) fund profiles
- [Private Equity International](https://www.privateequityinternational.com/institution-profiles/) institution profiles
- [The GIIN](https://thegiin.org/) member pages
- [Private Equity List](https://privateequitylist.com/) (documented; team emails are paid — excluded as broker)

**FOUND gate:** exact target person name and exact `person@firm` email on the **same** directory record/page, with citation-grade excerpt. Firm-only generics (`info@`, `contact@`, `proparco@`) → **EMPTY**. Paywalled or login-only email fields → **EMPTY** (not Mercury-class for that field).

**Forbidden:** Hunter, Apollo, RocketReach, ZoomInfo, Lusha, paid databases, LinkedIn/Sales Navigator scraping, SMTP verification, pattern guessing, invented emails, Monday API writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND seats only |
| `summary.md` | Scorecard |
| `evidence/` | Snapshots, URL index, negative excerpts |

## Result (this run)

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Re-run notes

```bash
UA='MailFinderResearch/1.0 (cth-matters; L07-arm03) contact@example.com'
EV=mail-finder/wave4/L07/arm-03/evidence
curl -sL -A "$UA" -o "$EV/mercury_investor_sitemap.xml" \
  https://mercury.com/investor-database/sitemap.xml
curl -sL -A "$UA" -o "$EV/mercury_shruti_gandhi.html" \
  https://mercury.com/investor-database/shruti-gandhi
```

## Scope

Write **only** under `mail-finder/wave4/L07/arm-03/`.

Protocol: `mail-finder/protocol/Mail-Finder-Workbench-Strategy.md`.
