# Wave5 L02 Arm 05 — Team / people mailto scorecard

**Run date:** 2026-09-25  
**Input:** 5 P2 seats (`input.csv`)  
**Method:** `wave5_L02_arm05_team_mailto` — first-party Team / About / People / Contact (and firm bio) pages; FOUND requires exact `Contact_name` and personal `person@firm` mailto co-occurring on the same page or bio.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Contact_name | Firm / domain | Outcome |
|----------------|--------------|---------------|---------|
| 13080749061 | Federico Storani | Riverwood Capital / riverwoodcapital.com | EMPTY — bio + team; contact generics only |
| 13100506101 | Felix Klühr | HV Capital / hvcapital.com | EMPTY — profile confirmed; no mailto |
| 13028371748 | Fernando Lelo de Larrea H | rumbo.ventures | EMPTY — team + LinkedIn; no mailto |
| 13096680140 | Filipe Portugal | Canary / canary.com.br | EMPTY — team JSON + LinkedIn; no mailto |
| 13028371858 | Franck Nouyrigat | electis.com | EMPTY — /equipe + LinkedIn; contact `aide@` generic |

## Notes

- Generics (`info@`, `press@`, `aide@`, etc.) → **EMPTY** per lane rules.
- **No Monday writes** from this folder.
- Evidence: `evidence/` HTML snapshots, `excerpts.md`, `url-index.md`.
