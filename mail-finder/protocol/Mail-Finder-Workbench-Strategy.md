# Mail Finder Workbench — Strategy & n8n Flow Spec

**Date:** 23 Sep 2026 (yield lessons patched 24 Sep 2026)  
**Owner:** Teclogi desk (CTH Growth / IR)  
**Client:** Teclogi Series A  
**Status:** Named + specified (HITL). Build workbench + n8n when Gideon says go.  
**Name lock:** **Mail Finder** (was draft name CiteMail — superseded).

**Canonical path:** `mail-finder/protocol/Mail-Finder-Workbench-Strategy.md`

---

## Name

| Layer | Name | What it is |
|---|---|---|
| **Stack** | **Mail Finder** | Open-source / public-web attribution stack for `person@firm` emails |
| **Workbench** | **Mail Finder Workbench** | Desk + automations that run Mail Finder + ReachGate |
| **n8n flow** | **Mail Finder Flow** | Automated pipeline under the workbench |
| **Companion lane** | **ReachGate** | Reach *without* corporate inbox (forms, Calendly, WhatsApp HITL, warm forwards) |

**Tagline:** Only store an email if a public source cites it next to the named person.

---

## Forbidden (unchanged)

Do **not** use or route through:

- Paid finders / enrichment APIs (**Hunter**, **Apollo**, etc.)
- **LinkedIn** scrape, **Sales Nav**, **PhantomBuster**, or any LI ToS–violating email jobs
- **Pattern guessing** or invented addresses (including `{first}.{last}@`, `{f}{last}@`, role templates without a published cite)
- SMTP verify or “validation” on addresses that were not read from a public source
- Storing domain-wide harvest hits without **person-name co-occurrence** on the same page/snippet/block

LinkedIn URLs may appear in input CSV for human context only — **LinkedIn-primary** seats → **HITL hold** (no Sales Nav, no scrape).

---

## Hands HARD (operating model)

| Role | Who |
|---|---|
| **Craft / crawl / PDF / filing / Wayback execution** | **Cursor Cloud Hands** only — all method arms run as Hands jobs with artifacts |
| **Workbench** | Coordinates batches, wave design, attribution review, ReachGate routing |
| **Monday / Gmail connector stamps** | Workbench (or approved Flow) **after** attribution review — never auto-stamp UNCERTAIN or guessed emails |

No local bot grind on large seat-only batches; yield comes from **focused method waves**, not volume crawling.

---

## Monday Contact columns (IDs)

Board context: Teclogi Contact board (e.g. `18425305222` — verify in Monday UI).

| Column | ID | Use |
|---|---|---|
| **Email (Contact)** | `email_mm7ffmz4` | Patch **only** on FOUND with attribution-approved cite |
| **Website** | `link_mm7gdv8s` | Public firm/site URL for the seat — **Website backfill** wave uses this column **only**; **skip row if already filled** |

**Website backfill:** When Monday Website is empty, Hands may infer domain from firm name + public registries — **sniff-test** noisy domain inferences before crawl; do not overwrite an existing Website value.

**Notes:** FOUND → patch email + source URL in Notes; EMPTY → Notes stamp only (no fake email). UNCERTAIN → **no email stamp** (explain in Notes if needed).

---

## Goal

For Teclogi capital contacts missing Contact email:

1. **Mail Finder** finds verified `person@firm` (or attributed personal domain) from publications, team pages, filings, PDFs, Wayback, firm-site crawl.
2. **ReachGate** starts a conversation when Mail Finder returns EMPTY (form / Calendly / WhatsApp / shared thread / warm intro).
3. Monday Contact stays clean: FOUND → patch; EMPTY → Notes stamp only; UNCERTAIN / DOMAIN_UNRESOLVED → no invented email.

---

## Result statuses

| Status | Meaning | Monday action |
|---|---|---|
| **FOUND** | Citation-grade `person@email` with public source attributing address to **that person** | Patch `email_mm7ffmz4` + source in Notes (HITL approve if Flow) |
| **EMPTY** | Methods exhausted for this wave; no attributable cite | Notes only → ReachGate |
| **UNCERTAIN** | Weak or ambiguous co-occurrence; not citation-grade | **No email stamp** |
| **DOMAIN_UNRESOLVED** | Firm/site domain not established to crawl | Fix domain hygiene / alias cleanup; re-queue |

---

## Mail Finder stack (tools)

