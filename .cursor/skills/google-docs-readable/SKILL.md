---
name: google-docs-readable
description: Write and rebuild human-readable Google Docs with real headers, nested bullets, markdown tables, and Gantt/clock charts. Use whenever creating, replacing, or formatting a Google Doc for humans — proposals, meeting briefs, talking points, briefs. Never dump text/plain into Drive.
---

# Google Docs — readable (not a text dump)

Human-facing Docs must look like a document a partner can scan in 30 seconds: **H1 / H2 / H3**, **nested bullets**, **tables**, and **chart-like tables** (clock, Gantt, budget bars). A wall of plain paragraphs is a failure even if the facts are right.

## Never

- `Google-drive.create_file` (or Drive upload) with `contentMimeType=text/plain` for a Doc people will read. That is what produced the unreadable dumps PASO could not scan.
- Invent a new Doc when a shared link already exists. Rebuild **in place** so Mercy / Juan / other writers keep the same URL.
- Cram every pipe-table into one create/append if the Docs API returns **400**. Chunk: one or a few tables per `GOOGLEDOCS_UPDATE_DOCUMENT_SECTION_MARKDOWN` call.
- Invent missing numbers, org counts, or tech-stack claims. Leave a Review comment instead.
- Embed a chart PNG from a **private** GitHub raw URL (404). Use a markdown Gantt table, or upload the PNG to Drive first and insert that URL.

## Accounts (CleantechHUB)

| Job | Toolkit | Account |
| --- | --- | --- |
| Create / replace / style Docs | `googledocs` | `googledocs_osiris-aion` (`gideon.blaauw@cleantechhub.net`) |
| Share, comments, folder moves | `googledrive` | `googledrive_via-jag` |
| Composio meta tools | — | `session_id`: `"when"` (reuse the live search session) |

Sheets on a file owned by `gideon.blaauw@cleantechhub.net` 403 if you use the `gideon@runupholdings.com` Sheets identity. Share **writer** to that identity first, or use the CTH account.

## Tools

Discover via Composio `COMPOSIO_SEARCH_TOOLS`, then run with `COMPOSIO_MULTI_EXECUTE_TOOL`.

| Intent | Tool |
| --- | --- |
| New Doc from markdown | `GOOGLEDOCS_CREATE_DOCUMENT_MARKDOWN` |
| Replace **entire** body | `GOOGLEDOCS_UPDATE_DOCUMENT_MARKDOWN` (`id` + `markdown`) |
| Append / replace a range | `GOOGLEDOCS_UPDATE_DOCUMENT_SECTION_MARKDOWN` |
| Read structure + indices | `GOOGLEDOCS_GET_DOCUMENT_BY_ID` |
| Read as text (QA only) | `GOOGLEDOCS_GET_DOCUMENT_PLAINTEXT` |
| Landscape, margins | `GOOGLEDOCS_UPDATE_DOCUMENT_STYLE` |
| Review ask, do not invent | `GOOGLEDRIVE_CREATE_COMMENT` (`quoted_file_content_value`) |

## Rebuild in place (keep the share link)

1. `GOOGLEDOCS_GET_DOCUMENT_BY_ID` → last body `endIndex` (the final `paragraph` is usually a lone `\n`).
2. Prefer `GOOGLEDOCS_UPDATE_DOCUMENT_MARKDOWN` with the full markdown.
3. If that 400s (common with **many** pipe-tables in one payload):
   - Delete range `start_index=1`, `end_index=lastEndIndex - 1` via section markdown with empty/`\n` replacement, **or** `deleteContentRange` through Docs batch update.
   - Append in chunks with `GOOGLEDOCS_UPDATE_DOCUMENT_SECTION_MARKDOWN` (omit `start_index` to append). One wide table per chunk is safest.
4. Do **not** delete the document’s final newline. The API rejects `end_index` that includes it.

## Page setup

Wide tables (Gantt, 8-column clocks, decision matrices) need landscape and equal L/R margins. Portrait + fat side margins wrap table cells into unreadable stacks.

```
GOOGLEDOCS_UPDATE_DOCUMENT_STYLE
document_id: <id>
fields: "pageSize,marginTop,marginBottom,marginLeft,marginRight"
document_style:
  pageSize: { width: { magnitude: 792, unit: PT }, height: { magnitude: 612, unit: PT } }
  marginTop / marginBottom / marginLeft / marginRight: { magnitude: 54, unit: PT }
```

