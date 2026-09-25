# Deferred high-yield URL index — L09 Arm 03

Seats reused from Wave4 **L01 Arm 05** (domain hygiene) and **L05 Arm 07** (impact/LP PDF) closeouts. Each row: primary hinted URL + one same-domain expand.

| Seat | Hinted URL (prior closeout) | Same-domain expand | Outcome |
| --- | --- | --- | --- |
| Humberto Matsuda | `https://overboost.me/` (L01 corrected homepage) | `https://kamayventures.com/` (linked instrument from Overboost) | Team lists Matsuda; only `speed@overboost.me` / `hola@kamayventures.com` generics — no person bind |
| Igor Piquet | `https://colombia.endeavor.org/.../INFORME-2024_FINAL_04-03-2025_Baja.pdf` (L05) | `https://endeavor.org/about-us/global-team/` (L01 mapped) | Informe names Piquet; zero `@endeavor.org` in PDF. Global team HTML names Piquet; no mailto |
| Ingo Ramesohl | `https://www.bosch-presse.de/.../press_kit_162950_en.pdf` (L05) | `https://www.sec.gov/Archives/edgar/data/1843714/000119312524085161/d13242dex104.htm` (EFTS hit) | Press kit pairs Ramesohl with spokesperson email. SEC exhibit: signature block only, no person email |
| J.P. Keating | `https://www.prochain.vc/` (L01 corrected site) | `https://www.prochain.vc/about` + `/team` (CF challenge on `/team`) | Wix homepage loads; no Keating name or person `@prochain.vc` in static HTML |
| James Todd | `https://www.oikocredit.org/wp-content/uploads/2025/09/ENG-Impact-Report-2025-3.pdf` (L05) | Re-scan + `https://arcpower.co/wp-content/uploads/2025/07/Press-Release_ARC_Power_Oikocredit_Triodos.pdf` (L05 deferred) | Impact PDF: org `info@oikocredit.org` only; no James Todd. Press PDF quotes Todd; media `karl.boyce@arcpower.co` only |

Additional deferred retries (promising EMPTY):

| Seat | URL | Outcome |
| --- | --- | --- |
| Igor Piquet | ProPublica Endeavor Catalyst 990 PDF download | HTML bot wall (not PDF); not scored |
| Igor Piquet | `https://www.lavca.org/wp-content/uploads/2025/08/LAVCA_Startup-Ecosystem-Insights_2025.pdf` | Re-fetched; no Piquet + `@endeavor.org` co-occurrence |
| Igor Piquet | `https://www.lavca.org/feature/from-belief-to-breakouts-in-conversation-with-endeavor-catalyst/` | Cloudflare challenge page from this environment |
| Ingo Ramesohl | `https://www.rbvc.com/current/team/ingo-ramesohl/` | IIS 404 from this environment |