| Tool | Role in flow |
|---|---|
| Web search / dorks | `"Name" "@domain"` / `filetype:pdf` / conference names / press |
| **Photon** (or equivalent site crawler) | Crawl *firm domain only* for mailto + PDF links |
| **Archive.org CDX / Wayback** | Historical `/team` `/people` `/about` mailto: — **one CDX pass** on promising EMPTY, then move on |
| **theHarvester** | Domain-indexed public emails → **human filter** to named person |
| **pdfgrep / pdftotext** | Extract name + email from speaker / corp / regulatory PDFs |
| OpenCorporates / CNPJ / **SEC EDGAR** / IAPD / **BCSC**-class registries | Filings & registries; signature blocks |
| DocuSign / ethics / impact PDFs | High-yield PDF lane when firm publishes them |
| Mercury-class public DBs | Structured public contact tables (when firm appears) |
| Crossref / Semantic Scholar | Corresponding-author style hits (rare) |
| Cross-check vs Brian / Jop / Jorge sheets | Prefer owned books before crawl |

**Hard gate (attribution):** Email column only if source attributes address to **that person**. Domain-wide harvest alone is not enough. **Stamp published spelling** from the source — never pattern-guess local-part or domain.

---

## ReachGate (Track B — no inbox)

| Channel | Automation | HITL |
|---|---|---|
| Fund IR / contact form | Draft subject+body | Gideon (or designee) submits |
| Calendly / booking | Detect public book URL | Gideon books; blurb prepped |
| WhatsApp | Draft only | WhatsApp desk + Gideon yes |
| Shared Gmail thread | Draft reply | Gideon sends |
| Warm forward (GAWA / Accial / founders) | Draft ask | Gideon sends |

---

## Wave design (method arms over seat batches)

Prefer **method arms** over large seat-only batches:

1. **Filings / regulatory PDF** — EDGAR signature blocks, BCSC/securities PDFs, IAPD where applicable  
2. **`filetype:pdf` + press** — speaker decks, ethics/impact reports, DocuSign PDFs  
3. **Wayback** — single CDX pass on **promising EMPTY** (had mailto hints or old team page), not 403/SPA retry loops  
4. **Domain-alias cleanup** — resolve wrong-entity / parked domains **before** crawl  
5. **Website backfill** — empty `link_mm7gdv8s` only; skip if filled  
6. **Firm team pages** — person `mailto:` co-occurrence with display name  
7. **Press pages** — mailto + name on same page  
8. **Deferred high-yield URL follow-ups** — queue URLs discovered in prior wave  
9. **Second pass** — **only** on promising EMPTY (not generic re-grind)

**Escalate early off generics:** `info@` / `hello@` / `team@` only → treat as **EMPTY** for that method; escalate to PDF / press / filings.  
**Stop early:** 403/SPA after one Wayback pass; parked/wrong-entity domains; personal domains failing firm gate.

**Domain hygiene before crawl** is mandatory.

---

## Yield lessons — deep50 24 Sep 2026

Authoritative lessons from the **deep50 Hands wave** (24 Sep 2026). Encode these into every batch plan and workbench review.

### Throughput reality

- Roughly **~10 citation-grade FOUNDs** across deep50 ≈ **~6% of seats**.
- Hitting a **goal of 50 FOUND** requires **multiple focused method waves** — never a local bot grind on seat-only batches.

### High-yield sources (prioritize)

- Regulatory / securities PDFs (**BCSC**, similar provincial/state filings)
- **SEC EDGAR** signature blocks and exhibit PDFs
- **DocuSign**, ethics, and impact PDFs on firm or fund sites
- Press / news pages with **mailto + person name co-occurrence**
- **Mercury-class** public DBs (structured tables with named contacts)
- Firm **team / people** pages with **person-specific mailto:**

### Low-yield / stop early

- **Generics-only** (`info@`, `hello@`, `team@`) → **EMPTY** for attribution; escalate to PDF / press / filings
- **403 / SPA** → **one Wayback CDX pass**, then move on
- **Parked** or **wrong-entity** domains → fix domain hygiene; do not crawl blindly
- **Personal domains** that fail the firm attribution gate → do not force FOUND
- **LinkedIn-primary** evidence → **HITL hold** (no Sales Nav, no scrape)

### Wave design (recap)

