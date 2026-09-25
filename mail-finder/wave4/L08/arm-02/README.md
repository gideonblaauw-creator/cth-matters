# Mail Finder — Wave4 L08 Arm 02

**Exclusive path:** `mail-finder/wave4/L08/arm-02/`  
**Lane:** Lane B (CTH Matters)  
**Input:** `input.csv` (5 P2 seats)

## Method

Targeted **Wayback CDX** on one firm path per seat (`/team`, `/about`, or `/people`, including equivalent exact paths):

1. Require a non-blank firm **website** on the seed row.
2. Run **at most one** CDX query per seat for the chosen path.
3. When CDX returns captures, fetch **one** archived snapshot and inspect HTML for **target name + person@firm mailto** co-occurrence on the same page.
4. **FOUND** only when that co-occurrence is present; record snapshot URL, timestamp, and excerpt.
5. **EMPTY** for no captures, name without email, email without name, or generic inboxes (`info@`, regional ops mail, etc.).
6. **Forbidden:** pattern guessing, SMTP verification, invented emails, Hunter/Apollo, LinkedIn scrape, broad Wayback crawling, authenticated sources, Monday writes.

## Deliverables

| File | Description |
|------|-------------|
| `input.csv` | Seed rows (Monday export) |
| `results.csv` | One row per seat; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND-only stamps (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | CDX audit + snapshot excerpts |

## Outcome (this run)

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Re-run (User-Agent)

```bash
UA='CTH-Matters-MailFinder/1.0 (Lane B; contact research)'
EV=mail-finder/wave4/L08/arm-02/evidence
curl -s -A "$UA" \
  'https://web.archive.org/cdx/search/cdx?url=angelventures.vc/team&output=json&limit=3&filter=statuscode:200'
curl -s -A "$UA" -o "$EV/angelventures-team-20200616181332.html" \
  'https://web.archive.org/web/20200616181332id_/http://www.angelventures.vc/team'
```

## Scope

Write **only** under `mail-finder/wave4/L08/arm-02/`.
