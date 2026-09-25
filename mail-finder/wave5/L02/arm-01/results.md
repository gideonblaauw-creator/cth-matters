# Wave5 L02 arm-01 — first-party team / people mailto scorecard

**Run date:** 2026-09-25  
**Input:** 5 P2 seats (`input.csv`)  
**Method:** `wave5-L02-arm01-first-party-team` — public HTTP crawl of firm Website plus standard Team / About / People / Contact paths and firm-specific about pages; **FOUND** only when **Contact_name** and a non-generic **person `@Domain` mailto** co-occur on the same page or firm bio.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Contact_name | Domain | Outcome |
|----------------|--------------|--------|---------|
| 13028370683 | Bryony Parker | saviaventures.com | EMPTY — team roster on homepage; no personal mailto; privacy `contacto@` generic |
| 13028358405 | Camilo Arango | clicoh.com | EMPTY — no `@clicoh.com` in crawl; name not on site |
| 13100506379 | Camilo Kejner | angelventures.vc | EMPTY — `/team` LinkedIn only; `infocolombia@` generic sitewide |
| 13028336730 | Carlos Iván Vargas Perdomo | dibanka.co | EMPTY — name absent on sobre-dibanka / team paths |
| 13028371786 | Carolina Ocampo-Maya | epicangelnetwork.com | EMPTY — `/team` generic `info@` only; name not in HTML |

## Deliverables

| File | Purpose |
|------|---------|
| `input.csv` | Seed rows (5 seats) |
| `results.csv` | One row per seat with `Checked_URLs` |
| `stamp-list.json` | FOUND stamps only (empty this run) |
| `results.md` | This scorecard |
| `CLOSEOUT.md` | Run counts and notes |
| `evidence/` | HTML snapshots + negative excerpts |

**No Monday writes** from this folder.
