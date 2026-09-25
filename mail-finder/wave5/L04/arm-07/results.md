# Mail Finder Wave5 — L04 Arm 07 scorecard

**Method:** Public regulatory filings / registries / adviser disclosures that contain mailboxes (SEC EDGAR Form D, FINRA/IAPD Form ADV Part 1 PDF, EDGAR full-text index; BCSC/CVM probes). **FOUND** only when exact `Contact_name` and a personal `person@firm` e-mail co-occur in the **same** qualifying HTML/PDF/XML block. Form D / ADV Part 1 **name-only** rows do not qualify. Role/generic inboxes → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, SMTP verify, invented e-mails, or Monday writes.

**Seats:** 5 (`input.csv`)  
**Run date (UTC):** 2026-09-25

## Counts

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Per seat

| Monday_item_id | Contact_name | Firm | Status | Summary |
|----------------|--------------|------|--------|---------|
| 13132451595 | Ryan Russell | Avenue Growth Partners | EMPTY | Form ADV + Form D name Russell; no personal `@avenuegrowth.com` on same artifact |
| 13132451597 | Sam Altman | Altman Capital | EMPTY | Altman Capital Management ADV has no Sam Altman + mailbox; EDGAR/IAPD negative |
| 13132420361 | Santiago Fossatti | Kaszek | EMPTY | Kaszek ADV/Form D; SEC exhibit `pr@kaszek.com` is generic press only |
| 13132412663 | Santiago Álvarez | ALIVE Ventures | EMPTY | Form ADV + ALIVE Form D name Álvarez; name-only (no e-mail field) |
| 13132429598 | Shu Nyatta | Bicycle Capital | EMPTY | Form ADV + Bicycle Form D name Nyatta; EDGAR 0 for `@bicycle.capital` |

## Artifacts

- `results.csv`, `stamp-list.json` (empty), `CLOSEOUT.md`
- `evidence/url-index.md`, `evidence/negative-excerpts.md`, `evidence/adv/*.pdf`, Form D / filing snapshots

**Monday:** Not written (`stamp-list.json` empty).
