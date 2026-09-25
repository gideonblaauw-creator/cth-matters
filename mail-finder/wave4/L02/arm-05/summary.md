# Wave4 L02 Arm 05 — First-party team/people mailto scorecard

**Loop:** Mail Finder Wave4 L02 Arm 05 (firm-site team/people mailto discovery)  
**Seats processed:** 4  
**Run date:** 2026-09-25

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 4 |

## Method

Public HTTP crawl of each seat’s Monday **Website** domain plus standard team paths (`/team`, `/people`, `/about`, `/our-team`, `/leadership`, `/about-us`, `/equipo`) and saved page source. **FOUND** only when display name and a non-generic `person@firm` `mailto:` co-occur on the same first-party page/block. Generics (`info@`, `hello@`, `contacto@`, `support@`, etc.) → **EMPTY**.

## Per-seat notes

| Name | Domain | Outcome |
|------|--------|---------|
| Tiffany Chen | carbonequity.com | Team page live; zero mailto links; contact not on /team/ |
| Alfredo Neila | plasticrepair.eu | Name in news copy; only `info@` generic mailto |
| Lucía Gaitán Sánchez | gawacapital.com | `/our-team` profile + LinkedIn; only `info@` generic |
| Mau Messina | sf500.vc | Team profile + LinkedIn; `contacto@` is site-wide generic |

## Deliverables

- `input.csv` — source batch (4 seats)
- `results.csv` — all seats
- `stamp-list.json` — no FOUND emails (`[]`)
- `evidence/` — HTML snapshots for audited pages
- `README.md` — arm spec

**Monday:** no writes (workbench review only).
