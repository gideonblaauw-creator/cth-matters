# Mail Finder — Wave5 L04 Arm 03 scorecard

**Method:** Public regulatory filings / registries / adviser disclosures **that contain mailboxes** (SEC IAPD Form ADV PDF, SEC Form D, EDGAR full-text, IAPD search API). Form D / ADV Part 1 name-only rows excluded per arm rules.

**Seats:** 5 (from `input.csv`)  
**Exclusive path:** `mail-finder/wave5/L04/arm-03/`

| Monday_item_id | Contact | Firm | Status | Email |
|----------------|---------|------|--------|-------|
| 13132420302 | Jonathan Whittle | Quona Capital | EMPTY | — |
| 13132427073 | Keiji Matsunaga | SMBC | EMPTY | — |
| 13132412479 | Lachy Groom | Lachy Groom (fund) | EMPTY | — |
| 13132412512 | Lauren Morton | QED Investors | EMPTY | — |
| 13132420129 | Lawrence G. Chua | Accial Capital | EMPTY | — |

## Totals

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |

## Notes

- **Quona / Whittle:** Name on IAPD Schedule A and Quona-related Form D; no personal `@quona.com` in the same regulatory artifact.
- **SMBC / Matsunaga:** No EDGAR artifact with exact name; no regulatory mailbox co-occurrence.
- **Lachy Groom:** Extensive Form D name/signature presence; zero EDGAR email fields for `@lachygroom.com`.
- **QED / Morton:** Active adviser ADV package contains no `@` strings; Morton absent from Form D related-person lists.
- **Accial / Chua:** Inactive adviser ADV without target or emails; Accial Form D filings without Chua or mail fields.

**Monday:** No writes (`stamp-list.json` empty).  
**Evidence:** `evidence/url-index.md`, `evidence/negative-excerpts.md`, `evidence/quona-whittle-adv-excerpt.md`, `evidence/edgar_search.json`, saved Form D XML samples.
