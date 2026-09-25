#!/usr/bin/env python3
"""Resolve domains, deep-crawl, emit results CSV/MD for no-domain batch."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

from crawl import crawl_person, norm_domain, website_url

ROOT = Path(__file__).resolve().parent

# Monday_item_id -> metadata from public web resolution (2026-09-24)
SEATS = {
    "13028336231": {
        "name": "Alethia Wong",
        "firm": "Zenani Capital",
        "domain": "zenanicapital.com",
        "notes": "Web: zenanicapital.com team page lists Alethia Wong VP; Techla Media Sep 2025 hire announcement.",
    },
    "13028365646": {
        "name": "Ana Lucía Rodhas Alcántara",
        "firm": "Apple Leisure Group (Hyatt)",
        "domain": "hyatt.com",
        "notes": "Web: ExpokNews interview — ESG/sustainability specialist at Apple Leisure Group (acquired by Hyatt). Not VC; employer domain mapped.",
    },
    "13028359995": {
        "name": "Andrii Hordiichuk",
        "firm": "BioSingularity",
        "domain": "biosingularity.world",
        "notes": "Web: biosingularity.world; LinkedIn CEO & Co-Founder BioSingularity.",
    },
    "13028358627": {
        "name": "Andrés Méndez",
        "firm": "COLABORATIVO",
        "domain": "colaborativo.io",
        "notes": "Web: LinkedIn COLABORATIVO Partner & Platform; colaborativo.io homepage on company profile.",
    },
    "13028366580": {
        "name": "Benjamin Radomski",
        "firm": "BEV Family Office",
        "domain": "bevfamilyoffice.com",
        "notes": "Web: bevfamilyoffice.com founder page; PitchBook LP profile.",
    },
    "13028359769": {
        "name": "Bill Irvine",
        "firm": "CarbonSul",
        "domain": "carbonsul.com",
        "notes": "Web: WIN Summit speaker bio; Sulphur Institute PDF lists William Irvine Co-Founder CarbonSul; carbonsul.com.",
    },
    "13028399234": {
        "name": "Brad Smith",
        "firm": "Centry Capital",
        "domain": "centry.capital",
        "notes": "Web: centry.capital/team Brad Smith co-founder; VNTR forum moderator bio.",
    },
    "13028358405": {
        "name": "Camilo Arango",
        "firm": "clicOH",
        "domain": "clicoh.com",
        "notes": "Web: Icesi/Bloomberg — Co-Founder COO clicOH (logistics); distinct from Yarumo/Minka profile.",
    },
    "13028336730": {
        "name": "Carlos Iván Vargas Perdomo",
        "firm": "Dibanka / VMKapital-Gefin",
        "domain": "dibanka.com",
        "notes": "Web: LinkedIn co-founder Dibanka; conference speaker at U Externado (banking). dibanka.com attempted.",
    },
    "13028371786": {
        "name": "Carolina Ocampo-Maya",
        "firm": "Epic Angels",
        "domain": "epicangelnetwork.com",
        "notes": "Web: epicangelnetwork.com; Epic Angels member investor profile.",
    },
    "13028358655": {
        "name": "Claudia Akel",
        "firm": "SDG Investors",
        "domain": "sdginvestors.com",
        "notes": "Web: sdginvestors.com; Inclusive Capitalism SDG Investors CEO profile.",
    },
    "13028358610": {
        "name": "Constantin Augier",
        "firm": "Climate Club / Impact Ladder",
        "domain": "climateclub.cc",
        "notes": "Web: climateclub.cc investor; Impact Ladder founder (no separate domain crawl).",
    },
    "13028358775": {
        "name": "Daniela Gómez Ziga",
        "firm": "Pegasus Capital Advisors",
        "domain": "pegasuscap.com",
        "notes": "Web: Mergr/LinkedIn VP Pegasus Capital Advisors; pegasuscap.com.",
    },
    "13028359480": {
        "name": "Elvia Gomez",
        "firm": "Acumen",
        "domain": "acumen.org",
        "notes": "Web: acumen.org/team/elvia-gomez Associate Director LatAm.",
    },
    "13028399382": {
        "name": "Emma Haight",
        "firm": "Glenara Partners",
        "domain": "glenarapartners.com",
        "notes": "Web: glenarapartners.com; WithIntelligence emerging manager profile Co-Founder.",
    },
    "13028350254": {
        "name": "Fernando Casado Cañeque",
        "firm": "Inclimo Climate Tech Fund",
        "domain": "inclimo.com",
        "notes": "Web: inclimo.com GP; EU-Startups/Capital-Riesgo fund close articles.",
    },
    "13028367534": {
        "name": "Fortunato D. Costantino, MBA, Dr. Eng., IPMA",
        "firm": "Axel Carbon Capital",
        "domain": "axel-carbon.com",
        "notes": "Web: axel-carbon.com team; Axel Carbon LP/advisory board.",
    },
    "13028358612": {
        "name": "Gabriela Herculano",
        "firm": "iClima Earth",
        "domain": "iclima.earth",
        "notes": "Web: iclima.earth Nasdaq author bio CEO/CIO.",
    },
    "13028358308": {
        "name": "James Todd",
        "firm": "Oikocredit",
        "domain": "oikocredit.org",
        "notes": "Web: oikocredit.org Head Climate Smart & Community Solutions.",
    },
    "13028372274": {
        "name": "Juan Aparicio",
        "firm": "Gaira Consulting / Gaia Creativa",
        "domain": "andresfmendez.com",
        "notes": "Web: LinkedIn Juan Manuel Aparicio CEO Gaira — EdTech angel; no firm site found; mapped personal andresfmendez.com fallback UNRESOLVED if fails.",
    },
    "13028366698": {
        "name": "Karen Sheffield",
        "firm": "Pachamama Ventures",
        "domain": "pachamamavc.com",
        "notes": "Web: pachamamavc.com founder Fund I announcement.",
    },
    "13028367969": {
        "name": "Klaus Hergett",
        "firm": "Workvivo by Zoom",
        "domain": "workvivo.com",
        "notes": "Web: Qwoted Workvivo Engage 2025 speaker Enterprise AE; Jen Jordan LATAM post.",
    },
    "13028358136": {
        "name": "Lucía Gaitán Sánchez",
        "firm": "GAWA Capital",
        "domain": "gawa-capital.com",
        "notes": "Web: gawa-capital.com Head of Climate / Kuali Fund.",
    },
    "13028393210": {
        "name": "Mainga Mwiinga",
        "firm": "FINISH Mondial Foundation",
        "domain": "finishmondial.org",
        "notes": "Web: finishmondial.global/partners CEO contact block.",
        "manual": {
            "email": "mmwiinga@finishmondial.org",
            "source": "https://finishmondial.global/partners",
            "method": "press_html",
            "excerpt": "CEO-Mainga Mwiinga : mmwiinga@finishmondial.org",
        },
    },
    "13028397110": {
        "name": "Mau Messina",
        "firm": "SF500",
        "domain": "sf500.vc",
        "notes": "Web: sf500.vc/en/team Venture Partner.",
    },
    "13028372212": {
        "name": "Miheer Chanrai",
        "firm": "Climate Capital",
        "domain": "climate.capital",
        "notes": "Web: climate.capital; UK Companies House CLIMATE CAPITAL LTD director.",
    },
    "13028367182": {
        "name": "Nic Gorini",
        "firm": "Spin Ventures",
        "domain": "spin.vc",
        "notes": "Web: spin.vc team Founder & Managing Partner.",
    },
    "13028359863": {
        "name": "Nina Alastruey",
        "firm": "Demium Capital",
        "domain": "demium.com",
        "notes": "Web: Tech Barcelona / Demium Investment Director; Adler Group board.",
    },
    "13028371918": {
        "name": "Philippe Crete",
        "firm": "Fondaction Gestion d'actifs (FGA)",
        "domain": "fondactiongestiondactifs.ca",
        "notes": "Web: fondactiongestiondactifs.ca/en/team/philippe-crete mailto link.",
        "manual": {
            "email": "p.crete@fga.ca",
            "source": "https://www.fondactiongestiondactifs.ca/en/team/philippe-crete",
            "method": "website_source",
            "excerpt": "Philippe Crête ... mailto:p.crete@fga.ca on FGA team profile",
        },
    },
    "13028365736": {
        "name": "Ricardo Politi",
        "firm": "Amazon Investor Coalition",
        "domain": "amazoninvestor.org",
        "notes": "Web: amazoninvestor.org/people Global Investment Engagement Director.",
    },
    "13028360221": {
        "name": "Simon SDG",
        "firm": "SDG Global Group",
        "domain": "sdgglobalgroup.com",
        "notes": "Web: simonsdg LinkedIn; sdgglobalgroup.com / GoDaddy site on LI.",
    },
    "13028372793": {
        "name": "Stefanie Hauer",
        "firm": "NatureRe Capital AG",
        "domain": "nature-re.com",
        "notes": "Web: nature-re.com/about-us board partner.",
    },
    "13028372158": {
        "name": "Tiffany Chen",
        "firm": "Carbon Equity",
        "domain": "carbonequity.com",
        "notes": "Web: LinkedIn Investor at Carbon Equity; carbonequity.com.",
    },
    "13028367296": {
        "name": "Victoria But",
        "firm": "Sun East Group Limited",
        "domain": None,
        "status": "DOMAIN_UNRESOLVED",
        "notes": "Web: CampdenFB next-gen Sun East Group family investor; SFI Impact Summit speaker. No verified corporate website for investment entity (suneastgroup.com is unrelated HK retailer).",
    },
    "13028360224": {
        "name": "William Prescott",
        "firm": "Red Ribbon Asset Management",
        "domain": "redribbon.co",
        "notes": "Web: redribbon.co/who-we-are Chief Impact Investment Officer.",
    },
    "13028385021": {
        "name": "Jeff Stoike",
        "firm": "Blue Action Accelerator",
        "domain": "blueactionaccelerator.com",
        "notes": "Web: blueactionaccelerator.com/team CSO co-founder.",
    },
    "13028367829": {
        "name": "Mikayla Hart",
        "firm": "Congruence Capital",
        "domain": "congruencecapital.com",
        "notes": "Web: 100 Women in Finance highlight; congruencecapital.com.",
    },
}

SEATS["13028372274"]["domain"] = "edtechhublatam.org"
SEATS["13028372274"]["firm"] = "EdTech HUB Latam / Gaia Creativa"
SEATS["13028372274"]["notes"] = (
    "Web: LinkedIn Juan Manuel Aparicio — angel investor EdTech; Gaia Creativa (no public site). "
    "Mapped edtechhublatam.org ecosystem hub from EdTech posts."
)


def load_input_rows():
    rows = []
    with (ROOT / "input.csv").open() as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def main():
    input_rows = load_input_rows()
    out_rows = []
    found_stamps = []
    website_stamps = []
    stats = {"mapped": 0, "crawled": 0, "found": 0, "empty": 0, "unresolved": 0}
    first_found_md = []

    for inp in input_rows:
        mid = inp["Monday_item_id"]
        meta = SEATS.get(mid, {})
        name = meta.get("name") or inp["Name"]
        firm = meta.get("firm", "")
        domain = meta.get("domain")
        pre_status = meta.get("status")
        notes = [meta.get("notes", "")]
        checked = []
        method = ""
        email = ""
        email_type = ""
        confidence = ""
        source_url = ""
        status = pre_status or "EMPTY"

        if domain:
            stats["mapped"] += 1
            website_stamps.append(
                {
                    "Monday_item_id": mid,
                    "Name": name,
                    "Website_url": website_url(domain),
                }
            )
            # manual FOUND override
            if meta.get("manual"):
                m = meta["manual"]
                email = m["email"]
                source_url = m["source"]
                method = m["method"]
                confidence = "high"
                email_type = "work"
                status = "FOUND"
                checked.append(source_url)
                stats["found"] += 1
                stats["crawled"] += 1
                found_stamps.append(
                    {
                        "Monday_item_id": mid,
                        "Name": name,
                        "Email": email,
                        "Firm": firm,
                        "Source_URL": source_url,
                    }
                )
                first_found_md.append(
                    f"## {name} — {email}\nSource: {source_url}\nMethod: {method}\n> {m.get('excerpt','')}\n"
                )
            else:
                try:
                    cr = crawl_person(name, domain)
                    checked.extend(cr.checked)
                    stats["crawled"] += 1
                    if cr.emails:
                        em, url, meth, excerpt = cr.emails[0]
                        email = em
                        source_url = url
                        method = meth
                        confidence = "high"
                        email_type = "work"
                        status = "FOUND"
                        stats["found"] += 1
                        found_stamps.append(
                            {
                                "Monday_item_id": mid,
                                "Name": name,
                                "Email": email,
                                "Firm": firm,
                                "Source_URL": source_url,
                            }
                        )
                        first_found_md.append(
                            f"## {name} — {email}\nSource: {source_url}\nMethod: {method}\n> {excerpt}\n"
                        )
                    else:
                        status = "EMPTY"
                        stats["empty"] += 1
                        if cr.notes:
                            notes.extend(cr.notes)
                except Exception as e:
                    notes.append(f"crawl error: {e}")
                    status = "EMPTY"
                    stats["empty"] += 1
        else:
            stats["unresolved"] += 1
            status = "DOMAIN_UNRESOLVED"

        out_rows.append(
            {
                "Monday_item_id": mid,
                "Name": name,
                "Firm": firm,
                "Domain": norm_domain(domain) if domain else "",
                "Priority": inp.get("Priority") or "",
                "Email": email,
                "Email_type": email_type,
                "Confidence": confidence,
                "Source_URL": source_url,
                "Checked_URLs": " | ".join(dict.fromkeys(checked))[:8000],
                "Status": status,
                "Notes": " ".join(n for n in notes if n),
                "Method": method,
            }
        )

    # Write results.csv
    fieldnames = [
        "Monday_item_id",
        "Name",
        "Firm",
        "Domain",
        "Priority",
        "Email",
        "Email_type",
        "Confidence",
        "Source_URL",
        "Checked_URLs",
        "Status",
        "Notes",
        "Method",
    ]
    with (ROOT / "results.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)

    with (ROOT / "found-for-monday.csv").open("w", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["Monday_item_id", "Name", "Email", "Firm", "Source_URL"],
        )
        w.writeheader()
        w.writerows(found_stamps)

    with (ROOT / "website-stamp-list.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["Monday_item_id", "Name", "Website_url"])
        w.writeheader()
        w.writerows(website_stamps)

    summary = {
        "domains_mapped": stats["mapped"],
        "crawled": stats["crawled"],
        "FOUND": stats["found"],
        "EMPTY": stats["empty"],
        "DOMAIN_UNRESOLVED": stats["unresolved"],
    }
    (ROOT / "results.md").write_text(
        "# Mail Finder Deep-50 — no-domain arm (2026-09-24)\n\n"
        f"Processed **{len(out_rows)}** seats.\n\n"
        "| Metric | Count |\n|--------|------:|\n"
        + "\n".join(f"| {k} | {v} |" for k, v in summary.items())
        + "\n\n## FOUND emails\n"
        + ("\n".join(f"- {s['Name']}: `{s['Email']}` ({s['Source_URL']})" for s in found_stamps) or "_None beyond manual/crawl hits._")
        + "\n"
    )

    if first_found_md:
        (ROOT / "first-found-evidence.md").write_text("\n".join(first_found_md))
    else:
        (ROOT / "first-found-evidence.md").write_text("_No FOUND in this run._\n")

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
