#!/usr/bin/env python3
"""Generate arm-04 deliverables from adjudicated seat outcomes."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SEATS = [
    {
        "Monday_item_id": "13028358775",
        "Name": "Daniela Gómez Ziga",
        "Firm": "",
        "Current_Website": "https://pegasuscap.com",
        "Proposed_Website": "https://www.pcalp.com/",
        "Domain": "pegasuscap.com",
        "Status": "WEBSITE_CORRECTED",
        "Notes": "pegasuscap.com does not serve Pegasus Capital Advisors (SSL timeout/403); Daniela is VP on official pcalp.com team. No person mailto on team/profile crawl.",
        "Checked_URLs": "https://pegasuscap.com (fail: SSL timeout/403) | https://www.pcalp.com/ (200) | https://www.pcalp.com/team/ (200) | https://www.pcalp.com/news/person/daniela-gomez-ziga/ (200)",
    },
    {
        "Monday_item_id": "13028359182",
        "Name": "Dennis Zaidi",
        "Firm": "",
        "Current_Website": "https://www.checkmatecapital.net/",
        "Proposed_Website": "",
        "Domain": "checkmatecapital.net",
        "Status": "WEBSITE_OK",
        "Notes": "Live Checkmate Capital Wix site; Dennis listed on /team. Contact form only; no Dennis+person mailto.",
        "Checked_URLs": "https://www.checkmatecapital.net/ (200) | https://www.checkmatecapital.net/team (200)",
    },
    {
        "Monday_item_id": "13096668277",
        "Name": "Diego Serebrisky",
        "Firm": "Dalus Capital",
        "Current_Website": "https://daluscapital.com",
        "Proposed_Website": "",
        "Domain": "daluscapital.com",
        "Status": "WEBSITE_OK",
        "Notes": "daluscapital.com redirects to www.daluscapital.com (200, Wix). Firm match; no person mailto on public pages.",
        "Checked_URLs": "https://daluscapital.com (301→https://www.daluscapital.com/) | https://www.daluscapital.com/ (200) | https://www.daluscapital.com/about (200)",
    },
    {
        "Monday_item_id": "13028349815",
        "Name": "Dondi Hananto",
        "Firm": "",
        "Current_Website": "https://circulatecapital.com",
        "Proposed_Website": "",
        "Domain": "circulatecapital.com",
        "Status": "WEBSITE_OK",
        "Notes": "circulatecapital.com returns Cloudflare 403 to automated fetch; known live Circulate Capital domain. Team path blocked to bot; no public person mailto verified.",
        "Checked_URLs": "https://circulatecapital.com (403 Cloudflare challenge) | https://circulatecapital.com/team/ (403 Cloudflare challenge)",
    },
    {
        "Monday_item_id": "13028336225",
        "Name": "Dr. Luke Kirke",
        "Firm": "",
        "Current_Website": "https://greenbondcorp.com",
        "Proposed_Website": "https://www.greenbondcorporation.com/",
        "Domain": "greenbondcorp.com",
        "Status": "WEBSITE_CORRECTED",
        "Notes": "greenbondcorp.com is unrelated Squarespace 'GREENBOND CORP' placeholder. Dr Luke Kirke is Co-Founder at Green Bond Corporation (greenbondcorporation.com). No person mailto on executive team page.",
        "Checked_URLs": "https://greenbondcorp.com (301→https://www.greenbondcorp.com/ 200 wrong entity) | https://www.greenbondcorporation.com/ (200) | https://www.greenbondcorporation.com/who-we-are (200, lists Dr Luke Kirke)",
    },
    {
        "Monday_item_id": "13114451141",
        "Name": "Eduardo Brennand Campos",
        "Firm": "OneVC",
        "Current_Website": "https://onevc.vc",
        "Proposed_Website": "",
        "Domain": "onevc.vc",
        "Status": "WEBSITE_OK",
        "Notes": "onevc.vc live; partner profile /team/eduardo-campos confirms seat. LinkedIn only on profile; no mailto.",
        "Checked_URLs": "https://onevc.vc (200) | https://onevc.vc/team/eduardo-campos (200)",
    },
    {
        "Monday_item_id": "13114460590",
        "Name": "Elias Mufarech",
        "Firm": "Collide Capital",
        "Current_Website": "https://collide.capital",
        "Proposed_Website": "https://collidecap.com/",
        "Domain": "collide.capital",
        "Status": "WEBSITE_CORRECTED",
        "Notes": "collide.capital 301→collidecap.com (canonical Webflow site). Elias listed on /teams; footer general@collidecap.com generic only.",
        "Checked_URLs": "https://collide.capital (301→https://collidecap.com/) | https://collidecap.com/ (200) | https://collidecap.com/teams (200, lists Elias Mufarech)",
    },
    {
        "Monday_item_id": "13028359480",
        "Name": "Elvia Gomez",
        "Firm": "",
        "Current_Website": "https://acumen.org",
        "Proposed_Website": "",
        "Domain": "acumen.org",
        "Status": "WEBSITE_OK",
        "Notes": "acumen.org returns Cloudflare 403 to automated fetch; established impact investor domain. Team crawl blocked; no person mailto verified.",
        "Checked_URLs": "https://acumen.org (403 Cloudflare challenge) | https://acumen.org/about/team/ (403 Cloudflare challenge)",
    },
    {
        "Monday_item_id": "13028399382",
        "Name": "Emma Haight",
        "Firm": "",
        "Current_Website": "https://glenarapartners.com",
        "Proposed_Website": "",
        "Domain": "glenarapartners.com",
        "Status": "WEBSITE_OK",
        "Notes": "glenarapartners.com live (200). Team page /Team/ loads; no Emma+person mailto on crawl.",
        "Checked_URLs": "https://glenarapartners.com (200) | https://glenarapartners.com/Team/ (200)",
    },
    {
        "Monday_item_id": "13028370265",
        "Name": "Etienne Gillard",
        "Firm": "",
        "Current_Website": "https://manatechmiami.com",
        "Proposed_Website": "https://tech.manacommon.com/",
        "Domain": "manatechmiami.com",
        "Status": "WEBSITE_CORRECTED",
        "Notes": "manatechmiami.com NXDOMAIN. Etienne Gillard is Head of Ventures at Mana Tech (tech.manacommon.com). No person mailto on team page.",
        "Checked_URLs": "https://manatechmiami.com (NXDOMAIN) | https://tech.manacommon.com/ (200) | https://tech.manacommon.com/team/etienne-gillard/ (200)",
    },
    {
        "Monday_item_id": "13028371139",
        "Name": "Federico Giannetti",
        "Firm": "Federico Giannetti, PhD",
        "Current_Website": "https://axelcarbon.com",
        "Proposed_Website": "https://www.axel-carbon.com/",
        "Domain": "axelcarbon.com",
        "Status": "WEBSITE_CORRECTED",
        "Notes": "axelcarbon.com (no hyphen) NXDOMAIN. Live Axel Carbon site is www.axel-carbon.com (Squarespace). No person mailto on team/about crawl.",
        "Checked_URLs": "https://axelcarbon.com (NXDOMAIN) | https://www.axel-carbon.com/ (200)",
    },
    {
        "Monday_item_id": "13080749061",
        "Name": "Federico Storani",
        "Firm": "Riverwood Capital",
        "Current_Website": "https://riverwoodcapital.com",
        "Proposed_Website": "",
        "Domain": "riverwoodcapital.com",
        "Status": "WEBSITE_OK",
        "Notes": "riverwoodcapital.com Cloudflare 403 to bot; known PE firm domain. No person mailto verified on public crawl.",
        "Checked_URLs": "https://riverwoodcapital.com (403 Cloudflare challenge) | https://www.riverwoodcapital.com/ (403 Cloudflare challenge)",
    },
    {
        "Monday_item_id": "13100506101",
        "Name": "Felix Klühr",
        "Firm": "HV Capital",
        "Current_Website": "https://hvcapital.com",
        "Proposed_Website": "",
        "Domain": "hvcapital.com",
        "Status": "WEBSITE_OK",
        "Notes": "hvcapital.com live (200). /team lists partners; no Felix+person mailto on page HTML.",
        "Checked_URLs": "https://hvcapital.com (200) | https://www.hvcapital.com/team (200)",
    },
    {
        "Monday_item_id": "13028371748",
        "Name": "Fernando Lelo de Larrea H",
        "Firm": "",
        "Current_Website": "https://rumbo.ventures/",
        "Proposed_Website": "",
        "Domain": "rumbo.ventures",
        "Status": "WEBSITE_OK",
        "Notes": "rumbo.ventures live ClimateTech VC site (200). No person mailto on team/about paths checked.",
        "Checked_URLs": "https://rumbo.ventures/ (200) | https://rumbo.ventures/team/ (404) | https://rumbo.ventures/about-us/ (404)",
    },
    {
        "Monday_item_id": "13096680140",
        "Name": "Filipe Portugal",
        "Firm": "Canary",
        "Current_Website": "https://canary.com.br",
        "Proposed_Website": "",
        "Domain": "canary.com.br",
        "Status": "WEBSITE_OK",
        "Notes": "canary.com.br live (200→www). Team at /team/; no Filipe+person mailto on HTML crawl.",
        "Checked_URLs": "https://canary.com.br (301→https://www.canary.com.br/) | https://www.canary.com.br/team/ (200)",
    },
    {
        "Monday_item_id": "13028367534",
        "Name": "Fortunato D. Costantino, MBA, Dr. Eng., IPMA",
        "Firm": "Fortunato D. Costantino, MBA, Dr. Eng., IPMA",
        "Current_Website": "https://axel-carbon.com",
        "Proposed_Website": "",
        "Domain": "axel-carbon.com",
        "Status": "WEBSITE_OK",
        "Notes": "www.axel-carbon.com live Axel Carbon Squarespace site (200). Firm seat aligns with Axel Carbon brand. No person mailto.",
        "Checked_URLs": "https://axel-carbon.com (301→https://www.axel-carbon.com/) | https://www.axel-carbon.com/ (200)",
    },
    {
        "Monday_item_id": "13028371858",
        "Name": "Franck Nouyrigat",
        "Firm": "",
        "Current_Website": "https://www.electis.com/",
        "Proposed_Website": "",
        "Domain": "electis.com",
        "Status": "WEBSITE_OK",
        "Notes": "electis.com live (200). electis.io 301→electis.com. No Franck+person mailto on /about or /team paths.",
        "Checked_URLs": "https://www.electis.com/ (200) | https://electis.io (301→https://electis.com) | https://electis.com/team (404)",
    },
    {
        "Monday_item_id": "13028358612",
        "Name": "Gabriela Herculano",
        "Firm": "",
        "Current_Website": "https://iclima.earth",
        "Proposed_Website": "https://www.investandgrow.org/",
        "Domain": "iclima.earth",
        "Status": "WEBSITE_CORRECTED",
        "Notes": "iclima.earth hijacked: 301 chain to unrelated climatewire.net/gambling content. iClima Earth Ltd dissolved UK Mar 2025. First-party investandgrow.org (Gabriela Herculano) is current public investment-facing site per bio. No person mailto.",
        "Checked_URLs": "https://iclima.earth (301→climatealpha.ai→climatewire.net wrong entity) | https://www.investandgrow.org/ (200)",
    },
    {
        "Monday_item_id": "13100506409",
        "Name": "George Chalmers",
        "Firm": "Molten Ventures",
        "Current_Website": "https://moltenventures.com",
        "Proposed_Website": "",
        "Domain": "moltenventures.com",
        "Status": "WEBSITE_OK",
        "Notes": "moltenventures.com live; George Chalmers partner page confirmed. LinkedIn connect only; no personal mailto.",
        "Checked_URLs": "https://moltenventures.com (301→https://www.moltenventures.com/) | https://www.moltenventures.com/people/platform-team/george-chalmers (200)",
    },
]

FIELDNAMES = [
    "Status",
    "Monday_item_id",
    "Name",
    "Firm",
    "Current_Website",
    "Proposed_Website",
    "Domain",
    "Notes",
    "Checked_URLs",
    "Email",
    "Source_URL",
]


def main():
    rows = []
    for s in SEATS:
        rows.append({**s, "Email": "", "Source_URL": ""})

    with (ROOT / "results.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES)
        w.writeheader()
        w.writerows(rows)

    corrections = [
        {
            "Monday_item_id": s["Monday_item_id"],
            "Corrected_URL": s["Proposed_Website"],
            "Why": s["Notes"].split(".")[0] + ".",
        }
        for s in SEATS
        if s["Proposed_Website"]
    ]
    (ROOT / "website-corrections.json").write_text(json.dumps(corrections, indent=2) + "\n")
    (ROOT / "stamp-list.json").write_text("[]\n")

    counts = {}
    for s in SEATS:
        counts[s["Status"]] = counts.get(s["Status"], 0) + 1

    summary = f"""# Wave4 L01 Arm 04 — Domain hygiene scorecard

