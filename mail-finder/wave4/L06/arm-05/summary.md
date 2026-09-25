# Wave4 L06 Arm 05 — Press / podcast / speaker + mailto

**Run date:** 2026-09-25  
**Input:** 5 seats (`input.csv`)  
**Method:** Public press releases, podcast/show notes, conference agendas, and speaker pages where the target **name** and an exact **personal** email or `mailto:` co-occur on the **same page**. Generics (`press@`, `info@`, `communications@`, fund inboxes, another person’s PR mailbox) → **EMPTY**. No Hunter/Apollo, LinkedIn scrape, pattern guess, SMTP verify, invented emails, or Monday writes.

## Scorecard

| Status | Count |
|--------|------:|
| **FOUND** | 0 |
| **EMPTY** | 5 |
| **UNCERTAIN** | 0 |

## Per seat

| Monday_item_id | Name | Firm / domain | Outcome |
|----------------|------|---------------|---------|
| 13028367182 | Nic Gorini | spin.vc | EMPTY — speaker pages clean; HOI press has quentin@spin.vc (media), not Nic |
| 13100488906 | Niccolò Camerana | Stellantis Ventures | EMPTY — team 403; corporate media generic only |
| 13028359863 | Nina Alastruey | demium.com | EMPTY — event/podcast pages; SPRI PDF has organizer info@wstartupc.com |
| 13100506349 | Pat Martin | Venture 53 | EMPTY — speaker page generic events@; press wire amymack@ (spokesperson) |
| 13028367036 | Pauline de Valk | abnamro.com | EMPTY — news uses sif@; contact-page personal email out of arm scope |

## Near-misses (still EMPTY)

- **Pat Martin** — EIN Presswire pairs his quote with **amymack@venture53.com** (Amy Mack PR), not Pat’s inbox.
- **Pauline de Valk** — Bank contact page JSON includes **pauline.de.valk@abnarmo-privateequity.nl** beside her name; treated as contact bio, not press/podcast/speaker evidence for this arm.

## Artifacts

- `results.csv` — all seats, non-blank `Checked_URLs`
- `stamp-list.json` — empty (no FOUND)
- `README.md`, `summary.md`, `evidence/` (`url-index.md`, `negative-excerpts.md`, saved HTML snapshots)
