# Regulatory / securities PDF pass — audit notes (L03 Arm 08)

Method: SEC EDGAR EFTS, Form D primary XML, Form 4 insider filings, FINRA IAPD Form ADV (PDF text), BCSC document search HTML. No Hunter/Apollo, no LinkedIn scrape, no pattern guessing.

## Cross-cutting

- EFTS full-text queries for `@eclipse.capital`, `@lendable.io`, `@atlantico.vc`, `@wayra.com` returned **0** EDGAR hits (2026-09-25).
- IAPD Form ADV for **ECLIPSE** (SEC# 802-101492) and **LENDABLE ASSET MANAGEMENT LLC** (SEC# 802-119775) include standard instruction: *"Do not provide the individual electronic mail (e-mail) addresses of employees"* — no person-level `@firm` co-occurrence for target seats.

## Per-seat negatives (summary)

| Monday_item_id | Name | Key regulatory artifacts reviewed |
|----------------|------|-----------------------------------|
| 13100509887 | Andrés Saborido | EFTS `"Andres Saborido" wayra` (0); `"Saborido" telefonica` (0); `@wayra.com` (0) |
| 13100506305 | Mark Crawford | EFTS `"Mark Crawford" Caterpillar` (no CAT entity co-email); Form D / CAT 10-K exhibits list **Caterpillar Venture Capital Inc.** subsidiary only — no Crawford + `@cat.com` |
| 13114466721 | Ana Clara Martins | Atlantico Partners Form D filings (CIK 1795625, 1933742, 2132291): related person **Julio Vasconcellos** only; signature blocks without email; no Ana Martins |
| 13028336256 | Greg Reichow | Enovix EX-99.1 press exhibit names Reichow; emails on page are **Enovix IR/PR** only (`canderson@enovix.com`, etc.). Form 4 (0001584531-26-000003): no reporting-owner email. Eclipse Fund I Form D: no `@` fields |
| 13114485032 | Iñaki García Llorente | LENDABLE SPC Form D (CIK 1816111): no `@lendable` emails; EFTS name+lendable (0). Lendable.io impact PDF blocked (403) from bot — not used without extractable text |
