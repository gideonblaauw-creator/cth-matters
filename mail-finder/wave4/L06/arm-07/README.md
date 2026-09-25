# Mail Finder — Wave4 / L06 / Arm 07

**Focus:** Public **press releases**, **podcast/show notes**, **conference/speaker** pages where the target **name** and a **non-generic personal email** (or `mailto:` target) appear on the **same page**.

## Inputs

- `input.csv` — 5 seats (Monday export).

## Method (`press_releases;podcast_show_notes;speaker_pages;mailto_cooccurrence`)

1. Discover first-party or publisher-controlled pages (firm blogs, job/press posts, event/speaker bios, podcast landing pages).
2. Fetch rendered HTML and extract visible text plus `mailto:` links.
3. **FOUND** only when the seat person’s name and a **non-generic** person email co-occur on one URL (exact published local-part).
4. **Generics** (`info@`, `press@`, `contact@`, `hello@`, `team@`, `bookings@`, `webmaster@`, etc.) → **EMPTY**.
5. **Forbidden:** Hunter/Apollo, LinkedIn/Sales Navigator scraping, pattern guessing, SMTP verification, invented emails, paid/authenticated sources, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, non-blank `Checked_URLs`, optional `Email` when FOUND |
| `summary.md` | Scorecard |
| `stamp-list.json` | FOUND seats only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `evidence/` | HTML snapshots, URL index, negative/generic excerpts |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L06-arm07) contact@example.com'
EV=mail-finder/wave4/L06/arm-07/evidence
curl -sL -A "$UA" -o "$EV/13114431023-robert-weber-gnv-job.html" \
  'https://greatnorthventures.com/head-finance-fund-admin-vc-firm/'
curl -sL -A "$UA" -o "$EV/valor-press-sitemap.xml" \
  'https://valorcapitalgroup.com/valor-in-press-sitemap.xml'
```

## Result

**1 FOUND / 4 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L06/arm-07/`.
