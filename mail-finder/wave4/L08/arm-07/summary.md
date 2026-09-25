# Wave4 L08 Arm 07 — Wayback CDX on /team, /about, or /people

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`).  
**Method:** One targeted **Internet Archive CDX** lookup per seat on the firm **`/team`** path (firm website present on every seed row). When CDX returned captures, fetch **one** archived HTML snapshot and require **target name + exact person@firm email/mailto on the same page** for FOUND. CDX metadata alone is not evidence.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Domain | Outcome |
|----------------|------|--------|---------|
| 13028370003 | Daniel Blandón | simmacapital.com | EMPTY — team archive names Daniel; LinkedIn only, no `@simmacapital.com` |
| 13028358775 | Daniela Gómez Ziga | pegasuscap.com | EMPTY — CDX `/team` returned no captures |
| 13028359182 | Dennis Zaidi | checkmatecapital.net | EMPTY — “Dennis Zaidi (Dony)” on archived team; no mailto |
| 13096668277 | Diego Serebrisky | daluscapital.com | EMPTY — person absent from Dec 2024 `/team` snapshot; no firm person emails |
| 13028349815 | Dondi Hananto | circulatecapital.com | EMPTY — person absent from May 2023 `/team/` snapshot |

## Deliverables

- `results.csv`, `stamp-list.json`, `README.md`, `summary.md`, `evidence/` (CDX JSON, Wayback HTML, `url-index.md`, `negative-excerpts.md`)

**No Monday writes** from this folder.
