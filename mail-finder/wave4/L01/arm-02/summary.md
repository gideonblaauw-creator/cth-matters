# Wave 4 L01 Arm 02 — Domain hygiene scorecard

**Input seats:** 19 (from `wave4-l01-arm02.csv`)  
**Run date:** 2026-09-25

## Status counts

| Status | Count |
|--------|------:|
| WEBSITE_OK | 13 |
| WEBSITE_MAPPED | 4 |
| WEBSITE_CORRECTED | 2 |
| DOMAIN_UNRESOLVED | 0 |
| FOUND | 0 |
| EMPTY | 0 |

## Corrections

- **13028360241** (Alfredo Neila): `plasticrepairsystem.com` → `https://www.plasticrepair.eu/` (non-resolving / timeout).
- **13100509887** (Andrés Saborido): `telefonica.com` → `https://wayra.com/` (parent corp vs Wayra investment entity).

## Canonical mappings (same entity)

- Congruent Ventures, Angel Ventures, Atlantico, Amplifica Capital: apex → `www` canonical host (HTTP 200 after redirect).

## Email discovery

No first-party team page with person name + non-generic `mailto:` co-occurrence. `stamp-list.json` is empty.

## Notes

- **bii.co.uk** and **clocktowerventures.com** return bot-mitigation (Cloudflare / SiteGround captcha) to automated fetch; treated as live firm sites based on redirect target and public firm profiles.
- **hyatt.com** verified as Hyatt Hotels corporate site (employer for Ana Lucía Rodhas Alcántara CSR role; not a VC fund domain).
