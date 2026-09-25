# Mail Finder — Wave4 / L08 / Arm 04

**Focus:** Targeted **Wayback Machine CDX** on a single **`/team`**, **`/about`**, or **`/people`** URL per seat (firm website required). **FOUND** only when an archived page shows the **target name** and a **non-generic personal email** (`person@firm` or `mailto:`) **together**.

**Write path:** `mail-finder/wave4/L08/arm-04/` only. **No Monday API writes** from this arm.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. Choose one promising path among `/team`, `/about`, `/people` on the firm domain.
2. Run **one** CDX query for that exact URL prefix.
3. If captures exist, open one or more archived snapshots and search page HTML for name + person email co-occurrence.
4. **EMPTY** when CDX has no captures, or archived/live page has name without email, email without name, or only generic inboxes (`team@`, `hi@`, `info@`, etc.).

## Prohibited

Hunter/Apollo, LinkedIn/Sales Navigator scraping, email pattern guessing, SMTP verification, invented addresses, broad Wayback enumeration beyond the single path, paid/authenticated sources, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Every seed row once; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND rows only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | CDX JSON, Wayback HTML, negative excerpts |

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l08-arm04-eb24`
