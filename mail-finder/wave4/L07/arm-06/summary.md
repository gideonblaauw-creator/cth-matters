# Wave4 L07 Arm 06 — curated public investor directories (Mercury-class)

**Method:** Open, curated investor directories that publish contact tables (Mercury Investor Database, Gaebler.com VC profiles, Silicon Valley Investclub, NFX Signal where applicable). No Hunter/Apollo/RocketReach, no LinkedIn scrape, no pattern guessing.

**Processed:** 2026-09-25 (UTC)  
**Seats:** 5 P1  
**Monday writes:** None (`stamp-list.json` empty)

## Scorecard

| Monday_item_id | Name | Firm | Status | Directory outcome |
|----------------|------|------|--------|---------------------|
| 13114460584 | David García Acero | BBVA Spark | EMPTY | No Mercury profile; Gaebler/SVIC/Wayback team — no David + person@bbvaspark.com |
| 13114433880 | Eduardo González Montes de Oca | BBVA Spark | EMPTY | No Mercury profile; Eduardo named on SVIC/Wayback without person email on same record |
| 13114467046 | Edward Goldstein | i80 Group | EMPTY | No Mercury profile; Gaebler i80 lists origination@i80group.com for Marc Helwani only |
| 13028336256 | Greg Reichow | Eclipse | EMPTY | No Mercury profile; Gaebler lists Greg Reichow with social links only |
| 13114485032 | Iñaki García Llorente | Lendable | EMPTY | No Mercury profile; Gaebler Lendable generic info@lendable.io; no Llorente row |

**FOUND:** 0 / 5  
**EMPTY:** 5 / 5  
**UNCERTAIN:** 0 / 5

## Method notes

- **Mercury:** All five expected slugs return **404**; Mercury remains a valid Mercury-class directory (positive control: `chris@fuelcapital.com` on Chris Howard page).
- **Gaebler:** Public VC firm profiles used; firm-level generics (`openinnovation.es@bbva.com`, `origination@i80group.com`, `info@lendable.io`, `admin@eclipse.vc`) excluded when not name-attributed to the seat.
- **OpenVC:** `openvc.app` blocked automated HTTP (403); no fund/person+email hits for these seats in public web index — insufficient for FOUND; other directories checked.

## Artifacts

- `results.csv`, `stamp-list.json`, `README.md`, `summary.md`
- `evidence/` — HTML snapshots, `url-index.md`, `negative-excerpts.md`, `mercury-slug-probes.txt`
