# L06 arm-04 — Public press / podcast / speaker research notes

**Run date:** 2026-09-25  
**User-Agent:** `MailFinderResearch/1.0` (all fetches via `curl -sL -A 'MailFinderResearch/1.0'`)  
**Method:** Public HTML/PDF only — conference speaker pages, firm news, podcast show pages, LAVCA/Innovation Zero listings, portfolio-adjacent press, `senecaimpact.earth` perspectives, `netradyne.com` news/press.  
**Excluded as non-valid:** Hunter/Apollo/LinkedIn scrape, email-pattern guessing, role/generic inboxes (`press@`, `info@`, `hello@`, `contact@`, `bookings@`, `team@`, `impact@`, etc.).

**Evidence cache:** `evidence/fetched/` (134 snapshots from this arm).

---

## 1. Michal Lasocki (EEC Ventures — `eecventures.com`)

**Monday item:** `13028367245`

### URLs checked (HTTP status)

| URL | HTTP | Name on page? | Personal email co-occurring? |
|-----|------|---------------|------------------------------|
| https://www.eecventures.com/en/eec-ventures/ | 200 | Yes (Michał Lasocki, Partner) | No — no mailbox on page |
| https://www.eecventures.com/en/contact/ | 200 | No (generic contact page) | No — `contact@eecventures.com` only (generic) |
| https://www.eecventures.com/en/ | 200 | Yes (team tile) | No |
| https://www.eecventures.com/eec-ventures/ | 200 | Yes | No — footer `contact@eecventures.com` (generic, not name-attributed) |
| https://www.eecventures.com/kontakt/ | 200 | — | No — generic firm contact |
| https://www.eecventures.com/portfolio/ | 200 | No | No |
| https://www.eecventures.com/en/portfolio/ | 200 | No | No |
| https://www.eecventures.com/en/eec-magenta-funds/ | 200 | No | No |
| https://startuppoland.org/fundusz/eec-magenta/ | 200 | Yes (MICHAŁ LASOCKI in fund team) | No — `contact@eecventures.com`, `kontakt@startuppoland.org` only |
| https://www.failory.com/blog/venture-capital-firms-warsaw | 200 | Yes (EEC row cites Lasocki as founder) | No — row lists generic `contact@eecventures.com`; other emails are other firms |
| https://topautomotive.pl/prelegenci/michal-lasocki/ | 200 | Yes (speaker bio) | No — page lists **event organizer** mailto addresses (`katarzyna.czajka@sqda.pl`, `marta.skalik@sqda.pl`, etc.), not Lasocki |
| https://innovationzero.com/speakers | 200 | No | No |
| https://www.innovationzero.com/speakers | 200 | No | No |
| https://www.innovationzero.com/speakers/michal-lasocki | 404 | — | — |

Additional probes (portfolio / news): `lekta.ai`, `icsec.pl/kontakt` — no Lasocki + personal email co-occurrence.

### Result: **EMPTY**

**Why empty:** Multiple first-party and third-party **speaker/press/directory** pages confirm identity but publish only **generic** `contact@eecventures.com` or unrelated organizer emails. No public page found with **Michal/Michał Lasocki** and a **non-generic personal** mailbox on the same page.

---

## 2. Miheer Chanrai (Climate Capital — `climate.capital`)

**Monday item:** `13028372212`

### URLs checked

| URL | HTTP | Name on page? | Personal email co-occurring? |
|-----|------|---------------|------------------------------|
| https://climate.capital/about-1 | 200 | No (firm narrative only) | No |
| https://climate.capital/contact-1 | 200 | No | No — contact via embedded form; no `@climate.capital` in HTML |
| https://climate.capital/home | 200 | No | No |
| https://climate.capital/about | 200 | No | No |
| https://www.climatecapitalsummit.com/ | 200 | No | No — `events@equal.vc` (generic, unrelated to Chanrai) |
| https://climatecapitalsummit.com/ | 200 | Same | No |
| https://innovationzero.com/speakers | 200 | No | No |
| https://www.innovationzero.com/speakers | 200 | No | No |
| https://one-world-admin.squarespace.com/virtual-impact-summit | 200 | Yes (guest list: “Miheer Chanrai”) | No — name appears in LinkedIn-only guest roster; page emails are `info@oneworld.training` etc., not Chanrai |
| https://www.aspect.ac.uk/ | 200 | No | No |
| https://www.greenangelsyndicate.co.uk/ | 200 | No | No |
| https://equal.vc/ | 200 | No | No |
| https://www.zedify.co.uk/ | 200 | No | No |
| https://nakedenergy.co.uk/ | 200 | No | No |

