# CLOSEOUT — Mail Finder Wave5 L04 Arm-02

**Lane:** Regulatory with mailbox  
**Exclusive path:** `mail-finder/wave5/L04/arm-02/`  
**Seats:** 5  
**Run date:** 2026-09-25

## Counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Deliverables

- [x] `input.csv` (5 seed rows)
- [x] `results.csv` (5 rows, all `Checked_URLs` non-blank)
- [x] `results.md` (scorecard)
- [x] `stamp-list.json` (empty — no FOUND)
- [x] `evidence/` (URL index, negative excerpts, SEC/IAPD snapshots)

## Method summary

Primary sources: SEC EDGAR full-text (EFTS), Form D primary XML, IAPD Form ADV PDFs (CRD 305587 Accial, 304179 Upper90, 160318 Tiger), CNMV capital-riesgo registry portal for Arrebol. No Hunter/Apollo, SMTP guessing, LinkedIn scrape, or Monday writes.

## Outcome notes

- **Accial / Miller:** ADV and Form D bind Jared Miller to Accial vehicles; no `@accialcapital.com` in regulatory artifacts.
- **Upper90 / Finger:** Same pattern — chairman disclosure without mailbox in ADV or Form D.
- **Arrebol / Barreiro:** No EDGAR or CNMV manager filing with name + personal email.
- **Stoike:** No securities/regulatory filing with mailbox; marketing contacts excluded.
- **Curtius:** Closest hit is Olo investors’ rights agreement notice listing **sboyd@tigerglobal.com** under John Curtius header — does not meet personal-mailbox FOUND gate.

## PR

Draft PR opened; **not merged**.
