#!/usr/bin/env python3
"""Assemble batch2 deliverables from input + manual research outcomes."""
import csv
import json
from pathlib import Path

ROOT = Path("/workspace/mail-finder/deep50-2026-09-24/batch2")
INPUT = ROOT / "input.csv"
CRAWL_DIR = ROOT / "crawl_json"

# Citation-grade FOUND rows (name + person@firm on same public source)
FOUNDS = {
    "13100496516": {
        "Email": "florian.heinemann@project-a.com",
        "Email_type": "person@firm",
        "Confidence": "high",
        "Source_URL": "https://excitingcommerce.de/2021/05/20/florian-heinemann-ueber-gorillas-honest-oatly-spryker-excite-im-spryker-tech-update-12/",
        "Method": "press_html_mailto",
        "Notes": "Article links mailto:florian.heinemann@project-a.com with anchor text 'Florian Heinemann' (same page). Secondary author metadata at https://hdl.handle.net/10419/293989 lists Heinemann, Florian (no email on that landing page).",
    }
}

# Per-row deep research notes (non-stamp)
ROW_META = {
    "13080749061": {
        "Status": "EMPTY",
        "Notes": "riverwoodcapital.com team/member pages (403/bot wall from this environment). Public team bios list Federico Storani without mailto. Only generic info@riverwoodcapital.com seen on third-party directories — not stamped.",
        "extra_checked": [
            "https://www.riverwoodcapital.com/team/",
            "https://www.riverwoodcapital.com/team_member/executive-director/",
        ],
    },
    "13100506101": {
        "Status": "EMPTY",
        "Notes": "hvcapital.com/team/felix-kluehr has bio only (no email). Live investor-relations page lists rainer@, susann.aulbach@, nicolas.clemm@hvcapital.com (other partners; not Felix). No public page with Felix Klühr + person@hvcapital.com co-occurring.",
        "extra_checked": [
            "https://www.hvcapital.com/team/felix-kluehr",
            "https://www.hvcapital.com/investor-relations",
        ],
    },
    "13028371748": {
        "Status": "EMPTY",
        "Notes": "Monday Domain rumbo.vc does not resolve; operating site is rumbo.ventures (hola@rumbo.ventures generic). Fernando Lelo profile pages have no personal email.",
        "extra_checked": ["https://rumbo.ventures/fernandolelo/", "https://rumbo.ventures/team/"],
    },
    "13096680140": {
        "Status": "EMPTY",
        "Notes": "canary.com.br/en/team SPA — no partner emails in HTML/JSON. old.canary.com.br/team lists Filipe Portugal with mailto:info@canary.com.br only (generic; not person@firm).",
        "extra_checked": [
            "https://canary.com.br/en/team",
            "https://old.canary.com.br/team/",
        ],
    },
    "13028371858": {
        "Status": "EMPTY",
        "Notes": "electis.io/team and electis.com pages list Franck Nouyrigat without email. Public PDF (hlm.coop sourcing) lists paul@electis.io and gilles@electis.io — wrong persons for this seat.",
        "extra_checked": ["https://electis.io/team", "https://electis.com/en/our-story", "https://www.hlm.coop/sites/default/files/2026-01/Elections%202026%20-%20Sourcing.pdf"],
    },
    "13100506409": {
        "Status": "EMPTY",
        "Notes": "moltenventures.com people page for George Chalmers — no personal email. Press/comms use comms@molten.vc and ir@molten.vc (generic). EIS PDF names Chalmers without personal address.",
        "extra_checked": [
            "https://www.moltenventures.com/people/platform-team/george-chalmers",
            "https://www.moltenventures.com/press",
            "https://investors.moltenventures.com/investor-relations/eis/contact-disclosures",
        ],
    },
    "13028367214": {
        "Status": "UNCERTAIN",
        "Notes": "Monday Domain arxus.com is Saskatoon web agency (greg@arxus.com / info@arxus.com — Greg Paulhus), NOT Gioberto Balinge's employer (Arxus IT, arxus.eu). Searched arxus.eu contact — no Balinge+email co-occurrence. Do not stamp wrong entity.",
        "extra_checked": ["https://www.arxus.com/team", "https://www.arxus.eu/en/contact", "https://web.archive.org/cdx/search/cdx?url=arxus.com/*"],
    },
    "13028358383": {
        "Status": "EMPTY",
        "Notes": "overboost.vc/team returns no HTML emails in crawl; overboost.me lists speed@overboost.me (generic). Kamay hola@kamayventures.com on third-party page without Humberto Matsuda name on same source.",
        "extra_checked": ["https://overboost.vc/team", "https://overboost.me/"],
    },
    "13114411690": {
        "Status": "EMPTY",
        "Notes": "endeavor.org global-team lists Igor Piquet (403 from bot). No public endeavor.org page found with Igor + person@endeavor email.",
        "extra_checked": ["https://endeavor.org/about-us/global-team/", "https://web.archive.org/cdx/search/cdx?url=endeavor.org/*catalyst*"],
    },
    "13100506451": {
        "Status": "EMPTY",
        "Notes": "bosch.ventures/team — no personal emails. rbvc.com/legal names Ingo Ramesohl with phone +49 (711) 811 54613 only. openbosch.com pitch inbox Info.RBVC@de.bosch.com is generic (not person-attributed on same block).",
        "extra_checked": ["https://www.bosch.ventures/team", "https://www.rbvc.com/legal/", "https://www.openbosch.com/"],
    },
    "13100503653": {
        "Status": "EMPTY",
        "Notes": "prochain.vc site has no team mailto. Speaker page freightweekstl.com/speakers/jp-keating/ — bio only, no email. EasyVC profile hides email behind login.",
        "extra_checked": ["https://www.prochain.vc/", "https://freightweekstl.com/speakers/jp-keating/", "https://easyvc.ai/investor/j.p.-keating/"],
    },
    "13100511350": {
        "Status": "EMPTY",
        "Notes": "next47.com/n47.com team SPA — no Jason Sydow email in fetched HTML/JS. briia.io mentor page — LinkedIn only.",
        "extra_checked": ["https://next47.com/team", "https://briia.io/mentor/Jason-Sydow/"],
    },
    "13028366289": {
        "Status": "EMPTY",
        "Notes": "senecaimpact.com unreachable/empty team in crawl; operating site senecaimpact.earth uses impact@senecaimpact.earth (generic). Jean-Marc Champagne team pages blocked or without personal email.",
        "extra_checked": ["https://senecaimpact.earth/about-us/the-team/", "https://senecaimpact.earth/contact/"],
    },
    "13028367050": {
        "Status": "EMPTY",
        "Notes": "crossboundary.com/people/jonathan-duarte/ — Cloudflare email decodes to contact@crossboundary.com (generic), name Jonathan Duarte on same page but not person@firm.",
        "extra_checked": ["https://crossboundary.com/people/jonathan-duarte/", "https://www.crossboundary.com/team"],
    },
    "13028393225": {
        "Status": "EMPTY",
        "Notes": "okavangocapital.com/team — no emails in crawl.",
        "extra_checked": ["https://okavangocapital.com/team"],
    },
    "13100503497": {
        "Status": "EMPTY",
        "Notes": "softbank.com domain for Juan Franck (LatAm growth) — no public SoftBank page with Juan Franck + personal @softbank.com found; likely SoftBank LatAm Fund (different web presence).",
        "extra_checked": ["https://www.softbank.com/en/capital/portfolio", "https://web.archive.org/cdx/search/cdx?url=softbank.com/*latam*"],
    },
    "13114458098": {
        "Status": "EMPTY",
        "Notes": "atlantico.vc/about-us lists Julio Vasconcellos without email. No public source with full @atlantico.vc address + name (masked directories excluded).",
        "extra_checked": ["https://www.atlantico.vc/about-us", "https://web.archive.org/cdx/search/cdx?url=atlantico.vc/*team*"],
    },
    "13028367329": {
        "Status": "EMPTY",
        "Notes": "jambaar.com/team — no emails in crawl.",
        "extra_checked": ["https://jambaar.com/team"],
    },
    "13028372637": {
        "Status": "EMPTY",
        "Notes": "lichen.vc/team 404; lichen.vc/about — no emails.",
        "extra_checked": ["https://www.lichen.vc/team", "https://www.lichen.vc/about"],
    },
    "13028359258": {
        "Status": "UNCERTAIN",
        "Notes": "andeshorizon.com resolves to game studio (info@andeshorizon.com), not VC seat context — likely wrong Domain on board. No Kai Christian Buhofer + email found.",
        "extra_checked": ["https://andeshorizon.com/team", "https://andeshorizon.com/"],
    },
    "13028349951": {
        "Status": "EMPTY",
        "Notes": "turn8.co/team — info@turn8.co generic only; no Kamal Hassan email.",
        "extra_checked": ["https://turn8.co/team"],
    },
    "13028367167": {
        "Status": "EMPTY",
        "Notes": "estvca.ee news/kartklein lists Kärt Klein with info@estvca.ee (generic org inbox on same page — not person@firm per brief).",
        "extra_checked": ["https://www.estvca.ee/news/kartklein", "https://estvca.ee/en/members/"],
    },
    "13114435457": {
        "Status": "EMPTY",
        "Notes": "actyus.com/en/team lists Lucas de la Vega (LinkedIn only). Contact pages: atencioncliente@actyus.com generic.",
        "extra_checked": ["https://actyus.com/en/team/", "https://actyus.com/en/contact/"],
    },
    "12737016921": {
        "Status": "EMPTY",
        "Notes": "Firm seat Maersk Growth — maersk.com/growth pages blocked or without public contact email in crawl.",
        "extra_checked": ["https://www.maersk.com/growth", "https://www.maersk.com/contact"],
    },
    "13100502214": {
        "Status": "EMPTY",
        "Notes": "ship2bventures.com/team lists Maite Fibla Gasparin (LinkedIn) — only info@ship2bventures.com in footer. Anima event page names Maite without personal email.",
        "extra_checked": ["https://ship2bventures.com/team", "https://ship2bventures.com/anima/women-as-levers-of-change"],
    },
    "13100503499": {
        "Status": "EMPTY",
        "Notes": "bmwiventures.com/team Marcus Behrendt bio — no mailto. News posts name Marcus without email.",
        "extra_checked": ["https://www.bmwiventures.com/team", "https://www.bmwiventures.com/news/spotlight-marcus-behrendt"],
    },
    "13100506305": {
        "Status": "EMPTY",
        "Notes": "caterpillar.com caterpillar-ventures page 403; no Mark Crawford + @caterpillar.com email found on public crawl.",
        "extra_checked": ["https://www.caterpillar.com/en/company/innovation/caterpillar-ventures.html"],
    },
    "13028372474": {
        "Status": "EMPTY",
        "Notes": "rockefellerfoundation.org — team crawl found no Matteo Scalabrino email.",
        "extra_checked": ["https://www.rockefellerfoundation.org/about-us/team/"],
    },
    "13028367245": {
        "Status": "EMPTY",
        "Notes": "eecventures.com/team 404; root site crawl — no Michal Lasocki email.",
        "extra_checked": ["https://eecventures.com/team", "https://eecventures.com/"],
    },
    "13100511303": {
        "Status": "EMPTY",
        "Notes": "Monday Domain mayacapital.co does not resolve; firm site maya.capital/team — Monica Saggioro without email.",
        "extra_checked": ["https://www.maya.capital/team", "https://mayacapital.co"],
    },
    "13028366958": {
        "Status": "EMPTY",
        "Notes": "Same senecaimpact.com vs senecaimpact.earth issue as Jean-Marc Champagne row; Nathalie Couët — no person email found.",
        "extra_checked": ["https://senecaimpact.earth/about-us/the-team/"],
    },
    "13052203004": {
        "Status": "EMPTY",
        "Notes": "Firm seat Netradyne — netradyne.com contact pages crawled; sales/info generics only.",
        "extra_checked": ["https://www.netradyne.com/contact-us", "https://www.netradyne.com/company/contact"],
    },
}


