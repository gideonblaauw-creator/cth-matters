# Mail Finder — Wave4 / L02 / Arm 05

**Focus:** First-party **team / people** page `mailto:` discovery (Potential Investors). Monday **Website** values are already set — this arm does **not** backfill or correct Website.

## Input

`input.csv` — columns: Monday_item_id, Name, Contact_name, Firm, Kind, Priority, Status, Website, Domain, LinkedIn.

**Seats:** 4 (Wave4 L02 Arm 05 batch).

## Method

For each seat:

1. Fetch the firm **Website** homepage and standard team paths: `/team`, `/people`, `/about`, `/our-team`, `/leadership`, `/about-us`, `/equipo` (with and without trailing slash; `www` / apex where HTTP allows).
2. Parse page source for `mailto:` links on the **same domain** as the seat.
3. **FOUND** only when a **non-generic** `person@firm` address co-occurs with the seat **display name** in the same page region (citation-grade name + mailto attribution).
4. Generics (`info@`, `hello@`, `team@`, `contact@`, `contacto@`, `support@`, `ventures@`, etc.) → **EMPTY** for this arm.
5. **Prohibited:** Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP verify, invented emails. LinkedIn URLs in input are human context only.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat FOUND/EMPTY, checked URLs, notes |
| `stamp-list.json` | FOUND emails for Monday workbench stamp (after review) |
| `summary.md` | Scorecard |
| `evidence/` | HTML snapshots supporting EMPTY/FOUND adjudication |
| `crawl_scan.json` | Machine-readable crawl log (audit trail) |

## Result statuses

| Status | Meaning |
|--------|---------|
| `FOUND` | Citation-grade person email on first-party page |
| `EMPTY` | No qualifying name + person@firm mailto co-occurrence |

## Scope guardrails

- Write **only** under `mail-finder/wave4/L02/arm-05/`.
- Do **not** modify other arms or Monday.

## Regenerate crawl log

```bash
python3 mail-finder/wave4/L02/arm-05/crawl_team_mailto.py
```
