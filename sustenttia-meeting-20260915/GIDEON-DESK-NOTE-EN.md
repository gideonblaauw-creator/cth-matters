# Desk note for Gideon (English) — Sustenttia meeting pack 15 Sep 2026

**Meeting:** Juan Guarin + Javier Serrano (tomorrow)  
**Status:** All artifacts are **drafts**. Nothing sent. HITL required before any client communication.

---

## What's ready

| Deliverable | Location | Public URL |
|-------------|----------|------------|
| Platform Explain (ES) | `/workspace/sustenttia-platform-explain-20260914/` | https://sustenttia-platform-explain-2026091.vercel.app/ |
| Features fuera SoW + hours (ES) | `/workspace/sustenttia-features-fuera-sow-20260914/` | https://sustenttia-features-fuera-sow-20260.vercel.app/ |
| Build progress deck (existing) | `/workspace/sustenttia-build-progress-20260914/` | https://sustenttia-build-progress-20260914.vercel.app/ |
| Client review pack (existing) | — | https://sustenttia-client-review-20260914-c.vercel.app/ |
| HITL workbook | `/workspace/sustenttia-meeting-20260915/sustenttia-hitl-workbook-20260915.xlsx` | Attach / Drive — your call |
| Email draft (ES) | `/workspace/sustenttia-meeting-20260915/EMAIL-DRAFT-ES.md` | Do not send yet |

**Meeting folder:** `/workspace/sustenttia-meeting-20260915/`

---

## What's sourced vs estimate

### Hours (Gideon) — do not change without source

| Period | Hours | Label |
|--------|-------|-------|
| Anexo 21 May 2026 | **46.5 h** | **Sourced** (Anexo) |
| Through 14 Aug 2026 | **131.5 h** | **Sourced** |
| Through 26 Aug 2026 | **147.5 h** | **ESTIMATE** (documented in hours/ update) |
| 1–14 Sep 2026 | — | **Pendiente de consolidar** — no timesheet on VM |

The features doc and email use this framing only. Sep line needs your timesheet before invoicing or client-facing hour claims.

### Workbook caveat

Base template `docs/juan-hitl/sustenttia-template-first-workbook.xlsx` was **not available** on this VM (sustenttia-v2 repo inaccessible). Workbook was **rebuilt** from:

- 5 HITL tabs (narración, BP, riesgos, plantillas, biblioteca from `biblioteca-juan-definitiva-2026-09-03.xlsx`)
- `Pendientes_Cliente` tab from session notes + deck structure
- Seed rows marked `PENDIENTE_JUAN` where appropriate

**Your HITL:** Skim workbook tabs; replace seed rows with live data from VPS/Drive if you have the canonical template.

### Anexo §II fuera de alcance

Full Anexo docx was not on VM. Features list uses deck PR refs (#40, #56, #45–48, #60–#67) + session dump (Sep 11). Summary box in features doc says "ver documento fuente en Drive/VPS."

---

## Your HITL before send

1. **Dashboard credentials** — Included in email draft §3 (`app.sustenttia.com/dashboard`); temp passwords HITL-only, not in Platform Explain.
2. **Attach workbook** — Replace `[PLACEHOLDER]` in email with Drive link or attachment.
3. **Fillout Comentarios** — **ALREADY LIVE since 12 Sep 2026** (~12:57 UTC / 7:57 AM Bogotá) on form `w1tryPCL7sus` (FIL-001/002: ALWAYS 8→93, CONDITIONAL 85→0, MISSING 1→0; scoring/text untouched; spot-check PASS Energía Q4 + Residuos Q1). Client validates live; **no publish decision needed**.
4. **Hours Sep line** — Consolidate 1–14 Sep before client sees hours table; or leave as "Pendiente" (current state).
5. **Skim decks/docs** — Slides 10–11 of build deck + pack URLs against live state.
6. **Send email** — Only after you approve `EMAIL-DRAFT-ES.md`.

---

## Distinction: client pendings vs CTH eng backlog

Per `juan-3pass-vs-recs` framing (not on VM; applied from brief):

- **Client pendings** → `Pendientes_Cliente` tab (Juan/Javier content, taxonomy, library curation, pack feedback).
- **CTH eng** → PR merges, gate tuning, re-bench — not listed as client homework.

---

## Deploy notes

Static HTML deployed to Vercel from `cth-matters` branch `cursor/sustenttia-meeting-pack-20260915-2da1`. Sustenttia teal branding throughout; no CTH lime.

**Vercel alias note:** Long project names truncate (e.g. `…20260914` → `…2026091` / `…20260`). Use the working aliases above, not the idealized long names.
