# CLOSEOUT — MF CCB Clúster Energía W1 arm-07 Track A

## Scope

- **Path:** `mail-finder/ccb-cluster-energia/W1/arm-07/`
- **Track:** A (first-party firm contact)
- **Seeds:** 7 rows from `input.csv`

## Deliverables

| File | Status |
| --- | --- |
| `input.csv` | Copied from arm-07 intake |
| `results.csv` | 7/7 seeds adjudicated |
| `results.md` | Summary counts |
| `stamp-list.json` | `[]` (no FOUND); schema below for downstream stamps |
| `evidence/` | URL index, negative excerpts, AMV/ZFS HTML snapshots, AMV PDF |

## Results

- **FOUND:** 0
- **EMPTY:** 7
- **DOMAIN_UNRESOLVED:** 0

## `stamp-list.json` (FOUND rows only)

Each object stamps Monday Contact email column and, when applicable, name column **`text_mm7hkeme`**.

| Field | Monday / use |
| --- | --- |
| `nit` | Join key (seed NIT) |
| `Email` | Contact email |
| `Source_URL` | Citation page |
| `Evidence_excerpt` | Verbatim excerpt |
| `contact_name` | Maps to **`text_mm7hkeme`** — published person name on the **same first-party page** as the mailbox. Omit or `""` for ROLE-only inboxes. Never invent names. |

This run: no FOUND → file remains `[]`.

## Compliance

- No Hunter/Apollo, LinkedIn scrape, pattern+SMTP, or invented emails
- No Monday/CRM/Resend writes
- Writes confined to exclusive path above

## PR

Draft: **MF CCB W1 arm-07 Track A firm contact** (do not merge)
