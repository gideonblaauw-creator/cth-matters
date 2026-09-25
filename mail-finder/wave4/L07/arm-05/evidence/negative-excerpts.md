# Wave4 L07 Arm 05 — negative excerpts (curated public investor directories)

Method gate: **FOUND** requires exact target name + person@firm email on the **same** Mercury-class public directory record. Generics (`admin@`, `founders@`, `info@`) → **EMPTY**.

## Mercury Investor Database (`mercury.com/investor-database`)

- Full sitemap scanned (`mercury-investor-sitemap.xml`): **0** URLs matching `cendek`, `driegert`, `madigan`, `de-luca`, `arenas`, `lendable`, `autotech`, or `eclipse`.
- Direct slug probes return **404** (saved under `evidence/mercury-*.html`).

## findfunding.vc (Mercury-class public VC profiles)

**Eclipse Ventures** — lists **Aidan Madigan-Curtis** on investing team; contact block is firm generic only:

> How to reach them **admin@eclipse.capital**

(Bill Driegert not listed on Eclipse findfunding team roster as of capture.)

**Autotech Ventures** — lists **Burak Cendek** on investing team; contact block is firm generic only:

> How to reach them **founders@autotechvc.com**

No Lendable or Community Investment Management profiles located on findfunding.vc index/search.

## Investor Match (`investormatch.pro/vcs/*`)

- **Eclipse Ventures** / **Autotech Ventures**: partner names + LinkedIn links in static HTML; **no** person email fields on firm or person records.
- **Lendable**, **Community Investment Management**, **cim-llc**: firm slug URLs **404**.

## Evalyze.ai (`/investors/{slug}`)

- **Burak Cendek**: profile loads; **no** email in public HTML.
- **Aidan Madigan-Curtis**: profile loads; **no** email in public HTML.
- **Agustin De Luca**, **Bill Driegert**, **Alejandro Arenas**: error/noindex responses — no directory email.

## NFX Signal (`signal.nfx.com/investors/*`)

Public investor pages load (e.g. Burak Cendek partner profile) but expose **no** attributed person@firm mailbox without login/warm-intro flow.

## OpenVC (`openvc.app/p/*`)

Cloudflare **403** on automated fetch for all five name slugs — provenance not verified; not used for FOUND.

## Firm issuer pages (not directory FOUND; negative cross-check)

- `eclipse.capital/team/aidan-madigan-curtis`: footer **admin@eclipse.capital** only (generic).
- `cim-llc.com/profile/Alejandro-Arenas`: bio only, no email.
