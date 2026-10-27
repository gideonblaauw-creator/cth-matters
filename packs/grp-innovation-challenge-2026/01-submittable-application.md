# Submittable concept note — Title 1045 / ID 54180078

Source of truth: [`GRP-Submission-1045-confirmation.pdf`](GRP-Submission-1045-confirmation.pdf) (pulled from Gmail, forwarded 25 Jun 2026 as `GRP-Submission-1045-confirmation.pdf` / `Submission_ 1045.pdf`). Submitted 21 May 2026 by Gideon Blaauw to GRP Challenge Fund.

Line breaks in the PDF extract are cleaned here. Do not edit the PDF; edit the full proposal instead.

## Cover

| Field | Answer |
| --- | --- |
| Title | 1045 |
| Submission ID | 54180078 |
| Applicant | Gideon Blaauw |
| Address | Cl 90 No. 19-41 Of 801, Bogotá 110221, Cundinamarca, Colombia |
| Phone | +57 313 715 5965 |
| Email | gideon.blaauw@cleantechhub.net |

## Project facts

| Field | Answer |
| --- | --- |
| Project title | PDET-CIDM: AI Anticipatory Action for Deforestation-Vulnerable Women-Led Cooperatives |
| Main implementation country | Colombia |
| Other countries | — |
| Amount requested (USD) | 50,000 |
| Minimum viable amount (USD) | 32,000 |
| Project start | 1 Jan 2027 |
| Project end | 31 Dec 2027 |
| Shocks / stresses | Deforestation, climate shocks, EUDR market exclusion, post-conflict economic stress |
| CORE1 people supported | 800 |
| CORE2 investments mobilised (USD) | 200,000 |
| GRP partner / former grantee | Yes |
| Youth-led (18–35) | No |
| Women-led | No |
| Lead organisation | CleantechHUB Foundation |
| Category | Non-profit |
| Registered ID | NIT 901.523.941-9 (Cámara de Comercio de Bogotá, inscripción ESAL No. S0059867) |
| Website | www.cleantechhub.net |
| Postal / geo | Calle 90, #19-41, Bogotá, Cundinamarca, 110221, CO (4.676172, -74.0565779) |
| Main contact | Gideon Blaauw — gideon.blaauw@cleantechhub.net — +57 313 715 5965 |
| Additional contact | Juan Fernando Lucio López — paso@pasoglobal.org |
| Other partners | PASO Colombia (Fundación para la Paz Sostenible) / One Earth Future Foundation — named consortium partner (signed LOI attached). Agencia de Renovación del Territorio (ART) — collaborating institution on PDET data (Climate Innovation Data Matching). |
| Thematic window | Technology for Evolving Challenges in Humanitarian Contexts (TECH) 4 Resilience |
| How heard | GRP newsletter |
| Attachments | [GRP Supporting Docs](https://drive.google.com/drive/folders/1Ii7eq_n6gwB5FpclEXb0FOmPqXza6sEd) |

## Project summary

PDET-CIDM is an AI anticipatory-action system that fuses open satellite intelligence (Copernicus Sentinel-2; NASA/UMD DIST-ALERT) with CleantechHUB's PDET data warehouse — the only registry covering all 108,671 development records across Colombia's 170 post-conflict municipios — to detect deforestation pressure around women-led, ethnic-community cacao and coffee cooperatives before it materialises. When a trigger fires, the CleantechHUB–PASO Colombia consortium delivers a 14-day pre-emptive bundle: EUDR-compliant geolocation, climate-adaptation technical assistance, and deforestation-free supply-chain matchmaking. We pilot across eight initiatives in Pacífico Nariñense, Chocó, and Putumayo — keeping forests standing while securing European market access ahead of the 2026–2027 EUDR deadlines.

## Problem statement

Colombia's 170 PDET municipios — the territories most affected by 50+ years of armed conflict — are now climate frontlines. National deforestation rose 35% in 2024; north Chocó and Putumayo are active hotspots, with Putumayo the only Amazon region where deforestation rose in 2025 (+1,569 ha). In these territories, women-led, Afro-Colombian and Indigenous cacao and coffee cooperatives are the productive backbone of post-conflict recovery.

Two compounding shocks threaten them. First, climate volatility — erratic rainfall, drought, floods — destabilises smallholder agroforestry incomes. Second, the EU Deforestation Regulation (EUDR) takes effect December 2026 (large operators) and June 2027 (smallholders): any cacao or coffee that cannot prove plot-level, deforestation-free origin since December 2020 loses European market access. Most PDET smallholders lack this geolocation evidence.

When commodity income collapses — from climate damage or EUDR exclusion — historical evidence shows communities are pushed into clearing primary forest to survive, feeding the very deforestation that endangers them.

Resilience for whom: ~800 women- and youth-led producers (>50% women or youth) across eight ethnic-community cooperatives, plus their communities (~6,000 people). Resilience to what: climate shocks, market exclusion, and the deforestation-poverty trap. Resilience of what: household livelihoods, community social fabric, and the standing forests these territories depend on.

The gap is not knowledge (satellite alerts are public) or money (climate finance exists) — it is anticipation: connecting the alert to the right community with the right pre-emptive support, within days, before an irreversible clearing decision is made.

## Solution statement

PDET-CIDM is an AI anticipatory-action layer that turns public satellite alerts into pre-emptive, community-level action. It fuses Copernicus Sentinel-2 (10m, 5-day revisit) and NASA/UMD DIST-ALERT deforestation alerts with CleantechHUB's PDET data warehouse — the only unified registry of all 108,671 development records across Colombia's 170 PDET municipios. For each cooperative an AI model scores deforestation pressure, climate vulnerability, EUDR exposure, and women/youth leadership. When the score crosses a threshold, a trigger fires to the CleantechHUB–PASO Colombia consortium, which delivers within 14 days: (a) EUDR-compliant plot geolocation, locking deforestation-free status; (b) climate-adaptation technical assistance via PASO's Escuelas Rurales Alternativas; (c) deforestation-free supply-chain matchmaking with EUDR-ready buyers; (d) climate-finance donor matching.

Why this beats the status quo: Global Forest Watch provides alerts but no action; the FNC's SICA database geolocates coffee only, after the fact; humanitarian anticipatory-action mechanisms target weather extremes, not commodity-driven deforestation. No one integrates alert + warehouse + 14-day field response + market and finance linkage. It is anticipatory, not reactive — preventing forest loss rather than measuring it.

Current state: the PDET warehouse is built and live (pdet-api.cleantechhub.net); CleantechHUB operates the Climate Innovation Data Matching framework; PASO has field presence across the target subregiones. This funding builds the anticipatory scoring layer over the warehouse and runs the pilot across eight named ethnic-community cacao/coffee initiatives in Pacífico Nariñense, Chocó, and Putumayo — proving the model before scaling to all 170 municipios.

## TECH challenge alignment

PDET-CIDM bridges both TECH4Emergencies and TECH4Nature.

**TECH4Emergencies — Anticipatory Action:** the system operationalises a genuine AA framework. It ingests dynamic risk indicators — Copernicus Sentinel-2 and NASA/UMD DIST-ALERT deforestation alerts plus IDEAM precipitation anomalies — and an AI model converts them into a composite, cooperative-level risk score. When the score crosses a calibrated threshold, it triggers pre-emptive, in-kind support within 14 days, before economic stress forces an irreversible forest-clearing decision. This is the logic of anticipatory cash triggers, applied to commodity-driven deforestation in fragile, post-conflict settings.

**TECH4Nature:** the same engine uses AI and remote sensing to protect and restore nature. It detects emerging degradation around eight ethnic-community agroforestry cooperatives, directs adaptation and EUDR-compliance support to keep standing forest standing, and verifies outcomes through repeat satellite passes over 5km buffers — a measurable, nature-positive feedback loop.

Technical expertise and use case: CleantechHUB built and operates the PDET warehouse (108,671 records, 170 municipios; live FastAPI at pdet-api.cleantechhub.net) and the Climate Innovation Data Matching framework. The AI value proposition is precision targeting: rather than broad, after-the-fact monitoring, the model fuses four signal classes (deforestation, climate, EUDR exposure, women/youth leadership) to surface exactly which community needs which intervention, and when. PASO Colombia contributes deep agroforestry and conflict-context expertise. Transformation potential: EUDR becomes a market opportunity (15–30% premiums), satellite alerts become early action rather than loss accounting, and at-risk communities gain durable preparedness — turning shocks into stronger livelihoods and standing forests.

## Potential for impact

Beneficiaries are among the most vulnerable in the Global South: women-led, Afro-Colombian and Indigenous cooperatives in post-conflict, climate-exposed PDET territories. The solution improves resilience by simultaneously protecting income (EUDR market access + climate-adaptation TA) and the ecosystems they depend on (preventing forest clearing).

End-of-project targets (per GRP indicator guidance):

- CORE1 — People supported: 800 producers across eight cooperatives, ≥50% women or youth; ~6,000 community-level indirect beneficiaries.
- CORE2 — Investments mobilised: USD 200,000 (climate-finance donor matches via CleantechHUB's Climate Innovation Data Matching framework + deforestation-free supply-chain purchase commitments).
- Project-specific: 8 EUDR-compliance dossiers prepared; ≥3 buyer agreements signed; hectares of forest within 5km buffers verified standing via repeat satellite passes.

Route to impact: AI surfaces at-risk cooperatives → 14-day pre-emptive bundle → forest stays standing + market access secured + adaptation finance flows. Each link is concrete and independently verifiable: repeat Copernicus/DIST-ALERT imagery confirms forest cover; buyer contracts confirm market access.

Long-term impact: a satellite-verifiable model for directing climate-adaptation finance to the precise communities and moments where intervention prevents irreversible loss — replicable across all 170 PDET municipios and to other EUDR-affected smallholder geographies.

Managing for results: PASO Colombia's established semi-annual reporting and impact-measurement systems (already tracking 2,368 jobs and 89% social-fabric improvement across its portfolio) generate gender- and youth-disaggregated evidence against each indicator, complemented by the warehouse's baseline data and an academic M&E partner.

## Equity

Equity is structural, not an add-on. The eight pilot initiatives are drawn from the Government of Colombia's Proyectos Étnicos MEC 2026 portfolio — every one is an Afro-Colombian, Indigenous, or Raizal community organisation in PDET territories, the 170 municipios most marginalised by armed conflict.

Beneficiary composition exceeds the >50% women-or-youth threshold and likely reaches 70%. Cacao cooperatives in Carmen del Darién (Chocó), Magüí Payán (Nariño), and Vigía del Fuerte (Antioquia–Chocó border) report female membership above 55%; PDET territories have youth-heavy demographic pyramids (median rural age 22–26 in Chocó and Nariño).

Meaningful involvement, not just benefit: PASO Colombia's Escuelas Rurales Alternativas methodology — refined over 12 years across 2,368 jobs and 63 community alliances — places community decision-making at the centre of every intervention. Women and youth co-design the adaptation measures, consent to plot geolocation, and lead local implementation. PASO's Redes de Paz (recognised by the Kroc Institute of Notre Dame as a peacebuilding model) operate the independent grievance mechanism, separate from CleantechHUB.

All monitoring data is disaggregated by gender, age, and ethnic identity. EUDR geolocation is performed with free, prior and informed consent, and data ownership remains with the communities — avoiding the extractive data practices that often accompany compliance schemes. By securing premium market access for women-led cooperatives, the project shifts economic power toward those historically excluded from formal value chains, turning a regulatory threat (EUDR) into an equity opportunity.

## Scalability and additionality

Scalability is built into the architecture. The PDET warehouse already covers all 170 PDET municipios — the eight pilot initiatives are under 0.1% of the 33,007 community-identified PATR initiatives the AI scoring system can already operate on. Post-pilot, the methodology extends without redevelopment to all 16 PDET subregiones, then to other territorial-development contexts (Peru's sierra and selva, Guatemala's faja transversal). The open-data feeds (Copernicus, NASA/UMD DIST-ALERT, Global Forest Watch) are global, so the model replicates to any EUDR-affected smallholder geography — Ghanaian and Ivorian cocoa, Indonesian palm, Brazilian Amazon supply chains.

Demand is real and time-bound: EUDR enforcement (December 2026 / June 2027) creates immediate, regulation-driven demand from both smallholders (who risk market exclusion) and buyers (who need compliant supply). CleantechHUB will publish the scoring methodology and data architecture as open knowledge products in English and Spanish; the codebase is already operational on a public API.

Additionality: nothing comparable exists. The grant funds the anticipatory scoring layer and the field response — neither of which any actor currently provides. It does not displace existing funding; it complements the ART MEC-2026 portfolio (which identifies projects but cannot target deforestation pressure) and channels new climate finance toward initiatives currently invisible to international cooperation. Synergy, not duplication: GRP funds the anticipatory mechanism, while the PDET warehouse, PASO's field network, and the cooperatives' own production are existing assets the project activates rather than rebuilds.

## Profitability and sustainability

Three convergent streams reduce grant dependence over time.

First, market revenue: EUDR-compliant cacao and specialty coffee command 15–30% price premiums in the EU. For the eight pilot cooperatives this represents an estimated USD 200,000–350,000 in additional annual revenue accruing directly to producers — sustaining participation without ongoing producer-level subsidy.

Second, low marginal operating cost: the PDET warehouse already runs on CleantechHUB's existing infrastructure (VPS, database, API, monitoring). The marginal cost of operating the anticipatory scoring layer is roughly USD 800/month, covered by CleantechHUB's broader Climate Innovation Data Matching operations, funded through consulting revenue and complementary grants.

Third, institutional adoption: CleantechHUB's active collaboration with the Agencia de Renovación del Territorio on Climate Innovation Data Matching provides a credible pathway to embedding the anticipatory triggers into government territorial-planning workflows.

Exit strategy: by December 2027 the system is jointly operated by CleantechHUB (technical) and PASO Colombia (field), with market revenue sustaining producers and a clear route to government uptake — no further GRP funding required. There is strong scope for policy engagement on EUDR-readiness for smallholders.

Fundraising status and track record: CleantechHUB has managed grants from P4G, UNDP-AFCIA, GIZ, Climate-KIC, and the Pvblic Foundation. Financial oversight is provided by external professional accountants (Soluciones JV) and an independent statutory auditor (Revisor Fiscal, LG Asesores Contables SAS); the 2025 financial statements are signed and audited. PASO Colombia operates under One Earth Future Foundation's financial governance standards.

## Team

- Gideon Blaauw — M, 49 — gideon.blaauw@cleantechhub.net — Legal Representative & Project Lead, CleantechHUB. Built the PDET warehouse and Climate Innovation Data Matching framework.
- Juan Fernando Lucio López — M — paso@pasoglobal.org — Director, PASO Colombia / One Earth Future. LSE economist; leads field implementation and MEL.
- Angelica Diaz, Tech Lead — F, 46 — builds and operates the AI anticipatory scoring layer.

The consortium triangulates the three competencies the project needs. CleantechHUB brings the unique data asset (108,671-record PDET warehouse — the only such infrastructure in Colombia), AI/data engineering, and grant-management track record (P4G, UNDP-AFCIA, GIZ, Climate-KIC). PASO Colombia brings deep community trust and a peacebuilding methodology validated by the Kroc Institute and the Carter Center, with field presence in all three target subregiones, 2,368 jobs created and USD 11.5M mobilised through its Alianzas Comerciales Colaborativas. The Agencia de Renovación del Territorio collaborates as the government PDET coordinator, with whom CleantechHUB jointly reviewed the MEC-2026 portfolio.

CleantechHUB leads as applicant and contract holder; PASO Colombia is the named, signed consortium partner (LOI attached). Per GRP guidance, a full implementation team is not required at application; remaining technical roles are recruited on award.

## Risks

| Risk | Impact | Probability | Mitigation |
| --- | --- | --- | --- |
| Satellite false positives | Medium | Medium | Composite scoring (deforestation alert + climate signal + EUDR exposure + funding gap) plus mandatory PASO field verification before any action bundle deploys. |
| EUDR enforcement delay or weakening | Medium | Medium | Even absent EUDR, geolocated deforestation-free cacao/coffee earns a ~10–15% specialty-market premium; the value proposition and forest-protection outcome hold regardless. |
| Community refusal or consent withdrawal | Medium | Low | PASO's FPIC protocols and co-design methodology are standard; no intervention proceeds without consent; communities retain data ownership. |
| Security and access in conflict-affected territories | High | Medium | PASO's Redes de Paz are the established, trusted peacebuilding presence in these subregiones; ART coordinates territorial access; no consortium member operates where safety protocols are absent. |
| Partner or staffing gaps | Medium | Low | PASO LOI signed before submission; consortium agreement formalised within 60 days of award; technical roles recruited early. |
| Climate event damaging a target cooperative during the pilot | Medium | Medium | This is precisely the shock the project anticipates; the adaptation-TA and finance-matching bundle is designed to respond. |

Trade-offs and unintended consequences: we guard against data dependence or surveillance perceptions by keeping geolocation consent-based and community-owned. No activity carries environmental or social do-harm risk; the project is net forest-positive by design.

## Work plan

**Q1 2027 (Jan–Mar):** Consortium agreement signed; AI anticipatory scoring layer built and calibrated over the warehouse for the eight pilot initiatives; baseline established with PASO and the academic M&E partner; community consent secured across the three subregiones. Deliverables: operational scoring system; baseline report. Due 31 Mar 2027.

**Q2 2027 (Apr–Jun):** Live monitoring begins on Copernicus/DIST-ALERT feeds; first triggers processed; EUDR-compliant geolocation completed for the first cooperatives; climate-adaptation technical assistance delivered via PASO's ERA methodology. Deliverables: 4+ EUDR dossiers; TA logs. Due 30 Jun 2027.

**Q3 2027 (Jul–Sep):** Remaining geolocation and TA completed across all eight initiatives; deforestation-free supply-chain matchmaking events held; first buyer agreements signed; climate-finance donor matches initiated via Climate Innovation Data Matching. Deliverables: 8 EUDR dossiers; ≥3 buyer agreements; donor-match pipeline. Due 30 Sep 2027.

**Q4 2027 (Oct–Dec):** Endline measurement; repeat satellite verification of forest cover within 5km buffers; open knowledge product (methodology + replication playbook) published in English and Spanish; results shared with ART for institutional uptake. Deliverables: endline/impact report; published methodology; sustainability handover. Due 31 Dec 2027.

Approach: anticipatory triggers run continuously throughout; each trigger initiates the 14-day pre-emptive bundle. Semi-annual progress reports (June, December) submitted under GRP's MEL framework. PASO leads field activities; CleantechHUB leads the technical layer and reporting; the academic partner leads independent M&E.

## Budget (concept note)

Total requested: USD 50,000 (12 months). Personnel held to 39%.

| Line | USD | Share | Notes |
| --- | --- | --- | --- |
| Personnel | 19,500 | 39% | Project Lead 0.4 FTE; Data Scientist 0.2 FTE; Program Coordinator 0.2 FTE |
| Pilot delivery | 14,000 | 28% | EUDR geolocation; ERA TA; supply-chain matchmaking |
| Travel & logistics | 5,500 | 11% | ~4 missions each to Pacífico Nariñense, Chocó, Putumayo |
| AI development & data integration | 4,000 | 8% | Scoring layer over existing warehouse; Copernicus/DIST-ALERT/GFW |
| MEL | 4,000 | 8% | Academic M&E subcontract; baseline/endline |
| Communications | 1,500 | 3% | Open knowledge product; visibility |
| Overhead | 1,500 | 3% | Administration and audit |
| **Total GRP** | **50,000** | **100%** | |

Co-financing (in-kind, ~USD 88,000; 2.8× leverage): CleantechHUB PDET warehouse and infrastructure (~USD 35,000) and REIN Hubs network (~USD 15,000); PASO Colombia field presence and MEL systems (~USD 33,000); academic partner M&E time (~USD 5,000).

Financial management: CleantechHUB uses Soluciones JV and Revisor Fiscal LG Asesores Contables SAS; 2025 statements signed and audited. PASO operates under One Earth Future Foundation systems.
