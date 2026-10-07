# 50 Colombian companies with their own 2024 or 2025 sustainability report

Research only. No one was contacted. Each counted row is a company that operates in Colombia and publishes its own sustainability, ESG, integrated, or GRI report. The source is the company’s own PDF or its own report page. News, rankings, Issuu, Scribd, and third-party summaries were not used as the source.

The year filter is strict. A row counts only when the document title or the text of the report states 2024 or 2025. Older reports are rejects, with the reason `older than 2024`. If the year could not be read from the document, the company was left out.

Checked on 7 October 2026. **47 of the 50 source URLs opened as PDFs.** The other three are the company’s own HTML report (Postobón, Riopaila Castilla, Universidad EAFIT), each returning HTTP 200 with the year in the page title. Coomeva’s download link returns `application/octet-stream`; the bytes are a PDF titled 2024, so it is included in the 47.

CIIU was left blank. None of the opened reports was used as a cited CIIU source, and no code was inferred.

`companies.csv` has exactly 50 counted rows. Columns: `company`, `legal_name_if_shown`, `sector`, `city_hq`, `report_title`, `report_year`, `report_type`, `source_url`, `url_checked_status`, `group`, `ciiu`, `ciiu_source`, `notes`.

Years: 45 reports for 2024 and 5 for 2025 (Comfandi, Incauca, Ingenio Providencia, Enka, LaCardio). Manuelita’s title is `2023-2024`, so the counted year is 2024.

## Counted companies

