# Mail Finder — Wave4 / L09 / Arm 03

**Focus:** **Deferred high-yield URL follow-ups** from Wave4 **L01–L03** closeouts and related evidence notes (same five seats previously run in **L01 Arm 05** domain hygiene and **L05 Arm 07** impact/LP PDF).

## Input

- `input.csv` — 5 P2 Potential Investors seats (Monday export).

## Method (`deferred_highyield_url_followup`)

1. For each seat, take **hinted URLs** already discovered in prior arms (website corrections, PDF url-index, EFTS hits, blocked 990 links).
2. Fetch and inspect each hinted artifact for **display name + exact person@firm** co-occurrence on the **same page/PDF**.
3. Perform **one same-domain expand** (e.g. Overboost → Kamay; prochain.vc `/about`; Endeavor informe → global team).
4. **FOUND** only with citation-grade excerpt. Generics (`info@`, `speed@`, `hola@`, spokesperson inboxes for another person) → **EMPTY**.
5. **Forbidden:** Hunter/Apollo, LinkedIn/Sales Navigator scrape, pattern guessing, SMTP verification, invented emails, paid/authenticated brokers, **Monday writes**, broad crawling beyond hinted URLs + single expand.

## Outputs

| File | Purpose |
| --- | --- |
| `results.csv` | One row per seat: `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`), non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND seats only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | URL index, negative excerpts, HTML/PDF snapshots |

## Result (this run)

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Re-run

```bash
UA='MailFinderResearch/1.0 (cth-matters; L09-arm03) contact@example.com'
EV=mail-finder/wave4/L09/arm-03/evidence
curl -sL -A "$UA" -o "$EV/overboost_me.html" https://overboost.me/
curl -sL -A "$UA" -o "$EV/endeavor_global_team.html" https://endeavor.org/about-us/global-team/
```

## Scope

Write **only** under `mail-finder/wave4/L09/arm-03/`.

Protocol: `mail-finder/protocol/Mail-Finder-Workbench-Strategy.md` (method arm 8 — deferred high-yield URL follow-ups).
