# Wave5 L02 Arm 03 — Closeout

**Arm:** Team person mailto (page-source)  
**Path:** `mail-finder/wave5/L02/arm-03/`  
**Completed (UTC):** 2026-09-25

## Counts

| Metric | Value |
|--------|------:|
| Input seats | 5 |
| FOUND | 0 |
| EMPTY | 5 |
| UNCERTAIN | 0 |
| stamp-list entries | 0 |

## Notes

- All five firms expose team/people content on first-party sites, but none publish a personal `mailto:` (or visible person `@domain`) co-occurring with the target `Contact_name` on Team/About/People/Contact or individual bio pages crawled.
- Pegasus (`pcalp.com`) contact page only lists generic mailboxes (`investorrelations@`, `careers@`, `feedback@`).
- OneVC lists **Eduardo Campos** on the bio page; Monday `Contact_name` is **Eduardo Brennand Campos** — identity aligned via team roster and profile LinkedIn URL, still no published personal email.
- Green Bond Corporation roster lives on `/who-we-are`; `/team` and `/contact` return 404.
- No Monday writes performed (`stamp-list.json` empty).
- Method constraints observed: no Hunter/Apollo, LinkedIn scrape, pattern guess, or SMTP verify.
