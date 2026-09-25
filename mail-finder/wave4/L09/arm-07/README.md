# Mail Finder — Wave4 / L09 / Arm 07

**Focus:** **Deferred high-yield URL follow-ups** queued from L01–L03 closeouts and evidence notes — one targeted pass per seat on promising URLs (regulatory PDFs, CDTI/CNMV tables, SEC exhibits, Mercury/Fundraising Fox/Signal NFX, Wayback CDX, impact reports), not a broad crawl.

## Input

- `input.csv` — 5 P2 seats (Monday export).

## Method (`deferred_high_yield_url_followups`)

1. Pull deferred URL hints from prior wave evidence under `mail-finder/wave4/L01/`–`L03/` (and L06 press batch for overlap seats).
2. For each seat, fetch **only** the queued high-yield URLs (plus one Mercury sitemap slug check and one directory people URL when applicable).
3. **FOUND** only when **display name + exact person@firm** (or personal non-generic mailbox) co-occur on the **same page / citation block**; preserve published spelling.
4. Generics (`info@`, `contacto@`, `comunciacion@`, `admin@`, comms desks, entity-row emails without target name) → **EMPTY**.
5. **Forbidden:** Hunter/Apollo, LinkedIn scrape, pattern+SMTP, invented emails, paid/masked contact brokers, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`); non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only |
| `summary.md` | Scorecard |
| `evidence/` | Deferred queue, URL index, excerpts, directory search log |

## Result (this run)

**1 FOUND / 4 EMPTY** — see `summary.md`.

## Re-run

```bash
UA='Mozilla/5.0 MailFinderResearch/1.0 (cth-matters; L09-arm07)'
EV=mail-finder/wave4/L09/arm-07/evidence
curl -sL -A "$UA" -o "$EV/fundraisingfox-marcus-people.html" \
  'https://fundraisingfox.com/people/marcus-behrendt-bmw-i-ventures'
curl -s -A 'CTH-Matters contact@example.com' -o "$EV/sec-ex101-d124653dex101.htm' \
  'https://www.sec.gov/Archives/edgar/data/1844862/000119312521190525/d124653dex101.htm'
```

## Scope

Write **only** under `mail-finder/wave4/L09/arm-07/`.
