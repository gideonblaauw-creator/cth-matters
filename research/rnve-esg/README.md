# RNVE ESG filings for BVC local issuers

As-of date for every count below: **7 October 2026**. Figures are taken from the sources named in each section. Nothing here is an average or an estimate.

The crawl universe is the BVC local issuer directory, not the full RNVE and not the Mercado Global Colombiano. Sister note on how the published totals differ: `research/bvc-listed-companies/README.md` on branch `cursor/bvc-listed-companies-75da` (PR #166).

## Counts reconciliation

| Population | Count | Source |
| --- | ---: | --- |
| BVC local issuer directory | 174 | https://www.bvc.com.co/listado-de-emisores-mercado-local — feed `https://rest.bvc.com.co/market-information/rv/lvl-3/issuer?filters[marketDataRv][type]=Local` |
| Of those 174, records with an equity nemotécnico | 75 | same directory (`symbol` non-empty) |
| Of those 174, records with no equity nemotécnico | 99 | same directory |
| Mercado Global Colombiano directory (excluded) | 89 | https://www.bvc.com.co/listado-de-emisores-mercado-global — same feed with `type=MGC` |
| RNVE inscribed entities | 311 | https://www.superfinanciera.gov.co/SIMEV2/rnve/emisoresinscritosvigentes — `reporteFront`, 311 distinct names and NITs |
| Of the 311, type 095 FIC and/or FCP | 143 | same RNVE file |
| Of the 311, negocios fiduciarios (type 092) | 23 | same RNVE file |
| Standalone investment funds removed from the 174 | 12 | named below; none is a real-estate vehicle |
| **Crawl universe** | **162** | 174 minus those 12 |
| Of the 162, equity nemotécnico still on the directory | 69 | 75 minus 6 excluded funds that carry a symbol |
| Of the 162, no equity nemotécnico | 93 | 99 minus 6 excluded funds with an empty symbol |
| Of the 162, matched to an RNVE vigente row (NIT and entity type) | 152 | name crosswalk against `reporteFront` |
| Of the 162, no RNVE vigente row (NIT left blank) | 10 | named below |

WFE “number of listed companies” for the Bolsa de Valores de Colombia is 60 at end-August 2026 (59 domestic and 1 foreign). That is a different population from the 174. The local equity board the same day had 67 named issuers. Rankia’s secondary “174 and 64” matches the directory total and does not match the 75 symbols or the WFE 60. Those comparisons are documented in the sister note; they are not used to drop anyone from this crawl.

The HTML page at bvc.com.co returned CloudFront 403 from this environment. The directory JSON feed responded. The handshake token used to read it is not stored in this repo.

### Twelve funds excluded

Standalone collective-investment or ETF vehicles. Real-estate vehicles stay in the crawl (PEI, Fondo Gibraltar, Inmoval, the Oikos fideicomisos, Visum rentas inmobiliarias, Nexus / Hoteles Estelar, Igneous compartimento inmuebles, and the other real-estate rows in the instrument table).

| Directory id | Directory name | RNVE match |
| --- | --- | --- |
| FBR | BTG Pactual títulos de participación | no unique vigente row |
| ACI | Cartera cerrada Accicolf | 095\|310 ACCICOLF VANGUARDIA |
| F26 | FICC Fonval / derechos económicos 2026 | 095\|476 |
| GLO | FICC Global Opportunities crédito (facturas) | 095\|416 |
| GSC | FICC Global Opportunities títulos valores | 095\|219 |
| CC1 | FICC Occidecol | 095\|159 |
| FBP | Fondo BTG Pactual crédito clase A (symbol FALABEC1) | 095\|507 |
| TVA | Fondo bursátil BTG Pactual Teva (TEVAICOL) | 095\|533 |
| GXT | Fondo bursátil Global X TES (GXTESCOL) | 095\|523 |
| HCO | Fondo bursátil Horizons Colombia (HCOLSEL) | 095\|362, RNVE name Fondo Bursátil Global X Colombia Select de S&P |
| ICP | Fondo bursátil iShares Colcap (ICOLCAP) | 095\|233 |
| FGT | Fondo Ganadero del Tolima (FGNTOLIMA) | no vigente row (Fondo Ganadero del Atlántico is a different entity and was not used) |

Six of the twelve have an equity symbol (FBP, TVA, GXT, HCO, ICP, FGT).

### Ten kept issuers with no RNVE vigente row

NIT and instrument type are blank / Pendiente. No NIT was invented.

Alpina Productos Alimenticios; Colpensiones Minhacienda (not merged with Colpensiones or with Gobierno Nacional); Credifinanciera (not Credifamilia); Excelcredit S.A. (the originator; the patrimonio autónomo is a separate row); Fideicomiso Concesionaria de O; Fideicomiso Fibratolima; Fideicomiso Grupo Nutresa (not Grupo Nutresa the company); Giros y Finanzas; Occidental de Colombia; PAT AUT INV LA 14 2009 01.

Itaú BBA and Itaú Corpbanca both map to the single RNVE entity ITAÚ COLOMBIA S.A. Both rows stay, and the notes say so.

## Instrument types on the 162

An issuer can carry more than one label, so the counts sum to more than 162. Labels come from the RNVE securities extract of the matched entity (acciones, bonos, papeles comerciales, titularizaciones, participaciones inmobiliarias, and a residual “other”). `equity_listed` in the CSV is y/n from a non-empty BVC directory symbol, not from an ACCION row.

| Instrument | Issuers |
| --- | ---: |
| Bonds | 78 |
| Equity | 66 |
| Other | 53 |
| Real estate fund / REIT | 15 |
| Titularización | 13 |
| Commercial paper | 12 |
| Unclassified (no RNVE row) | 10 |

Nine directory symbols had no ACCION row in the securities extract and are still share nemotécnicos, so equity was added with a note: Bancoldex, Bancolombia, GNB Sudameris, Pichincha, Celsia Colombia, Enel Colombia, ISAGEN, Scotiabank Colpatria, Surtigas. Celsia Colombia’s ordinary-share inscription was cancelled in 2026; the 7 October 2026 directory still shows CSACOL and the company remains a bond issuer.

PEI, Fondo Gibraltar, and Titularizadora Colombiana keep a directory symbol and are classified as real-estate or titularización. They are not also labeled as corporate equity.

## ESG filing availability

Channel: SIMEV “informes de fin de ejercicio” for the matched entity (`/fin-ejercicio/tipo-entidad/{tipo}/codigo-entidad/{codigo}/pagina`). The public page URL is stored in `source_url`. A filing is **yes** when the chosen document is a non-quarterly informe periódico de fin de ejercicio, a Circular 031 social-and-environmental chapter, or a standalone sustainability / ESG / integrated report. **Partial** means the channel only had a quarterly file, financial statements, or a weaker fin-de-ejercicio attachment. **None found** means the SIMEV list was empty, the issuer has no RNVE row, or the query timed out.

| Availability | Issuers |
| --- | ---: |
| Yes | 120 |
| Partial | 19 |
| None found | 23 |

Report year on the chosen filing (the exercise year printed in the title or filename, not the registration date): 2025: 113; 2026: 13; 2024: 4; 2021: 3; 2022: 2; 2020: 1; 2023: 1; blank: 25. Twenty-three of the blanks are the “none found” rows. The other two are yes filings whose title did not yield a year: Banco Santander de Negocios and Fideicomiso Estaciones Metrolínea.

Banco Popular’s filename cites Circular Externa 031 de 2021. The PDF itself is the Informe de Gestión y Sostenibilidad 2025, registered 27 March 2026, so `report_year` is 2025. KOA’s filename date 21 April 2026 is the publication date; the title is the 2025 year-end report, so `report_year` is 2025.

An ESG-chapter heading was found for 70 issuers (`esg_start_page`). Where the heading regex missed, the page stays Pendiente even if later pages mention ESG topics.

## How topic pages were read

PDFs were downloaded from SIMEV and searched with Spanish keyword patterns. A topic is “reported p.N” when the phrase appears on that page of the issuer’s own file. It is not a judgement that the disclosure is complete, and it is not a number.

Eleven patterns were coded, covering these requested topics: GHG scope 1–2, GHG scope 3, energy, air emissions, water, waste, biodiversity, climate risk, community, health and safety, supply chain. **Governance was not a separate pattern.** Notes say `topic_hits=N/11`. A count of 8 means at least eight of those eleven phrases have a page. A governance-only disclosure would not have been flagged, so the count is a lower bound on the twelve-topic list.

131 issuers have a `topic_hits` tag. The 31 without one are the 23 “none found” rows, four PDF download failures, two ZIP archives, and two yes filings that named a report but returned an empty `simev_file_id` (Adecaña and FCP Igneous compartimento inmuebles).

`key_data_points` is filled only where a figure was copied from the page that was read:

- Surtigas, p. 29 (2025, Ton CO2eq): alcance 1 = 16.547,98; alcance 2 = 136,28; alcance 3 = 1.592.258,26; alcances 1+2+3 = 1.608.942,52.
- KOA, p. 34: huella de carbono 22.280 kg CO2 in 2025, from 35.790 kg CO2 (baseline year not stated on the page); reduction 37.75%.

Every other `key_data_points` cell is empty.

## Who reaches Diaco depth

Diaco depth here means two things at once: the issuer’s own materiality list, verbatim, with a page, and at least eight of the topic flags with a page. Eight issuers meet that bar. None of them is in the showcase 40 (`overlap_with_showcase_40` = n).

| Issuer | Topic hits | Own list |
| --- | ---: | --- |
| Grupo Cibest S.A. | 10/11 | p. 190 (2025 update). Ambiental: cambio climático; biodiversidad y ecosistemas. Social: personal propio; trabajadores de la cadena de valor; relación con la comunidad; consumidores y usuarios finales. Gobierno: conducta empresarial; ciberseguridad y protección de datos; digitalización e innovación; finanzas sostenibles. |
| FINDETER | 10/11 | PDF p. 424 (printed “pág. 423”), Mega Materialidad “Economía Popular”: transferencia de capacidades hacia entidades territoriales; medición de impactos ambientales, sociales y económicos; finanzas responsables; infraestructura social; estrategia de relacionamiento. |
| Grupo Bolívar | 9/11 | p. 349. Dimensión económica y de gobierno: Prosperidad, Capital Económico, Confianza, Servicio. Social: Bienestar, Inclusión. Ambiental: Capital Natural. The page says these are the Grupo Bolívar topics; Davivienda’s 2025 review did not change them. |
| BBVA Colombia | 8/11 | pp. 24–25. 2023 double-materiality list ratified for the 2025 report: gestión de riesgos; crecimiento inclusivo; desempeño económico; gobierno corporativo, ética y transparencia; acción climática; ciberseguridad; ciudadanía corporativa; digitalización; compromiso con empleados. |
| Banco Caja Social | 8/11 | pp. 35–37. Four functions plus the environmental dimension: satisfacción de verdaderas necesidades; generación y distribución de riqueza con criterio de justicia; comunidad de personas; responsabilidad como actor de la sociedad civil; dimensión ambiental. |
| Electrificadora de Santander (ESSA) | 8/11 | PDF p. 217 (printed 216), Anexo 10 Temas materiales. Grouped labels include agua y biodiversidad; cambio climático; acceso y comprabilidad; bienestar laboral y adaptabilidad; calidad y seguridad de los productos y servicios; derechos humanos; tecnología e innovación; energías renovables; gobierno corporativo; transparencia; solidez financiera. |
| Financiera de Desarrollo Nacional | 8/11 | pp. 15–16, seven numbered topics (evaluación de riesgos e impactos socioambientales en los proyectos; impulso al desarrollo territorial; estrategia climática y descarbonización; productos con criterios ASG; crecimiento rentable; alianzas estratégicas; apertura a nuevos mercados). The GRI index on pp. 228–229 also heads “Gestión del talento”, which is not in that numbered list. |
| Banco Popular | 8/11 | PDF pp. 5–6. Doubly material: desempeño económico y rentabilidad; innovación y transformación digital; finanzas incluyentes; ecosistema de productos accesibles e inclusivos; transformación cultural; gobierno corporativo y riesgos ASG; educación financiera. Plus separate financial-materiality, impact, and “gestión técnica” lists on the same page. |

These are the next issuers by topic-hit count. Their own list was not on the pages read, so they are not Diaco depth yet:

| Issuer | Topic hits | Why the list is still Pendiente |
| --- | ---: | --- |
| Enel Colombia | 11/11 | Heading regex missed. p. 3 is a table of contents (“asuntos materiales” there is the ownership section). p. 203 describes the double-materiality process; the opportunity list was not in the captured text. |
| Empresas Públicas de Medellín | 10/11 | pp. 141–145 describe the double-materiality method. The topic names were not in the captured pages. |
| Fabricato | 10/11 | The 2025 PDF text that was searched has no “materialidad” / “temas materiales” hit. |
| Finagro | 10/11 | A later re-download of the materiality pages timed out. An earlier snippet on p. 22 only points at the mechanism. |
| Surtigas | 9/11 | p. 4 is a glossary. p. 29 says management of material issues focused on waste and resources, climate change, and biodiversity. That is an operational focus, not the full ranking. The GHG table on that page is copied above. |
| Celsia Colombia | 9/11 | p. 316 describes the 2025 double-materiality update. The topic list itself was not in the captured pages. |
| Banco Contactar | 9/11 | p. 21 says the 2025 report keeps the 2024 topics unchanged and points to https://bancocontactar.com/informes-de-gestion/ for the list. The topics are not printed in this filing. |
| Banco Citibank | 9/11 | pp. 4–5 describe a five-phase financial-materiality process (SASB commercial banking, ISSB, TCFD). The final matrix results were not in the captured pages. The filename year on the chosen file is 2026 (“2026 Reporte ASG”). |
| KOA Compañía de Financiamiento | 8/11 | p. 34 says that for 2025 no factor qualified as financially material risk information. That is a conclusion, not a topic list. The carbon figures on that page are copied above. p. 23 “asuntos materiales” is the ownership section. |
| Sodimac Colombia | 9/11 | The keyword hit is “asuntos materiales relativos a su estructura propietaria” (p. 15). That is shareholding, not an ESG ranking. |

Also read and left Pendiente on purpose: Banco GNB Sudameris (p. 8 is the accounting definition of “material”; p. 135 describes time horizons and does not list topics); Bolsa de Valores de Colombia (p. 3 is the Circular 012 glossary of “cambio material”).

## Overlap with the showcase 40

24 of the 40 names are in the 162 and are flagged `overlap_with_showcase_40=y`. Filing rows were still recorded for them.

Acerías Paz del Río; Alpina; Bancolombia; Banco Davivienda (the bank, not Davivienda Group); Banco de Bogotá; Banco de Occidente; Carvajal S.A.; Celsia (not Celsia Colombia); Cementos Argos; Colombina; Corficolombiana; Ecopetrol; Grupo Éxito; Gases de Occidente; Grupo Argos; Grupo Aval; Grupo Nutresa; Grupo SURA; ISA; Mineros; Organización Terpel; Promigas; Suramericana S.A.; UNE EPM Telecomunicaciones (the Tigo / UNE row; Colombia Móvil is not a separate RNVE name).

Alpina is in the directory and is flagged, and it has no RNVE vigente row, so its filing is “none found”.

16 of the 40 are not in the local directory and are not flagged. A nearby name was not treated as the same issuer:

Alianza Team (only an unrelated liquidating fondo uses the name); Alquería; Audifarma; Carvajal Empaques (Compañía de Empaques is a different issuer); Cerrejón; Diaco; Esenttia; GHL Hoteles (Fideicomiso Hoteles Estelar is the Nexus real-estate vehicle, not GHL); Ladrillera La Campana; Odinsa; Procafecol; Renault-Sofasa; Securitas; Seguros Bolívar (Grupo Bolívar is the holding and is in the crawl, unflagged); TGI; Vanti.

Grupo Cibest holds the Bancolombia equity story and is not one of the 40. Bancolombia the bank is the flagged row.

None of the 24 flagged issuers has a verbatim materiality list transcribed in this pass, so none of them is in the Diaco-depth table above. Several do have high topic-page counts (Banco de Bogotá, Ecopetrol, and Mineros at 11; Éxito, Cementos Argos, Banco de Occidente, Davivienda, and Bancolombia at 10).

## Failures and blocked sources

- bvc.com.co HTML: CloudFront 403. The local-directory JSON feed worked. MGC issuers were excluded by using `type=Local`, not by failing to read them.
- SIMEV fin-de-ejercicio query timed out: Conconcreto S.A. Availability is “none found” for that reason. A retry also timed out.
- SIMEV file is a ZIP, not a single PDF, so pages were not read: Banco Agrario; Patrimonio Autónomo Troncales. Both still have a filing title and a source URL.
- PDF download failed (timeout or HTTP error) after retry: Banco BTG Pactual Colombia; Colombia Telecomunicaciones; Fondo Gibraltar; Metro de Medellín. Filing metadata is filled; pages are not.
- Yes filing with an empty file id, so no PDF: Adecaña (en liquidación judicial); FCP Igneous compartimento inmuebles.
- Later re-reads that timed out and so did not add a materiality list: Finagro; a second pass on GNB Sudameris (an earlier pass already showed the accounting definition and the time-horizon section).
- Ten issuers have no RNVE NIT, listed above. Their periodic-report query was not run.

## Files

`issuers.csv` has one row per crawl issuer and the columns requested for this research: issuer, NIT when the RNVE file publishes it, instrument types, equity listed, ESG filing availability, report year, title, source URL, ESG start page, own materiality, topic flags, key data points, frameworks, showcase overlap, and notes.