**Not used:** Companies House / SEC / LinkedIn (out of lane). Podcast hits in search were for a **different** “Miheer Walavalkar”, not Chanrai.

### Result: **EMPTY**

**Why empty:** Climate Capital’s public site and common conference/summit pages do not expose `person@climate.capital` alongside **Miheer Chanrai**. Innovation Zero speaker index (2026 fetch) did not list him; One World 2020 agenda lists the name without a personal email.

---

## 3. Monica Saggioro Leal (Maya Capital — `maya.capital`)

**Monday item:** `13100511303`

### URLs checked

| URL | HTTP | Name on page? | Personal email co-occurring? |
|-----|------|---------------|------------------------------|
| https://www.maya.capital/team | 200 | Yes | No — LinkedIn links only, no mailto |
| https://www.maya.capital/ | 200 | No | No |
| https://www.maya.capital/contact | 200 | No | No |
| https://www.maya.capital/portfolio | 200 | No | No |
| https://maya.capital/blog | 200 | No | No |
| https://www.lavca.org/people/monica-saggioro/ | 403 | — | Blocked from this environment |
| https://www.lavca.org/wp-content/uploads/2025/08/LAVCA_Startup-Ecosystem-Insights_2025.pdf | 200 | PDF text: no Monica + email line match | No |
| https://neofeed.com.br/podcasts/cafe-com-investidor/podcast-cafe-com-investidor-41-monica-saggioro-cofundadora-da-maya-capital/ | 200 | Yes (podcast title & body) | No — no `@` address in page source |
| https://globalhub.uninter.com/talking-business-startups-na-america-latina/ | 200 | Yes (speaker bio) | No — no email in page source |
| https://www.listennotes.com/podcasts/the-j-curve-with/monica-saggioro-maya-capital-9g2JknFLKaP/ | 403 | — | — |
| https://www.vcsheet.com/who/monica-saggioro-leal | 403 | — | — |

### Result: **EMPTY**

**Why empty:** First-party team page and multiple **podcast / webinar speaker** pages name Monica Saggioro (Leal) but contain **no non-generic personal email** on the same page. LAVCA people profile and some aggregators returned **403** here; LAVCA 2025 ecosystem PDF did not contain name + personal email co-occurrence.

---

## 4. Nathalie Couët (CRM: `senecaimpact.com` → live org `senecaimpact.earth`)

**Monday item:** `13028366958`

### A. Seneca Impact Advisors (requested lane)

| URL | HTTP | Couët on page? | Personal `@senecaimpact` co-occurring? |
|-----|------|----------------|--------------------------------------|
| https://senecaimpact.earth/about-us/the-team/ | 200 | **No** (not on team roster) | No |
| https://senecaimpact.earth/contact/ | 200 | No | No — `impact@senecaimpact.earth` only (generic) |
| https://senecaimpact.earth/perspective/seneca-championing-nature-smart-business/ | 200 | No | No |
| First **40** URLs in `perspective-sitemap.xml` (curl each) | 200 | **No** “Couët/Couet/Nathalie” hits | No |

**Seneca lane:** **EMPTY** — no publication/team page ties **Nathalie Couët** to a non-generic `@senecaimpact.earth` / `@senecaimpact.com` address (consistent with prior wave: CRM entity likely ≠ her public profile as Couët Strategic Advisors / HYDGEN CMO).

### B. Other public speaker / press pages (same person)

| URL | HTTP | Name? | Personal email? |
|-----|------|-------|-----------------|
| https://women-in-green-hydrogen.net/nathalie-couet/ | 200 | Yes | **Yes** — see FOUND below |
| https://www.gasworld.tv/webinar-program/2026-electrolysers-1/ | 200 | Yes (panelist) | No — `info@gasworld.com` only |
| https://www.gaebler.com/Funded-Company-CFF32BBC-D1AD-4715-8903-5A4D940AABBD-Hydgen | 200 | Yes (mgmt table) | No — firm `info@hyd-gen.com` only |
| https://www.hyd-gen.com/ | 200 | No | No |
| https://www.hyd-gen.com/contact | 404 | — | — |
| https://www.gofractional.com/member/nathalie-couet | 403 | — | — |
| https://couet-strategy.com/ / `www` | NXDOMAIN / fail | — | — |

