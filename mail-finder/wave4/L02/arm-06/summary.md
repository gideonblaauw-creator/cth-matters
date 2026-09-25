# Wave4 L02 Arm 06 — first-party team/people mailto scorecard

**Run:** 2026-09-25 · **Seats:** 4 · **Input:** `input.csv`  
**Method:** Public HTTP crawl of each Monday Website domain — homepage plus `/team`, `/people`, `/about`, `/our-team`, `/leadership`, `/contact` seeds and limited in-domain BFS on team-like paths. **FOUND** only when a non-generic `person@firm` `mailto:` co-occurs with the seat name on the same page/block.

## Results

| Status | Count |
|--------|------:|
| FOUND | 0 |
| EMPTY | 4 |

**Yield:** 0 / 4 citation-grade personal emails.

## Per seat (short)

| Name | Domain | Outcome |
|------|--------|---------|
| Stefanie Hauer | nature-re.com | Team bio on `/about-us/`; no mailto anywhere on domain |
| William Prescott | redribbon.co | Team on `/who-we-are`, `/rrfm`; only regional `enquiries.*@redribbon.co` footers |
| Jeff Stoike | blueactionaccelerator.com | `/team` lists name + LinkedIn; no mailto |
| Mikayla Hart | congruencecapital.com | Person not on public site; only `IR@congruencecapital.com` generic footer |

## Hygiene

- No Hunter/Apollo/LinkedIn scrape, pattern guessing, or SMTP validation.
- Generic inboxes (`enquiries.*`, `IR@`) treated as EMPTY per protocol.
- **No Monday writes** — `stamp-list.json` is empty.

## Artifacts

- `evidence/` — saved HTML snapshots + `crawl_report.json`
- `scripts/crawl_team_mailto.py` — reproducible crawler
