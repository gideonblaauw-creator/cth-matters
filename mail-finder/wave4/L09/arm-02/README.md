# Mail Finder — Wave4 L09 Arm 02

**Exclusive path:** `mail-finder/wave4/L09/arm-02/`  
**Lane:** Lane B (CTH Matters)  
**Input:** `input.csv` (5 P2 seats — deferred high-yield batch)

## Method (`deferred_highyield_leads`)

Second-pass **leads only** on URLs and artifacts noted in Wave4 **L01–L03** (and L05) closeouts — not a full site crawl or regulatory PDF re-grind.

1. For each seat, open the **deferred URL queue** (old team HTML, press/spotlight posts, conference advisory rosters, third-party LP sourcing PDFs, academic repository bitstreams linked from prior arms).
2. **FOUND** only when the target **display name** and an exact **person@firm** mailbox (or equivalent `mailto:` on the same public page/artifact) co-occur with citation-grade spelling.
3. **Generics** (`info@`, `press@`, `eis@`, `sales@`, `contact@`, RAM/tax desk blocks not attributed to the person) → **EMPTY**.
4. **Personal domains** (e.g. legacy Gmail on old wiki pages) → **EMPTY** for firm attribution.
5. **Excluded:** Hunter/Apollo, ZoomInfo/RocketReach/Mintround-style brokers, LinkedIn scrape, pattern guessing, SMTP verification, invented emails, Monday writes, writes outside this directory.

## Deliverables

| File | Description |
|------|-------------|
| `input.csv` | Seed rows (Monday export) |
| `results.csv` | One row per seat; `Status` ∈ FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND-only stamps |
| `summary.md` | Scorecard |
| `evidence/` | URL index, negative excerpts, fetched HTML/text (large issuer PDFs cited by URL; text extracts only in repo) |

## Outcome (this run)

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Re-run

```bash
UA='MailFinderResearch/1.0 (cth-matters; L09-arm02) contact@example.com'
EV=mail-finder/wave4/L09/arm-02/evidence
curl -sL -A "$UA" -o "$EV/molten_team_spotlight.html" \
  'https://www.moltenventures.com/news/team-spotlight-george-chalmers'
curl -sL -A "$UA" -o "$EV/hlm_electis_sourcing.txt" \
  'https://www.hlm.coop/sites/default/files/2026-01/Elections%202026%20-%20Sourcing.pdf' \
  && pdftotext "$EV/hlm_electis_sourcing.txt" -
```

## Scope

Write **only** under `mail-finder/wave4/L09/arm-02/`.
