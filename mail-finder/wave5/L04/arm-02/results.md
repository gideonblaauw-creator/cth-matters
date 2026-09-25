# Wave5 L04 Arm-02 — Regulatory with mailbox (scorecard)

**Method:** Public regulatory filings / registries / IAPD adviser disclosures containing mailboxes. **FOUND** requires target `Contact_name` and personal `person@firm` email in the **same** artifact.

| Monday_item_id | Contact | Firm | Status | Email | Citation |
|----------------|---------|------|--------|-------|----------|
| 13132427794 | Jared Miller | Accial Capital | EMPTY | — | IAPD ADV + Form D name-only |
| 13132423016 | Jason Finger | Upper90 | EMPTY | — | IAPD ADV + Form D name-only |
| 13103773472 | Javier Barreiro | Arrebol | EMPTY | — | No SEC/CNMV co-occurrence |
| 13028385021 | Jeff Stoike | (Blue Action) | EMPTY | — | No EDGAR/regulatory mailbox artifact |
| 13132447177 | John Curtius | Tiger Global | EMPTY | — | Olo exhibit: sboyd@ only; Form D name-only |

## Totals

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Notes

- Form D / ADV Part 1 rows for Miller, Finger, and Curtius (Cedar) confirmed **names without personal email fields** — skipped as non-yield per W2 lesson.
- Curtius / Olo EX-10.1 pairs the name with **sboyd@tigerglobal.com**; treated as **non-personal** (another individual’s mailbox), not stamped.

Evidence: `evidence/negative-excerpts.md`, `evidence/url-index.md`, downloaded filings under `evidence/`.