**Batch:** Potential Investors (19 seats)  
**Method:** HTTP domain checks + public web search + first-party team page mailto scan (no Hunter/Apollo/LinkedIn scrape/pattern SMTP).

## Status counts

| Status | Count |
|--------|------:|
"""
    for status in [
        "WEBSITE_OK",
        "WEBSITE_CORRECTED",
        "WEBSITE_MAPPED",
        "DOMAIN_UNRESOLVED",
        "FOUND",
        "EMPTY",
    ]:
        summary += f"| {status} | {counts.get(status, 0)} |\n"

    summary += f"""
**Total seats:** {len(SEATS)}

## Website corrections proposed

{len(corrections)} Monday Website values need update (see `website-corrections.json`).

## Email (FOUND)

0 citation-grade person emails on first-party team pages this arm.

## Notes

- Cloudflare 403 responses on acumen.org, circulatecapital.com, and riverwoodcapital.com treated as bot challenge; domains retained as WEBSITE_OK with documented fetch outcome.
- Wix/Squarespace hosts are live firm sites, not parking, when firm-branded content loads.
"""
    (ROOT / "summary.md").write_text(summary)

    readme = """# Mail Finder — Wave4 Loop L01 Arm 04

**Focus:** Domain hygiene + Website backfill (Potential Investors only).

