#!/usr/bin/env python3
"""Emit per-seat URL check manifest from curated curl list."""
import json
import subprocess
from pathlib import Path

UA = "MailFinderResearch/1.0"
EV = Path(__file__).parent / "fetched"

SEAT_URLS = {
    "13028367245_Michal_Lasocki": [
        "https://www.eecventures.com/en/eec-ventures/",
        "https://www.eecventures.com/en/contact/",
        "https://www.eecventures.com/en/",
        "https://www.eecventures.com/eec-ventures/",
        "https://www.eecventures.com/kontakt/",
        "https://www.eecventures.com/portfolio/",
        "https://www.eecventures.com/en/portfolio/",
        "https://www.eecventures.com/en/eec-magenta-funds/",
        "https://startuppoland.org/fundusz/eec-magenta/",
        "https://www.failory.com/blog/venture-capital-firms-warsaw",
        "https://topautomotive.pl/prelegenci/michal-lasocki/",
        "https://innovationzero.com/speakers",
        "https://www.innovationzero.com/speakers",
    ],
    "13028372212_Miheer_Chanrai": [
        "https://climate.capital/about-1",
        "https://climate.capital/contact-1",
        "https://climate.capital/home",
        "https://climate.capital/about",
        "https://www.climatecapitalsummit.com/",
        "https://climatecapitalsummit.com/",
        "https://innovationzero.com/speakers",
        "https://www.innovationzero.com/speakers",
        "https://one-world-admin.squarespace.com/virtual-impact-summit",
        "https://www.aspect.ac.uk/",
        "https://www.greenangelsyndicate.co.uk/",
        "https://equal.vc/",
        "https://www.zedify.co.uk/",
        "https://nakedenergy.co.uk/",
    ],
    "13100511303_Monica_Saggioro_Leal": [
        "https://www.maya.capital/team",
        "https://www.maya.capital/",
        "https://www.maya.capital/contact",
        "https://www.maya.capital/portfolio",
        "https://maya.capital/blog",
        "https://www.lavca.org/people/monica-saggioro/",
        "https://www.lavca.org/wp-content/uploads/2025/08/LAVCA_Startup-Ecosystem-Insights_2025.pdf",
        "https://neofeed.com.br/podcasts/cafe-com-investidor/podcast-cafe-com-investidor-41-monica-saggioro-cofundadora-da-maya-capital/",
        "https://globalhub.uninter.com/talking-business-startups-na-america-latina/",
        "https://www.listennotes.com/podcasts/the-j-curve-with/monica-saggioro-maya-capital-9g2JknFLKaP/",
        "https://www.vcsheet.com/who/monica-saggioro-leal",
    ],
    "13028366958_Nathalie_Couet": [
        "https://senecaimpact.earth/about-us/the-team/",
        "https://senecaimpact.earth/contact/",
        "https://senecaimpact.earth/perspective/seneca-championing-nature-smart-business/",
        "https://women-in-green-hydrogen.net/nathalie-couet/",
        "https://www.gasworld.tv/webinar-program/2026-electrolysers-1/",
        "https://www.gaebler.com/Funded-Company-CFF32BBC-D1AD-4715-8903-5A4D940AABBD-Hydgen",
        "https://www.hyd-gen.com/",
        "https://www.hyd-gen.com/contact",
        "https://www.gofractional.com/member/nathalie-couet",
        "https://couet-strategy.com/",
        "https://www.couet-strategy.com/",
    ],
    "13052203004_Netradyne": [
        "https://www.netradyne.com/company/contact",
        "https://www.netradyne.com/company/news/",
        "https://www.netradyne.com/news/netradyne-strengthens-leadership-team-with-new-cfo-and-coo-appointments",
        "https://www.netradyne.com/news/netradyne-celebrates-10th-anniversary-with-cross-country-customer-obsession-tour",
        "https://www.netradyne.com/news-press/netradyne-celebrates-10th-anniversary-with-cross-country-customer-obsession-tour",
        "https://www.netradyne.com/news-press/netradyne-driver-i-named-ai-safety-solution-of-the-year-in-2025-ai-breakthrough-awards-program",
        "https://www.netradyne.com/news-press/netradyne-strengthens-leadership-team-with-new-cfo-and-coo-appointments",
        "https://www.netradyne.com/news/netradyne-acquires-moove-press-release",
        "https://www.netradyne.com/news/netradyne-and-hyundai-translead-launch-strategic-oem-integration",
    ],
}


def fetch(url: str) -> int:
    out = EV / "manifest_tmp.body"
    r = subprocess.run(
        ["curl", "-sL", "-A", UA, "-o", str(out), "-w", "%{http_code}", "--max-time", "35", url],
        capture_output=True,
        text=True,
    )
    return int(r.stdout.strip() or "0")


def main():
    manifest = {}
    for seat, urls in SEAT_URLS.items():
        manifest[seat] = []
        for u in urls:
            manifest[seat].append({"url": u, "http": fetch(u)})
    Path(__file__).parent.joinpath("url-manifest.json").write_text(json.dumps(manifest, indent=2))
    print("wrote url-manifest.json")


if __name__ == "__main__":
    main()
