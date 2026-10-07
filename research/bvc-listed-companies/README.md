# How many companies are listed on the Bolsa de Valores de Colombia?

Retrieved 7 October 2026. No figure below is an estimate. Where a source publishes a number, that number is quoted. Where a source publishes a list and not a total, the count is the number of records in that list on the retrieval date, and the method is stated.

There is no single current total. The World Federation of Exchanges (WFE) “number of listed companies” for the Bolsa de Valores de Colombia is **60 at end-August 2026** (59 domestic and 1 foreign). The live BVC equity board the same week shows **67 named local issuers**. The BVC local issuer directory shows **174 issuers**, and the Registro Nacional de Valores y Emisores (RNVE) query shows **311 inscribed entities**. Those are different populations.

## Summary

| Segment | Count | As-of date | Source |
| --- | ---: | --- | --- |
| WFE listed companies, total | 60 | End-August 2026 | https://focus.world-exchanges.org/issue/october-2026/market-statistics |
| WFE domestic listed companies | 59 | End-August 2026 | https://focus.world-exchanges.org/issue/october-2026/market-statistics |
| WFE foreign listed companies | 1 | End-August 2026 | https://focus.world-exchanges.org/issue/october-2026/market-statistics |
| WFE listed companies, total | 61 | End-December 2025 | https://focus.world-exchanges.org/issue/february-2026/market-statistics |
| WFE domestic / foreign | 60 / 1 | End-December 2025 | https://focus.world-exchanges.org/issue/february-2026/market-statistics |
| World Bank “Listed domestic companies, total” | 61 | Year 2025 (series updated 13 July 2026) | https://api.worldbank.org/v2/country/COL/indicator/CM.MKT.LDOM.NO?format=json |
| BVC local issuer directory, all records | 174 | 7 October 2026 | https://www.bvc.com.co/listado-de-emisores-mercado-local |
| BVC local directory records with an equity nemotécnico | 75 | 7 October 2026 | https://www.bvc.com.co/listado-de-emisores-mercado-local |
| BVC local directory records with no equity nemotécnico | 99 | 7 October 2026 | https://www.bvc.com.co/listado-de-emisores-mercado-local |
| Local equity board (EQTY): named issuers | 67 | 7 October 2026 session | https://www.bvc.com.co/mercado-local-en-linea |
| Local equity board (EQTY): lines, excluding mnemonic CASH | 110 | 7 October 2026 session | https://www.bvc.com.co/mercado-local-en-linea |
| Of those 67, board name begins “FONDO BURSATIL” | 4 | 7 October 2026 session | https://www.bvc.com.co/mercado-local-en-linea |
| MGC issuer directory | 89 | 7 October 2026 | https://www.bvc.com.co/listado-de-emisores-mercado-global |
| MGC board: lines / distinct issuer-name strings | 151 / 143 | 7 October 2026 session | https://www.bvc.com.co/mercado-local-en-linea |
| RNVE inscribed entities (unique names) | 311 | 7 October 2026 | https://www.superfinanciera.gov.co/SIMEV2/rnve/emisoresinscritosvigentes |
| Of the 311, entity type “FONDO DE INVERSIÓN COLECTIVA y/o FONDO DE CAPITAL PRIVADO” | 143 | 7 October 2026 | same RNVE query |
| Of the 311, entity type “NEGOCIOS FIDUCIARIOS” | 23 | 7 October 2026 | same RNVE query |
| RNVE issuers in the Código País filing described by the SFC | 125 | Survey year 2024; published 22 December 2025 | https://www.superfinanciera.gov.co/publicaciones/10115939/se-consolida-la-tendencia-creciente-en-la-implementacion-de-buenas-practicas-de-gobierno-corporativo-en-los-emisores-del-mercado-de-capitales/ |

## What each number is

### Listed companies in the WFE sense

Latest monthly table, WFE Focus, October 2026 issue, section “Equity - Number of listed companies”. Columns are Domestic, Foreign, Total Aug'26, and the year-on-year change.

Quote:

> Bolsa de Valores de Colombia | 59 | 1 | 60 | -1.6%

Source: https://focus.world-exchanges.org/issue/october-2026/market-statistics

