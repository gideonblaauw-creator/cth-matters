# Wave5 L02 Arm 07 — Team / people mailto scorecard

**Loop:** Mail Finder Wave5 L02 Arm 07  
**Seats:** 5  
**Run date:** 2026-09-25

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 4 |
| UNCERTAIN | 1 |

## Per seat

| Monday_item_id | Contact_name | Firm | Outcome |
|----------------|--------------|------|---------|
| 13100503653 | J.P. Keating | proChain Ventures | EMPTY — no team roster or mailto on prochain.vc |
| 13028358308 | James Todd | Oikocredit | UNCERTAIN — Cloudflare blocks team/about HTML fetch |
| 13100511350 | Jason Sydow | next47 (Siemens) | EMPTY — absent from n47 team/sitemap; no mailto |
| 13028367050 | Jonathan Duarte | CrossBoundary | EMPTY — people bio; LinkedIn only |
| 13028393225 | Josep Oriol | Okavango Capital | EMPTY — team bio; generic contact only |

## Method

First-party Team / About / People / Contact pages and firm bios only. **FOUND** requires exact `Contact_name` and personal `person@firm` mailto on the same page (or qualifying bio). No Hunter/Apollo, LinkedIn scrape, pattern guess, or Monday writes.

## Deliverables

| File | Purpose |
|------|---------|
| `input.csv` | Monday export (5 seats) |
| `results.csv` | One row per seat + `Checked_URLs` |
| `results.md` | This scorecard |
| `stamp-list.json` | FOUND only (empty array) |
| `CLOSEOUT.md` | Run closeout |
| `evidence/` | HTML snapshots, URL index, excerpts |
