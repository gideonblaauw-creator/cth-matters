# Mail Finder — Wave4 / L06 / Arm 02

**Exclusive path:** `mail-finder/wave4/L06/arm-02/`  
**Lane:** Lane B (CTH Matters)  
**Focus:** Public **press**, **podcast/show notes**, **event**, and **speaker** pages with visible personal email / `mailto` co-occurring with the target name.

## Inputs

- `input.csv` — 5 seats (Monday export).

## Method (`press_podcast_speaker;event_pages`)

1. Discover publisher-controlled speaker bios, summit agendas, podcast episode pages, and event/training rosters (first-party or reputable media).
2. Inspect rendered HTML or linked **speaker decks** when the event page links a single citation artifact.
3. **FOUND** when display name and exact **person** mailbox co-occur on the same public page/artifact; capture excerpt verbatim.
4. **Generics** (`info@`, `hello@`, `contacto@`, `atencioncliente@`, `press@`, etc.) → **EMPTY**.
5. **Forbidden:** Hunter/Apollo, LinkedIn/Sales Navigator scraping, pattern guessing, SMTP verification, invented emails, paid/authenticated sources, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status`; non-blank `Checked_URLs`; `Email` when FOUND |
| `stamp-list.json` | FOUND only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | URL index, negative excerpts, FOUND snippets |

## Re-run (2026-09-25)

```bash
UA='MailFinderResearch/1.0 (cth-matters; L06-arm02) contact@example.com'
EV=mail-finder/wave4/L06/arm-02/evidence
curl -sL -A "$UA" -o "$EV/unepfi_circular_webinar.html" \
  'https://www.unepfi.org/events/training/serie-de-webinars-sobre-financiamiento-de-economia-circular-2/'
curl -sL -A "$UA" -o "$EV/lucia_gaitan_unepfi_2022.pdf" \
  'https://www.unepfi.org/wordpress/wp-content/uploads/2022/08/Lucia-Gaitan-–-La-Economia-Circular-y-su-importancia-en-el-camino-de-transicion-hacia-el-Cero-Neto-en-Emisiones..pdf'
pdftotext "$EV/lucia_gaitan_unepfi_2022.pdf" - | grep -i gait
```

## Result

**1 FOUND / 4 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L06/arm-02/`.