| company | sector | report_year | source_url |
| --- | --- | --- | --- |
| Holcim (Colombia) | Cemento | 2024 | https://www.holcim.com.co/sites/colombia/files/docs/ids-2024-baja-vf-0409.pdf |
| Colgas | Gas GLP | 2024 | https://colgas.com/wp-content/themes/insa/assets/pdfs/informe-sostenibilidad-2024.pdf |
| Comfama | Caja de compensación | 2024 | https://serviciosenlinea.comfama.com/Contenidos/Servicios/MarketingCloud/2025/Informe2024/InformeSostenibilidad2024.pdf |
| Organización Corona | Manufactura y retail | 2024 | https://empresa.corona.co/wp-content/uploads/2025/04/Informe_OC_2024.pdf |
| Claro Colombia | Telecomunicaciones | 2024 | https://www.claro.com.co/portal/co/recursos/co/pdf/Informe_de_Sostenibilidad_Claro_2024.pdf |
| Banco Agrario de Colombia | Banca | 2024 | https://www.bancoagrario.gov.co/system/files/2025-03/informe_de_gestion_y_sostenibilidad_2024.pdf |
| Grupo Energía Bogotá | Energía | 2024 | https://www.grupoenergiabogota.com/content/download/53239/file/REPORTE%20INTEGRADO%20%20SOSTENIBILIDAD%202024_vf.pdf |
| Bancóldex | Banca de desarrollo | 2024 | https://www.bancoldex.com/sites/default/files/2025-03-28_super_informe_sostenibilidad_bancoldex_version_final.pdf |
| Banco W | Banca / microfinanzas | 2024 | https://storage.googleapis.com/strapi-banco-w/Informe_de_Sostenibilidad_2024_32fdc04714/Informe_de_Sostenibilidad_2024_32fdc04714.pdf |
| BDO Colombia | Servicios profesionales | 2024 | https://www.bdo.com.co/getmedia/cb185e44-6d32-40f4-bbd3-ae8441c83132/BDO-Informe-Sost-Col-V7-1.pdf |
| Comfandi | Caja de compensación | 2025 | https://informesostenibilidad.comfandi.com.co/wp-content/uploads/2026/04/Informe_sost_2025_30ABR.pdf |
| Gases del Caribe | Gas natural | 2024 | https://gascaribe.com/wp-content/uploads/2025/03/GC-Informe-de-Gestion-2024-FINAL-PARA-FIRMA.pdf |
| Hospital Pablo Tobón Uribe | Salud | 2024 | https://cdn.shopify.com/s/files/1/0832/6162/0533/files/MEMORIA_DE_SOSTENIBILIDAD_HPTU_2024.pdf |
| Pontificia Universidad Javeriana | Educación | 2024 | https://www.javeriana.edu.co/recursosdb/d/universidad-sostenible/informe-de-sostenibilidad-2024-pontificia-universidad-javeriana-digital |
| Enka | Manufactura / reciclaje de PET | 2025 | https://www.enka.com.co/wp-content/uploads/2026/03/IS_2025_enka_completo_V2_C.pdf |
| Fundación Santa Fe de Bogotá | Salud | 2024 | https://fundacionsantafedebogota.org/sites/institucional/files/2025-06/Informe%20de%20Sostenibilidad%202024.pdf |
| TEBSA | Energía térmica | 2024 | https://tebsa.com.co/wp-content/uploads/2025/04/INFORME-DE-SOSTENIBILIDAD-2024-VF-1.pdf |
| Unibán | Agroindustria bananera | 2024 | https://uniban.com/sostenibilidad/wp-content/uploads/Reporte_Sostenibilidad_2024_Uniban.pdf |
| Incauca | Agroindustria azucarera | 2025 | https://www.incauca.com/wp-content/uploads/2026/07/Informe-de-sostenibilidad-2025.pdf |
| Banco Santander Colombia | Banca | 2024 | https://www.santander.com.co/recursos/archivos/informe-anual-finanzas-verdes-sostenibles-2024.pdf |
| INDUMIL | Industria | 2024 | https://www.indumil.gov.co/wp-content/uploads/2025/06/Informe-de-Gestion-y-Sostenibilidad-2024.pdf |
| COMPAS | Puertos | 2024 | https://compas.com.co/wp-content/uploads/2025/06/COMPAS_Informe-de-gestion-2024.pdf |
| Metro de Medellín | Transporte | 2024 | https://www.metrodemedellin.gov.co/hubfs/memorias-de-sostenibilidad/2024/Memoria_%20Sostenibilidad_MetrodeMedellin_2024.pdf |
| Porvenir | Pensiones y cesantías | 2024 | https://www.porvenir.com.co/documents/20152/0/informe-sostenibilidad-2024-porvenir.pdf/e19fc738-d797-5ef9-d1b8-a981374390df?t=1712172235227 |
| Manuelita | Agroindustria | 2024 | https://www.manuelita.com/wp-content/uploads/2025/09/Informe-de-Sostenibilidad-Manuelita-2023-2024.pdf |
| Ingenio Providencia | Agroindustria azucarera | 2025 | https://www.providenciaco.com/wp-content/uploads/2026/06/Informe-de-sostenibilidad-Providencia-2025.pdf |
| Drummond | Minería | 2024 | https://drummondltd.com/wp-content/uploads/2025/09/Informe-de-Sostenibilidad-2024-Drummond-Ltd.pdf |
| Aguas de Malambo | Agua | 2024 | https://www.grupo-epm.com/content/dam/Grupo-Epm/aguas-de-malambo/nuestra-gestion/informes-de-sostenibilidad/INF%20SOSTENIBILIDAD%202024.pdf |
| ESSA | Energía | 2024 | https://www.essa.com.co/site/Portals/0/documentos/transparencia-ita/transparencia-essa/informes-de-sostenibilidad/Informe-de-sostenibilidad-2024-ESSA-web.pdf |
| Findeter | Banca de desarrollo | 2024 | https://www.findeter.gov.co/system/files/internas/IGS-2024-Final-.pdf |
| Efigas | Gas natural | 2024 | https://www.efigas.com.co/ef_resources/2025/03/Informe-de-Gestion-y-Sostenibilidad-Efigas-2024.pdf |
| ALIÓN | Cemento | 2024 | https://alion.com.co/wp-content/uploads/2025/06/ALION-Informe-Sostenibilidad-2024.pdf |
| Industrias Spring | Manufactura | 2024 | https://marca.colchonesspring.com.co/Informe-sostenibilidad-2024.pdf |
| Harinera del Valle | Alimentos | 2024 | https://www.hv.com.co/wp-content/uploads/2025/05/Reporte-de-Sostenibilidad-2024.pdf |
| Zeuss | Químicos | 2024 | https://zeuss.com.co/wp-content/uploads/2025/09/Informe_de_sostenibilidad_Zeuss_2024_F.pdf |
| Veolia Colombia y Panamá | Servicios ambientales | 2024 | https://www.santander.veolia.co/sites/g/files/dvc3001/files/document/2025/05/Memoria%20de%20Sostenibilidad%202024%20%281%29.pdf |
| Tecnoglass | Manufactura de vidrio | 2024 | https://www.tecnoglass.com/wp-content/uploads/2025/09/Informe-de-Sostenibilidad-Espan%CC%83ol-2024_compressed-1.pdf |
| CENS | Energía | 2024 | https://www.cens.com.co/Portals/cens/institucional/informes-de-sostenibilidad/2024/Informe%20Ejecutivo%20de%20Sostenibilidad%20CENS%202024.pdf |
| Grupo Auteco | Movilidad | 2024 | https://media.autecomobility.com/recursos/web/informes/Informe_Auteco2024_23_04_2025_V4.pdf |
| Ultracem | Cemento | 2024 | https://ultracem.co/wp-content/uploads/2025/07/INFORME-DE-SOSTNIBILIDAD-2024_compressed.pdf |
| Aguas Nacionales | Agua | 2024 | https://www.grupo-epm.com/content/dam/Grupo-Epm/aguas-nacionales/nuestra-gestion/informes-de-sostenibilidad/infrome-gestion-aguas-nacionales-2024.pdf |
| Postobón | Bebidas | 2024 | https://informe2024.postobon.com/ |
| Riopaila Castilla | Agroindustria azucarera | 2024 | https://isyg2024.riopailacastilla.co/ |
| Universidad EAFIT | Educación | 2024 | https://www.eafit.edu.co/informe-de-sostenibilidad-2024 |
| Colsubsidio | Caja de compensación | 2024 | https://cms.colsubsidio.com/sites/default/files/Documentos/colsubsidio/2025/informe-de-gestion-y-sostenibilidad-colsubsidio-2024.pdf |
| Ocensa | Hidrocarburos / transporte | 2024 | https://ocensa.com.co/sites/default/files/inline-files/informe-gestion-sostenibilidad-2024-ocensa.pdf |
| Coomeva | Cooperativa | 2024 | https://www.coomeva.com.co/loader.php?lServicio=Tools2&lTipo=descargas&lFuncion=descargar&idFile=lgLUiN1YxVYaMidJvTjMbDpDL0ZnSVJDaw |
| San Vicente Fundación | Salud | 2024 | https://hospitalmedellin.sanvicentefundacion.com/sites/default/files/2025-04/2024-informe-de-sostenibilidad.pdf |
| Mayagüez | Agroindustria azucarera | 2024 | https://ingeniomayaguez.com/inicio/wp-content/uploads/2025/04/INFORME-DE-SOSTENIBILIDAD-MAYAGUEZ-2024-1.pdf |
| LaCardio | Salud | 2025 | https://www.lacardio.org/wp-content/uploads/2026/08/informe-de-sostenibilidad-resumen-ejecutivo-2025_vf2.pdf |

