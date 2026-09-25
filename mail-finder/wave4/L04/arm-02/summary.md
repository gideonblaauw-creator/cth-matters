# Wave4 L04 Arm 02 — SEC EDGAR exhibits / Form D / signature blocks

**Method arm:** Public SEC EDGAR filings and exhibits (Form D, 6-K, press-release exhibits, Form 4 signature blocks); firm/name disambiguation via EDGAR full-text (`efts.sec.gov`).

**Seats:** 5 | **FOUND:** 0 | **EMPTY:** 5 | **UNCERTAIN:** 0

| Monday_item_id | Name | Firm / domain | Status | Summary |
|----------------|------|---------------|--------|---------|
| 13114460584 | David García Acero | BBVA Spark / bbvaspark.com | EMPTY | No EDGAR artifact with García Acero + @bbvaspark.com; BBVA 6-K generic `comunicacion.corporativa@bbva.com` only. |
| 13114433880 | Eduardo González Montes de Oca | BBVA Spark / bbvaspark.com | EMPTY | 0 EDGAR name hits; same BBVA 6-K corporate mailbox without Eduardo attribution. |
| 13114467046 | Edward Goldstein | i80 Group / i80group.com | EMPTY | i80 Form D names Marc Helwani; Goldstein not in Form D XML; no Goldstein + @i80group.com co-occurrence. |
| 13028336256 | Greg Reichow | Eclipse / eclipse.capital | EMPTY | Enovix EX-99.1 names Reichow; exhibit emails are Enovix/PR only. Form D / Form 4 lack Reichow @eclipse mailboxes. |
| 13114485032 | Iñaki García Llorente | Lendable / lendable.io | EMPTY | LENDABLE SPC Form D filings have no @lendable.io and no Llorente in related-person blocks. |

**Attribution gate:** No seat met co-occurrence of published person name + exact non-generic `person@firm` email in the same SEC filing or exhibit.

**Monday:** No writes (`stamp-list.json` empty).

**Evidence:** `evidence/negative-excerpts.md`, filing snapshots under `evidence/`.
