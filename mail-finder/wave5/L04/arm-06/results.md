# Wave5 L04 Arm 06 — Regulatory with mailbox

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`)  
**Method:** Public regulatory filings / registries / adviser disclosures that contain mailboxes (SEC Form D, Form ADV, Form C, issuer 6-K/8-K, EDGAR full-text). **FOUND** only when exact `Contact_name` and personal `person@firm` co-occur in the **same** artifact. Role/generic inboxes → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, SMTP verify, invented emails, or Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Contact_name | Firm | Outcome |
|----------------|--------------|------|---------|
| 13132406681 | Rachel Holt | Construct Capital | EMPTY — Form D + IAPD ADV name Holt; no `@construct.capital` on same regulatory doc |
| 13132420099 | Rafa de la Guia | Quona Capital | EMPTY — Quona Form D/ADV; de la Guia not in related-person tables; no personal `@quona.com` |
| 13132420370 | Rodolfo Elias Dieck | Proeza Ventures | EMPTY — SEC 8-K/S-4 path names Dieck without `@proezaventures.com` |
| 13132427200 | Rodrigo Velasco | BBVA Spark | EMPTY — BBVA 6-K mentions Spark; no Velasco + `@bbvaspark.com` |
| 13132419842 | Roy Bahat | Bloomberg Beta | EMPTY — Form D name-only Bahat; no `@bloombergbeta.com` in EDGAR |

## Artifacts

- `results.csv`, `stamp-list.json` (empty), `CLOSEOUT.md`, `evidence/` (`url-index.md`, `negative-excerpts.md`, Form D / ADV snapshots)