The July 2026 row, in the September 2026 issue, was still 61 domestic, 1 foreign, total 62 (`Total Jul'26`, change `1.6%`). Source: https://focus.world-exchanges.org/issue/september-2026/market-statistics

Year-end 2025, February 2026 issue, columns Domestic, Foreign, Total Dec'25:

> Bolsa de Valores de Colombia | 60 | 1 | 61 | 0.0%

Source: https://focus.world-exchanges.org/issue/february-2026/market-statistics

The WFE foreign count is 1. That is not the Mercado Global Colombiano. The MGC board on 7 October 2026 carried 151 lines. BVC’s report to the WFE does not treat those foreign shares and ETFs as the “foreign listed companies” column.

World Bank indicator `CM.MKT.LDOM.NO`, “Listed domestic companies, total”, Colombia, value **61** for 2025. The API records `lastupdated` **2026-07-13**. Source organization: “World Federation of Exchanges database, World Federation of Exchanges (WFE)”.

Source note, quoted from https://api.worldbank.org/v2/indicator/CM.MKT.LDOM.NO?format=json :

> Listed domestic companies, including foreign companies which are exclusively listed, are those which have shares listed on an exchange at the end of the year. Investment funds, unit trusts, and companies whose only business goal is to hold shares of other listed companies, such as holding companies and investment companies, regardless of their legal status, are excluded. A company with several classes of shares is counted once. Only companies admitted to listing on the exchange are included.

The 2025 World Bank value (61) matches the WFE December 2025 **total** (60 domestic + 1 foreign), not the domestic column alone (60). The series for 2024 is 60. This note does not apply the exclusion language to the BVC lists to produce another number.

### Local equity issuers on bvc.com.co

Two BVC feeds, both read on 7 October 2026.

**Issuer directory.** Page https://www.bvc.com.co/listado-de-emisores-mercado-local . The page copy is: “Estas son las empresas que emiten valores en bvc. Analiza el desempeño de tu portafolio o decídete a invertir.” The page does not print a total. It loads `https://rest.bvc.com.co/market-information/rv/lvl-3/issuer?filters[marketDataRv][type]=Local`.

That response contained **174** records, **174** distinct `issuerName` values and **174** distinct `issuerId` values.

- **75** records have a non-empty `symbol` (one nemotécnico per issuer, not one row per share class).
- **99** records have an empty `symbol`.

The 99 are not labeled “renta fija” by the feed. Reading the names, the set includes banks and finance companies, the Gobierno Nacional, municipalities, fideicomisos, patrimonios autónomos, fondos de inversión colectiva, and some corporates (for example EPM, Alpina, Gases del Caribe, UNE EPM Telecomunicaciones). It is the directory’s no-equity-symbol slice, not a published fixed-income census. No BVC page consulted for this note states a single number of renta fija issuers.

**Equity board.** Page https://www.bvc.com.co/mercado-local-en-linea , session of 7 October 2026. Market status in the same payload: `status` **OPEN**, `delay` **15** (minutes). Feed: `https://rest.bvc.com.co/market-information/rv/lvl-2` with `filters[marketDataRv][tradeDate]=2026-10-07` and boards EQTY, REPO and TTV.

EQTY returned **111** rows. One row is mnemonic **CASH** with no issuer. The other **110** rows belong to **67** named issuers. **76** of the 111 EQTY rows had quantity 0 or null, so the board is the listed set for that session, not the set that traded.

Four of the 67 issuers are named on the board as a fondo bursátil: ICOLCAP, GXTESCOL, HCOLSEL, and TEVAICOL. PEI, Protección, Fondo Ganadero del Tolima and Fondo Gibraltar are also on the board; their names do not begin with “FONDO BURSATIL”, so they stay inside the 67.

Several issuers have more than one EQTY line (ordinary, preferred, and dividend-right lines). Grupo Energía Bogotá has four. Banco AV Villas has seven. The issuer count is 67; the line count is 110.

The directory’s 75 symbols and the board’s 67 names are not the same list. Name strings differ for at least the Global X ETFs. Directory symbols with no same-string issuer on the EQTY board that day include Banco Bancoldex, Banco GNB Sudameris, Banco Pichincha, Enel Colombia, ISAGEN, Scotiabank Colpatria, Surtigas, and FOND BTGPACTUAL CREDIT CLASE A. Those rows are left in the directory count. They are not dropped to force agreement with the board or with the WFE.

