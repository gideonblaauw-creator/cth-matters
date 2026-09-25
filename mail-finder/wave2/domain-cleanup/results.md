# Mail Finder Wave 2 — Domain cleanup (METHOD ARM)

**Board:** 18425305222 (Potential Investors) · **Website column:** `link_mm7gdv8s` (stamp list only)  
**Run:** 2026-09-25 · **Seats:** 16 · **Method:** public firm About/Team/Press/registry resolve — no Hunter/Apollo, no LinkedIn scrape, no pattern guessing

## Summary

| Status | Count |
|--------|------:|
| EMPTY (domain resolved, no citation-grade person email) | 15 |
| DOMAIN_UNRESOLVED | 1 |
| FOUND | 0 |

## Domain hygiene

| Verdict | Seats |
|---------|------:|
| PARKED / wrong entity on Monday Domain | Alistair (783capital.com), Dennis (checkmatecap.com), Gioberto (arxus.com), Kai (andeshorizon.com) |
| Legacy / non-resolving alias | Asia (tmv.com→tmv.vc), Fernando (rumbo.vc→rumbo.ventures), Jean-Marc (senecaimpact.com→.earth), Monica (mayacapital.co→maya.capital) |
| Wrong corporate root | Juan Franck (softbank.com→latinamericafund.com) |
| Dead board alias + personal site rejected | Philippe (itauventures.com.br→itau.com.br/ventures; reject schlumpf.xyz) |
| OK / canonical redirect | George, Ingo, Lucas, Maite, Franck (electis.io→electis.com) |
| No verified firm website | Victoria But (Sun East family office) |

## Website stamp list

15 seats with live verified firm URLs → `website-stamp-list.csv` (Monday Website blanks only; Victoria excluded).

## Email

No citation-grade person@firm mailto found on newly resolved domains after hygiene pass. Prior deep50 conclusions retained; no `found-for-monday.csv`.

## Notable resolutions

- **783 Partners:** [783partners.com/team](https://www.783partners.com/team) lists Alistair Langer; 783capital.com is parked.
- **TMV:** [tmv.vc/team/azzi-agnelli](https://www.tmv.vc/team/azzi-agnelli) — board name Asia Agnelli maps to Azzi Agnelli at Trail Mix Ventures.
- **SoftBank LatAm:** [latinamericafund.com](https://www.latinamericafund.com/) is the fund’s public site (Juan Franck role corroborated via fund press/board pages, not softbank.com alone).
- **Itaú Ventures:** Official page [itau.com.br/ventures](https://www.itau.com.br/ventures); `itauventures.com.br` does not resolve.
- **Andes Horizon Capital:** [andeshorizoncapital.com/en/nosotros/](https://andeshorizoncapital.com/en/nosotros/) — distinct from game studio on andeshorizon.com.

## Deliverables

- `input.csv` — wave2 seat export  
- `results.csv` / `results.md` — classifications  
- `website-stamp-list.csv` — Monday Website stamps (no API writes)