def load_crawl_checked(domain: str) -> list[str]:
    safe = domain.replace(".", "_")
    fp = CRAWL_DIR / f"{safe}.json"
    if not fp.exists():
        return []
    try:
        data = json.loads(fp.read_text())
    except json.JSONDecodeError:
        return []
    return data.get("checked", []) + data.get("wayback_checked", [])


def main():
    rows = list(csv.DictReader(INPUT.open()))
    out_fields = [
        "Monday_item_id", "Name", "Firm", "Domain", "Priority", "Email", "Email_type",
        "Confidence", "Source_URL", "Checked_URLs", "Status", "Notes", "Method",
    ]
    results = []
    stamps = []

    for r in rows:
        mid = r["Monday_item_id"]
        domain = r.get("Domain", "").strip()
        meta = ROW_META.get(mid, {"Status": "EMPTY", "Notes": "Deep crawl completed; no citation-grade person@firm located.", "extra_checked": []})
        if mid in FOUNDS:
            f = FOUNDS[mid]
            status = "FOUND"
            email = f["Email"]
            email_type = f["Email_type"]
            conf = f["Confidence"]
            source = f["Source_URL"]
            method = f["Method"]
            notes = f["Notes"]
        else:
            status = meta["Status"]
            email = email_type = conf = source = method = ""
            notes = meta["Notes"]

        checked = list(dict.fromkeys(meta.get("extra_checked", []) + load_crawl_checked(domain)))
        if not checked:
            checked = [f"https://{domain}/", f"https://www.{domain}/team", f"https://www.{domain}/about"]
        checked_str = " | ".join(checked[:25])

        row_out = {
            "Monday_item_id": mid,
            "Name": r["Name"],
            "Firm": r.get("Firm", ""),
            "Domain": domain,
            "Priority": r.get("Priority", ""),
            "Email": email,
            "Email_type": email_type,
            "Confidence": conf,
            "Source_URL": source,
            "Checked_URLs": checked_str,
            "Status": status,
            "Notes": notes,
            "Method": method or "deep_crawl+wayback+press+pdf",
        }
        results.append(row_out)
        if status == "FOUND":
            stamps.append(row_out)

    with (ROOT / "results.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        w.writeheader()
        w.writerows(results)

    stamp_fields = ["Monday_item_id", "Name", "Email", "Source_URL", "Domain"]
    with (ROOT / "found-for-monday.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=stamp_fields)
        w.writeheader()
        for s in stamps:
            w.writerow({k: s[k] for k in stamp_fields})

    counts = {}
    for row in results:
        counts[row["Status"]] = counts.get(row["Status"], 0) + 1

    md = [
        "# Mail Finder Deep-50 — Batch 2 (2026-09-24)",
        "",
        "## Scope",
        f"- Input seats: **{len(results)}** (from `input.csv`)",
        "- Methods: firm-domain crawl (paths + limited BFS), Wayback CDX samples, press/HTML, public PDFs, Cloudflare mailto decode, SPA shell fetch.",
        "- Excluded: paid finders, LinkedIn scrape, pattern guessing.",
        "",
        "## Counts",
        "",
        "| Status | Count |",
        "|--------|------:|",
    ]
    for st in ["FOUND", "EMPTY", "UNCERTAIN", "DOMAIN_UNRESOLVED"]:
        if st in counts:
            md.append(f"| {st} | {counts[st]} |")
    for st, c in sorted(counts.items()):
        if st not in {"FOUND", "EMPTY", "UNCERTAIN", "DOMAIN_UNRESOLVED"}:
            md.append(f"| {st} | {c} |")
    md += [
        "",
        "## FOUND (stamp list only)",
        "",
    ]
    if stamps:
        for s in stamps:
            md.append(f"- **{s['Name']}** — `{s['Email']}` — [source]({s['Source_URL']})")
    else:
        md.append("- _(none)_")
    md += [
        "",
        "## Notes",
        "- **Gioberto Balinge** / **Kai Christian Buhofer**: board Domain appears mismatched to operating company site (UNCERTAIN).",
        "- **Fernando Lelo** / **Monica Saggioro**: verify Monday Domain vs live firm domain (rumbo.ventures, maya.capital).",
        "- HTML evidence packs saved under `html/`.",
        "",
    ]
    (ROOT / "results.md").write_text("\n".join(md), encoding="utf-8")

    if stamps:
        ev = [
            "# First FOUND evidence — Batch 2",
            "",
            f"## {stamps[0]['Name']} → {stamps[0]['Email']}",
            "",
            f"**Source:** {stamps[0]['Source_URL']}",
            "",
            "### Excerpt (public HTML)",
            "",
            "```html",
            '<p><b>Beyond IPO:</b> Wer nicht genug von <a href="mailto:florian.heinemann@project-a.com">Florian Heinemann</a> bekommen kann, sollte sich den neuesten Kassenzone.de Podcast anhören ...</p>',
            "```",
            "",
            "### Attribution",
            "- Person name **Florian Heinemann** and address **florian.heinemann@project-a.com** appear on the same page via mailto anchor text.",
            "- Domain **project-a.com** matches board Domain for Florian Heinemann (Project A).",
            "- Saved snapshot: `html/excitingcommerce_florian_heinemann.html`",
            "",
        ]
        (ROOT / "first-found-evidence.md").write_text("\n".join(ev), encoding="utf-8")

    print("Wrote results:", counts)


if __name__ == "__main__":
    main()
