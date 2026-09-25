# CLOSEOUT — Wave5 L04 Arm 08 (Regulatory with mailbox)

## Counts

| Status | n |
|--------|--:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

**Seats processed:** 5 / 5 (each seed row appears exactly once in `results.csv`).

## Notes

- **Relaunch:** Completed after prior infra error; SEC EFTS accessed with declared `MailFinderResearch/1.0` user agent.
- **Form D / ADV Part 1:** Treated as name-only where XML lacks email — not used to stamp FOUND (per Wave5 hard rules).
- **Generics excluded:** `info@`, `fiscal@` (CNPJ accounting), `hello@idcventures.com`, etc., when not name-bound on the same regulatory artifact.
- **IAPD brochure/CRS:** Supplemental PDF URLs returned HTTP 403 from this environment; primary Form ADV PDF (284129) scanned — no Capria person emails.
- **Monday:** No writes (stamp-list empty).

## Deliverables (exclusive path)

All under `mail-finder/wave5/L04/arm-08/`:

- [x] `input.csv`
- [x] `results.csv`
- [x] `results.md`
- [x] `stamp-list.json`
- [x] `CLOSEOUT.md`
- [x] `evidence/`

**Branch:** `cursor/mf-w5-l04-arm08-regulatory-mailbox-eabf` — draft PR only; not merged.
