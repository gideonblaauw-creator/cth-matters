# Proposed protocol deltas — Mail Finder Workbench Strategy & Hands tickets skill

**Format:** Bullet-only proposals for maintainers. **Do not** apply in this PR to sand-workflow skills unless paired with `mail-finder/protocol/` CHANGELOG (not required for research-only deliverable).

---

## Workbench Strategy

- Add explicit **method-arm roster** with expected yield band: `regulatory-PDF` (high), `press-mailto` (medium), `IAPD-ADV-2B` (medium), `curated-directory` (medium), `live-team-HTML` (low), `Form-D-only-EDGAR` (low), `Wayback-CDX` (low unless prior mailto signal).
- Document **Wave2 evidence**: Form D / bulk EDGAR text arm = 0 FOUND; deferred regulatory PDF = 1 FOUND (Fernando Casado / Inclimo).
- Require **domain hygiene gate** before any crawl arm: resolve parked/wrong Website (`link_mm7gdv8s`) using Wave2 #19 playbook; stamp Website only when blank.
- Define **escalation ladder** per seat: (1) regulatory PDF search → (2) IAPD/BCSC/CNMV → (3) press/podcast → (4) curated directory → (5) one first-party HTML pass → (6) one Wayback CDX on `/team|/about|/people` → STOP (no third HTML pass).
- Add **“generics trap”** rule: after two methods yield only `info@`/`team@`/`ventures@`, seat is **closed EMPTY** unless new URL ticket attached.
- Clarify **Form D usage**: names/roles for pivot only; do not expect email in Form D body ([SEC Form D Item 2](https://www.sec.gov/files/formd.pdf)).
- Add **LatAm/EU impact** source tier: DFI PDFs, CNMV gestora tabs, Colombia/Mexico ethics & governance PDFs (Wave2 + Deep50 FOUND classes).
- Cap parallel Hands at **3–5** with exclusive paths; research outputs live under `mail-finder/research/<date>-<topic>/` only.

---

## Hands tickets skill

- Ticket template field **`method_arm`** (enum): `regulatory_pdf` | `iapd_adv` | `press_mailto` | `directory_mercury` | `team_html` | `wayback_cdx` | `domain_hygiene` | `deferred_url`.
- Ticket template field **`citation_requirement`**: verbatim quote or mailto anchor showing **full name + email** (+ firm gate): copy snippet path in exclusive folder.
- Ticket template field **`forbidden_checklist`**: confirm no Hunter/Apollo, no LinkedIn scrape, no pattern guess, no SMTP verify for this ticket.
- **Pre-flight block** (mandatory): Monday Website populated or explicitly DOMAIN_UNRESOLVED; if hygiene arm changed Website, downstream tickets must reference new domain.
- **Deferred high-yield URL** ticket type: max 5 seats, 1 URL each, 30-minute timebox (Wave2 #20 model).
- **EDGAR ticket** must specify exhibit types (EX-10, EX-99, registration statements) — prohibit “EDGAR name search only” tickets without PDF exhibit target.
- **Wayback ticket** requires **`mailto_signal`**: prior evidence of historical mailto OR older firm site known to list emails; else deny ticket (Wave2 0/18 lesson).
- **HITL tag** for LinkedIn **public post/comment** URL pasted by human; stamp source URL; no automated LinkedIn fetch beyond public HTML already indexed.
- **Status rules** repeat: UNCERTAIN never stamped to Monday; publish **published spelling** for local-part (e.g. Citi `vibhor.rastorgi@citi.com`).
- Post-run **eval handoff**: each wave drops `00-wave2-eval.md`-style summary in dated research folder linking PR and FOUND count toward goal 50.

---

## OSINT tooling (optional Hands appendix)

- **ALLOWED assist:** theHarvester / Photon on **firm domain** — output is **candidate list**; operator marks FOUND only after citation review ([theHarvester README](https://raw.githubusercontent.com/laramies/theHarvester/master/README.md), [Photon README](https://github.com/s0md3v/Photon/blob/master/README.md)).
- **FORBIDDEN modules:** Hunter API, breach/paste modules, SMTP verification CLIs (e.g. HN Email Sleuth pattern+verify class).
- Require **`attribution_filter.md`** snippet in ticket closure: one paragraph tying name, firm, email, URL.

---

## Monday column locks (unchanged — restate)

- Email: `email_mm7ffmz4`
- Website: `link_mm7gdv8s` (Potential Investors only)
- Website stamps **only when blank**; sniff-test noisy firm inferences before write.

---

## Research ↔ protocol feedback loop

- After each multi-arm wave, open research folder `mail-finder/research/YYYY-MM-DD-*` with eval + source catalogue updates.
- Promote deltas from `02-protocol-deltas.md` into skills when FOUND rate per arm changes by ≥2x or new forbidden community pattern appears (e.g. new scrape extension named in r/coldemail).
