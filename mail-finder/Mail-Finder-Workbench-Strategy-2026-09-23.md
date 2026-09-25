# Mail Finder Workbench — Strategy & n8n Flow Spec
**Date:** 23 Sep 2026  
**Owner:** Teclogi desk (CTH Growth / IR)  
**Client:** Teclogi Series A  
**Status:** Named + specified (HITL). Build workbench + n8n when Gideon says go.  
**Name lock:** **Mail Finder** (was draft name CiteMail — superseded).

---

## Name

| Layer | Name | What it is |
|---|---|---|
| **Stack** | **Mail Finder** | Open-source / public-web attribution stack for `person@firm` emails |
| **Workbench** | **Mail Finder Workbench** | Desk + automations that run Mail Finder + ReachGate |
| **n8n flow** | **Mail Finder Flow** | Automated pipeline under the workbench |
| **Companion lane** | **ReachGate** | Reach *without* corporate inbox (forms, Calendly, WhatsApp HITL, warm forwards) |

**Tagline:** Only store an email if a public source cites it next to the named person.

**Out of scope:** Paid finders (Hunter/Apollo/etc.), LinkedIn scrape / Sales Nav / PhantomBuster email jobs, pattern guessing, SMTP verify on invented addresses, LI ToS violations.

---

## Goal

For Teclogi capital contacts missing Contact email:

1. **Mail Finder** finds verified `person@firm` (or personal domain) from publications, team pages, filings, PDFs, Wayback, firm-site crawl.
2. **ReachGate** starts a conversation when Mail Finder returns EMPTY (form / Calendly / WhatsApp / shared thread / warm intro).
3. Monday Contact stays clean: FOUND → patch; EMPTY → Notes stamp only (no fake email).

---

## Mail Finder stack (tools)

| Tool | Role in flow |
|---|---|
| Web search / dorks | `"Name" "@domain"` / `filetype:pdf` / conference names |
| **Photon** (or equivalent site crawler) | Crawl *firm domain only* for mailto + PDF links |
| **Archive.org CDX / Wayback** | Historical `/team` `/people` `/about` mailto: |
| **theHarvester** | Domain-indexed public emails → **human filter** to named person |
| **pdfgrep / pdftotext** | Extract name + email from speaker / corp PDFs |
| OpenCorporates / CNPJ / EDGAR / IAPD | Filings & registries (Anderson Thees pattern) |
| Crossref / Semantic Scholar | Corresponding-author style hits (rare) |
| Cross-check vs Brian / Jop / Jorge sheets | Prefer owned books before crawl |

**Hard gate:** Email column only if source attributes address to **that person**. Domain-wide harvest alone is not enough.

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

## Operating rhythm

1. Input CSV: Name, Firm, Domain, Priority, Monday_item_id, LinkedIn (URL only — no scrape).
2. Run **Mail Finder Flow** on batch (P1 first).
3. Output: FOUND / EMPTY + Source_URL + Checked_URLs + Confidence.
4. FOUND → Monday Contact patch (desk or Flow with HITL approve).
5. EMPTY → ReachGate channel pick + HITL draft.
6. Weekly light re-run only on new PDFs/filings — not Contact Us spam.

**First cohort:** 8 P1 — Lendable (De Luca, García Llorente), CIM (Arenas, Haar), i80 (Goldstein, Helwani), BBVA Spark (García Acero, González Montes de Oca).

---

## Mail Finder Flow — n8n outline

**Trigger:** Manual / cron / webhook with CSV or Monday “missing Contact” view.