### Mercado Global Colombiano

**Issuer directory.** Page https://www.bvc.com.co/listado-de-emisores-mercado-global . Feed: the same issuer endpoint with `filters[marketDataRv][type]=MGC`. On 7 October 2026 it returned **89** records, **89** distinct `issuerName` values and **89** distinct symbols. Countries on that file: Chile 31, Estados Unidos 27, Irlanda 14, Perú 12, Canadá 2, Colombia 1, Alemania 1, Brasil 1. Several Irish and US names are ETF umbrellas (iShares, Invesco, JPMorgan, ARK), so 89 is not 89 operating companies.

**MGC board**, same session, `filters[marketDataRv][board]=MGC`: **151** lines and **143** distinct issuer-name strings. **94** lines had quantity 0. This feed names the security (for example a specific iShares ETF). The directory often names the umbrella (for example “ISHARES IV PUBLIC LIMITED”). The two counts are both from BVC and both current; they are not interchangeable, and they are not added here.

The WFE foreign column remains 1. It does not describe this board.

### RNVE (inscribed issuers, not the same as listed companies)

Page: https://www.superfinanciera.gov.co/SIMEV2/rnve/emisoresinscritosvigentes (“Emisores inscritos vigentes y sus valores”).

The register’s own description, from https://www.superfinanciera.gov.co/SIMEV2/rnve :

> El Registro Nacional de Valores y Emisores - RNVE - tiene por objeto inscribir las clases y tipos de valores, así como los emisores de los mismos y las emisiones que estos efectúen. La inscripción en este registro es requisito para aquellas entidades que deseen realizar una oferta pública de sus valores o que los mismos se negocien en un sistema de negociación.

The public query behind that page (`/sfcservices/SIMEV2/emisores-inscritos-vigentes/reporteFront`), retrieved 7 October 2026, returned **311** rows, **311** distinct `nmEntidad` values and **311** distinct NITs. Security-type fields (`nmTitulo`, `nmMercado`) were empty on every row, so this extract does not split acciones from bonos.

Entity-type codes on the same rows:

| Entity type on the row | Count |
| --- | ---: |
| FONDO DE INVERSIÓN COLECTIVA y/o FONDO DE CAPITAL PRIVADO (code 095) | 143 |
| BC-ESTABLECIMIENTO BANCARIO (001) | 29 |
| NEGOCIOS FIDUCIARIOS (092) | 23 |
| ENTIDADES PUBLICAS (260) | 14 |
| SOCIEDADES INVERSORAS (066) | 13 |
| COMPANIA DE FINANCIAMIENTO (004) | 10 |
| All other types combined | 79 |
| Total | 311 |

Supervision level on the same 311 rows: control concurrente 188, control exclusivo 65, vigilado 58.

Código País, Superintendencia Financiera, 22 December 2025, about the 2024 filing:

> Entre los 125 emisores inscritos en el Registro Nacional de Valores y Emisores (RNVE), la implementación general en 2024 llegó a 66,17%, es decir 1,42% más que en 2023.

And:

> De acuerdo con el Reporte de Implementación de Mejores Prácticas Corporativas– Código País remitido por los 125 emisores inscritos en el Registro Nacional de Valores y Emisores (RNVE), el porcentaje a nivel general para 2024 se ubicó en 66,17%.

Source: https://www.superfinanciera.gov.co/publicaciones/10115939/se-consolida-la-tendencia-creciente-en-la-implementacion-de-buenas-practicas-de-gobierno-corporativo-en-los-emisores-del-mercado-de-capitales/

125 is the number of RNVE issuers the SFC says filed that report for 2024. It is not the 7 October 2026 headcount of the register. The live query is 311, and 143 of those 311 are classified on the file as fondos de inversión colectiva or fondos de capital privado.

### Segments with no company census in these sources

**Renta fija.** BVC did not publish, on the pages checked, a total of fixed-income issuers. The closest primary cut is the 99 local-directory records with no equity symbol, described above. Today’s corporate-debt trades were not used: a trade blotter is not a listing list.

**Derivatives.** The BVC derivatives board is futures and options contracts. No issuer count was taken from it.

