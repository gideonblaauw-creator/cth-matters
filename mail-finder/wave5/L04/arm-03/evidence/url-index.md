# Wave5 L04 Arm 03 — checked regulatory URLs

Method: public regulatory filings / registries / adviser disclosures **with mailboxes** (IAPD Form ADV PDF, SEC Form D, EDGAR full-text, IAPD search API). BCSC portal URLs returned 404 from this environment.

| Seat | Primary artifacts checked |
|------|---------------------------|
| Jonathan Whittle / Quona Capital | IAPD ADV CRD 277131; Accion Quona Form D (2015–2019); EDGAR `@quona.com` |
| Keiji Matsunaga / SMBC | EDGAR `"Keiji Matsunaga"`; SMFG 20-F index (smfg.co.jp disclosure page) |
| Lachy Groom / Lachy Groom fund | EDGAR `"Lachy Groom"` Form D corpus (34 filings); `@lachygroom.com` |
| Lauren Morton / QED Investors | IAPD ADV CRD 284908; EDGAR `@qedinvestors.com`; `"Lauren Morton" AND @` |
| Lawrence G. Chua / Accial Capital | IAPD ADV CRD 305587; Accial Form D (2023, 2026); EDGAR `@accialcapital.com` |

## URL list (pipe-delimited in `results.csv`)

- https://api.adviserinfo.sec.gov/search/firm?query=Quona%20Capital
- https://api.adviserinfo.sec.gov/search/individual?query=Whittle%20Quona
- https://reports.adviserinfo.sec.gov/reports/ADV/277131/PDF/277131.pdf
- https://efts.sec.gov/LATEST/search-index?q=%40quona.com
- https://efts.sec.gov/LATEST/search-index?q=%22Jonathan%20Whittle%22
- https://efts.sec.gov/LATEST/search-index?q=%22Jonathan%20Whittle%22+AND+%40
- https://www.sec.gov/Archives/edgar/data/1755618/000175561819000001/primary_doc.xml
- https://www.sec.gov/Archives/edgar/data/1657690/000165769015000001/primary_doc.xml
- https://api.adviserinfo.sec.gov/search/firm?query=Sumitomo%20Mitsui
- https://efts.sec.gov/LATEST/search-index?q=%22Keiji%20Matsunaga%22
- https://efts.sec.gov/LATEST/search-index?q=Matsunaga+SMBC
- https://www.smfg.co.jp/english/investor/financial/disclosure.html
- https://efts.sec.gov/LATEST/search-index?q=%22Lachy%20Groom%22
- https://efts.sec.gov/LATEST/search-index?q=%40lachygroom.com
- https://www.sec.gov/Archives/edgar/data/1833010/000183301021000001/primary_doc.xml
- https://api.adviserinfo.sec.gov/search/firm?query=QED%20Investors
- https://reports.adviserinfo.sec.gov/reports/ADV/284908/PDF/284908.pdf
- https://efts.sec.gov/LATEST/search-index?q=%40qedinvestors.com
- https://efts.sec.gov/LATEST/search-index?q=%22Lauren%20Morton%22+AND+%40
- https://efts.sec.gov/LATEST/search-index?q=%22Lauren%20Connolley%22
- https://api.adviserinfo.sec.gov/search/firm?query=Accial%20Capital
- https://reports.adviserinfo.sec.gov/reports/ADV/305587/PDF/305587.pdf
- https://efts.sec.gov/LATEST/search-index?q=%22Accial%20Capital%22
- https://efts.sec.gov/LATEST/search-index?q=%40accialcapital.com
- https://efts.sec.gov/LATEST/search-index?q=%22Lawrence%20Chua%22+Accial
- https://www.sec.gov/Archives/edgar/data/2116828/000093583626000146/primary_doc.xml
- https://www.sec.gov/Archives/edgar/data/1932077/000193207723000003/primary_doc.xml
