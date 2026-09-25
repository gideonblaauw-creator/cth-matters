# Wave4 L08 Arm 04 — Wayback CDX negative evidence

One CDX lookup per seat on `/team`, `/about`, or `/people` only. **FOUND** requires target **name** and **person@firm** (or `mailto:`) on the same archived page.

## Anna Raptis — Amplifica Capital (`EMPTY`)

- **CDX target:** `amplifica.capital/team` → **0 captures** (`cdx-amplifica-team.json`: `[]`).
- Live `https://amplifica.capital/team` → 404. Site uses `/aboutus`, outside allowed paths for this arm.

## Aquilino Peña — Kibo Ventures (`EMPTY`)

- **CDX target:** `kiboventures.com/team` → multiple 200 captures; reviewed:
  - [2026-06-10 snapshot](https://web.archive.org/web/20260610210505/https://www.kiboventures.com/team) — **Aquilino Peña** on team roster; **0** `@kiboventures.com` / `mailto` on page.
  - [2019-01-17 snapshot](https://web.archive.org/web/20190117071833/http://kiboventures.com/team/) — bio block: `<span>Aquilino Peña</span>`; no email addresses in HTML.

## Asia Agnelli — TMV (`EMPTY`)

- **CDX target:** `tmv.vc/team` → captures through 2026; reviewed:
  - [2026-06-11 snapshot](https://web.archive.org/web/20260611032402/https://www.tmv.vc/team) — lists **Azzi Agnelli** (not **Asia Agnelli**); only generic `team@tmv.vc`.
  - [2023-05-30 snapshot](https://web.archive.org/web/20230530041330/https://tmv.vc/team/) — no **Asia Agnelli**; footer `mailto:hi@tmv.vc` (generic).

## Belkacem Hammoulhadj — Greenbull (`EMPTY`)

- **CDX target:** `greenbull.com/team` → **0 captures** (`cdx-greenbull-team.json`: `[]`). Live `/team` → 404.

## Benjamin Radomski — BEV Family Office (`EMPTY`)

- **CDX target:** `bevfamilyoffice.com/team` → **0 captures** (`cdx-bev-team.json`: `[]`). Live `/team` → 404.