## Showcase, not counted

| company | what was found | why it is not in the 50 |
| --- | --- | --- |
| Constructora Bolívar | Informe de Sostenibilidad 2024, PDF opened. https://cbolivarstoragedev.blob.core.windows.net/fileslive-2023-20-11/2025-04/Informe%20de%20Sostenibilidad-2024.pdf | Requested showcase only. Period in the PDF is 1 January–31 December 2024. |
| Amarilo | Own sustainability page lists reports through 2023. Latest file found: https://media1.amarilo.com.co/website/s3fs-public/informes/2024-04/informe-de-sostenibilidad-amarilo-2023.pdf | older than 2024. No 2024 or 2025 sustainability report was found. A 2025 brochure on the site is marketing, not the report. |

## Rejects

The named exclusion list was applied and those companies were not counted. Reports that turned up for names on that list (including Grupo Éxito, Ecopetrol, Bancolombia, TGI, Procafecol / Juan Valdez, and UNE EPM / Colombia Móvil Tigo) were dropped as already identified.

| company or document | reason |
| --- | --- |
| Amarilo, Informe de Sostenibilidad 2023 | older than 2024 |
| Coomeva COP 2011, 2012, and 2014, still linked on the same downloads page | older than 2024 |
| Bavaria, latest own sustainability PDF found was a 2023 summary | older than 2024 |
| EPM historical sustainability PDFs for 2023 and earlier, linked from the institutional index | older than 2024 |
| Nestlé Evaluación Anual 2024 | global parent report, not a Colombia-specific report |
| Smurfit Westrock / Smurfit Kappa 2025 report linked from the Colombia page | global parent report, not a Colombia-specific report |
| UNE EPM Telecomunicaciones, Informe de Gestión y Sostenibilidad 2024 | already identified (Colombia Móvil / Tigo) |
| Homecenter / Sodimac Colombia | covered inside Organización Corona’s 2024 report, not a separate company report |
| Fundación Caicedo González Riopaila Castilla PDF | foundation report, not Riopaila Castilla S.A. The company site was used instead |
| Grupo Keralty, Informe de Sostenibilidad 2024 | an earlier download opened as that PDF, but on 7 October 2026 the public URL returned an HTML captcha, so it was not counted |
| EPM, Informe de Sostenibilidad 2024 (linked from epm.com.co) | the index labels 2024, but the file was not opened and the year was not read from the document |
| CHEC 2025 sustainability PDF | file is about 181 MB; the year was not read from the document |
| Isagen, Informe de Gestión 2024 (resumen) and Informe de gestión 2025 | titled as a management report. The 2025 file discusses ESG and SASB, but it was not counted as a sustainability, integrated, or GRI report |
| Conconcreto, Informe de Gestión 2025 | management report; not confirmed as a sustainability, ESG, integrated, or GRI report |
| Grupo Bios | 2024/2025 “informe de impacto positivo” found only on Issuu |
| Haceb | found on Scribd, not on a company-hosted report |
| Levapan | 2024 and 2025 download buttons on the management-report page do not resolve to a file |
| Belcorp 2024 | child-labour due-diligence note, not a sustainability report; parent is not a Colombian report |
| Fundación Valle del Lili | 2024/2025 labels on the hospital page; the 2025 file is embedded via Calameo, not a company-hosted PDF |
| Enel Colombia 2024 | the informes page returned a bot wall; no PDF URL returned the report |
| BBVA Colombia, informe no financiero 2024 | URL returned HTTP 403 on recheck |
| Protección, informe 2025 | content host returned HTTP 403 |
| Empresas Públicas de Medellín microsite sostenibilidadgrupoepm.com.co | Cloudflare challenge, not used as a source |

## Groups kept as separate reports

Postobón, Incauca, and Ingenio Providencia each publish their own report and are all marked Organización Ardila Lülle. CENS, ESSA, Aguas de Malambo, and Aguas Nacionales are marked Grupo EPM. Efigas is marked Promigas (the parent is excluded). Porvenir is marked Grupo Aval (the parent is excluded). Ocensa is a separate company; Ecopetrol is a shareholder. Multinational subsidiaries are flagged in the CSV notes: Holcim, Claro, BDO, Banco Santander Colombia, Drummond, Tecnoglass, and Veolia Colombia y Panamá.
