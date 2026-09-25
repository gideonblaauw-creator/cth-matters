# Wave4 L08 Arm 04 — Wayback CDX on /team, /about, or /people

**Run:** 2026-09-25 (UTC) · **Seats:** 5 · **Input:** `input.csv`  
**Method:** One targeted Internet Archive **CDX** lookup per seat on the firm’s `/team`, `/about`, or `/people` URL (exact path). When captures exist, review archived HTML for **target name + personal `person@firm` or `mailto:` on the same page**. CDX metadata alone is not evidence.

## Results

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

**Yield:** 0 / 5 citation-grade personal emails via Wayback team/about/people lane.

## Per seat

| Monday_item_id | Name | Domain | CDX path | Outcome |
|----------------|------|--------|----------|---------|
| 13100496455 | Anna Raptis | amplifica.capital | `/team` | **EMPTY** — CDX 0 captures; live /team 404 |
| 13100509893 | Aquilino Peña | kiboventures.com | `/team` | **EMPTY** — Aquilino on archived team pages; no person email on same page |
| 13028370676 | Asia Agnelli | tmv.vc | `/team` | **EMPTY** — no Asia Agnelli + personal @tmv.vc on archived /team |
| 13028372799 | Belkacem Hammoulhadj | greenbull.com | `/team` | **EMPTY** — CDX 0 captures |
| 13028366580 | Benjamin Radomski | bevfamilyoffice.com | `/team` | **EMPTY** — CDX 0 captures |

## Hygiene

- No Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP checks, broad Wayback crawl, or Monday writes.
- Work confined to `mail-finder/wave4/L08/arm-04/`.
- Negative excerpts: `evidence/negative-excerpts.md`; Wayback HTML cache under `evidence/wayback-*.html`.
