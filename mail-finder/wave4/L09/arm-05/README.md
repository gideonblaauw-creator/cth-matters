# Mail Finder — Wave4 / L09 / Arm 05

**Focus:** **Deferred high-yield** follow-up from Wave4 **L01–L03 closeouts** and evidence notes (Potential Investors batch).

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (`wave4_L09_arm05_deferred_L01_L03`)

For each seat:

1. **L01 closeout** — use corrected/mapped canonical firm URL from `mail-finder/wave4/L01/arm-05/` (`website-corrections.json` / `results.csv`).
2. **L02 lane** — one targeted pass on first-party team/about paths on that domain (`/about-us`, `/about`, `/nosotros`, founder profile URLs from L01 notes). **FOUND** only for non-generic `person@firm` + seat display name on the **same page** (`mailto:` or visible text).
3. **L03 lane** — where closeouts tied the seat to a US fund vehicle (e.g. Atlantico Partners Form D family), run **EFTS** + inspect public Form D XML for name + `@domain` co-occurrence (signature-only blocks without email → **EMPTY**).
4. **Deferred high-yield** — if steps 2–3 are EMPTY, follow **leads only** documented in L01–L03 evidence (e.g. AWI member showcase PDF after Jambaar domain correction; public event contact blocks tied to the seat). Independently fetch and verify before **FOUND**.
5. Generics (`info@`, `contact@`, `hello@`, `press@`, etc.) and unsupported claims → **EMPTY** / **UNCERTAIN**.

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, pattern guessing, SMTP verification, invented emails, paid/authenticated sources, **Monday writes**, writes outside `mail-finder/wave4/L09/arm-05/`, broad site crawls beyond the paths above.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | HTML/PDF snapshots, excerpts, closeout lead index |

## Prior closeouts (read-only context)

- `mail-finder/wave4/L01/arm-05/` — website hygiene for this seat batch (tail rows)
- `mail-finder/wave4/L02/arm-05/` — team mailto lane spec (same wave family)
- `mail-finder/wave4/L03/arm-05/` — regulatory PDF lane spec; Atlantico Form D notes in `L03/arm-08/`

## Scope

Write **only** under `mail-finder/wave4/L09/arm-05/`.

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l09-arm05-ce1d`