```
[Trigger: batch CSV]
    → [Normalize: name, firm, domain, monday_id]
    → [Owned-books match: Brian/Jop/Jorge] ──hit──→ [Review gate]
    → [Photon: site crawl domain]
    → [Wayback CDX: /team|/people|/about|/contact]
    → [theHarvester: domain public emails]
    → [PDF discovery: search + download allowlisted hosts]
    → [pdfgrep: name near @domain]
    → [Registry pass: CNPJ/OpenCorp/EDGAR/IAPD by firm country]
    → [Merge + dedupe candidates]
    → [Attribution filter: person-name co-occurrence]
    → [HITL Review gate] ──approve──→ [Monday Contact patch + Notes]
                      └──reject/empty──→ [ReachGate draft queue]
```

**n8n node hints**
- Credentials: none for core public crawl; Monday API for patch; optional Drive for PDF store.
- Rate limits: polite crawl delays; one domain at a time.
- Secrets: Monday token only; no LI cookies.
- Artifacts: write `mail-finder-run-YYYY-MM-DD.csv` + `.json` to Drive /workspace.

**Success metrics**
- % FOUND (Mail Finder)
- % conversations started (ReachGate)
- 0 invented emails; 0 LI scrape jobs

---

## Workbench standup (when Gideon says go)

1. Create agent/workbench **Mail Finder** (or lane under Teclogi desk).
2. Install on box: Photon, theHarvester, pdfgrep/poppler, waybackpy (or curl CDX).
3. Port flow to n8n on VPS (`{type: machine, name: vps}` per CTH Hands norms).
4. Wire Monday board `18425305222` Contact + Notes columns.
5. Pilot: 8 P1 → review CSV with Gideon → only then enable Monday auto-patch.

---

## Naming lock

Use **Mail Finder** in tickets, n8n workflow title (`Mail Finder Flow`), and Monday Notes tags (`MAIL FINDER FOUND` / `MAIL FINDER EMPTY → REACHGATE form`).

Do not use paid-enrichment framing — attribution from public publications and firm sites only.

---

## Yield lessons — deep50 (24 Sep 2026)

Synced to workbench skill [Mail Finder Hands tickets](sand-workflow:mail-finder-hands-tickets). Hands wave ~10 citation-grade FOUNDs (~6% seats). Goal 50 → multiple **method** micro-Hands waves, never local bot grind.

### High-yield evidence (prioritize)
- Regulatory / securities PDFs with name + email + signature (e.g. BCSC Form 45-106F1)
- SEC EDGAR exhibits / signature blocks — stamp **published** local-part spelling
- DocuSign / ethics / impact-finance PDFs binding person ↔ mailbox
- Press / industry pages where `mailto:` co-occurs with the person name
- Curated public investor directories (Mercury-class) — not paid finders
- Firm team pages with real person `mailto:`

### Low-yield / stop early
- Generics-only (`info@`, `hello@`, `team@`, `ventures@`) → EMPTY; escalate to PDF/press/filings (do not deepen HTML grind)
- 403 / bot walls / SPAs without personal mailto → one Wayback CDX on `/team|/about|/people`, then move on
- Parked or wrong-entity domains; personal domains that fail firm gate
- LinkedIn as primary source → HITL hold (no Sales Nav / scrape / PhantomBuster)

### Wave design (success-rate)
1. **Method arms** over large seat-only batches: filings/EDGAR; filetype:pdf + press; Wayback on promising EMPTY; domain-alias cleanup; **Website backfill** for empty Monday Website (`link_mm7gdv8s`, Potential Investors only).
2. Domain hygiene before crawl (alias + live-vs-parked).
3. Escalate off generics early.
4. Ticket deferred high-yield URLs as short follow-up Hands.
5. Second pass only on promising EMPTY; drop Pass / wrong-entity / generics-after-two-methods.
6. Never pattern-guess or “correct” published spellings.
7. Website stamps only when blank; sniff-test noisy firm inferences.
8. Cap 3–5 parallel Hands; exclusive paths; workbench stamps Email/Website after attribution review.

### Monday columns (lock)
- Email: `email_mm7ffmz4`
- Website: `link_mm7gdv8s` only

### Status
FOUND | EMPTY | UNCERTAIN (do not stamp) | DOMAIN_UNRESOLVED

