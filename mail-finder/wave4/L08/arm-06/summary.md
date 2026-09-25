# Wave4 L08 Arm 06 — Wayback CDX on /team, /about, or /people

**Run date:** 2026-09-25 (UTC)  
**Input:** 5 seats (`input.csv`)  
**Method:** One targeted Internet Archive **CDX** lookup per seat on the firm’s **`/team`** path (live path probe: first 200 among `/team`, `/about`, `/people`; all five firms resolved to `/team`). Review CDX `statuscode:200` snapshots for **target name** and **person@firm** mailto/text co-occurring on the **same** archived page. Generics, name-only, email-only, and CDX metadata alone → **EMPTY**.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm | Outcome |
|----------------|------|------|---------|
| 13028371786 | Carolina Ocampo-Maya | (Epic Angel Network) | EMPTY — archived /team generic `info@` only; name not in HTML |
| 13114411688 | Chip Hazard | Flybridge | EMPTY — name on 2015 /team; only `hello@flybridge.com` |
| 13100505949 | Christopher Gottschalk | Mouro Capital | EMPTY — “Chris Gottschalk” on /team; no person email |
| 13100511323 | Clete Brewer | NewRoad Capital Partners | EMPTY — name on /team card; no mailto |
| 13028358610 | Constantin Augier | (Climate Club) | EMPTY — no Wayback captures for /team |

## Artifacts

- `results.csv`, `stamp-list.json` (empty), `README.md`
- `evidence/cdx_analysis.json`, `evidence/url-index.md`, `evidence/negative-excerpts.md`, `evidence/snapshots/*.html`