## Input

`input.csv` — columns: Monday_item_id, Name, Contact_name, Firm, Kind, Priority, Status, Website, Domain, LinkedIn.

## Method (this arm)

1. **Blank Website:** resolve live investment-entity homepage via public web search (firm + contact).
2. **Filled Website:** HTTP-check for NXDOMAIN, parking, wrong entity, or redirect to a different firm domain.
3. **Propose** corrected `https://…` when blank/wrong/parked; sniff-test noisy inferences before proposing.
4. **Opportunistic email:** first-party team/people page with **name + person@firm mailto** co-occurrence → `FOUND`. Generics (`info@`, `hello@`, `team@`, etc.) are not FOUND.
5. Name/domain may seed search only — never invent emails, pattern+SMTP, Hunter/Apollo, or LinkedIn scrape.

## Outputs

| File | Purpose |
|------|---------|
| `results.csv` | Per-seat status, websites, notes, checked URLs |
| `website-corrections.json` | Monday Website patch list (wrong/blank/parked only) |
| `stamp-list.json` | FOUND emails for workbench Monday stamp |
| `summary.md` | Scorecard |
| `evidence/` | Excerpts for any FOUND (empty this run) |

## Scripts (audit trail)

- `scripts/check_websites.py` — HTTP fetch + parking heuristics
- `scripts/scan_team_emails.py` — mailto + name proximity scan
- `scripts/generate_deliverables.py` — writes deliverables from adjudicated outcomes
"""
    (ROOT / "README.md").write_text(readme)
    print(f"Wrote {len(rows)} seats, {len(corrections)} corrections")


if __name__ == "__main__":
    main()
