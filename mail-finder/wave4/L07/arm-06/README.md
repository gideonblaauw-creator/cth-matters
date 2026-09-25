# Mail Finder — Wave4 / L07 / Arm 06

**Focus:** Curated, **openly accessible** investor directories comparable to **Mercury-class** public listings (structured name + contact on the same directory record). Examples checked: [Mercury Investor Database](https://mercury.com/investor-database), [Gaebler.com VC profiles](https://www.gaebler.com/), [Silicon Valley Investclub](https://siliconvalleyinvestclub.com/investors/), [NFX Signal](https://signal.nfx.com/) (investor profiles).

**Write path:** `mail-finder/wave4/L07/arm-06/` only. **No Monday API writes** from this arm.

## Input

- `input.csv` — 5 seats (Monday export).

## Method (per seat)

1. Search **Mercury Investor Database** for a profile slug matching the target name; confirm **404 vs FOUND** gate.
2. Search **Mercury-class** third-party directories (Gaebler VC firm pages, SV Investclub investor/team cards, NFX Signal investor pages, OpenVC when reachable).
3. **FOUND** only when the **same public directory record** shows the **exact target name** and a **person@firm** email (exact spelling from the page).
4. Directory row with name + social only, or firm generic mailbox (`info@`, `origination@`, `openinnovation@`, `admin@`) **without** the target name on the same record → **EMPTY**.
5. Do **not** join data across records or infer mailboxes from domain patterns.

## Prohibited

Hunter, Apollo, RocketReach, ZoomInfo, Lusha, paid contact brokers, LinkedIn/Sales Navigator scraping, SMTP verification, pattern guessing, invented emails, Monday writes, writes outside this directory.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Every seed row once; `Status` = FOUND \| EMPTY \| UNCERTAIN; non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND rows only (`Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt`) |
| `summary.md` | Scorecard |
| `evidence/` | URL index, negative excerpts, optional HTML snapshots |

## FOUND gate

Record email only when a **curated public directory page** attributes a **person@firm** address to **that named person** on the **same record** (citation-grade excerpt required).

## Run metadata

- Processed: 2026-09-25 (UTC)
- Branch: `cursor/mail-finder-wave4-l07-arm06-4a91`
