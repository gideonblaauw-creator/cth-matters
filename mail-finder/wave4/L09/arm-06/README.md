# Mail Finder — Wave4 / L09 / Arm 06

**Exclusive path:** `mail-finder/wave4/L09/arm-06/`  
**Lane:** Lane B (CTH Matters)  
**Focus:** **Deferred high-yield URL follow-ups** from Wave4 **L01–L03** closeouts and evidence notes (website corrections, firm-site empties, CNMV/regulatory deferrals, queued publisher PDFs and Mercury-class fund directories).

## Inputs

- `input.csv` — 5 seats (Monday export).

## Method (`deferred_highyield_URL_followups`)

1. Start from **L01** website map/correction URLs (correct entity before crawl).
2. Re-open **L02/L03 EMPTY** hints: CNMV gestora views, fund folio PDFs, press/speaker decks linked from event pages, curated fund directories (e.g. Everything Startups fund profiles).
3. **FOUND** only when the seat’s published name and an exact **non-generic personal email** co-occur on the **same public page or PDF artifact** (independent re-fetch; do not trust prior arms without excerpt).
4. **Generics** (`info@`, `contacto@`, `contacto.actyus@`, association `info@`, etc.) → **EMPTY**.
5. **Forbidden:** Hunter/Apollo, LinkedIn/Sales Navigator scraping, pattern guessing, SMTP verification, invented emails, paid contact brokers, broad crawl, **Monday writes**.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status`; non-blank `Checked_URLs`; `Email` when FOUND |
| `stamp-list.json` | FOUND only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | URL index, negative excerpts, FOUND excerpts, snapshots |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L09-arm06)'
EV=mail-finder/wave4/L09/arm-06/evidence
curl -sL -A "$UA" -o "$EV/everythingstartups_pachamama.html" \
  'https://www.everythingstartups.com/vc-funds/pachamama-ventures'
curl -sL -A "$UA" -o "$EV/lucia_unepfi.pdf" \
  'https://www.unepfi.org/wordpress/wp-content/uploads/2022/08/Lucia-Gaitan-–-La-Economia-Circular-y-su-importancia-en-el-camino-de-transicion-hacia-el-Cero-Neto-en-Emisiones..pdf'
python3 -c "from pypdf import PdfReader; r=PdfReader('$EV/lucia_unepfi.pdf'); print(''.join(p.extract_text() or '' for p in r.pages)[-400:])"
```

## Result

**2 FOUND / 3 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L09/arm-06/`.
