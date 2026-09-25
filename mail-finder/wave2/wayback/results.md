# Mail Finder Wave2 — Wayback CDX arm

Board **18425305222** · Input: `input.csv` (20 deep50 EMPTY seats).

**Primary method:** Internet Archive CDX API on each seat `Domain` for paths matching `/team`, `/about`, `/people`, `/leadership`, `/contact`, `/our-team` (and equivalents); fetch `id_` snapshots; parse HTML source for `mailto:` + name co-occurrence. Generics → EMPTY; no live deep-crawl except one retry when snapshot truncated.

Hard rules: citation-grade only; no Hunter/Apollo/LinkedIn scrape/pattern guessing.

## Status counts

| Status | Count |
|--------|------:|
| EMPTY | 18 |
| HOLD | 2 |

## FOUND (stamp list)

_None this pass — no citation-grade name + person@firm on archived team/about pages._

## Per-seat summary

| Monday_item_id | Name | Domain | Status | Notes (abbrev.) |
|----------------|------|--------|--------|-----------------|
| 13080749061 | Federico Storani | riverwoodcapital.com | EMPTY | CDX on riverwoodcapital.com/* (collapse urlkey): no archived /team//about//people URLs with status 200 in index sample. … |
| 13096680140 | Filipe Portugal | canary.com.br | EMPTY | CDX on canary.com.br/*: no team/about/contact captures in index (SPA-era). Deep50: old.canary.com.br/team lists Filipe P… |
| 13028367050 | Jonathan Duarte | crossboundary.com | EMPTY | Wayback our-team/about/advisory contact snapshots (2019–2019) — no Jonathan Duarte + person@crossboundary.com. Live prof… |
| 13100502214 | Maite Fibla Gasparin | ship2bventures.com | HOLD | ship2bventures.com/team lists Maite Fibla Gasparin (LinkedIn) — only info@ship2bventures.com in footer. Anima event page… |
| 13114411690 | Igor Piquet | endeavor.org | EMPTY | endeavor.org global-team lists Igor Piquet (403 from bot). No public endeavor.org page found with Igor + person@endeavor… |
| 13100511350 | Jason Sydow | next47.com | HOLD | next47.com/n47.com team SPA — no Jason Sydow email in fetched HTML/JS. briia.io mentor page — LinkedIn only. Wayback CDX… |
| 13080749096 | Rabobank Partnerships | rabobank.com | EMPTY | CDX on rabobank.com/* returned about-us/carbon-bank and contact pages (not innovation/partnerships index). Snapshots rev… |
| 13114433880 | Eduardo González Montes de Oca | bbvaspark.com | EMPTY | Wayback snapshot https://web.archive.org/web/20231130210549id_/https://www.bbvaspark.com/about-us/ — org metadata only; … |
| 13100496708 | Abe Yokell | congruentvc.com | EMPTY | generics only on https://congruentvc.com/contact/ (20210813064641): info@congruentvc.com, investors@congruentvc.com; gen… |
| 13028372613 | Alistair Langer | 783capital.com | EMPTY | CDX returned no 200 snapshots for team/about/contact paths Wayback CDX arm: no citation-grade name+person@ on archived p… |
| 13028350632 | Amaya Baliño Sanz | angelventures.vc | EMPTY | Live crawl errors: 5; Generics only on domain: infocolombia@angelventures.vc Wayback CDX arm: no citation-grade name+per… |
| 13100506379 | Camilo Kejner | angelventures.vc | EMPTY | Live crawl errors: 5; Generics only on domain: infocolombia@angelventures.vc Wayback CDX arm: no citation-grade name+per… |
| 13100505949 | Christopher Gottschalk | mourocapital.com | EMPTY | Archived https://www.mourocapital.com/our-team/ (20200915000847) lists Chris Gottschalk; no mailto on page. Contact-us s… |
| 13080768682 | CrossBoundary | crossboundary.com | EMPTY | Live crawl errors: 5; Generics only on domain: contact@crossboundary.com Wayback CDX arm: no citation-grade name+person@… |
| 13114460590 | Elias Mufarech | collide.capital | EMPTY | CDX on collide.capital/*: no team/about/contact 200 rows in index. Prior crawl investors@collidecap.com generic only. Wa… |
| 13028371748 | Fernando Lelo de Larrea H | rumbo.vc | EMPTY | CDX on rumbo.vc/*: no captures (domain non-resolving; operating rumbo.ventures out of scope for seat domain). Wayback/CD… |
| 13028358383 | Humberto Matsuda | overboost.vc | EMPTY | CDX returned no 200 snapshots for team/about/contact paths Wayback CDX arm: no citation-grade name+person@ on archived p… |
| 13100506451 | Ingo Ramesohl | bosch.ventures | EMPTY | CDX on bosch.ventures/*: no indexed /team//about 200 responses in sample (site newer). Prior crawl: team page without pe… |
| 13028366289 | Jean-Marc Champagne | senecaimpact.com | EMPTY | CDX returned no 200 snapshots for team/about/contact paths Wayback CDX arm: no citation-grade name+person@ on archived p… |
| 13028349951 | Kamal Hassan | turn8.co | EMPTY | generics only on http://www.turn8.co/contact/ (20140326081709): contact@turn8.co Wayback CDX arm: no citation-grade name… |

## Artifacts

- `results.csv` — all input seats
- `found-for-monday.csv` — FOUND rows only (empty if none)
- `first-found-evidence.md` — evidence blocks for FOUND
- `html/` — saved Wayback snapshot sources reviewed this pass
- `scripts/run_wayback_cdx.py` — CDX + snapshot parser

CDX queries logged in each row `Checked_URLs` (first entry is the CDX API URL for the seat domain).