### Result: **FOUND** (public speaker profile — not Seneca domain)

**Citation URL:** https://women-in-green-hydrogen.net/nathalie-couet/  
**Email:** `nathalie@couet-strategy.com`  
**Excerpt (same page, HTML):**

```html
<h1 class="entry-title" itemprop="headline">Nathalie Couët</h1>
...
<a href="mailto:nathalie@couet-strategy.com" class="social-media-email">
```

Plain-text window: “Nathalie Couët … Advisor | Couet Strategic Advisors & CMO | HYDGEN …” with mailto on the speaker card.

**Note for desk:** Treat as **person-level** public cite for Nathalie Couët; **not** `@senecaimpact.earth`. Seneca-specific search remains **EMPTY**.

---

## 5. Netradyne (firm seat — label “Netradyne”)

**Monday item:** `13052203004`

### URLs checked (sample + press lane)

| URL | HTTP | “Netradyne” + personal email? |
|-----|------|------------------------------|
| https://www.netradyne.com/company/contact | 200 | Firm name yes; only `press@`, `driveri@`, `support@`, `partnersupport@` (all generic per brief) |
| https://www.netradyne.com/company/news/ | 200 | Listing only |
| https://www.netradyne.com/news/netradyne-strengthens-leadership-team-with-new-cfo-and-coo-appointments | 200 | **FOUND** |
| https://www.netradyne.com/news/netradyne-celebrates-10th-anniversary-with-cross-country-customer-obsession-tour | 200 | **FOUND** |
| https://www.netradyne.com/news-press/netradyne-celebrates-10th-anniversary-with-cross-country-customer-obsession-tour | 200 | **FOUND** |
| https://www.netradyne.com/news-press/netradyne-driver-i-named-ai-safety-solution-of-the-year-in-2025-ai-breakthrough-awards-program | 200 | **FOUND** (`sarah.duckett@netradyne.com`) |
| https://www.netradyne.com/news-press/netradyne-strengthens-leadership-team-with-new-cfo-and-coo-appointments | 404 | — |
| Additional `/news/` and `/news-press/` releases (12+ fetched) | mostly 200 | Many releases: **no** personal media contact in body; several repeat same media footer |

### Result: **FOUND**

**Primary citation URL:** https://www.netradyne.com/news/netradyne-strengthens-leadership-team-with-new-cfo-and-coo-appointments  
**Email:** `sarah.duckett@netradyne.com` (personal/local-part; not in generic denylist)  
**Excerpt:**

> … Stay up to date with **Netradyne** on LinkedIn … **Media Contact** Sarah Duckett Senior Communications Manager **sarah.duckett@netradyne.com**

Same block on 10th-anniversary press URL (`Communications Lead` title variant).

**Why valid for firm seat:** Page is Netradyne-owned press release; firm name and **named media contact** personal email co-occur in the standard “Media Contact” footer (`press@netradyne.com` on same page is **ignored** as generic).

---

## Summary table

| Seat | Status | Email (if FOUND) | Best public URL |
|------|--------|------------------|-------------------|
| Michal Lasocki | EMPTY | — | — |
| Miheer Chanrai | EMPTY | — | — |
| Monica Saggioro Leal | EMPTY | — | — |
| Nathalie Couët | **FOUND** (speaker; not Seneca) | `nathalie@couet-strategy.com` | https://women-in-green-hydrogen.net/nathalie-couet/ |
| Nathalie Couët @ Seneca | EMPTY | — | — |
| Netradyne (firm) | **FOUND** | `sarah.duckett@netradyne.com` | https://www.netradyne.com/news/netradyne-strengthens-leadership-team-with-new-cfo-and-coo-appointments |

---

## Negative / blocked notes

- **403:** `lavca.org/people/monica-saggioro/`, Listen Notes, VC Sheet, Go Fractional — could not verify HTML from this environment.
- **Search engines:** DuckDuckGo/Bing HTML endpoints returned empty result links from the VM; URL discovery supplemented via sitemaps, prior desk indexes, and targeted public URLs (not paid contact databases).
- **RocketReach / Mintround / NeverBounce / pattern pages:** deliberately not used as citations (paid/pattern lane).