- Prefer **method arms** (filings PDF; `filetype:pdf`/press; Wayback on promising EMPTY; domain-alias cleanup; Website backfill for empty Monday Website) over large seat-only batches
- **Domain hygiene before crawl**
- **Escalate off generics early**
- **Deferred high-yield URL follow-ups** from prior runs
- **Second pass only on promising EMPTY**
- **Stamp published spelling** — never pattern-guess
- **Website column** `link_mm7gdv8s` only; skip if filled; sniff-test noisy domain inferences
- Status: **FOUND** / **EMPTY** / **UNCERTAIN (no stamp)** / **DOMAIN_UNRESOLVED**

### Hands HARD (recap)

All craft via **Cursor Cloud Hands**. Mail Finder Workbench **coordinates**, **reviews**, and applies **Monday/Gmail connector stamps** only **after attribution review**.

Forbidden list unchanged: no Hunter/Apollo, no LinkedIn scrape/Sales Nav/PhantomBuster, no pattern guessing, no invented emails.

---

## Operating rhythm

1. Input CSV: Name, Firm, Domain, Priority, Monday_item_id, LinkedIn (URL only — no scrape).
2. Plan **method wave** (not default “all seats Photon”).
3. Run **Mail Finder Flow** / Hands jobs on wave (P1 first).
4. Output: FOUND / EMPTY / UNCERTAIN / DOMAIN_UNRESOLVED + Source_URL + Checked_URLs + Confidence.
5. FOUND → Monday Contact patch (`email_mm7ffmz4`) after review (desk or Flow with HITL approve).
6. EMPTY → ReachGate channel pick + HITL draft.
7. Weekly light re-run only on new PDFs/filings — not Contact Us spam.

**First cohort:** 8 P1 — Lendable (De Luca, García Llorente), CIM (Arenas, Haar), i80 (Goldstein, Helwani), BBVA Spark (García Acero, González Montes de Oca).

---

## Mail Finder Flow — n8n outline

**Trigger:** Manual / cron / webhook with CSV or Monday “missing Contact” view.

```
[Trigger: batch CSV or method wave]
    → [Normalize: name, firm, domain, monday_id]
    → [Domain hygiene + alias cleanup]
    → [Owned-books match: Brian/Jop/Jorge] ──hit──→ [Review gate]
    → [Method router: filings PDF | press/pdf dork | team mailto | ...]
    → [Photon: site crawl domain] (firm domain only)
    → [Wayback CDX: /team|/people|/about|/contact] (one pass if promising)
    → [theHarvester: domain public emails → attribution filter]
    → [PDF discovery: search + download allowlisted hosts]
    → [pdfgrep: name near @domain]
    → [Registry pass: CNPJ/OpenCorp/EDGAR/IAPD/BCSC by firm country]
    → [Merge + dedupe candidates]
    → [Attribution filter: person-name co-occurrence]
    → [Reject generics-only → escalate arm]
    → [HITL Review gate] ──approve──→ [Monday Contact patch + Notes]
                      └──reject/empty──→ [ReachGate draft queue]
```

**n8n node hints**

- Credentials: none for core public crawl; Monday API for patch; optional Drive for PDF store.
- Rate limits: polite crawl delays; one domain at a time.
- Secrets: Monday token only; no LI cookies.
- Artifacts: write `mail-finder-run-YYYY-MM-DD.csv` + `.json` to Drive / workspace.

**Success metrics**

- % FOUND (Mail Finder) — expect low single-digit % per seat batch; higher per method wave
- % conversations started (ReachGate)
- 0 invented emails; 0 LI scrape jobs

---

## Workbench standup (when Gideon says go)

1. Create agent/workbench **Mail Finder** (or lane under Teclogi desk).
2. Install on box: Photon, theHarvester, pdfgrep/poppler, waybackpy (or curl CDX).
3. Port flow to n8n on VPS (`{type: machine, name: vps}` per CTH Hands norms).
4. Wire Monday board Contact: `email_mm7ffmz4`, Website: `link_mm7gdv8s`, Notes.
5. Pilot: 8 P1 → review CSV with Gideon → only then enable Monday auto-patch.

---

## Naming lock

Use **Mail Finder** in tickets, n8n workflow title (`Mail Finder Flow`), and Monday Notes tags (`MAIL FINDER FOUND` / `MAIL FINDER EMPTY → REACHGATE form`).

Do not use paid-enrichment framing — attribution from public publications and firm sites only.

---

## Changelog

See `mail-finder/protocol/CHANGELOG-2026-09-24.md` for the deep50 yield patch delta.