**a2censo.** This is bvc’s collaborative-finance platform, not the equity list and not the RNVE. It is omitted from the table. A secondary report of “232 campañas exitosas” was not used, because that figure is campaigns, not listed companies, and it was not re-read from a bvc.com.co financial statement for this note.

**BVC informe de gestión.** The Superintendencia’s relevant-information log for bvc records that the 2025 annual management report was published on 27 March 2026. The public bvc “información relevante” page consulted on 7 October 2026 did not yield a PDF from which an issuer census could be quoted. No issuer total from an informe de gestión is included.

## Where the sources disagree

They disagree because they count different objects, and in one case the dates differ. Nothing here was averaged or adjusted.

1. **WFE listed companies, end-August 2026: 60 (59 domestic + 1 foreign).** World Bank, year 2025: **61**, under a definition that includes exclusively listed foreign companies and excludes investment funds and holding companies. WFE December 2025 total is also **61** (60 + 1). The August 2026 WFE total is one company lower than the July 2026 WFE total (62, which was 61 + 1).

2. **BVC local equity board, 7 October 2026: 67 named issuers and 110 lines.** That is higher than the WFE August total of 60. The board still includes four fondos bursátiles and other vehicles. The World Bank note says investment funds and holding companies are excluded from its series. This note does not reclassify the 67 to manufacture a match.

3. **BVC local directory: 174 issuers, of which 75 have an equity symbol.** A secondary article, Rankia, says “Según datos de la Bolsa de Valores de Colombia (BVC), a 2025 existen 174 emisoras de valores” and “64 compañías tienen acciones listadas”, with no day-level date (https://www.rankia.co/blog/analisis-colcap/5685995-emisoras-listadas-bolsa-valores-colombia). The 174 matches the directory retrieved on 7 October 2026. The 64 does not match the WFE 2025 figures (60 domestic, 61 total) or the 7 October 2026 board (67 named issuers). Rankia is not a primary source.

4. **MGC directory 89 versus MGC board 151 lines / 143 names.** Same day, same exchange, different naming grain (umbrella versus security). The WFE foreign column is 1 and does not describe either MGC figure.

5. **RNVE 311 on 7 October 2026 versus Código País 125 for the 2024 filing.** The 311 includes 143 fondos and 23 negocios fiduciarios. Inscription in the RNVE is the condition for a public offer; it is not admission to listing on the equity board.

6. **Celsia Colombia.** The issuer’s relevant-information log at the Superintendencia records, on 9 June 2026, cancellation of the ordinary-share inscription on the Bolsa de Valores de Colombia, and on 10 July 2026, cancellation of that inscription in the RNVE. Log: https://www.superfinanciera.gov.co/ReportesInformacionRelevante/faces/B_simevRelevantes/A_infoRelevante/repoInfoRelevante.xhtml?entidad=026&tipoEntidad=261 . On 7 October 2026 the EQTY board still had a row for CELSIA COLOMBIA S.A. E.S.P. under mnemonic SDEPSA, with no last price and no quantity. The parent, CELSIA, was trading (mnemonic CELSIA, last price 4735, quantity 72217). The local directory still had symbol CSACOL for Celsia Colombia. The issuer was not removed from the 67 or the 75. The RNVE query on the same day still returned “CELSIA COLOMBIA S.A. E.S.P. ANTES EMPRESA DE ENERGIA DEL PACIFICO S.A. E.S.P.”, which is consistent with the company remaining an issuer of bonds after the share cancellation. The January 2026 shareholder decision said the cancellation covered the ordinary shares only, because bond issues remained inscribed.

## Practical answer

For “how many companies are listed” in the sense used by the WFE and the World Bank, the latest primary figure is **60 listed companies at end-August 2026: 59 domestic and 1 foreign**.

For “who has shares on the local board today”, the 7 October 2026 EQTY board shows **67 named issuers** and **110 share lines**, plus the non-company mnemonic CASH.

For “who is an issuer of securities on the BVC local directory”, the same day’s directory shows **174**, of which **75** have an equity nemotécnico and **99** do not.

Foreign securities quoted on the MGC are a separate board: **151 lines** that day, against **89** names in the MGC issuer directory. They are not inside the WFE total of 60.

The RNVE, the legal register, had **311** inscribed entities that day, not 60 and not 174.