---

## Standard loop (LOCKED 25 Sep 2026 — Gideon GO)

Source: `STANDARD-LOOP-PROPOSAL-2026-09-25.md` (W1–W4 lessons). Skill: Mail Finder Hands tickets.

### Goal
+100 new citation-grade Contact emails on Potential Investors board `18425305222` (baseline post-W3 ~28; post-W4 live **39** / +11; gap ~89). Campaign window for daily n8n assist: **through 31 Oct 2026**.

### Unit of work
One **wave** = Email-blank **person-named** cohort → parallel **method arms** (cloud Hands, exclusive paths) → workbench attribution review + Monday stamp → deferred ledger → next wave.

### Hard gates
- Non-blank `contact_name` on email arms; firm-only / blank-name → Website hygiene only
- FOUND = person name + `person@firm` co-occurrence on same public artifact; published spelling only
- No Hunter/Apollo; no LinkedIn scrape / Sales Nav / PhantomBuster; **no Pattern+SMTP**; no invented emails
- Hands craft only; workbench stamps Email `email_mm7ffmz4` / Website `link_mm7gdv8s` after review (HITL before any outbound send)
- Statuses: FOUND | EMPTY | UNCERTAIN (do not stamp) | DOMAIN_UNRESOLVED
- Quiet mid-wave: merge EMPTY silent; ping FOUND / HOLD / wave gate
- Parallel: **4–8** cloud micro-Hands (`composer-2.5` + Fast ON); VPS one writer per shared path

### Method ladder (run in order; stop early)
1. Domain / Website hygiene (W2)
2. Team person mailto
3. Press / speaker mailto (W4 highest)
4. Impact / DocuSign / ethics PDFs (W1)
5. Regulatory **with mailbox** — not Form D name-only (W2)
6. Directories with **visible** mailto
7. One Wayback CDX if promising (not blind)
8. Deferred URL harvest (W2/W4)

### Cross-wave lessons (compressed)
| Wave | Yield signal | Loop implication |
|------|-------------:|------------------|
| W1 deep50 | ~10 FOUNDs; regulatory/DocuSign/press/team | Method arms; prioritize those classes |
| W2 | +1 deferred PDF; hygiene fixed Websites; Form D/Wayback 0 | Hygiene first; no blind Form D/Wayback |
| W3 | +1 hygiene; Pattern+SMTP refused | No Pattern+SMTP; don’t recycle exhausted EMPTY without new leads |
| W4 | +11; press best; deferred recovered; blind EDGAR/Wayback/CNPJ ≈0 | Person-named only; press+PDF+deferred first |

### Permanent HOLDs (skip email arms)
Bill Irvine, Claudia Akel, Gabriela Herculano, Juan Aparicio (LinkedIn-primary / weak attribution).

### n8n — Mail Finder Flow (daily assist through 31 Oct 2026)
- **WF to run:** **Mail Finder Flow** (`mail-finder/n8n/mail-finder-flow.json` → import title **Mail Finder Flow** on n8n-li `https://n8n-li.cleantechhub.net/`).
- **Schedule target:** cron `0 2 * * *` TZ `America/Bogota` (daily **02:00 COT**), **active only through 2026-10-31** (disable / expire after that date).
- **Today’s JSON state:** Manual triggers only (batch CSV + HITL gate). Scheduling requires adding a Schedule node + end-date guard; keep HITL before Monday Contact patch.
- **Not this job:** Teclogi Pass Watch (07:55 weekday Pass detect) — different purpose.
- **Ops:** Hands plant/activate on VPS `/opt/n8n-li`; dry-run inactive first; never LinkedIn creds; Monday auto-patch stays HITL until Gideon greenlights.

### Wave5+
Seed from fresh Monday Email-blank **person-named** queue only. Prefer ladder steps 1→3→4→8 over blind L04/L08/L10-style sweeps.