- Landscape letter = width **792** pt, height **612** pt.
- Equal **54 pt** L/R/T/B. Do not leave a large left margin from a previous dump.
- Justify **long narrative** only. Meeting briefs and tables stay left-aligned.

## What “structured” means

Use this shape for talking points, proposals, and lock-and-gap briefs.

### Headers

- **H1** = document title (one).
- **H2** = scan sections (Meeting card, Decisions, Budget, Path to submit).
- **H3** = sub-blocks (Clock visual, Geography, Split visual).
- One-line bold lede under the title (`**Lock-and-gap call. Not a redesign.**`).

### Bullets

- One idea per bullet. Bold the lock phrase (`**TECH only.**`, `**USD 20,000**`).
- Nested bullets only when the child is a constraint on the parent.
- Do not write a 40-line paragraph that could be five bullets.

### Tables (default for facts)

| Use a table when | Examples |
| --- | --- |
| People must compare | 25k vs 50k, CTH vs PASO, yes/no captures |
| People must look up | Track → place → organisations |
| People must act | D1–D8 with an empty **Yes / no** column |
| People must open files | File → why it is open (with live URLs) |

Keep header rows. Empty capture cells (`Yes / no`) are intentional.

### Charts (functional, not decoration)

Google Docs has no native Gantt. Use a **markdown table with `XX` in active cells** so it reads as a bar chart on the page.

**Clock / agenda**

```markdown
| Block | 0 | 5 | 10 | 15 | 20 | 25 | 30 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Open + locked | XX |  |  |  |  |  |  |
| Decisions D1–D8 |  | XX | XX | XX |  |  |  |
```

**12-month Gantt / phase band**

```markdown
| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Phase 1 | XX | XX |  |  |  |  |  |  |  |  |  |  |
| Phase 2 |  |  | XX | XX | XX |  |  |  |  |  |  |  |
```

**Budget split**

```markdown
| | 10k | 20k | 30k | 40k | 50k |
| --- | :---: | :---: | :---: | :---: | :---: |
| 50k — CTH ~30 | XX | XX | XX |  |  |
| 50k — PASO 20 |  |  |  | XX | XX |
```

Pair every visual with a numeric table above it (minutes, USD, dates). The `XX` chart is the scan; the numbers are the source.

Optional colour PNG (`gantt-2027.png` in the GRP pack): upload to Drive as a public-or-writer file, then `![2027 work plan](DRIVE_URL)`. Do not rely on private GitHub raw.

## Review comments instead of invented text

When CTH or PASO must fill a fact (tech stack, member counts, community profile):

1. Write a **placeholder sentence** the comment can quote.
2. `GOOGLEDRIVE_CREATE_COMMENT` with `quoted_file_content_value` matching that sentence exactly.
3. Name who replies (CTH / PASO) in the comment body.

Do not fill CORE1, org eighth-seat, or warehouse/API/model text from imagination.

## Worked examples in this repo

| Artifact | Local | Live Doc (rebuild in place) |
| --- | --- | --- |
| Full proposal | `packs/grp-innovation-challenge-2026/04-full-proposal-first-draft.md` | https://docs.google.com/document/d/1MnSsOMI_nsESC-0_TwIeC5UDnFSZXqQwDELNt2sZ9Uo/edit |
| PASO talking points | `packs/grp-innovation-challenge-2026/05-paso-meeting-talking-points.md` | https://docs.google.com/document/d/1cxFfnFMnmi9WLq5z3wtWlrGyJ_ekaUMELG9NM6WqMPA/edit |

Folder: https://drive.google.com/drive/folders/1Ii7eq_n6gwB5FpclEXb0FOmPqXza6sEd

## QA before you tell the user it is done

1. `GOOGLEDOCS_GET_DOCUMENT_PLAINTEXT` — confirm H1/H2 text, table pipes survived, and the old dump is gone.
2. Confirm the **same URL** still opens (no new file).
3. Landscape + 54 pt margins if any table is wider than ~6 columns.
4. Share writers unchanged (do not recreate sharing).
