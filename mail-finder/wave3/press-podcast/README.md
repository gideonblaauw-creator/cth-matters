# Mail Finder — Wave 3 / Arm 3 (press-podcast)

Exclusive path for **`press_mailto`** search-seed runs on the Wave 3 press/podcast seat list.

## Inputs

- `input.csv` — 12 seats exported from Monday (Wave 3 press/podcast cohort).

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status`, `Checked_URLs`, optional `Email` when FOUND |
| `summary.md` | Run scorecard and method notes |
| `stamp-list.json` | JSON array of FOUND seats only (for downstream stamping) |
| `evidence/` | Citation excerpts and URL index |

## Rules (hard)

1. **Search seeds only:** `"Full Name" "Firm" email`, `site:domain perspectives`, podcast show notes, public PDF footnotes.
2. **FOUND** requires public **name + person@firm** (or mailto anchor with name) on the same page/PDF.
3. **FORBIDDEN:** pattern guessing, SMTP verify, invented emails, Hunter/Apollo, Sales Nav / LinkedIn scrape, guest-form emails not published on web.
4. **Generics** (`info@`, `admin@`, `contact@`, team inboxes) → **EMPTY**.
5. **LinkedIn-only** contact path → **HOLD** or **EMPTY** (no scrape); this run recorded EMPTY where only LI appeared in show notes.
6. **No Monday writes** from this folder.

## Re-run search seeds (examples)

Use web search; fetch HTML/PDF; record every URL in `Checked_URLs`.

- `"Agustin De Luca" Lendable email site:lendable.io`
- `"Aidan Madigan-Curtis" eclipse podcast mailto`
- `"Bill Driegert" eclipse.capital podcast email`
- `"Burak Cendek" autotechvc podcast show notes email`
- `"Eduardo González" BBVA Spark email site:bbvaspark.com OR site:bbva.com`
- `"Edward Goldstein" i80 group mailto filetype:pdf`
- `"Greg Reichow" site:eclipse.capital blog email`
- `"Jacob Haar" CIM podcast mailto site:cim-llc.com`
- `"Jessica Diaz" idbinvest.org email filetype:pdf`
- `"Monica Salazar" idbinvest.org email`
- `"Mauricio Rosillo" bancolombia email site:bbvaspark.com` (also column bylines on legal press)
- `"Natalia Medianero" sumacapital email`

## 2026-09-25 result

0 FOUND / 12 EMPTY — see `summary.md`.
