# Mail Finder Wave 2 — METHOD ARM: deferred high-yield URLs

## Scope
- Input seats: **4** (`input.csv` from board upload)
- Method: hinted URLs only, then **one** same-domain expand (team/people/about/contact + linked PDFs on inclimo.com)
- Excluded: Hunter/Apollo, LinkedIn scrape, pattern guessing, Monday writes

## Counts

| Status | Count |
|--------|------:|
| FOUND | 1 |
| HOLD | 1 |
| EMPTY | 2 |

## FOUND (stamp list only)

- **Fernando Casado Cañeque** — `fernando.casado@inclimo.com` — [Inclimo DFI PDF](https://inclimo.com/wp-content/uploads/2023/06/Datos-fundamentales-para-el-Inversor-DFI-v.f.pdf)

## HOLD

- **Nic Gorini** — spin.vc/team confirms role; contact path is LinkedIn-only (no public person@spin.vc on allowed crawl).

## EMPTY

- **Elvia Gomez** — acumen.org/team/elvia-gomez bio only; no person@acumen.org co-occurrence on hinted or team expand.
- **Miheer Chanrai** — climate.capital no longer exposes team pages; no name/email on live about/contact pages.

## Artifacts
- HTML/PDF snapshots: `html/`
- Monday stamp row: `found-for-monday.csv` (1 FOUND)
