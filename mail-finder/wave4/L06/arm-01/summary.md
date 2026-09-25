# Wave4 L06 Arm 01 — Press / podcast / speaker + mailto scorecard

**Scope:** 5 seats from `input.csv`  
**Method:** Public press releases, podcast/show notes, conference or speaker pages, and comparable publisher-controlled HTML/PDF. **FOUND** only when the target name and an exact personal email or `mailto:` appear on the **same page** (generics such as `info@`, `contact@`, `press@` excluded).  
**Prohibited:** Hunter/Apollo, LinkedIn scrape, pattern guessing, SMTP verification, invented emails, paid/authenticated sources, Monday writes. Writes only under this directory.

## Status counts

| Status | Count |
|--------|------:|
| FOUND | 2 |
| EMPTY | 3 |
| UNCERTAIN | 0 |

## FOUND

| Monday_item_id | Name | Email | Source |
|----------------|------|-------|--------|
| 13028367329 | July ANDRAOUS | july.andraous@jambaar-capital.com | [AWI Members Showcase 2025 PDF](https://awiglobal.org/wp-content/uploads/2025/05/AWI-Members-Showcase_2025.pdf) |
| 13028372637 | Justin Brodie-Kommit | Justin@JustinBk.com | [DMV Climate Partners — 4WARD meetup event page](https://climatepartners.org/events/4ward-global-climate-sustainability-networking-meetups-dc-baltimore/) |

## Notable near-misses

| Seat | Why not FOUND |
|------|----------------|
| Julio Vasconcellos | Milken speaker page, 20VC show page, Atlantico/Graph sites — bios without published person mailbox. |
| Kai Christian Buhofer | Andes Horizon Capital site — partner bio and contact form only. |
| Kamal Hassan | TURN8 profile + Startup Village speaker bio — `info@turn8.co` generic only; no `kamal@turn8.co` on first-party pages. |

## Deliverables

- `input.csv`, `results.csv`, `stamp-list.json`, `README.md`, `summary.md`
- `evidence/` — AWI PDF, HTML snapshot, excerpts, `url-index.md`, `negative-excerpts.md`

**Processed:** 2026-09-25 (UTC)
