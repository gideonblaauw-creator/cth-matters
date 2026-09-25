# CLOSEOUT — MF CCB Clúster Energía W1 arm-06 Track A

## Scope

- **Path:** `mail-finder/ccb-cluster-energia/W1/arm-06/`
- **Track:** A (first-party firm contact)
- **Seeds:** 7 rows from `input.csv`

## Deliverables

| File | Status |
| --- | --- |
| `input.csv` | Copied from arm-06 intake |
| `results.csv` | 7/7 seeds adjudicated |
| `results.md` | Summary counts |
| `stamp-list.json` | `[]` (no FOUND) |
| `evidence/` | URL index, negative excerpts, ALZ HTML snapshots |

## Results

- **FOUND:** 0
- **EMPTY:** 5 (persona natural seeds)
- **DOMAIN_UNRESOLVED:** 2 (ALZ ENERGIA site entity mismatch; AM HABITAT no website)

## `stamp-list.json` (FOUND rows only)

Each object stamps Monday Contact email column and, when applicable, name column **`text_mm7hkeme`**.

| Field | Monday / use |
| --- | --- |
| `nit` | Join key (seed NIT) |
| `crm_id` | Optional CRM id from seed row |
| `Email` | Contact email (published spelling) |
| `Source_URL` | Citation page |
| `Evidence_excerpt` | Verbatim excerpt |
| `contact_name` | Maps to **`text_mm7hkeme`** — published person name on the **same first-party page** as the mailbox. Omit or `""` for ROLE-only inboxes. **Never invent names.** |

This run: no FOUND → file remains `[]`.

## Re-queue hints

- **901652763-7:** Confirm whether `alzenergy.com.co` is operated by ALZ ENERGIA S.A.S. (NIT 9016527637) or retire stale Allianz Energy privacy copy; re-run Track A once NIT/razón social co-locate with mailbox on `/contactanos` or legal page.
- **901023733-8:** Website backfill from Cámara/RUES before contact crawl.

## Compliance

- No Hunter/Apollo, LinkedIn scrape, pattern+SMTP, or invented emails
- No writes outside exclusive path; no Monday/CRM patches

## PR

Draft PR title: **MF CCB W1 arm-06 Track A firm contact**
