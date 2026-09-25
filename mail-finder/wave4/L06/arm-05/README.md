# Mail Finder — Wave4 / L06 / Arm 05

**Focus:** Public **press releases**, **podcast/show notes**, **conference agendas**, and **speaker pages** with visible **name + personal email / mailto** co-occurrence on the same page.

## Input

`input.csv` — 5 seats (Monday CRM export).

## Method (`press_podcast_speaker_mailto`)

1. Discover publisher-controlled press, podcast, event, and speaker URLs for each seat (first-party or reputable media).
2. Open rendered HTML/PDF; require target **display name** and exact **non-generic person@** mailbox (or `mailto:` target) on the **same artifact**.
3. **FOUND** → record email, source URL, citation excerpt; add to `stamp-list.json`.
4. **EMPTY** → generics, wrong person’s PR contact on same page, contact forms, social-only, or no co-occurrence.
5. **Prohibited:** Hunter/Apollo, LinkedIn/Sales Navigator scraping, pattern guessing, SMTP verification, invented emails, paid/authenticated sources, Monday writes.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | One row per seat: `Status` (`FOUND` \| `EMPTY` \| `UNCERTAIN`); non-blank `Checked_URLs` |
| `stamp-list.json` | FOUND only: `Monday_item_id`, `Email`, `Source_URL`, `Evidence_excerpt` |
| `summary.md` | Scorecard |
| `evidence/` | URL index, negative excerpts, saved page snapshots |

## Result (2026-09-25)

**0 FOUND / 5 EMPTY** — see `summary.md`.

## Scope

Write **only** under `mail-finder/wave4/L06/arm-05/`.  
Do **not** modify other arms or Monday.

## Re-run hints

```bash
UA='MailFinderResearch/1.0 (cth-matters; L06-arm05) contact-research@example.com'
EV=mail-finder/wave4/L06/arm-05/evidence
curl -sL -A "$UA" -o "$EV/spin-hoi-press.html" \
  'https://spin.vc/2024/11/17/spin-ventures-partners-with-house-of-impact-2024-to-promote-circularity/'
curl -sL -A "$UA" -o "$EV/einpresswire-genlogs.html" \
  'https://www.einpresswire.com/article/889760480'
```

Search log: `evidence/url-index.md`, `evidence/negative-excerpts.md`.
