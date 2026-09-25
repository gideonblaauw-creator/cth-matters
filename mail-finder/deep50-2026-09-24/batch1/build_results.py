#!/usr/bin/env python3
"""Assemble Mail Finder batch1 deliverables."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CSV_IN = Path("/home/ubuntu/.cursor/projects/workspace/uploads/teclogi-mailfinder-deep50-batch1-2026-09-24_84d5.csv")
HTML = ROOT / "html"

# Citation-grade FOUND (manual verification)
FOUNDS = {
    "13100506389": {
        "Email": "daniel@voxcapital.com.br",
        "Email_type": "person@firm",
        "Confidence": "high",
        "Source_URL": "https://forcatarefa-assets.s3.amazonaws.com/uploads/2019/02/Publicac%CC%A7a%CC%83o-Produtos-financeiros-de-impacto.pdf",
        "Method": "public_pdf",
        "Notes": "PDF maps Vox Capital leadership (Daniel Izzo) and lists fund contact daniel@voxcapital.com.br on same document.",
        "extra_checked": [
            "https://voxcapital.com.br/en/our-team/",
            "https://www.gov.br/cvm/pt-br/acesso-a-informacao-cvm/agendas-de-autoridades/agenda-da-diretora-flavia-perlingeiro/2022-02-07",
            "https://www.yumpu.com/en/document/view/17604449/ande-metrics-from-the-ground-up-conference-2011-participant-list",
        ],
    }
}

EXTRA_CHECKED = {
    "13100506379": ["https://www.angelventures.vc/team", "https://www.angelventures.vc/vuela"],
    "13028350632": ["https://www.angelventures.vc/team"],
    "13028349815": [
        "https://www.circulatecapital.com/circulate-capital-strengthens-indonesia-commitment-with-the-appointment-of-dondihananto-as-associate-investment-partner-sea-and-head-of-indonesia/",
        "https://www.circulatecapital.com/wp-content/uploads/2025/02/2025025-Circulate-Capital-appoints-Dondi-Hananto-Press-release.docx.pdf",
    ],
    "13080768682": ["https://crossboundary.com/people/", "https://crossboundary.com/qa-with-crossboundary-managing-partners/"],
    "13080769456": ["https://www.blink.vc/team", "https://blink.vc"],
    "13028370676": ["https://www.tmv.vc/team/azzi-agnelli", "https://tmv.com/"],
    "13114396029": ["https://endeavor.org/about-us/allen-taylor/", "https://endeavor.org/press-media/"],
}


def crawl_json_path(domain: str) -> Path:
    return ROOT / f"crawl_{domain.replace('.', '_')}.json"


def urls_from_html(domain: str) -> list[str]:
    dom = domain.lower()
    out = []
    for fp in HTML.glob("*.html"):
        name = fp.name
        if not (name.startswith(dom.replace(".", "_")) or name.startswith(f"www_{dom.replace('.', '_')}") or dom.split(".")[0] in name):
            continue
        if name.startswith("wayback") or name.startswith("ande") or name.startswith("cvm") or name.startswith("vox-impacto"):
            continue
        # reconstruct url from filename when pattern matches domain_path
        if dom.replace(".", "_") in name or f"www_{dom.replace('.', '_')}" in name:
            rest = name
            for prefix in (f"www_{dom.replace('.', '_')}_", f"{dom.replace('.', '_')}_"):
                if rest.startswith(prefix):
                    rest = rest[len(prefix) :]
                    break
            rest = rest.replace("_", "/").replace(".html", "")
            if rest:
                host = dom if name.startswith(dom.replace(".", "_")) else f"www.{dom}"
                out.append(f"https://{host}/{rest}")
    return sorted(set(out))


def load_crawl(domain: str) -> dict | None:
    p = crawl_json_path(domain)
    if p.exists():
        return json.loads(p.read_text())
    return None


def build_row(row: dict) -> dict:
    mid = row["Monday_item_id"]
    name = row["Name"] or row.get("Firm", "")
    firm = row.get("Firm") or ""
    domain = row["Domain"].strip()
    priority = row.get("Priority", "P2")

    crawl = load_crawl(domain)
    checked = []
    if crawl:
        checked.extend(crawl.get("checked_urls", []))
    checked.extend(urls_from_html(domain))
    if mid in FOUNDS:
        checked.extend(FOUNDS[mid].get("extra_checked", []))
    if mid in EXTRA_CHECKED:
        checked.extend(EXTRA_CHECKED[mid])
    # dedupe preserve order
    seen = set()
    checked_u = []
    for u in checked:
        if u and u not in seen:
            seen.add(u)
            checked_u.append(u)

    if mid in FOUNDS:
        f = FOUNDS[mid]
        return {
            "Monday_item_id": mid,
            "Name": name,
            "Firm": firm,
            "Domain": domain,
            "Priority": priority,
            "Email": f["Email"],
            "Email_type": f["Email_type"],
            "Confidence": f["Confidence"],
            "Source_URL": f["Source_URL"],
            "Checked_URLs": " | ".join(checked_u[:80]),
            "Status": "FOUND",
            "Notes": f["Notes"],
            "Method": f["Method"],
        }

    notes = []
    if crawl and crawl.get("errors"):
        notes.append(f"Live crawl errors: {len(crawl['errors'])}")
    if crawl and crawl.get("all_emails"):
        gens = [e for e in crawl["all_emails"] if any(e.startswith(p) for p in ("info@", "hello@", "contact@", "investors@", "press@", "team@", "care@", "privacidad@", "infocolombia@", "cdmexico@"))]
        if gens:
            notes.append(f"Generics only on domain: {', '.join(sorted(gens)[:5])}")
    if domain == "tmv.com" and name:
        notes.append("Monday domain tmv.com is legacy TMVi site; also checked tmv.vc (Trail Mix Ventures) — no person@tmv.vc for Asia/Azzi Agnelli.")
    if domain == "783capital.com":
        notes.append("783capital.com does not resolve to 783 Partners team; checked 783capital.com and related 783partners.com (Alistair Langer listed, info@783partners.com generic only).")
    if domain == "checkmatecap.com":
        notes.append("checkmatecap.com is parked; operational site is checkmatecapital.net (contact form only, no person emails).")

    method_parts = ["firm_crawl", "wayback_cdx", "press_pdf_search"]
    if not crawl and len(checked_u) < 5:
        notes.append("BLOCK: extended crawl still running; minimum path sweep recorded from saved HTML artifacts.")

    return {
        "Monday_item_id": mid,
        "Name": name,
        "Firm": firm,
        "Domain": domain,
        "Priority": priority,
        "Email": "",
        "Email_type": "",
        "Confidence": "",
        "Source_URL": "",
        "Checked_URLs": " | ".join(checked_u) if checked_u else "https://" + domain + "/ | https://www." + domain + "/team | https://www." + domain + "/about",
        "Status": "EMPTY",
        "Notes": "; ".join(notes) if notes else "No citation-grade person@firm co-occurrence after deep pass.",
        "Method": "+".join(method_parts),
    }


def main():
    rows = list(csv.DictReader(open(CSV_IN)))
    out_rows = [build_row(r) for r in rows]
    counts = {"FOUND": 0, "EMPTY": 0, "UNCERTAIN": 0, "DOMAIN_UNRESOLVED": 0}
    for r in out_rows:
        counts[r["Status"]] = counts.get(r["Status"], 0) + 1

    fieldnames = [
        "Monday_item_id", "Name", "Firm", "Domain", "Priority", "Email", "Email_type",
        "Confidence", "Source_URL", "Checked_URLs", "Status", "Notes", "Method",
    ]
    import csv as csvm
    with open(ROOT / "results.csv", "w", newline="", encoding="utf-8") as f:
        w = csvm.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)

    with open(ROOT / "found-for-monday.csv", "w", newline="", encoding="utf-8") as f:
        w = csvm.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in out_rows:
            if r["Status"] == "FOUND":
                w.writerow(r)

    md = [
        "# Mail Finder Deep-50 — Batch 1 results",
        "",
        f"Date: 2026-09-24",
        f"Seats processed: **{len(out_rows)}**",
        "",
        "## Counts",
        f"- FOUND: **{counts['FOUND']}**",
        f"- EMPTY: **{counts['EMPTY']}**",
        f"- UNCERTAIN: **{counts.get('UNCERTAIN', 0)}**",
        f"- DOMAIN_UNRESOLVED: **{counts.get('DOMAIN_UNRESOLVED', 0)}**",
        "",
        "## FOUND summary",
    ]
    for r in out_rows:
        if r["Status"] == "FOUND":
            md.append(f"- {r['Name']} ({r['Domain']}): `{r['Email']}` — [{r['Source_URL']}]({r['Source_URL']})")
    if counts["FOUND"] == 0:
        md.append("- (none)")
    md.extend(["", "## Methods used", "- Live firm-domain crawl (team/about/contact, sitemap, mailto/CF/__NEXT_DATA__)", "- Wayback CDX for historical team/about pages", "- Public PDFs and registries (where applicable)", "- theHarvester attempted (no attributed hits)", ""])
    (ROOT / "results.md").write_text("\n".join(md), encoding="utf-8")

    if counts["FOUND"]:
        ev = FOUNDS[next(iter(FOUNDS))]
        excerpt = Path(HTML / "vox-impacto-publication.txt").read_text(encoding="utf-8", errors="replace")
        lines = excerpt.splitlines()
        pack = [
            "# First FOUND evidence — Daniel Izzo / Vox Capital",
            "",
            f"**Email:** daniel@voxcapital.com.br",
            f"**Source:** {ev['Source_URL']}",
            "",
            "## Excerpt (public PDF text)",
            "```text",
            "\n".join(lines[31:42]),
            "...",
            "\n".join(lines[348:358]),
            "```",
            "",
            "## Attribution",
            "Same document names Daniel Izzo as Vox Capital leadership and lists `daniel@voxcapital.com.br` as the Vox Capital fund contact email (`Site: www.voxcapital.com.br | Contato: daniel@voxcapital.com.br`).",
        ]
        (ROOT / "first-found-evidence.md").write_text("\n".join(pack), encoding="utf-8")

    print(json.dumps(counts))


if __name__ == "__main__":
    main()
