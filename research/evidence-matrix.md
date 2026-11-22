# Evidence matrix

Links the substantive claims in each chapter to their sources and to the strength of support. One
section per chapter, filled in when the chapter is written. Planned chapters' expected sources are in
`curriculum.yaml`.

Columns: **Claim** as the chapter states it (short form). **Label** is the evidence label used in the
text. **Sources** are bibliography ids. **Basis** is how much of the source supports the claim
(full text, abstract, official summary, idea-level attribution of a metadata-only source).

## Chapter 27 — Quality Transformation at Enterprise Scale

Revised 2026-11-19 after the Part V fix pass: rows on psychological safety, postmortem culture, SPACE, and technical debt moved to the chapters that own them (19, 21, 25); chapter 27 cross-references them.

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A stock changes only through its flows and responds slowly to changes in flow | Practitioner (systems thinking) | meadows2008thinking | idea-level |
| 2 | A system's output is governed by its tightest constraint; improving non-constraints does not raise output | Practitioner | goldratt1984goal | idea-level |
| 3 | Small batches and an always-releasable system make releases understandable and reversible | Practitioner | humble2010continuous | idea-level |
| 4 | DORA's current guide lists five metrics in throughput and instability groups | Industry research | dora-metrics-guide | full text, page dated 2026-01-05 |
| 5 | DORA reports speed and stability are not trade-offs and its metrics correlate for most teams | Industry research, with survey caveats stated | dora-metrics-guide; forsgren2018accelerate | full text (guide); idea-level (book) |
| 6 | Indicators used for decisions are subject to distorting pressure (Campbell's law) | Expert opinion, widely cited | campbell1979assessing | idea-level; exact wording not quoted (gap G7) |
| 7 | DORA warns that using its metrics as goals invites gaming, and against comparing teams | Industry research | dora-metrics-guide | full text |
| 12 | A manager's output is the output of the organization under their influence | Practitioner | grove1983high | idea-level |
| 13 | 100 percent reliability is rarely the right target; error budgets as a decision mechanism (used in solution X1) | Documented practice | google2017embracing | full text |
| 15 | All Northstar figures, the capacity model, and the case-study results | Illustrative | — | fictional, recomputed in session 1 |

Book's own recommendations in the chapter (labeled as such in the text or clearly the author's
reasoning): inflow before stock; the capacity model and J-curve framing; the program-shape table; the
failure-mode catalogue; the cadence table; the 90-day playbook.

## Chapter 19 — Defining, Measuring, and Owning Software Quality

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Garvin identified five approaches to defining quality (transcendent, product-, user-, manufacturing-, value-based) and proposed eight dimensions | Research (conceptual management article) | garvin1984product | abstract and article landing-page text |
| 2 | ISO/IEC 25010:2023 defines a product quality model of nine characteristics with subcharacteristics, for specifying, measuring, and evaluating quality, eliciting requirements and setting test objectives | Standard | iso25010-2023 | abstract; characteristic names deliberately not printed |
| 3 | At three product companies, testing was done by many roles; testing by people with customer contact and domain expertise was important; developer-found defects had the highest fix rates, specialist-tester defects the lowest | Research finding, limits stated | mantyla2012who | abstract |
| 4 | After Firefox moved to rapid releases, system testing narrowed to the highest-risk features and regressions, and sustaining a testing community got harder, so Mozilla added contractors | Research finding, one project | mantyla2013rapid | abstract |
| 5 | No study directly compares central, embedded, and team-owned QA on outcomes | Gap statement | — | research-gaps G4 (partly addressed by rows 3 and 4) |
| 6 | Coverage has a low to moderate correlation with fault-detection effectiveness once suite size is controlled; it should not be a quality target | Research finding | inozemtseva2014coverage (entry in pending-sources/ch22.yaml; not duplicated) | abstract |
| 7 | Google is known for engineer-owned testing supported by shared infrastructure | Documented practice | winters2020software | idea-level |
| 8 | Platform and enabling teams supply self-service capability and help teams acquire skills | Practitioner | skelton2019team | idea-level |
| 9 | Quality is built in through an automated deployment pipeline rather than inspected in at the end | Practitioner | humble2010continuous | idea-level |
| 10 | DORA's guide lists five delivery metrics in two groups and warns against using them as goals or to rank teams | Industry research | dora-metrics-guide; forsgren2018accelerate | full text (guide); idea-level (book) |
| 11 | Team ownership of outcomes, embedded quality engineers where risk justifies, platform support, central QA only for specialized or mandated testing (D4) | This book's recommendation | — | synthesis of rows 3–10 |
| 12 | All Northstar figures, normalizations (defects per engineer and per deployment), the measure set, the QA allocation, and the case narrative | Illustrative | — | fictional; recomputed from baseline-data.md on 2026-11-19 |

## Chapter 20 — Engineering Standards and Their Governance

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Rules have a learning and maintenance cost and must pull their weight, so the set is kept small | Documented practice | schwartz2020style | full text (chapter) |
| 2 | Rules are mandatory with approved exceptions; guidance leaves room for judgment | Documented practice | schwartz2020style | full text |
| 3 | Rules are revisited when worked around or burdensome; exceptions are rare and frequent requests signal a rule needs revisiting | Documented practice | schwartz2020style | full text |
| 4 | Consistency operates at levels from file to team to project to codebase | Documented practice | schwartz2020style | full text |
| 5 | MUST is an absolute requirement, SHOULD may be ignored for weighed reasons, MAY is optional; imperatives should be used sparingly | Standard | bradner1997rfc2119 | full text |
| 6 | Platform teams reduce cognitive load through internal services; enabling teams help others acquire capabilities | Practitioner | skelton2019team | idea-level |
| 7 | Effective false positive defined by developer action, not tool correctness | Documented practice | sadowski2018lessons | full text |
| 8 | A nightly dashboard saw little use; a fix-it week fixed 640 of 3,954 reviewed warnings (16%); a review integration was dropped over false positives and per-user customization | Documented practice | sadowski2018lessons | full text |
| 9 | Compiler-error checks must have no effective false positives and concern correctness; developers ignored warnings | Documented practice | sadowski2018lessons | full text |
| 10 | Review-time checks may have up to 10% effective false positives; analyzers above a 10% not-useful ratio are disabled; threshold initially chosen somewhat arbitrarily | Documented practice | sadowski2018lessons | full text |
| 11 | In 20 developer interviews, false positives and warning presentation were barriers to static analysis use | Research finding (small qualitative sample) | johnson2013why | abstract |
| 12 | Fitness functions: automated tests of architectural characteristics run continuously | Practitioner | ford2017building | idea-level |
| 13 | SLSA v1.2 defines tracks with ascending levels; build track L0 to L3 | Standard | slsa-spec | full text |
| 14 | Formal structures adopted for legitimacy are decoupled from activities; inspection replaced by confidence and good faith | Research (theory, general organizations); application to standards is this book's analogy | meyer1977institutionalized | abstract |
| 15 | Indicators used for decisions come under distorting pressure | Expert opinion, widely cited | campbell1979assessing | idea-level, not quoted (gap G7) |
| 16 | Well-Architected reviews are framed as constructive conversations, not audits | Official documentation | aws-well-architected | full text |
| 17 | SSDF is a set of high-level secure development practices offering common vocabulary | Standard | nist2022ssdf | abstract |
| 18 | A council with capacity below its arrival rate accumulates an unbounded backlog (4 per fortnight vs 6 arriving) | This book's recommendation (arithmetic) | none | illustrative |
| 19 | Seven-part anatomy of a standard; enforcement ladder; tier criterion decided outside the team; owner-level decisions with a service level | This book's recommendation | synthesis of 1–14 | reasoning shown in chapter |
| 20 | Northstar standards page, CI checks, guild, PR sample, triage, and day-90 results | Illustrative | research/northstar-additions/ch20.md; components.csv | invented; tier 1 readiness computed from components.csv |

## Chapter 21 — Technical Debt: Identification, Economics, and Prioritization

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Cunningham likened first-time code to debt that speeds development if repaid promptly; unrepaid debt accrues interest and can bring an organization to a standstill | Expert opinion (experience report) | cunningham1992wycash | full text |
| 2 | The metaphor was introduced to explain the need for refactoring to non-technical stakeholders; the term came to cover many phenomena | Research commentary | kruchten2012technical | abstract only (guest editors' introduction) |
| 3 | A mapping of 94 studies (1992 to 2013) classified debt into 10 types, found "debt" used ambiguously, and code debt most studied | Research finding (about the literature) | li2015systematic | abstract |
| 4 | Fowler's quadrant: reckless/prudent by deliberate/inadvertent; prudent-inadvertent debt is unavoidable | Expert opinion | fowler2009debtquadrant | full text |
| 5 | 1,831 surveyed practitioners in three organizations named architectural decisions the most important source of debt and found tools unhelpful for managing details | Research finding (perception) | ernst2015measure | abstract |
| 6 | Developers in a 43-person longitudinal study reported wasting on average 23% of development time due to debt | Research finding, self-reported, small sample | besker2018technical; besker2019productivity | abstract |
| 7 | The journal version validated on an independent dataset; developers were often forced to add debt; extra time went mostly to additional testing | Research finding | besker2019productivity | abstract |
| 8 | In 39 proprietary codebases, low-quality code had about 15 times more defects and issues took on average 124% more development time | Research finding, observational, tool-defined quality | tornhill2022codered | abstract (arXiv) |
| 9 | Cost of delay as a decision tool is widely credited to Reinertsen | Practitioner | reinertsen2009principles | idea-level (metadata only) |
| 10 | SAFe defines WSJF as relative cost of delay over relative job size, with its named inputs | Official documentation (framework) | safe-wsjf | full text |
| 11 | No large peer-reviewed study measuring organizational debt cost with system data was found | Gap statement | — | research-gaps G9 |
| 12 | No evidence identifies a correct standing debt percentage | Gap statement | — | proposed new gap |
| 13 | Northstar register pricing, case study, and all derived numbers | Illustrative | — | fictional; recomputed in session |

Book's own recommendations (labeled in the text or clearly the author's reasoning): interest over
principal as the defining quantity; dormant-debt reasoning; the six working kinds of debt; the
interest/principal ratio with trigger override; remove/reduce/contain/accept; the 10 to 20 percent
starting share; governance mechanics; failure-mode catalogue; playbook.

Proposed research-gap update for the maintainer: G6 is partly addressed (WSJF verified as SAFe's,
`safe-wsjf`); G9 partly addressed (`besker2019productivity`, `ernst2015measure`, `tornhill2022codered`),
still no multi-company study using system data. New gap: evidence on the size of standing debt
allocations.

## Chapter 22 — Testing Strategy and Test Architecture

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | The test pyramid favors many unit tests and few UI tests because broad UI tests are slow, brittle and non-deterministic; Fowler credits Cohn and notes the case weakens if high-level tests are cheap and reliable | Expert opinion | fowler2012testpyramid | full text |
| 2 | The testing trophy emphasizes integration tests as an ROI judgment; definitions are loose | Expert opinion | dodds2021trophy | full text |
| 3 | The testing honeycomb for microservices emphasizes integration tests through interaction points and avoids tests that depend on other live systems | Documented practice | schaffer2018honeycomb | full text |
| 4 | Google's rough guideline is 80/15/5 unit/integration/E2E by count; ice cream cone and hourglass are antipatterns | Documented practice | bender2020testing | full text (summarized, CC BY-NC-ND) |
| 5 | No research shows one test distribution yields fewer escapes than another | Gap statement | — | searched in session; none found |
| 6 | Test size (resources) is distinct from scope; tests should be hermetic and avoid shared databases | Documented practice | bender2020testing | full text |
| 7 | Consumer-driven contracts: consumers state expectations, provider runs them, enabling independent evolution | Practitioner (pattern) | robinson2006cdc | full text |
| 8 | At Google, few tests ever fail; failing tests sit near the code; code recently modified by more than three developers breaks more often | Industry research (association) | memon2017taming | abstract (Google Research summary) |
| 9 | First extensive study of flaky tests: 201 fix commits in 51 open-source projects; root causes and fixes classified | Research finding | luo2014flaky | abstract |
| 10 | Survey of 76 papers; flaky tests threaten methods assuming outcome depends only on code | Research (survey) | parry2022flaky | abstract |
| 11 | Google 2016: about 1.5% of test runs flaky; almost 16% of tests show flakiness; about 84% of pass-to-fail transitions involve a flaky test; insertion rate about equals fix rate; retries, three-strikes and quarantine described, with quarantine able to mask bugs | Documented practice | micco2016flaky | full text |
| 12 | Tests lose value as flakiness approaches 1%; Google's rate around 0.15% | Documented practice | bender2020testing | full text; measurement differs from claim 11, stated in chapter |
| 13 | Coverage has low to moderate correlation with effectiveness when suite size is controlled; should not be a target | Research finding, limits stated | inozemtseva2014coverage | abstract |
| 14 | Coverage targets tend to become ceilings | Documented practice | bender2020testing | full text |
| 15 | Mutant detection correlates with real-fault detection independently of coverage (357 faults, 5 programs) | Research finding | just2014mutants | abstract |
| 16 | Diff-based, filtered mutation testing during code review is practical at very large scale (24,000+ developers) | Industry research (adoption, not outcome) | petrovic2021mutation | abstract |
| 17 | Automated pipeline with fast checks on every change keeps software releasable | Practitioner | humble2010continuous | idea-level |
| 18 | Exploratory testing finds what scripted checks miss | Practitioner consensus | — | no controlled industrial study found; stated in chapter |
| 19 | Migration rehearsal, ordering checks, configuration as code | This book's recommendation | — | labeled in chapter |
| 20 | All Northstar figures, the portfolio table, flakiness cost estimate, reallocation and case-study results | Illustrative | — | baseline plus research/northstar-additions/ch22.md, recomputed |

Book's own recommendations in the chapter: designing the portfolio from detection-point
classification and feedback time; flakiness budget, owner and admission check; coverage used only for
gaps; mutation testing scoped to changed high-risk code; the decision diagram and table; gate
retirement in steps; the playbook.

## Chapter 23 — Code Review, CI/CD, and Release Engineering

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Small batches and an always-releasable, automated path to production make releases small and understandable | Practitioner | humble2010continuous | idea-level |
| 2 | Decoupling deployment from release is a core DevOps practice | Practitioner | kim2016devops | idea-level |
| 3 | Defect-finding is the main stated motivation for review, but review finds fewer defects than expected and delivers knowledge transfer, awareness, and alternative solutions; understanding the change is the central challenge | Research finding (one company) | bacchelli2013expectations | abstract |
| 4 | Review increases the number of distinct files a developer knows about by 66 to 150 percent | Research finding | rigby2013convergent | abstract |
| 5 | Review coverage and participation are significantly linked with post-release defects (up to two and five additional defects per component) | Research finding (three OSS projects) | mcintosh2014impact | abstract |
| 6 | Google's modern review studied with interviews, a survey, and logs of about 9 million changes | Documented practice with research method | sadowski2018modern | abstract |
| 7 | Effect of change size on review effectiveness | Practitioner consensus; no study verified (gap) | none | stated as gap in text |
| 8 | Multi-approval review and asynchronous review queues are trunk-based development pitfalls | Industry research | dora-cap-trunk-based | full text |
| 9 | CI guidance: daily merges, build and tests on every change, broken build top priority, about ten minutes as an upper limit for feedback | Industry research | dora-cap-continuous-integration | full text |
| 10 | CI appears to help open-source projects release more often | Research finding, observational | hilton2016usage | abstract |
| 11 | CI associated with more integrated contributions and no observable loss of quality | Research finding, observational | vasilescu2015quality | abstract |
| 12 | 2016-2017 DORA data: three or fewer branches, daily merges, no freezes associated with higher performance | Industry research | dora-cap-trunk-based | full text |
| 13 | Toggle categories, lifetimes, carrying cost, expiry, and testing advice | Practitioner | hodgson2017featuretoggles | full text |
| 14 | Toggles reconcile rapid release with long-term feature work and add technical debt (Chrome) | Research finding | rahman2016feature | abstract |
| 15 | Knight Capital: reused flag, one of eight servers missed, no second-person review, about 45 minutes, about $460M loss, uninstalling new code worsened the problem | Official finding (regulatory order) | sec2013knight | full text, paragraphs 13-17, 26, 27 |
| 16 | Canarying as canary vs control comparison; split metrics by population; blue-green cutover is a before/after comparison unless traffic is split gradually; few user-visible attributable metrics | Documented practice | warner2018canarying | full text |
| 17 | Heavyweight external change approval associated with worse delivery performance and no lower change fail rate; peer review satisfies segregation of duties | Industry research | dora-cap-change-approval | full text |
| 18 | DORA's five metrics in throughput and instability groups | Industry research | dora-metrics-guide | full text |
| 19 | Software Engineering at Google describes one organization's review and CI practice | Practitioner | winters2020software | idea-level |
| 20 | All Northstar figures, the lead-time decomposition, the flaky-rerun upper bound, and the case study | Illustrative | northstar-additions/ch23.md | fictional; recomputed |

Book's own recommendations in the chapter: the six pipeline properties; revert-first and quarantine
rules; trunk-based development with the mobile and no-flags exceptions; the release-strategy table by
tier and change type; the staged cadence plan with entry criteria; the failure-mode catalogue.

Research gaps found: no verified study of change size versus review effectiveness or review
turnaround; no verified study of rollback or progressive-delivery outcomes beyond documented
practice; the Sadowski et al. findings beyond the abstract (for example, review latency and change
size at Google) were not read.

## Chapter 24 — Reliability Engineering: SLOs, Error Budgets, Observability, and Operational Readiness

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | 100 percent is probably never the right reliability target; match reliability to accepted risk | Documented practice | google2017embracing | full text |
| 2 | SLI, SLO, and SLA definitions; a commitment without consequences is an SLO | Documented practice | google2017service | full text |
| 3 | SLIs as good ÷ valid events; specification vs implementation; measurement points trade off quality, coverage, cost | Documented practice | thurgood2018implementing | full text |
| 4 | Common SLI types include availability, latency, freshness, correctness; model critical user journeys; four-week rolling window default | Documented practice | thurgood2018implementing | full text |
| 5 | Error budget as a shared, objective metric replacing political negotiation; releases slow or stop when exhausted | Documented practice | google2017embracing | full text |
| 6 | Product, developers, and SREs should all approve the error budget policy; if not enforced, revisit SLOs | Documented practice | thurgood2018implementing | full text |
| 7 | Two schools of thought on whether dependency-caused misses should freeze changes | Documented practice | thurgood2018implementing | full text |
| 8 | Example policy: freeze except P0 and security fixes; postmortem above 20 percent of budget; not a punishment; CTO arbitrates | Documented practice | thurgood2018policy | full text |
| 9 | Alerting judged by precision, recall, detection time, reset time; burn-rate definition | Documented practice | thurgood2018alerting | full text |
| 10 | Starting multiwindow burn-rate parameters (14.4/1 h, 6/6 h page; 1/3 d ticket; short window about 1/12) | Documented practice | thurgood2018alerting | full text |
| 11 | Low-traffic services need synthetic traffic, combined services, or a lower SLO or longer window | Documented practice | thurgood2018alerting | full text |
| 12 | Four golden signals; page on symptoms, use causes for debugging; pages urgent, actionable, need judgment | Documented practice | google2017monitoring | full text |
| 13 | Observability as the ability to ask new questions of a running system, distinct from monitoring | Expert opinion (vendor authors) | majors2022observability | idea-level |
| 14 | Google's PRR examines architecture, monitoring, emergency response, capacity, change management, performance; did not scale; move to frameworks | Documented practice | google2017engagement | full text |
| 15 | AWS ORR distills incident lessons into questions; teams self-assess across a service's life | Documented practice | aws2022orr | full text (introduction) |
| 16 | Well-Architected review is a constructive conversation, not an audit | Standard | aws-well-architected | full text |
| 17 | At most two incidents per 12-hour shift; minimum rotation sizes; pager-load inputs; trial alerts without paging; compensate out-of-hours on-call | Documented practice | cook2018oncall | full text |
| 18 | On-call capped at a quarter of SRE time; underload is a risk | Documented practice | google2017oncall | full text |
| 19 | On-call scheduling can pose risks to sleep, mental health, personal life; critical gaps in literature | Research finding (review, mostly non-software) | nicol2004oncall | abstract |
| 20 | On-call from home appears to reduce sleep quantity and usually quality; stress-physiology data insufficient (eight studies) | Research finding (systematic review, non-software) | hall2017oncall | abstract |
| 21 | No peer-reviewed study of on-call load among software engineers was found | Gap statement | — | searched this session; proposed new research gap |
| 22 | "When error budgets do not work" list; reporting mode below target; tier readiness bar; four blocking requirements; question bank from own incidents | This book's recommendation | — | reasoning shown in chapter |
| 23 | All Northstar SLOs, traffic volumes, replays (INC-403, INC-413), incident classification, and case-study events | Illustrative | — | fictional; arithmetic recomputed; additions in research/northstar-additions/ch24.md |

Sources cited for navigation only: beyer2016sre, beyer2018workbook (the books containing the chapters above; metadata only).

## Chapter 25 — Incidents, Postmortems, and Change Failure Analysis

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Overt failure in complex systems needs several small faults to combine; latent faults are always present; hindsight makes earlier signals look obvious | Expert opinion (safety science) | cook1998complex | full text |
| 2 | Single root-cause attribution is mistaken for complex systems and reflects a social need to blame; remedies aimed at the last step rarely prevent the next accident | Expert opinion (safety science), labeled as not an empirical result about software | cook1998complex | full text |
| 3 | Incident roles: commander, operations, communications, planning; declare early with criteria; explicit handoff; live incident document | Documented practice | google2017managing | full text |
| 4 | Blameless postmortems look for contributing causes without indicting individuals; review triggers defined in advance | Documented practice | google2017postmortem | full text |
| 5 | Fear of reprimand makes engineers withhold the details needed to understand a failure, so it is likely to recur; "second stories"; hindsight bias and attribution error; engineers remain accountable for helping make the system safer | Practitioner (first-hand account) | allspaw2012blameless | full text (archived copy) |
| 6 | Root cause analysis can make people less likely to admit mistakes; MTTR can be unreliable | Industry research, abstract only | nash2022void | official summary (talk abstract) |
| 7 | Qualitative study of 30 incidents from interviews and published postmortems | Research finding (qualitative) | sillito2020failures | abstract |
| 8 | Failure learning informal and ad hoc; recurring failures persist without structured processes | Research finding (qualitative, 15 interviews) | anandayuvaraj2026learning | abstract |
| 9 | Just-culture implementation evidence is scant and mostly theoretical; outcome research needed | Research finding (integrative review) | murray2023just | full text |
| 10 | A focus on safety rather than individual blame enhances trust in error reporting; less experienced staff fear blame more | Research finding (systematic review, healthcare) | vanmarum2022barriers | abstract |
| 11 | Psychological safety associated with learning behavior, which mediated performance, in 51 teams in one manufacturing company | Research finding, limits stated | edmondson1999psychological | abstract |
| 12 | No peer-reviewed study measures the outcome effect of blameless review in software; cross-domain evidence supports the mechanism, not the outcome | Gap statement | murray2023just; vanmarum2022barriers; sillito2020failures | research-gaps G1; disputed claim D6 |
| 13 | Change fail rate is the ratio of deployments needing immediate intervention | Industry research | dora-metrics-guide | full text |
| 14 | Classifying defects by meaning gives in-process feedback (Orthogonal Defect Classification) | Research finding | chillarege1992orthogonal | abstract |
| 15 | All Northstar figures, the control-point classification, re-ratings, and case-study results | Illustrative | — | fictional; recomputed from `incidents-last-quarter.csv` in this session; additions in `research/northstar-additions/ch25.md` |

Book's own recommendations in the chapter (labeled as such in the text or clearly the author's
reasoning): the four properties of severity definitions; the two customer-communication rules; trigger
versus contributing factors; the position on D6 (blameless toward individuals, strict about truthfulness
and follow-through); the control-point decision diagram and its three classification rules; the
decision table; the failure-mode catalogue; the playbook.

Notes for the maintainer:

- `allspaw2012blameless` is now verified from a Wayback Machine capture (2013-06-09) of the original
  codeascraft.com URL. The pending entry replaces the unverified bibliography entry with the same id;
  delete the old one when merging. Research gap G2 can be closed.
- G1 remains open. Searched this session: healthcare just-culture reviews (found `murray2023just`,
  `vanmarum2022barriers`; neither measures outcomes) and recent software studies (found
  `anandayuvaraj2026learning`, qualitative). No outcome study found.

## Chapter 26 — Security and Software Supply-Chain Quality

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | CSF 2.0 has six functions (Govern, Identify, Protect, Detect, Respond, Recover); Govern is central; 2.0 adds emphasis on governance and supply chains | Standard | nist2024csf | full text (bibliography claims) |
| 2 | CSF Core outcomes are not a checklist; order of functions implies no sequence or importance | Standard | nist2024csf | full text (bibliography claims; passage re-read in the PDF on 2026-11-19) |
| 3 | CSF Organizational Profiles: Current and Target Profiles, gap analysis, prioritized action plan; GV.SC category for supply chain risk management | Standard | nist2024csf | full text, PDF text extracted and read 2026-11-19; not yet in the entry's `claims` (maintainer: add on merge) |
| 4 | SSDF v1.1 is a core set of high-level secure development practices integrated into any SDLC; aims and common vocabulary | Standard | nist2022ssdf | abstract |
| 5 | SSDF practice groups: PO, PS, PW, RV | Standard (official documentation) | nist-ssdf-project | full text of project page |
| 6 | SSDF v1.2 (SP 800-218 Rev. 1) initial public draft December 17, 2025; comments closed January 30, 2026; no final seen | Standard | nist2025ssdf-draft | landing page |
| 7 | SLSA v1.2: Build L0–L3 and Source L1–L4 with the level summaries given | Standard | slsa-spec | full text; re-verified on slsa.dev 2026-11-19 |
| 8 | SBOM minimum elements: three areas and seven baseline data fields | Standard | ntia2021sbom | full text (PDF read) |
| 9 | CISA 2025 SBOM minimum elements published as a draft for comment in August 2025, building on NTIA 2021 | Standard | cisa2025sbom-draft | official summary |
| 10 | CISA says to use the KEV catalog as an input to vulnerability prioritization | Official documentation | cisa-kev | full text |
| 11 | Study of ~400 npm security reports over six years, on discovery, fixing, and propagation via dependency constraints | Research (scope only, no finding claimed) | decan2018impact | abstract |
| 12 | Secret leakage affects over 100,000 public GitHub repositories; thousands of new secrets leaked daily | Research finding | meli2019git | abstract |
| 13 | Threat modeling's four questions; values include design fixes over checkbox compliance | Practitioner consensus | threatmodeling-manifesto2020 | full text |
| 14 | Champions appointed without support: wide variation between teams, perceived lack of support; appointment not sufficient | Research finding (single organization) | gutfleisch2023champions | abstract |
| 15 | Voluntary vs assigned champions differ in motivation and tasks; onboarding, communication, training challenges | Research finding (single organization) | nguyenduc2023champions | abstract |
| 16 | Security is one of six Well-Architected pillars; reviews are conversations, not audits | Official documentation (vendor) | aws-well-architected | full text (bibliography claims) |
| 17 | All Northstar security facts, capacity estimate, and case-study results | Illustrative | — | research/northstar-additions/ch26.md; arithmetic recomputed |

Book's own recommendations in the chapter: the three organizing questions (inventory, provenance,
ownership); the engineering-practice-to-CSF/SSDF mapping table (stated in the text as the book's,
not NIST's); remediation service levels and the prioritization decision tree; the organizational
model table; SLSA targets by tier; the measures table and its pairings; the failure-mode catalogue;
the 90-day playbook; the 10 percent champion time allocation.

Gaps: no peer-reviewed outcome evidence was found that SBOMs, SLSA levels, or remediation service
levels reduce breach rates; the chapter states this in the case study. The added elements in CISA's
2025 SBOM draft and the new practices in the SSDF 1.2 draft were not confirmed on primary pages and
are not claimed.

## Chapter 1 — What Engineering Management Actually Is

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A manager's output is the output of the organization they manage plus neighboring organizations they influence; prefer high-leverage activities | Practitioner | grove1983high | idea-level |
| 2 | Effective executives record where their time actually goes before deciding how to spend it | Practitioner | drucker1967effective | idea-level |
| 3 | Tech lead and people manager are related but distinct roles on a path from tech lead to CTO | Practitioner | fournier2017manager | idea-level |
| 4 | Engineering management at scale as the design of systems | Practitioner | larson2019elegant | idea-level |
| 5 | Four staff archetypes (tech lead, architect, solver, right hand); most companies recognize one or two; some have no technical track; tech lead manager is a separate management-ladder role | Expert opinion | larson-staff-archetypes; larson2021staff | full text (web chapter); idea-level (book) |
| 6 | Replacing a bottom-10% supervisor with a top-10% one raises team output more than adding a worker to a nine-person team; better bosses reduce quits (one firm, technology-based service workers) | Research finding | lazear2015value | abstract (NBER working paper) |
| 7 | Survey-measured people management skills strongly reduce turnover, with designs supporting causality; no consistent effect on other outcomes (one high-tech firm) | Research finding | hoffman2021people | abstract (NBER working paper) |
| 8 | Boss technical competence is the strongest predictor of worker job satisfaction; rises in competence associated with higher well-being (US and British data) | Research finding | artz2017boss | abstract |
| 9 | Project Oxygen: teams with highly effective managers more likely to have better results, be happier, lower turnover; ten behaviors including technical skills | Industry research (company self-report) | rework-great-managers | full text |
| 10 | Span-of-control evidence for software teams is lacking | Gap | rajan2006flattening not cited; research gap G8 | — |
| 11 | All Northstar figures (managers' time splits, director's role definition) and the Jo example | Illustrative | — | fictional; checked against teams.csv and index.md |

Book's own recommendations in the chapter (labeled as such in the text or clearly the author's
reasoning): the drift toward delivery work; the four split shapes and their team sizes; the
calendar-audit procedure and its anti-gaming counters; the decision table and direct-report
thresholds; the failure-mode catalogue; the playbook.

Gap noted in the chapter: no study found relating how engineering managers split time across the
three jobs to team outcomes, and none of the manager-effect studies is of software teams.

## Chapter 2 — From Individual Contributor to Leader

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Project Oxygen started from the hypothesis that managers did not matter and found teams with highly effective managers had better results and lower turnover | Industry research (one company, correlational) | rework-great-managers; garvin2013google | full text (re:Work page); abstract-level (HBR) |
| 2 | Google's list of effective manager behaviors includes empowering without micromanaging and having key technical skills | Industry research | rework-great-managers | full text |
| 3 | Firms weight current job performance heavily in promotions though other traits better predict managerial performance; promoting lower-potential workers is costly (sales workers, 131 firms) | Research finding | benson2019promotions | abstract |
| 4 | The IC-to-manager transition is a profound psychological adjustment learned mainly from experience; balancing delegation and control is a central challenge; many do not complete it | Research finding (qualitative, 19 managers), at summary level | hill2019becoming | official summary |
| 5 | Professionals adapt to senior roles by observing role models, experimenting with provisional selves, and evaluating them against internal standards and feedback | Research finding (qualitative) | ibarra1999provisional | abstract |
| 6 | Delegation is higher to competent subordinates who share objectives and have longer tenure with the manager; managers are reluctant to delegate important decisions or tasks to inexperienced subordinates | Research finding (survey and interviews) | yukl1999determinants | abstract |
| 7 | Move decisions to the people with information, using stated intent rather than permission requests | Expert opinion | marquet2013turn | idea-level |
| 8 | The first months of a new leadership role are decisive; accelerate learning, match strategy to situation, agree expectations, secure early wins | Expert opinion | watkins2003first | idea-level |
| 9 | Engineering managers should stay technical enough to judge and coach while staying off the critical path | Expert opinion / practitioner consensus | fournier2017manager | idea-level |
| 10 | Five-level scale of control for delegation | This book's recommendation | (synthesis, inspired by marquet2013turn) | n/a |
| 11 | Manager's feedback loop is slower, shared, and filtered; steer by observable leading indicators | This book's recommendation | (reasoning; consistent with hill2019becoming) | n/a |
| 12 | Priya Raman's calendar, review load, and week 2 delegations | Illustrative | Northstar (research/northstar-additions/ch02.md) | invented |

## Chapter 3 — Managerial Leverage and Systems Thinking

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A system is stocks changed by flows, with feedback loops; a stock changes only through its flows and fills and drains at their rate | Practitioner (systems thinking) | meadows2008thinking | idea-level |
| 2 | Twelve places to intervene, ranked by effectiveness from parameters to paradigms; the list is tentative | Expert opinion | meadows1999leverage | full text |
| 3 | Most attention goes to parameters, which rarely change behavior | Expert opinion | meadows1999leverage | full text |
| 4 | Long delays relative to the system's rate of change cause overshoot and oscillation | Expert opinion | meadows1999leverage | full text |
| 5 | Reducing the gain of a reinforcing loop is usually more powerful than strengthening balancing loops | Expert opinion | meadows1999leverage | full text |
| 6 | Adding missing feedback is often a powerful and cheap intervention | Expert opinion | meadows1999leverage | full text |
| 7 | People often find a leverage point and push it in the wrong direction; higher leverage points meet more resistance | Expert opinion | meadows1999leverage | full text |
| 8 | Work harder versus work smarter; improvement has a delay and a worse-before-better profile; the capability trap; managers attribute structural shortfalls to people | Research finding (field studies plus simulation models) | repenning2001nobody | full text |
| 9 | In a nine-month study of a software team, collective time use, interruptions, crisis mentality, and rewards for heroics sustained a time famine; changing time use improved collective productivity | Research finding (one qualitative study) | perlow1999time | abstract |
| 10 | Output is limited by the tightest constraint; improving non-constraints does not raise output; identify, exploit, subordinate, elevate, repeat | Practitioner | goldratt1984goal | idea-level |
| 11 | A manager's output is the output of the organization under their influence | Practitioner | grove1983high | idea-level (Chapter 1 owns) |
| 12 | Multipliers draw out others' capability; diminishers underuse it | Practitioner | wiseman2010multipliers | idea-level |
| 13 | On-call load limit of two incidents per 12-hour shift; eight engineers minimum for a single-site 24/7 rotation | Documented practice | cook2018oncall | full text |
| 14 | Northstar Billing paging figures, attrition and backfill figures, previous management's responses, Ines Carvalho's unscheduled hours | Illustrative | — | fictional; recorded in research/northstar-additions/ch03.md |
| 15 | Billing median restore 495 minutes against 190 organization-wide | Illustrative | — | derived from incidents-last-quarter.csv and baseline |

Book's own recommendations in the chapter (labeled as such or clearly the author's reasoning): the
leverage definition (change in output per manager hour, over the period it persists); visibility as a
separate axis; the recurrence test for reinforcing and balancing loops; the intervention scoring table;
the decision diagram; the engineering mapping of Meadows's levels; the failure-mode catalogue; the
playbook.

## Chapter 4 — The Leadership Ladder: Senior Engineer to CTO

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Scope, time horizon, primary output, and failure mode per role (the ladder table) | This book's recommendation, built on practitioner descriptions | fournier2017manager; larson2021staff; larson2024primer | idea-level (books); synthesis is the book's |
| 2 | A manager's output is the output of the organization under their influence | Practitioner (idea credited) | grove1983high | idea-level; owned by Chapter 1 |
| 3 | Staff work has feedback loops of weeks, months, and years | Expert opinion | larson-staffeng-actually-do | full text |
| 4 | Core staff work: technical direction, mentorship and sponsorship, engineering perspective, exploration, glue; less coding | Expert opinion | larson-staffeng-actually-do | full text |
| 5 | Four staff archetypes (Tech Lead, Architect, Solver, Right Hand); roughly one tech lead per eight engineers; some companies push all experienced engineers to management | Expert opinion | larson-staff-archetypes | full text (claim on the one-per-eight ratio: see merge notes) |
| 6 | Staff reporting lines trade team fit against access to information and authority; people overestimate the help of formal authority | Expert opinion | larson-staffeng-reporting | full text |
| 7 | The engineering executive is defined by responsibility for all of engineering; CTO, VP, Head titles are used inconsistently | Expert opinion | larson2023executive-job | full text (unedited draft chapter) |
| 8 | CEO, peers, and engineering each hold a partial view; the executive solves the company's problem | Expert opinion | larson2023balancing | full text (unedited draft chapter) |
| 9 | People management skills are associated with lower attrition, with designs supporting causality, but do not consistently improve most other outcomes (one firm) | Research finding | hoffman2021people | abstract |
| 10 | Project Oxygen: teams with highly effective managers more likely to have better results, be happier, have lower turnover; ten behaviors | Industry research (company self-report) | rework-great-managers | full text of guide page |
| 11 | Firms weight current performance over predictors of managerial performance in promotions (Peter Principle), at high estimated cost; sales workers | Research finding, applied to engineering by analogy | benson2019promotions | abstract |
| 12 | Management is a change of profession; deliberate switching makes people better at both; tech-lead manager role unstable; best frontline managers rarely more than two to three years from hands-on work | Expert opinion | majors2017pendulum | full text |
| 13 | Manager span of six to eight engineers as a rule of thumb | Practitioner (idea credited) | larson2019elegant | idea-level; team sizing owned by Chapter 33 |
| 14 | Measure managers on unit outcomes, team health, people growth, and leverage over two quarters; activity only as a question | This book's recommendation | synthesis of rows 9, 10 | reasoning shown in chapter |
| 15 | Track-choice criteria and time-boxed trial of six to twelve months with a return path | This book's recommendation | majors2017pendulum (partial) | reasoning shown in chapter |
| 16 | All Northstar role facts, Rafael Duarte (character from Chapter 2), spans and ratios | Illustrative | Northstar canon; research/northstar-additions/ch02.md and ch04.md | invented |

### Merge notes (for the maintainer)

Four sources cited here are defined, with the same ids, in other authors' pending files. Chapter 4
verified them independently on 2026-11-19 and relies on these claims, which should be present in the
merged entries:

- **hoffman2021people** (ch01). Verified via https://api.crossref.org/works/10.1086/711409 and
  https://www.nber.org/papers/w24360 (abstract of NBER w24360, revised April 2020; the page gives the
  JPE citation). ch01's claims already cover what Chapter 4 uses. Add the NBER URL to `verified_via`.
- **rework-great-managers** (ch01). Verified via the same re:Work URL (page dated August 2025; authors
  Sarah Calderon and Debbie Newhouse). Chapter 4 additionally relies on the listed behaviors including
  "Be a good coach", "Empower the team without micromanaging", "Support career development and discuss
  performance", "Have key technical skills", and "Make strong decisions"; add a claim to that effect.
- **larson-staff-archetypes** (ch01). Verified via https://staffeng.com/guides/staff-archetypes/.
  Add the claim: "It describes the Tech Lead as the most common archetype, with roughly one needed for
  every eight engineers" (full text). ch01 records year 2021; the page itself shows only a 2025
  copyright year, so 2021 is the book year.
- **benson2019promotions** (ch02). Resolved 2026-11-19: ch02 corrected its entry to the published QJE
  abstract (131 firms, Crossref URL in `verified_via`, caveat noting the working paper's 214) and added
  the claim on lower weight for sales performance when manager roles carry more responsibility.
  Chapter 4's citation (131 firms) matches. No action needed.

## Chapter 15 — Planning, Prioritization, and Delivery Methods

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | The Agile Manifesto states four value preferences, including responding to change over following a plan, and says the items on the right still have value | Practitioner (statement of values) | beck2001manifesto | full text |
| 2 | Scrum is a lightweight framework built on empiricism, with three accountabilities, a Sprint of one month or less with four events, and three commitments (Product Goal, Sprint Goal, Definition of Done); the guide calls it immutable and partial implementations not Scrum | Official description | schwaber2020scrum | full text |
| 3 | Story points and velocity do not appear in the Scrum Guide | Official description (absence) | schwaber2020scrum | full text read; terms not present |
| 4 | Kanban is a strategy for optimizing flow, with three practices, explicit WIP control without a prescribed number, four flow measures, and no roles or iterations | Official description | vacanti2025kanban | full text |
| 5 | Shape Up uses six-week cycles, appetite instead of estimates, bets at a betting table, and cancels unfinished projects by default (circuit breaker) | Documented practice | singer2019shapeup | official summary (publisher podcast page); book not read, site blocked |
| 6 | A systematic review found 36 empirical agile studies up to 2005 and called for more and better studies | Research finding | dyba2008empirical | abstract |
| 7 | A review of Kanban in software found 19 primary studies by 2013 reporting benefits (lead time, quality, communication, consistency, fewer customer-reported defects) and challenges | Research finding (reported, not causal) | ahmad2013kanban | abstract |
| 8 | Under 15 percent of surveyed practitioners work purely traditional or purely agile; practices affect perceived agility more than methods; no method guarantees or prevents agility | Research finding (survey, perceived) | kuhrmann2022agile | abstract |
| 9 | No research finding shows a named method outperforms others across contexts | Gap statement / book's reading of rows 6-8 | dyba2008empirical; kuhrmann2022agile | abstract-level synthesis |
| 10 | Cost of delay as an idea is widely credited to Reinertsen | Practitioner, attribution unverified | reinertsen2009principles | idea-level; gap G6 |
| 11 | WSJF is SAFe's method: relative cost of delay (business value, time criticality, risk reduction or opportunity enablement) over job size; SAFe credits Reinertsen | Official description | safe-wsjf | full text |
| 12 | Output shipped is not outcome achieved (the build trap) | Practitioner | perri2018escaping | idea-level |
| 13 | Making work visible and reducing batch size | Practitioner | kim2016devops | idea-level |
| 14 | Orders CD3 example, sequence costs, and all Northstar planning facts | Illustrative | — | fictional; arithmetic recomputed in session |

Book's own recommendations (labeled in text or clearly the author's reasoning): choosing the method
by the shape of the work; the "about a third" interrupt threshold; planning proportional to
uncertainty (three-row table); the three-horizon team roadmap and monthly review; fixed-date items
scheduled backward rather than ranked; standardizing the reporting interface rather than the method;
the failure-mode catalogue; the playbook.

## Chapter 16 — Flow: Lead Time, Dependencies, and Unplanned Work

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | L = λW for a stationary queueing system with finite means | Research finding (mathematical theorem) | little1961proof | abstract |
| 2 | Over a finite window (system empty at start and end) the relation holds exactly for the data; in OM it is written WIP = throughput × cycle time; finite-window use is measurement, not forecasting; the law does not resolve trade-offs | Research finding | little2011law | full text (authorized reprint) |
| 3 | Reducing WIP lowers lead time only if throughput holds; throughput usually holds or rises | Practitioner consensus (labeled as such) | — | book's reasoning; stated as an assumption to check |
| 4 | Value stream mapping: map 5–15 blocks with people from the whole stream; record lead time, process time, %C/A; record the process as it really is; partial maps cause local optimization | Industry research / documented practice | dora-cap-work-visibility | full text |
| 5 | DORA research associates WIP limits with better delivery performance, especially with visual displays and monitoring feedback; listed pitfalls | Industry research | dora-cap-wip-limits | full text |
| 6 | Split work into pieces completed in hours to days; more than a week to complete and check is too big | Industry research | dora-cap-small-batches | full text |
| 7 | Small, frequent, automated releases | Practitioner | humble2010continuous | idea-level |
| 8 | Improving a non-constraint does not improve system output | Practitioner | goldratt1984goal | idea-level |
| 9 | Product development queues are invisible and grow with utilization | Expert opinion | reinertsen2009principles | idea-level |
| 10 | M/M/1 waiting time = service time × ρ/(1 − ρ) (4, 9, 19 at 80, 90, 95 percent) | Standard queueing result, presented as a simple model | — | textbook formula, computed in text; no study cited |
| 11 | Four types of work; unplanned work consumes the others | Practitioner | kim2013phoenix | idea-level |
| 12 | Distributed work items took about 2.5× as long; number of people strongly related to calendar time; replicated | Research finding (transfer to cross-team is inference, stated) | herbsleb2003empirical | abstract |
| 13 | Teams designed for fast flow with few deliberate interactions | Practitioner | skelton2019team | idea-level |
| 14 | No verified peer-reviewed benchmark for software flow efficiency | Gap, admitted in text | — | search not successful in session |
| 15 | All Northstar figures: standing-orders map, dependency matrix, unplanned breakdown, quarter 2 decisions on the accounting-system integration and the week 5 re-sample | Illustrative | — | fictional; recomputed (matrix rows/columns 86; unplanned rows match teams.csv; FTE 27.29) |

Book's own recommendations: four-category classification of unplanned work; remove/loosen/coordinate
sequence for recurring dependencies; slack on critical teams; quarterly map and dependency review;
expedite policy; the playbook.

## Chapter 17 — Predictability and Managing Uncertainty

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | The term "planning fallacy" comes from Kahneman and Tversky (1979) | Research (attribution) | jorgensen2004review; buehler1994exploring (caveat cites first author's blog) | full text (review) |
| 2 | People underestimate their own completion times but not others'; they focus on plan-based scenarios, discount past failures as external and transient; linking predictions to past experience removed the bias in the study | Research finding (individuals, mostly students) | buehler1994exploring | abstract |
| 3 | Expert judgment is the most common software estimation method; no substantial evidence that formal models do better; experts sometimes more accurate | Research finding (review) | jorgensen2004review | full text (author preprint) |
| 4 | Expert uncertainty ranges are too narrow; in one study of industrial projects, hit rates of effort intervals were below 50 percent | Research finding, as reported in the review | jorgensen2004review | full text |
| 5 | Bid, planned effort, and most-likely effort serve conflicting goals and are often not separated; pressure to please a manager reduces realism | Research (review, partly from general judgment studies, stated) | jorgensen2004review | full text |
| 6 | Underestimation more common in engineering/management studies than in psychology studies; many studies conflate effort and completion-date predictions | Research finding (review) | halkjelsvik2012origami | abstract |
| 7 | Reference-class forecasting: three steps; outside view; optimism bias versus strategic misrepresentation | Research / method | flyvbjerg2006nobel | full text (arXiv author version) |
| 8 | UK Department for Transport optimism-bias uplifts: road 15 percent at 50 percent accepted overrun risk, 45 percent at 10 percent | Research finding (transport infrastructure) | flyvbjerg2006nobel | full text |
| 9 | Estimates, targets, and commitments are different; executives asking for estimates often want commitments | Expert opinion (practitioner) | mcconnell2006software | official summary (publisher excerpt) |
| 10 | Monte Carlo forecasting from throughput; warning against forecasting from averages | Practitioner (expert opinion) | vacanti2018when | official summary (table of contents) |
| 11 | Walking skeleton named by Cockburn: a thinly connected functioning architecture | Expert opinion | cockburn2004crystal | author's own page; book metadata only |
| 12 | Experiments test business assumptions with the smallest thing that produces evidence | Practitioner | ries2011lean | idea-level |
| 13 | Brooks's law as commonly stated; mechanisms (ramp-up, communication overhead, indivisible tasks) and Brooks's own "oversimplification" | Expert opinion; wording verified only via secondary source (stated in text) | brooks1995mythical | idea-level, secondary source |
| 14 | Economic treatment of product development flow (further reading only) | Practitioner | reinertsen2009principles | idea-level |
| 15 | All Northstar figures: throughput history, Monte Carlo results, renewal dates, four-quarter roadmap record, miss reasons | Illustrative | — | research/northstar-additions/ch17.md; simulation rerun with several seeds; arithmetic recomputed |
| 16 | Two independent 85 percent parts give about 72 percent joint probability | Arithmetic | — | 0.85 x 0.85 = 0.7225 |

Book's own recommendations in the chapter (labeled as such in the text or clearly the author's
reasoning): commit at the 85th or 95th percentile; forecast/target/commitment table with owners;
calibration as the predictability measure; uncertainty-type decision diagram; forecasting-method
table; failure-mode catalogue; the playbook.

## Chapter 18 — Measuring Engineering Productivity: DORA, SPACE, and Their Limits

Written 2026-11-20. Closes research gap G3 (McKinsey article read from a Wayback snapshot of the original
URL) and the naming part of G5 (dimension names read on secondary official or author-affiliated pages;
the SPACE and DevEx full texts remain unread). G7 unchanged.

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Effort, output, outcome, impact chain; most of McKinsey's new measures sit at effort and output; measuring individuals changes behavior; Facebook survey account | Expert opinion | orosz2023measuring | full text |
| 2 | Indicators used for decisions are bent along with the activity they track (Campbell); popular "Goodhart's law" | Expert opinion, widely cited | campbell1979assessing | idea-level; wording not quoted (gap G7) |
| 3 | DORA's current guide: five metrics, throughput and instability groups, definitions; per application or service; goals invite gaming; improvement not competition | Industry research | dora-metrics-guide | full text, page dated 2026-01-05, re-checked 2026-11-20 |
| 4 | DORA's research is an annual survey recruited organically plus a panel; nearly 3,000 respondents in 2023, more than 36,000 overall; factor analysis and Bayesian SEM; confounding discussed | Industry research | dora2023accelerate | full text, methodology pp. 62-72 |
| 5 | Respondents differ each year; shifts may be sampling artifacts; new findings suspect until replicated | Industry research | dora-faq | full text (via summarizing fetcher) |
| 6 | Speed and stability not a trade-off in DORA's data; not evidence of local causal effect | Industry research with stated limits; book's interpretation | dora-metrics-guide; dora2023accelerate; forsgren2018accelerate | full text; idea-level (book) |
| 7 | Productivity cannot be captured by one metric or dimension | Research (practitioner-oriented scholarship) | forsgren2021space | abstract |
| 8 | SPACE dimension names (short and long forms); use at least three dimensions; activity most misused | Practitioner (secondary accounts) | forsgren2023navigating; alwell2021measuring | full text of secondary pages |
| 9 | DevEx combines developer feedback with system data; benefits to business outcomes are the authors' argument | Research (practitioner-oriented scholarship) | noda2023devex | abstract |
| 10 | DevEx dimensions: feedback loops, cognitive load, flow state | Practitioner (vendor page of first author) | dx-devex-report | official summary |
| 11 | McKinsey article's proposed measures, contribution analysis, reported client results without method, its own warnings on commits and deployment frequency | Expert opinion (consultancy) | mckinsey2023productivity | full text, Wayback snapshot 2023-08-20 |
| 12 | Gaming paths and pairs for each metric | This book's recommendation (practitioner consensus on mechanisms) | dora-metrics-guide (goals invite gaming) | reasoning |
| 13 | Refuse individual productivity scoring (five reasons) | This book's recommendation (disputed claim D1) | orosz2023measuring; forsgren2021space; dora-metrics-guide | reasoning on full text and abstract |
| 14 | Minimum reporting group of five for surveys | This book's recommendation | — | reasoning |
| 15 | Northstar figures, per-engineer table, Wilson intervals, the CFO request and the proposed measurement set | Illustrative | — | fictional; derived from teams.csv and recomputed in session |

Book's own recommendations in the chapter: the decision-first framework and its table; the gaming and
pairing table; the failure-mode catalogue; access rules; the playbook; the CTO's three questions.

Disputed claim D1: McKinsey content is now read; the book's position is unchanged and is stated in the
chapter. Suggested update to `disputed-claims.md` (for the maintainer): replace "Not verified" in D1 with
a summary of the article's proposals as recorded in the pending entry, and set Status to resolved for
reading.

## Chapter 5 — One-on-Ones, Coaching, and Mentorship

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Nearly half of employees find their one-on-ones lacking in substance; report participation is the strongest predictor of value; a plan predicts effectiveness; both sides rate meetings highest when the report sets the agenda; managers' self-ratings appear inflated; evidence fits weekly or every-other-week cadence | Expert opinion (researcher's summary of his own survey work; methods not read) | rogelberg2024unlocking | full text of the summary; underlying studies not read |
| 2 | The one-on-one is the subordinate's meeting, with their agenda, and a high-leverage activity | Practitioner | grove1983high | idea-level |
| 3 | One-on-ones are for the person, not the project | Practitioner consensus | fournier2017manager; zhuo2019making | idea-level |
| 4 | Leaders who supply every answer diminish others' thinking | Practitioner | wiseman2010multipliers | idea-level |
| 5 | Coaching in organizations has significant positive effects on five outcome categories, g = 0.43 to 0.74 | Research finding | theeboom2014coaching | abstract |
| 6 | Workplace coaching by internal or external coaches (k = 17) has positive effects; stronger for internal coaches; manager coaching excluded | Research finding | jones2016coaching | abstract (Crossref) |
| 7 | Mentoring is associated with favorable career and other outcomes, with generally small effects, small for objective outcomes | Research finding (correlational) | allen2004mentoring; eby2008mentoring | abstract |
| 8 | Sponsorship differs from mentoring; mostly men described being sponsored; men received 15 percent more promotions at follow-up (MBA graduates) | Industry research | ibarra2010promotions | full text on author's site |
| 9 | No meta-analysis of managerial (line-manager) coaching was read | Gap statement | — | see final report |
| 10 | All Northstar figures, the cadence arithmetic, and the case-study sample | Illustrative | — | fictional, recomputed in session |

Book's own recommendations (labeled in the text): the channel design (report-owned agenda, status
elsewhere, deeper-question rotation, visible follow-through); the decay-signal table and its
thresholds; the four-mode table and decision diagram; the running record format and monthly summary;
the cadence decision table; the enterprise floor, pulse, skip-level rule, and sponsorship map.

## Chapter 6 — Feedback, Conflict, and Difficult Conversations

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Feedback interventions improved performance on average (d = .41, 607 effect sizes, 23,663 observations) but over one third decreased performance | Research finding | kluger1996effects | abstract (author-hosted) |
| 2 | Feedback effectiveness decreases as attention moves from the task toward the self (feedback intervention theory) | Research finding (theory tested by moderator analyses) | kluger1996effects | abstract |
| 3 | Specific, behavioral, early feedback works better than trait-level or delayed feedback | Practitioner consensus, consistent with claim 2 | kluger1996effects; scott2017radical | abstract; idea-level |
| 4 | Caring personally and challenging directly; ruinous empathy as the common failure | Expert opinion | scott2017radical | idea-level (metadata-only) |
| 5 | Business cultures differ in how directly negative feedback is delivered; upgrading and downgrading words | Expert opinion | meyer2014culture | idea-level (metadata-only) |
| 6 | Relationship conflict correlates strongly and negatively with team performance and satisfaction | Research finding | dedreu2003task; dewit2012paradox | abstract |
| 7 | Task conflict correlated negatively with performance in 2003 meta-analysis, especially in complex tasks; not strongly negative in 2012 meta-analysis (116 studies, 8,880 groups) | Research finding, contested | dedreu2003task; dewit2012paradox | abstract |
| 8 | Task conflict is less harmful or more positive when weakly associated with relationship conflict | Research finding (both meta-analyses agree) | dedreu2003task; dewit2012paradox | abstract |
| 9 | Process conflict has a stable negative relationship with group outcomes | Research finding | dewit2012paradox | abstract |
| 10 | Status conflict is distinct, has a negative effect on group performance, moderates task conflict effects, and undermines information sharing | Research finding | bendersky2012status | abstract |
| 11 | Values conflict as a separate category | This book's recommendation (practitioner distinction; not measured in sources read) | none | gap: no verified source read |
| 12 | Unresolved process conflict at a boundary becomes relationship conflict; find the oldest layer | This book's recommendation | none | reasoning |
| 13 | Teams that avoid conflict end in artificial harmony | Expert opinion | lencioni2002five | idea-level (metadata-only) |
| 14 | A difficult conversation has three layers: what happened, feelings, identity; prefer a learning stance | Expert opinion | stone1999difficult | idea-level (metadata-only) |
| 15 | Five-part preparation including a plan for when it goes badly | This book's recommendation | none | synthesis |
| 16 | Team psychological safety associated with learning behavior, which mediated its link to performance | Research finding | edmondson1999psychological | abstract |
| 17 | Feedback delay cost (900-line merge requests, about 40 days of extra waiting over 10 weeks) | Illustrative | none | worked example with stated assumptions |
| 18 | Northstar Billing–Orders conflict is a process conflict that surfaced as status and relationship conflict | Illustrative | Northstar canon; northstar-additions/ch06.md | fictional case |

## Chapter 7 — Hiring and Structured Interviews

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Validity coefficients are correlations with later performance, usually supervisor ratings; meta-analyses correct for range restriction | Research (method description) | sackett2022revisiting; sackett2023revisiting | abstract (2022); full text (2023) |
| 2 | Schmidt and Hunter reported the highest validity for GMA combined with a work sample, integrity test, or structured interview, in the low-to-mid .60s | Research finding, superseded in part | schmidt1998validity | abstract (via OpenAlex inverted index) |
| 3 | Range-restriction corrections overcorrected; most estimates fall by roughly .10 to .20; structured interviews rank first | Research finding | sackett2022revisiting | abstract |
| 4 | Structured interview mean .42, SD .19, 80% credibility interval .18 to .66, ".42, plus or minus .24" | Research finding | sackett2023revisiting | full text (open access) |
| 5 | Biodata .38; cognitive ability .31, about .20 lower, no longer the stand-out predictor; work samples .21 lower, tied with assessment centers (.33) for fourth; unstructured interviews .19 lower | Research finding | sackett2023revisiting | full text; work-sample .33 inferred from two sentences (see caveat) |
| 6 | Top predictors are job-specific; considerable uncertainty remains | Research finding | sackett2023revisiting | full text |
| 7 | 15 components of interview structure, in content and evaluation; interviews can be improved by them | Research finding (review) | campion1997review | abstract |
| 8 | Google's structured interviewing: four components, attributes defined first, behavioral and hypothetical questions, rubrics; hard to maintain | Documented practice | rework-structured-interviewing | full text |
| 9 | Interviewers form confident impressions from random answers; unstructured interviews dilute valid information; people prefer random interviews to none | Research finding (students, GPA prediction) | dana2013belief | full text |
| 10 | Being watched halves performance on a whiteboard problem; higher stress and cognitive load | Research finding (48 students, lab) | behroozi2020stress | abstract |
| 11 | No peer-reviewed validity study found for live coding, take-home, pair-programming, or system-design interviews | Research gap (proposed new gap) | — | search in session; not exhaustive |
| 12 | Social influence reduces diversity of estimates without improving accuracy and raises confidence | Research finding (estimation tasks), applied to debriefs as an extension | lorenz2011social | abstract |
| 13 | Hiring treated as an instrumented funnel/system | Practitioner (idea-level) | larson2019elegant | metadata only |
| 14 | Translation of r = .42 into share of above-median hires (64%; 56% and 73% at the interval edges) | Illustrative computation | — | bivariate normal, 50% selection ratio; arithmetic in chapter |
| 15 | All Northstar facts, loop costs (8.75 h per loop, 47 h per hire, 9.4 engineer-weeks a year) | Illustrative | — | fictional; recomputed |

Book's own recommendations (labeled in the text): the two added
requirements; the debrief protocol and diagram; the attribute-to-method table; the decision-rule
table; the failure-mode catalogue; the playbook; post-hire tracking milestones.

Research gap G10: narrowed, not closed. The 2023 open-access article states the revised
structured-interview figure (.42) in its text; the 2022 paper's own table was not read, and the
2023 article's table (an image) was not read.

## Chapter 8 — Career Development, Promotion, and Compensation

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Career ladders are organizational infrastructure that make expectations explicit; leveling and performance processes are systems to design | Practitioner consensus | fournier2017manager; larson2019elegant | idea-level (metadata only) |
| 2 | Reaching staff level usually takes sponsorship and visible work; staff roles take several archetypes | Expert opinion | larson2021staff; larson-staff-archetypes | idea-level (book); full text (archetypes page) |
| 3 | Idiosyncratic rater effects accounted for over half of rating variance (62 and 53 percent); ratee performance 21 and 25 percent | Research finding, limits stated (developmental ratings of managers) | scullen2000latent | abstract |
| 4 | Women and minorities received less salary growth than white men with equal performance scores in one organization | Research finding | castilla2008gender | abstract |
| 5 | An explicitly meritocratic framing increased reward bias favoring men in three experiments (445 participants) | Research finding (experimental) | castilla2010paradox | abstract |
| 6 | Women received lower "potential" ratings despite higher performance; potential explained about half the gender promotion gap; the ratings were poor forecasts | Research finding (one retail chain) | benson2026potential | abstract |
| 7 | Firms weight current performance heavily in promotion (Peter Principle) | Research finding; cross-reference to Chapter 2 | benson2019promotions | abstract |
| 8 | Introducing accountability and transparency into reward decisions reduced a reward gap in one firm (almost 9,000 employees) | Research finding (one firm) | castilla2015accounting | abstract |
| 9 | Rating-scale design (6 versus 10 points) changed the gender gap in teaching evaluations | Research finding (university setting) | rivera2019scaling | abstract |
| 10 | No verified study shows that calibration meetings as engineering organizations run them improve fairness | Gap stated in text; practice labeled practitioner consensus and book's recommendation | — | search in session found none |
| 11 | EU Directive 2023/970: applicant pay information and pay-history ban (Art. 5), accessible pay criteria (Art. 6), right to information (Art. 7), gap reporting (Art. 9), joint pay assessment at 5 percent (Art. 10) | Standard (legal text; not outcome evidence; national transposition varies) | eu2023paytransparency | full text |
| 12 | US state laws protecting coworker pay discussion were followed by wage declines of about 2 percent | Research finding (one form of transparency, US) | cullen2023equilibrium | abstract |
| 13 | Useful criticism combines caring personally with challenging directly | Expert opinion | scott2017radical | idea-level |
| 14 | All Northstar figures: promotion history, level mix, bands, salaries, quarter-3 cycle | Illustrative | — | fictional; recomputed in session |

Book's own recommendations in the chapter (labeled in the text): the five ladder dimensions; removing
years and tools; the scope-availability check; calibration countermeasures (packets, independent
readers, decision rule, facilitator, budget not quota, outcome review); the five-part "not yet"; the
three grounds for pay decisions and the pay decision diagram; equity review thresholds (0.90 to 1.10,
10 percent peer gaps); separate funding for equity adjustments; publishing bands only after cleanup.

## Chapter 9 — Performance Management and Underperformance

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Performance problems are often reduced to two reasons, capability and motivation | Expert opinion | grove1983high | idea-level (metadata-only) |
| 2 | Diagnose a performance discrepancy before choosing a remedy; if the person could do it when it truly mattered, training is not the remedy | Expert opinion | mager1997analyzing | idea-level (metadata-only) |
| 3 | Most performance deficits come from the environment (information, resources, incentives) rather than the individual | Expert opinion | gilbert1978human | idea-level (metadata-only) |
| 4 | Four causes (system, skill, will, role fit), with confirming and disconfirming evidence | This book's synthesis | grove1983high; mager1997analyzing; gilbert1978human | synthesis |
| 5 | Expectations should be checkable by a third party, with evidence and support named | This book's recommendation | — | reasoning |
| 6 | Individual activity counts are not performance measures | This book's recommendation (owned by Ch 18, D1) | — | cross-reference |
| 7 | Performance management has been reduced to formal administrative steps disconnected from daily expectations and guidance; attention should shift to manager-employee communication | Research (position paper) | pulakos2011broken | abstract |
| 8 | Five properties of an improvement process with a real chance of success | This book's recommendation | pulakos2011broken (supporting) | reasoning |
| 9 | Legal and HR boundaries (consistency, facts, protected circumstances, no pretext); involve HR before a formal plan | This book's recommendation, jurisdiction-neutral | — | reasoning |
| 10 | A negative group member (withholding effort, negative affect, norm violation) triggers inequity perceptions, negative mood, and reduced trust, leading to defensive responses that damage cooperation | Research finding (review and model) | felps2006bad | abstract |
| 11 | Avoiding hard messages out of kindness harms the person and the team | Expert opinion | scott2017radical | idea-level (metadata-only) |
| 12 | Idiosyncratic rater effects accounted for 62% and 53% of rating variance; ratee performance 21% and 25% (developmental ratings of managers, two samples) | Research finding | scullen2000latent | abstract |
| 13 | A single rating is weak evidence; never start or end a process on a rating alone | This book's recommendation | scullen2000latent (extending) | reasoning |
| 14 | Simulated forced distribution with firing noticeably improves workforce potential, mostly in the first several years, depending on percentage fired and voluntary turnover | Research finding (simulation) | scullen2005forced | abstract |
| 15 | Permanent forced ranking is not advisable for engineering; at most a one-time correction | This book's recommendation | scullen2005forced (interpreting) | reasoning; cooperation effects not measured in the source |
| 16 | Bram Verhoeven case, costs and time reconstruction | Illustrative | Northstar (fictional) | invented; see research/northstar-additions/ch09.md |

## Chapter 10 — Motivation, Retention, and Managing Senior Engineers

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A broad meta-analysis of turnover antecedents found moderators of antecedent-turnover relationships | Research finding | griffeth2000meta | abstract; no effect sizes reported |
| 2 | An updated meta-analysis found many antecedent-turnover relationships context-dependent | Research finding | rubenstein2018surveying | abstract |
| 3 | Imported "top reasons" lists are a weak guide; measure your own organization | This book's recommendation | griffeth2000meta; rubenstein2018surveying | inference from rows 1-2 |
| 4 | Voluntary turnover follows several distinct decision paths involving external events | Research (theory) | lee1994unfolding | abstract |
| 5 | Job embeddedness (links, fit, sacrifice) predicts intent to leave and turnover beyond satisfaction, commitment, alternatives, and search | Research finding | mitchell2001why | abstract; non-software samples |
| 6 | Turnover research has turned toward the psychology of staying and collective turnover | Research (review) | hom2017hundred | abstract |
| 7 | Competence, autonomy, and relatedness needs support motivation and well-being; choice raises and imposed goals and deadlines lower intrinsic motivation | Research finding (review by theory's originators) | ryan2000self | full text |
| 8 | Contingent tangible rewards undermine intrinsic motivation | Contested; stated as such | ryan2000self | full text; the paper names the opposing view |
| 9 | Software engineers' motivation varies by characteristics, personality, and career stage | Research finding (systematic review) | beecham2008motivation | abstract (repository report version) |
| 10 | People-management skill strongly and negatively related to attrition at one tech firm | Research finding | hoffman2021people | abstract; cross-reference to Chapter 1 |
| 11 | Developer experience as friction in daily work, measured by pairing feedback with system data | Research (framework), used as Chapter 18 uses it | noda2023devex | abstract, via Chapter 18 |
| 12 | Stay interviews as a structured way to collect embeddedness data | Practitioner consensus; no cited test of effect | none | stated as a gap in the chapter |
| 13 | Split of ownership between expert (judgment), manager (decision rights, constraints, consequences), and joint record | This book's recommendation | marquet2013turn (idea), larson2021staff (idea) | idea-level |
| 14 | Staff archetypes: tech lead, architect, solver, right hand | Practitioner (expert opinion) | larson-staff-archetypes | full text |
| 15 | Leaders differ in how much of others' capability they draw out (multipliers, diminishers) | Expert opinion | wiseman2010multipliers | idea-level |
| 16 | Few studies examine counter-offers; they are discretionary and can be inequitable; women and racially minoritized faculty less likely to receive them | Research finding (one study, faculty) | whitelewis2024counteroffers | abstract |
| 17 | Popular counter-offer attrition statistics are from recruiting firms with undisclosed methods and are not repeated | Research gap | none | search in session found no peer-reviewed source |
| 18 | Counter-offer decision rules (peer equity check, pay fixes only pay, de-risk knowledge) | This book's recommendation | whitelewis2024counteroffers (equity warning) | reasoning |
| 19 | All Northstar exit data, stay interviews, Tomasz Wierzbicki's offer, and cost figures | Illustrative | Northstar canon and research/northstar-additions/ch10.md | invented; assumptions stated |

## Chapter 11 — High Performance: Trust, Psychological Safety, and Accountability

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Psychological safety is people's perception of the consequences of taking interpersonal risks in a context | Research (review definition) | edmondson2014psychological | abstract |
| 2 | Research has linked psychological safety to voice, teamwork, team learning, and organizational learning | Research finding (review) | edmondson2014psychological | abstract |
| 3 | In 51 teams in one manufacturing company, safety was associated with learning behavior, which mediated its association with performance; team efficacy was not associated once safety was controlled | Research finding | edmondson1999psychological | abstract (Crossref) |
| 4 | A meta-analysis pooled 136 samples (over 22,000 individuals, nearly 5,000 groups) and tested safety's relation to task performance beyond related constructs | Research finding (scope only; no effect sizes claimed) | frazier2017psychological | abstract |
| 5 | Project Aristotle studied 180 teams and lists five dynamics in order, psychological safety first and dependability second | Industry research | rework-team-effectiveness | full text (bibliography claims) |
| 6 | Effectiveness in Aristotle combined executive, team-leader and team-member ratings with sales performance; how a team worked together mattered more than who was on it | Industry research | rework-team-effectiveness | full text, page re-read 2026-11-20; not yet in the bibliography entry's claims (maintainer: add or cut) |
| 7 | In 38 Swedish agile teams (217 respondents), safety and norm clarity both predicted self-assessed performance and satisfaction; norm clarity stronger (about 30% and 71%) | Research finding | lenberg2018psychological | full text (arXiv preprint) |
| 8 | In 161 software teams (1,118 participants), safety was directly associated with better teamwork and less conflict | Research finding | verwijs2024double | abstract |
| 9 | Westrum typology by treatment of messengers; DORA states high-trust, information-flow cultures predict delivery and organizational performance; DORA reports its 2019 survey found safety predictive of delivery, organizational performance, productivity | Industry research | dora-cap-generative-culture; forsgren2018accelerate | full text (guide); idea-level (book) |
| 10 | Safety and performance standards are separate dimensions; high performance needs both | Practitioner (expert opinion) | edmondson2018fearless | idea-level (metadata-only) |
| 11 | Dysfunctions pyramid: absence of trust at the base, avoidance of accountability and inattention to results above | Expert opinion | lencioni2002five | idea-level (metadata-only) |
| 12 | Just culture balances safety and accountability; engineers are not "off the hook" | Practitioner | allspaw2012blameless | full text |
| 13 | No controlled study showing that raising safety causes better software delivery outcomes was found | Research gap | — | search in session; see report |
| 14 | Three tests of high performance (outcomes, sustainability, learning); four accountability elements; four team states and the diagnosis path | This book's recommendation | — | synthesis |
| 15 | Northstar comparison of Payments and Integrations and Orders; near-miss log; operations review; 630 recurrence minutes | Illustrative | incidents-last-quarter.csv; research/northstar-additions/ch11.md | computed from canon data plus chapter additions |

## Chapter 12 — Team Charters, Working Agreements, and Knowledge Sharing

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | In 32 MBA student teams in a simulation, high-quality performance strategies predicted performance, and charter quality interacted with strategy quality; teams high on both sustained the highest performance | Research finding | mathieu2009charters | abstract |
| 2 | Google's Project Aristotle lists structure and clarity among five dynamics of effective teams, after psychological safety and dependability | Industry research | rework-team-effectiveness | full text |
| 3 | Leaders should create and repeat clarity about a few basic questions (organizational health) | Expert opinion | lencioni2012advantage | idea-level |
| 4 | Teams should present a deliberate team API and choose interaction modes with neighbors | Expert opinion (practitioner) | skelton2019team | idea-level |
| 5 | Team psychological safety is associated with learning behavior, which mediates its link to performance (51 manufacturing teams) | Research finding | edmondson1999psychological | abstract |
| 6 | Truck factor defined as the minimum number of departures that put a project in serious trouble; about 65 percent of 133 GitHub projects had an estimated truck factor of 2 or less; surveyed developers mostly agreed with the identified main authors | Research finding | avelino2016truck | abstract |
| 7 | Projects are exposed to turnover losses several times the expected loss; simple truck-factor estimates exaggerate potential loss; successors reduce expected loss by up to 15 percent | Research finding | rigby2016turnover | abstract |
| 8 | Code review increased the number of distinct files a developer knew about by 66 to 150 percent, depending on the project | Research finding | rigby2013convergent | abstract |
| 9 | Single points of failure (bus factor) are a main obstacle to learning; written and one-to-one knowledge are complements; doing a task for someone keeps knowledge in one person | Documented practice | chen2020knowledge | full chapter |
| 10 | Documentation treated like code (owners, source control, review, deprecation), written for a named audience, one type per document | Documented practice | manshreck2020documentation | full chapter |
| 11 | Working agreements that work are observable, owned by the team, and checked at a fixed retrospective | This book's recommendation | — | author synthesis |
| 12 | Remove, spread, then write down, in order of durability; the truck factor is a screen, not a measure | This book's recommendation | extends avelino2016truck, rigby2016turnover, rigby2013convergent | reasoning shown in chapter |
| 13 | Billing ledger knowledge map, pairing cost, Data and Analytics charter, and case-study details | Illustrative | — | fictional; recorded in research/northstar-additions/ch12.md; aggregates checked against baseline-data.md and the CSV files |

Book's own recommendations in the chapter: the "named moment of use" test for documents; the
documentation practice table; the single-person-area decision diagram and mechanism table; the
playbook; the knowledge-risk register.

## Chapter 13 — Decision-Making in Teams

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Reversible decisions ("two-way doors") deserve a lightweight process; most decisions can be made with about 70 percent of desired information | Documented practice | bezos2016letter | full text |
| 2 | Disagree and commit, quick correction of bad decisions, and early escalation of misalignment | Documented practice | bezos2016letter | full text |
| 3 | Effective executives make few, fundamental decisions and build action into the decision | Practitioner | drucker1967effective | idea-level |
| 4 | DACI roles: one Driver, one Approver, Contributors with voice but no vote, Informed; record the outcome | Practitioner | atlassian-daci | full text |
| 5 | RAPID roles; Agree assigned sparingly; ideally one decider | Practitioner | bain-rapid | full text |
| 6 | Performance depends on making the right decisions quickly and executing them; clear decision roles as remedy | Practitioner | rogers2006whohasd | official summary |
| 7 | No evidence found that role models (RACI, DACI, RAPID) improve outcomes | This book's assessment | atlassian-daci; bain-rapid | absence noted |
| 8 | Decision records: context, decision, status, consequences; superseded not deleted; rationale prevents blind acceptance or reversal | Practitioner | nygard2011adr | full text |
| 9 | Discussion favors shared and preference-consistent information; groups chose the initial plurality option over the best one | Research finding | stasser1985pooling | abstract |
| 10 | Across 65 studies, groups mention common information more, fail more often when unique information must be pooled; medium has no effect | Research finding | lu2012hiddenprofiles | abstract |
| 11 | Team psychological safety associated with learning behavior | Research finding | edmondson1999psychological | abstract |
| 12 | Abilene paradox: agreement on a course members privately reject | Expert opinion | harvey1974abilene | idea-level |
| 13 | Awareness of biases has done little to improve decisions; executives rely on team proposals; checklist for reviewing a recommendation | Practitioner (authors include researchers) | kahneman2011bigdecision | official summary; checklist idea-level only |
| 14 | Free discussion, clear decision, full support | Practitioner | grove1983high | idea-level |
| 15 | Commitment depends on having been heard | Practitioner | lencioni2002five | idea-level |
| 16 | Moving decisions to the people with the information | Practitioner | marquet2013turn | idea-level |
| 17 | Groupthink as a complete model is weakly supported | Not asserted; gap admitted in text | none | review literature verified only at metadata level (Esser 1998) |
| 18 | Four-part decision model, method selector, decision framework table, record fields | This book's recommendation | none | synthesis |
| 19 | Decision log example (36 decisions) and core/permissions change counts | Illustrative | Northstar additions ch13 | invented |

Research gap: abstracts for Esser (1998), Turner and Pratkanis (1998), and Baron (2005) on groupthink were
not available from legitimate open sources (OpenAlex records have no abstract; ScienceDirect returned 403),
so the chapter does not cite the groupthink critique literature.

## Chapter 14 — Distributed Teams, Team Health, and Diagnosing Dysfunction

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Distributed work items took about 2.5 times as long as similar colocated ones; the number of people involved was strongly related to calendar time; replicated at a second organization | Research finding | herbsleb2003empirical | abstract |
| 2 | Firm-wide remote work at one large technology company made collaboration networks more static and siloed with fewer bridges; synchronous communication fell and asynchronous rose | Research finding, one firm, pandemic conditions | yang2022remote | abstract |
| 3 | During pandemic work from home at one IT services firm, hours rose while output did not; coordination time rose while uninterrupted work, coaching, and supervisor one-on-ones fell | Research finding, one firm, pandemic conditions; no percentage printed | gibbs2023wfh | abstract of the IZA working paper; published version metadata only |
| 4 | In a randomized trial (1,612 employees, two home days a week) quits fell by about a third with no effect on performance grades, promotions, or engineers' lines of code; managers' expectations moved from negative to slightly positive | Research finding, one firm | bloom2024hybrid | abstract (Europe PMC record) |
| 5 | Proximity to teammates increased coding feedback, most for newer and younger engineers; experienced engineers wrote less code | Research finding, one firm, working paper | emanuel2023proximity | abstract (NBER page) |
| 6 | No study shows one working arrangement is best for software teams; hybrid with anchor days is a low-risk default; full distance needs deliberate compensations; juniors gain most from time together (book's position on D5) | This book's recommendation | rows 1-5 | synthesis |
| 7 | National cultures differ in norms for negative feedback, disagreement, and decisions, and misreading them damages trust | Expert opinion | meyer2014culture | idea-level |
| 8 | The Team Diagnostic Survey assesses how well a team is structured, supported, and led, plus processes and members' reactions; psychometrics supported on 321 teams | Research finding (instrument validation) | wageman2005team | abstract (Crossref) |
| 9 | The squad health check is a facilitated self-assessment of about ten indicators in traffic-light colors with a trend; works only in high trust; teams should not be compared; support tool, not judgment tool | Documented practice | kniberg2014squad | full text |
| 10 | Survey scores became distorted once tied to reviews and manager pressure | Practitioner (opinion piece with an anecdote) | orosz2023measuring | full text |
| 11 | Dysfunctions stack from absent trust to inattention to results; the visible symptom sits on top of a lower cause | Expert opinion (business fable) | lencioni2002five | idea-level |
| 12 | Developer productivity cannot be captured by one metric (background for not reducing health to a score; referenced via Chapter 18, not cited directly) | Industry/scholarly | forsgren2021space | abstract; not cited in chapter 14 |
| 13 | Channel-by-channel compensations, health-check rules, the four-layer diagnosis order, the remedy decision diagram, the four-hour overlap heuristic | This book's recommendation | — | reasoning, drawing on rows 1-11 |
| 14 | All Northstar figures: locations, travel cost model ($3,000 per trip, $114,000 a year), departure cost (~$76,000), Customer Experience health check results | Illustrative | — | fictional; recomputed in session; locations recorded in research/northstar-additions/ch14.md |

Book's own recommendations in the chapter (labeled in the text): the D5 position, the compensation
table, the six health-check rules, the layer order (structure, leadership, relationships, individuals),
the decision table for arrangements, and the playbook.

## Chapter 28 — Architecture Decision-Making and Governance

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Architectures erode and become costly to change partly because design decisions stay implicit; treat an architecture as a set of explicit decisions | Expert opinion (research position paper) | jansen2005architecture | abstract |
| 2 | An architectural decision is a justified design choice addressing an architecturally significant requirement; an ADR records one decision and its rationale; the collection is the decision log | Practitioner | adr-github-io | full text |
| 3 | Formal authority (right to decide) differs from real authority (effective control); real authority follows information; more real authority for the informed party raises initiative and costs the superior control; overload and urgency raise subordinates' real authority | Research finding (formal economic model) | aghion1997formal | abstract |
| 4 | Setting technical direction is core staff engineer work with long feedback loops; the architect is one of four staff archetypes; people overestimate how much formal authority helps them | Expert opinion | larson-staffeng-actually-do; larson-staff-archetypes; larson-staffeng-reporting | full text |
| 5 | ADRs: short numbered records with context, decision, status, consequences, kept in the repository, superseded not deleted | Practitioner | nygard2011adr | full text |
| 6 | Lightweight ADRs were in Thoughtworks' Adopt ring Nov 2017 to May 2018; records belong in source control rather than a wiki | Practitioner consensus | thoughtworks-radar-lightweight-adr | full text |
| 7 | ADR adoption in open source is low but growing; about half of repositories with ADRs hold one to five records; systematic use is a team activity over time; Nygard's template is most used | Research finding (open source only, no outcome measure) | buchgeher2023adr | abstract |
| 8 | Design docs: informal, before coding, centered on trade-offs and alternatives; staged review from comments to formal meetings; formal review can slow development; skip when the solution is obvious | Documented practice | ubl2020designdocs; manshreck2020documentation | full text |
| 9 | Fitness functions: automated, continuous checks of architectural characteristics, buildable from existing tests, metrics, monitors | Practitioner | ford2017building; thoughtworks-radar-fitness-function | idea-level (book); full text (Radar) |
| 10 | Systems mirror the communication structures of the organizations that design them | Practitioner (argued essay) | conway1968committees | full text |
| 11 | Board-as-queue arithmetic and the illustrative 120-engineer organization | Illustrative | — (arithmetic; queue logic cross-referenced to Chapter 20) | recomputed: 90/13 = 6.9/week; (6.9 − 4) × 13 ≈ 38; 38/4 = 9.5 weeks; 30/4 = 7.5; 10/52 ≈ 19% |
| 12 | All Northstar facts in the case study, including ADR-0001 options and estimates | Illustrative | — | fictional; see research/northstar-additions/ch28.md; 5 ≤ 6 reserved engineer-weeks; 16 − 6 = 10 |

Book's own recommendations in the chapter (labeled in the text): the reversal test for "architectural";
the decision-rights table and its conditions (the D7 position); the five practices that keep a decision
log alive; feedback review over approval gates; the three architecture-specific board failures and their
signals; pairing ADRs with fitness functions owned by the decider; the routing and decision framework
tables; the playbook.

### Proposed new text for disputed claim D7 (for `research/disputed-claims.md`)

**Positions.** Managers own decisions because they own outcomes and staffing; staff-plus engineers own
technical direction; teams decide within guardrails. Practitioner sources differ by company shape.

**Book's position (Chapter 28).** Split the right by what the decision is mainly about, and give each
decision one named decider. Teams decide design inside their own components. Cross-team interfaces and
data contracts are decided by a technical leader with a written mandate for the domain (or the
providing team's technical lead), after written consultation of consumers; affected managers hold an
agreement right limited to capacity and dates. Organization-wide direction is decided by a small forum
of technical leaders with one named signer, the director or CTO agreeing on cost and risk. Trade-offs
of date, money, or risk appetite go to the director or CTO. Conditions: a technical leader holds the
right only with a written mandate, time to do the work, and accountability for consequences (review
trigger, involvement when the decision fails); otherwise the manager decides by default and says so; in
small organizations one person may wear both hats; disagreements between technical leaders escalate to
the owner of the trade-off; executive overrules are recorded as superseding decisions. **Evidence:**
the formal/real authority model of Aghion and Tirole (`aghion1997formal`, abstract level) and
practitioner sources (`larson-staffeng-actually-do`, `larson-staff-archetypes`,
`larson-staffeng-reporting`); no empirical study comparing these arrangements in software
organizations was found. **Owner:** Chapter 28.

## Chapter 29 — Staff and Principal Engineers

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | No peer-reviewed study of staff or principal engineer roles and their outcomes was found | Research gap, stated in text | — | search in session |
| 2 | Shared leadership is positively related to team effectiveness, more for attitudes, processes, and emergent states than performance, and more for complex work | Research finding (correlational, not software-specific) | wang2014shared | abstract |
| 3 | In agile software teams leadership is shared dynamically and is a property of the team rather than a role | Research finding (qualitative, 13 interviews) | gren2022agile | abstract |
| 4 | About 65 percent of 133 open-source projects had an estimated truck factor of two or fewer | Research finding (open source) | avelino2016truck | abstract |
| 5 | Four staff archetypes (tech lead, architect, solver, right hand); companies emphasize one or two; right hand mainly in very large organizations | Expert opinion | larson-staff-archetypes | full text |
| 6 | Staff work: direction, mentorship and sponsorship, engineering perspective, exploration, glue; coding reduced; feedback loops of weeks to years | Expert opinion | larson-staffeng-actually-do | full text |
| 7 | Reporting line should follow the archetype; people overestimate formal authority | Expert opinion | larson-staffeng-reporting | full text |
| 8 | Staff authority is borrowed from the organization through the sponsor; never surprise the manager; feed context | Expert opinion | larson-staffeng-authority | full text |
| 9 | Snacking, preening, chasing ghosts; existential issues first, growth, finishing, work only you can do | Expert opinion | larson-staffeng-what-matters | full text |
| 10 | Staff work in three pillars (big picture, execution, leveling up); staff engineer as force multiplier | Expert opinion | reilly2022staff | official summary (author's book page) |
| 11 | Glue work is technical leadership that often goes unrewarded at promotion; managers should track and share it | Expert opinion | reilly-being-glue | full text |
| 12 | Leaders who multiply versus diminish others' intelligence | Practitioner | wiseman2010multipliers | idea-level |
| 13 | Task conflict lacks a stable negative link to performance; relationship and process conflict are negative | Research finding | dewit2012paradox | abstract |
| 14 | Status conflict harms group performance, mainly by undermining information sharing | Research finding | bendersky2012status | abstract |
| 15 | Over a third of feedback interventions decreased performance; effectiveness falls as attention moves to the self | Research finding (meta-analysis, pre-1996 studies) | kluger1996effects | abstract |
| 16 | Directives and pressured evaluation undermine motivation; choice and acknowledgment support it | Research finding (review by the theory's originators) | ryan2000self | full text |
| 17 | Staff engineer as bet on owned decisions; five-part scope; disagreement rule with one written appeal; measure pairs; principal and distinguished level table | This book's recommendation | larson2021staff (context) | synthesis |
| 18 | All Northstar figures (time sample, design reviews, cost of unscheduled hours, draft scopes, coaching plan) | Illustrative | — | fictional, recomputed in session |

Book's own recommendations in the chapter: the mental model and loop diagram; the five-part scope and
five tests; the disagreement flow; the measure-pair table; the principal and distinguished table; the
failure-mode detection signals; the playbook.

## Chapter 30 — Technical Strategy, Technology Selection, and Build versus Buy

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Strategy has a kernel of diagnosis, guiding policy, and coherent action; goals and fluff are signs of bad strategy | Expert opinion | rumelt2011good | idea-level (metadata only) |
| 2 | Coherent actions are the most important part; policies should be applicable, enforced, and create leverage; written strategies often describe an ideal rather than diagnose today | Expert opinion | larson2023engstrategy | full text |
| 3 | Policies answer resource allocation, rules for all teams, and how decisions are made; actions sort into enforcements, escalations, transitions | Expert opinion | larson2023engstrategy | full text |
| 4 | Staff-plus engineers can build strategy by extracting what several design documents share; review impact about two months after publishing | Expert opinion | larson2023engstrategy | full text |
| 5 | Build what differentiates and can be staffed; buy or adopt commodity capabilities; compare on three-year TCO including exit | This book's recommendation | (synthesis) | reasoning shown in chapter |
| 6 | Vendor lock-in risk grows with cloud migration; interoperability, portability, standards, and contract terms mitigate it | Research finding (survey, n=114) | opara-martins2016lockin | abstract |
| 7 | 81.5 percent of 4,600+ GitHub projects kept outdated dependencies; developers rarely responded to advisories; 69 percent of those surveyed were unaware of vulnerable dependencies | Research finding (open source) | kula2018developers | abstract |
| 8 | Vulnerability reach in a dependency network was studied across nearly 400 npm security reports over six years | Research finding (no quantitative result claimed) | decan2018impact | abstract |
| 9 | Scorecard automates open-source health and security checks (maintenance, security policy, code review, pinned dependencies) | Official documentation | openssf-scorecard | full text |
| 10 | Innovation tokens; boring means well-understood failure modes; additions carry long-term operational cost; commit to migrating off what is replaced | Expert opinion | mckinley2015boring | full text |
| 11 | A radar uses Adopt, Trial, Assess, and Caution rings, is published twice yearly, and organizations are encouraged to build their own | Practitioner (publisher's description) | thoughtworks-radar-faq | full text |
| 12 | Architecture is about trade-offs among quality characteristics | Expert opinion | richards2020fundamentals | idea-level (metadata only) |
| 13 | Well-Architected has six pillars and frames reviews as conversations, not audits | Standard (vendor guidance) | aws-well-architected | full text |
| 14 | Java LTS end-of-availability dates are published as minimums by at least one distribution | Official documentation | adoptium-support | full text |
| 15 | About 65 percent of 133 popular GitHub projects had an estimated truck factor of two or less | Research finding (open source) | avelino2016truck | abstract |
| 16 | A technology risk register for EOL, concentration, and skills risk, with owner, horizon, response, review date | This book's recommendation | (synthesis) | reasoning shown in chapter |
| 17 | Northstar strategy draft, risk register, and tax-svc options and costs | Illustrative | Northstar canon plus research/northstar-additions/ch30.md | invented |

Gaps: no peer-reviewed evidence was found on the outcomes of build-versus-buy decisions in software
organizations. Li et al. (ICSE 2006, "An empirical study on decision making in off-the-shelf
component-based development", DOI 10.1145/1134285.1134446) was located and its bibliographic data
confirmed via Crossref, but no abstract could be read from a legitimate source (ACM returned 403), so it
is not cited. No research evidence was found that technology radars or risk registers improve outcomes;
the chapter labels them as recommendation and practitioner practice.

## Chapter 31 — Service Boundaries: Microservices, Modular Monoliths, and Ownership

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Module effectiveness depends on the decomposition criteria; modules should hide design decisions likely to change | Research (design argument), idea-level for information hiding | parnas1972criteria | abstract; information-hiding criterion credited at idea level |
| 2 | The microservice style: independently deployable services around business capabilities, with decentralized data, design for failure, products not projects | Practitioner | lewis2014microservices | full text |
| 3 | Maintainability and scalability are the main migration drivers; finding the service cut is a major challenge; most companies rewrote rather than split | Research finding (qualitative, 14 systems, 10 companies) | fritzsch2019migration | abstract |
| 4 | Practitioners rank maintainability and scalability highest; slow ROI judged worth reduced long-run maintenance | Research finding (survey of migrators) | taibi2017processes | abstract |
| 5 | In one company, measured technical debt spiked when services were built, then grew more slowly than in the monolith | Research finding (single case, one tool) | lenarduzzi2020migrating | abstract |
| 6 | Mature microservice teams often cut services by resource consumption rather than business capability and credit early shared infrastructure | Research finding (21 interviews, 37 survey respondents) | wang2021promises | abstract |
| 7 | Almost all successful microservice stories began as monoliths; boundaries are hard to find up front; evidence sparse | Expert opinion | fowler2015monolithfirst | full text |
| 8 | Prime Video moved one monitoring service from serverless components to a single process; scaling limit at about 5% of expected load; infrastructure cost down by over 90%; "case by case" | Documented practice (self-reported, one service) | kolny2023primevideo | full text from Wayback capture of 2023-03-23 |
| 9 | Release history reveals logical coupling between modules and points to restructuring opportunities | Research finding (one industrial system) | gall1998logical | abstract |
| 10 | Mined version histories reveal coupling undetectable by program analysis; top-3 suggestions correct >70% on eight OSS projects | Research finding | zimmermann2005mining | abstract |
| 11 | Organizations design systems that copy their communication structures | Practitioner (argued essay); evidence owned by Ch 33 | conway1968committees | full text |
| 12 | Size software responsibilities to what one team can hold in mind | Practitioner | skelton2019team | idea-level (metadata only) |
| 13 | No controlled cross-organization comparison of the styles was found; choose by change patterns, team structure, and operational capability | This book's recommendation | — | synthesis of rows 2–10 |
| 14 | Ownership model: one owning team per component, open contribution, interim owner with deadline | This book's recommendation | lewis2014microservices (products not projects) | synthesis |
| 15 | All Northstar co-change figures, the module table, document-store callers, Ines Carvalho's proposal, the $18,500 service-cost example | Illustrative | — | fictional, recomputed twice |

### Proposed updated text for D3 (research/disputed-claims.md)

> ## D3. Microservices or a modular monolith?
>
> **Positions.** The case for microservices as independently deployable services organized around
> business capabilities, with decentralized data and team ownership (`lewis2014microservices`); the
> case for starting with a monolith and extracting services when boundaries are understood
> (`fowler2015monolithfirst`, expert opinion with stated caveats); and accounts of teams folding
> distributed components back into one process, of which the best known is Prime Video's
> audio/video monitoring service (`kolny2023primevideo`, now **verified** from a Wayback Machine
> capture of the original post: one service, serverless components replaced by a single process,
> self-reported infrastructure cost reduction of over 90 percent, and an explicit "case by case"
> conclusion; it is not evidence that Amazon or Prime Video abandoned microservices).
>
> **Evidence.** No controlled comparison of the two styles across organizations was found. Studies of
> migrations are qualitative or survey-based and sample organizations that chose to migrate:
> maintainability and scalability are the main motives and the service cut the main challenge
> (`fritzsch2019migration`, `taibi2017processes`); one case shows technical debt growing more slowly
> after extraction (`lenarduzzi2020migrating`); mature teams credit shared infrastructure built early
> (`wang2021promises`). Change history carries real coupling signal for drawing boundaries
> (`gall1998logical`, `zimmermann2005mining`). The mirroring hypothesis is covered in Chapter 33.
>
> **Book's position (taken in Chapter 31).** The decision follows from change patterns, team
> ownership, runtime needs, and operational capability, not from fashion. Separate the module,
> deployment, data, and ownership boundaries and choose the weakest one that solves the problem.
> Where the platform cannot yet give every service a pipeline, monitoring, and on-call, an
> organization under about 100 engineers is usually better served by a well-modularized monolith
> with a few services extracted for clear reasons. This is this book's recommendation, not a
> research finding.

### Proposed update for G11 (research/research-gaps.md)

G11 can be closed: the Prime Video post was read in full from a Wayback Machine capture
(20230323220106) of the original URL; `kolny2023primevideo` is replaced in
`research/pending-sources/ch31.yaml` with access_level full-text and an `archive_url`.

### Gaps recorded

- Soldani et al. 2018 (systematic grey literature review, JSS) was located but its abstract states no
  findings; not cited.
- Bogner et al. on evolvability assurance of microservices was not found on arXiv in this session;
  not cited.
- No study found that measures outcomes of ownership models (single-owner versus shared) for software
  components; the ownership model is this book's recommendation.

## Chapter 32 — Platform Engineering, Developer Experience, and Legacy Modernization

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A platform is a foundation of self-service capabilities arranged as a compelling internal product; it cannot succeed on mandate alone | Expert opinion | bottcher2018platforms | full text |
| 2 | Platforms should be built and evolved like products with users involved early, not adopted by top-down mandate; a platform can be very thin | Practitioner consensus | cncf-platforms-whitepaper | full text (web version) |
| 3 | A platform team exists to reduce delivery teams' cognitive load; the thinnest viable platform | Practitioner | skelton2019team | idea-level |
| 4 | Platform users report 8% higher individual productivity, 10% higher team performance, 6% higher organizational performance, but 8% lower throughput and 14% lower change stability | Industry research | dora2024accelerate | full text of platform chapter, pp. 49, 53–54 |
| 5 | Developer independence associated with about 5% higher productivity; exclusive mandated platform use associated with 6% lower throughput; not collecting feedback negative | Industry research | dora2024accelerate | full text, pp. 51, 53 |
| 6 | Platform pitfalls: no user research, rigid standards, ticket-ops, big-bang launch, golden cage; clear task feedback most associated with positive user experience (2025 data) | Industry research | dora-cap-platform-engineering | full text of capability page (summary of report data) |
| 7 | DevEx frames developer experience as friction in daily work measured by combining feedback and system data; dimensions feedback loops, cognitive load, flow | Research (practitioner-oriented); vendor summary for dimension names | noda2023devex; dx-devex-report | abstract; official summary |
| 8 | Platform measures fall into satisfaction, organizational efficiency, and delivery outcomes | Practitioner consensus | cncf-platforms-whitepaper | full text |
| 9 | Strangler fig: incremental replacement, earlier value, lower risk, learning; requires transitional architecture; seams rare | Expert opinion | fowler2024stranglerfig | full text |
| 10 | Rewriting a large product from scratch discards embedded fixes and stalls the product | Expert opinion, anecdotal | spolsky2000never | full text |
| 11 | Practitioners value legacy systems highly; modernization challenges are business and organizational as well as technical | Research finding | khadka2014legacy | abstract |
| 12 | Many monoliths are too entangled to split cleanly | Expert opinion | fowler2015monolithfirst | full text |
| 13 | Fitness functions guard architectural properties automatically | Practitioner | ford2017building | idea-level |
| 14 | No controlled or large-sample evidence compares rewrite and incremental modernization outcomes | Research gap, admitted in text | — | search in session found none verifiable |
| 15 | All Northstar figures, the roadmap, capacity arithmetic, and adoption measures | Illustrative | — | fictional; recomputed in session |

Book's own recommendations in the chapter: mandate outcomes, not tools; the feedback-loop selection
rule (latency and frequency first, cognitive load second, ticket-bound capabilities discounted);
pairing adoption measures with outcomes and denominators; the modernization decision table and its
rule that every step has a removal date and a success measure; the failure-mode catalogue; the
playbook.

## Chapter 33 — Conway's Law, Team Topologies, and Cognitive Load

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Organizations that design systems are constrained to produce designs copying their communication structures | Expert opinion | conway1968committees | full text (essay; no empirical data) |
| 2 | Conway also argued that organizing a design team already makes design decisions, that organizations must stay flexible as the design changes, and that communication paths grow roughly with the square of headcount | Expert opinion | conway1968committees | full text, read 2026-11-19 (beyond the bibliography entry's recorded claim; maintainer may add these claims) |
| 3 | In matched pairs of same-function products, those built by loosely coupled open source communities were significantly more modular than those from tightly coupled commercial firms | Research finding | maccormack2012mirroring | abstract (working-paper version); no magnitude cited |
| 4 | Across 142 studies, mirroring is prevalent but not universal; partial mirroring likely better in dynamic industries; firms can break the mirror; open collaborative projects did not support the hypothesis; mirroring conserves cognitive resources | Research finding (review) | colfer2016mirroring | abstract |
| 5 | When coordination matches coordination needs from technical dependencies, modification requests resolve significantly faster; logical dependencies matter more than call or data dependencies | Research finding | cataldo2008congruence | abstract |
| 6 | Distributed work items took about 2.5 times as long; more people involved meant longer calendar time | Research finding (applied to team boundaries as inference) | herbsleb2003empirical | abstract |
| 7 | The reverse Conway maneuver is promoted by Team Topologies; its effect on existing systems is not established by the evidence read | Practitioner (idea level); evidence gap is this book's reading | skelton2019team; maccormack2012mirroring | idea-level; abstract |
| 8 | Four team types and three interaction modes as defined by the authors | Practitioner consensus | teamtopologies-key-concepts; skelton2019team | official summary; idea-level |
| 9 | No peer-reviewed validation of the team-type taxonomy found | Research gap | none | search in this session |
| 10 | Conventional problem solving consumes processing capacity otherwise available for schema acquisition | Research finding (individual learners) | sweller1988cognitive | abstract |
| 11 | Team cognitive load (intrinsic, extraneous, germane) is a transfer from learning research to teams; no validated team instrument found | Practitioner idea; transfer labelled; research gap | skelton2019team; teamtopologies-key-concepts; sweller1988cognitive | idea-level; official summary; abstract |
| 12 | Cognitive load is one dimension of developer experience | Practitioner | dx-devex-report | official summary |
| 13 | Adding people adds communication and ramp-up overhead | Expert opinion | brooks1995mythical | idea-level (secondary summary) |
| 14 | Dunbar-style group-size thresholds are not used for software teams | This book's recommendation | none | Dunbar not read; software team-size study (Rodríguez et al., JSS 2012) abstract unavailable |
| 15 | Teams of about five to nine; separate team from reporting group | This book's recommendation | none | reasoning from rows 2, 6, 13 |
| 16 | Match the move to the kind of load (platform, facilitation, move or split) | This book's recommendation | skelton2019team (vocabulary) | synthesis |
| 17 | All Northstar figures, knowledge counts, and capacity arithmetic | Illustrative | Northstar canon; research/northstar-additions/ch33.md | fictional |

## Chapter 34 — Spans, Layers, and Dependency Mapping

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Graicunas counted manager–subordinate relationships, which grow far faster than headcount, and suggested a maximum of about four or five | History (practitioner) | graicunas1937relationship | idea-level, secondary pages; presented as history only |
| 2 | Large US firms flattened: wider CEO spans, fewer levels between division heads and CEO, authority delegated downward | Research finding | rajan2006flattening | abstract |
| 3 | Average span in Gallup's US panel rose from 10.9 to 12.1 (2024–2025), median about six | Industry research | harter2026span | full text |
| 4 | Manager talent matters more than span; less talented managers lose engagement as team size and hands-on workload rise | Industry research | harter2026span | full text |
| 5 | More reports associated with lower engagement for remote and hybrid managers, minimal effect on-site | Industry research | harter2026span | full text |
| 6 | Managers' median individual-contributor time is 40 percent; above that, engagement lower and worse with team size | Industry research | harter2026span | full text |
| 7 | Managers should support six to eight engineers; managers of managers four to six managers | Expert opinion | larson2018sizing | full text |
| 8 | No software-specific outcome study of span found (gap G8) | Research gap | — | search in this session |
| 9 | Span set from five factors; default eight to ten, range five to twelve | This book's recommendation | (consistent with Ch 1, Ch 4) | reasoning |
| 10 | Organizational structures distort information reaching decision makers; control loss compounds across levels | Theoretical model | williamson1967hierarchical | abstract (opening); control-loss idea via secondary sources |
| 11 | Latency per hop and 80 percent information retention per level | Illustrative | — | stated assumptions |
| 12 | Systems copy organizations' communication structures | Practitioner (essay) | conway1968committees | full text |
| 13 | Organizational and system boundaries moderate whether design interfaces are matched by team interactions | Research finding | sosa2004misalignment | abstract |
| 14 | Congruence between coordination needs and actual coordination reduces modification-request resolution time | Research finding | cataldo2008congruence | abstract (canonical entry: ch33 pending) |
| 15 | Organizational complexity metrics predicted failure-prone Windows Vista binaries better than code metrics | Research finding | nagappan2008organizational | abstract-level claims (canonical entry: ch35 pending, full text) |
| 16 | Cross-site work items took about 2.5 times as long | Research finding | herbsleb2003empirical | abstract (via Ch 16) |
| 17 | Teams designed for fast flow with few deliberate interactions | Practitioner | skelton2019team | idea-level |
| 18 | Recount the dependency matrix on every proposed boundary | This book's recommendation | — | reasoning |
| 19 | All Northstar numbers, link classification, quarter 2 analysis, and the assessment of the Chapter 35 year-2 proposal | Illustrative | Northstar canon; northstar-additions/ch34.md; northstar-additions/ch35.md | — |

## Chapter 35 — Designing Organizations of 20, 50, 100, and 500 Engineers

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | n people have n(n−1)/2 possible communication paths; adding people to a late project is widely stated to make it later, and Brooks called the law an oversimplification | Expert opinion (classic); formula is arithmetic | brooks1995mythical; nagappan2008organizational | idea-level / official-summary (secondary); formula as stated in the Nagappan full text |
| 2 | Organizational measures of ownership diffusion predicted failure-prone binaries in Windows Vista (precision 0.87, recall 0.84 over 50 splits), better than churn, complexity, coverage, dependency, or pre-release defect models | Research finding | nagappan2008organizational | full text; one system, authors disclaim generalization |
| 3 | Number of people involved strongly related to calendar time to complete a work item | Research finding | herbsleb2003empirical | abstract; distributed setting, application to team boundaries is an inference |
| 4 | Coordination congruent with coordination needs reduced modification-request resolution time | Research finding | cataldo2008congruence | abstract (OpenAlex record) |
| 5 | Systems mirror the communication structure of the organizations that design them | Expert opinion (classic essay) | conway1968committees | full text |
| 6 | No validated optimal team size, span, or layer threshold exists for software organizations | This book's assessment; gap G8 | rajan2006flattening (context only) | literature gap |
| 7 | What breaks at about 20, 50, 100, and 500 engineers and which structures answer it | Practitioner consensus / this book's recommendation | larson2019elegant; fournier2017manager; skelton2019team | idea-level |
| 8 | The management job changes at each level (engineers, managers, organization) | Practitioner | fournier2017manager | idea-level |
| 9 | Organization design treated as an engineering problem with explicit sizing rules, planned ahead, changed rarely | Practitioner | larson2019elegant | idea-level |
| 10 | GitLab documents a target range for direct reports, the same at every level to avoid a layer, sized for six months ahead; and a dual career path forking above Senior | Documented practice | gitlab2026structure | full text |
| 11 | Platform teams provide internal services used by self-service, run as a product | Practitioner | skelton2019team | idea-level |
| 12 | Four staff archetypes; the right hand appears mainly in very large organizations | Expert opinion | larson-staff-archetypes | full text |
| 13 | Staff-plus reporting line trade-off; formal authority is overestimated | Expert opinion | larson-staffeng-reporting | full text |
| 14 | Large US firms flattened, with wider CEO spans and authority delegated downward | Research finding (context) | rajan2006flattening | abstract; corporate hierarchies only |
| 15 | A 12-team, 175-person programme used many coordination arenas that changed over time; extra roles and arenas reduced team autonomy | Research finding (single case) | dingsoyr2018exploring | full text |
| 16 | Structure is a core responsibility of the engineering executive | Practitioner | larson2024primer | idea-level |
| 17 | Sequencing order: platform team and staff mandate before a management layer; check process first | This book's recommendation | — | reasoning in chapter |
| 18 | Fernwick, Brackenridge Freight, Halvard Systems, and the Northstar year 2 proposal | Illustrative | — | fictional |

## Chapter 36 — Reorganizations, Organizational Evolution, and Succession

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A systematic review of 39 longitudinal studies (2000–2012) found restructuring, with and without staff reductions, mainly harmed employee well-being, short and long term | Research finding, limits stated (mergers and downsizing; well-being not delivery) | dejong2016restructuring (pending-sources/ch36.yaml) | abstract |
| 2 | Intervening variables include job control, communication, information, training, procedural justice, job insecurity, change acceptance | Research finding | dejong2016restructuring | abstract |
| 3 | A review of 79 quantitative studies groups antecedents of reactions to change into prechange factors and change process, perceived benefit or harm, and content | Research finding (review structure only) | oreg2011recipients | abstract |
| 4 | In one large software project, proximity to organizational change was associated with more customer-reported defects; recent departures likewise | Research finding, one project, observational | mockus2010volatility | abstract |
| 5 | Consulting-firm surveys on reorganization failure rates are not used | Gap statement | — | research gap G12 |
| 6 | Reorganizations are expensive and should be reserved for structural problems | Expert opinion | larson2019elegant | idea-level |
| 7 | Leaders should agree on a few answers and repeat them far more than feels necessary | Expert opinion | lencioni2012advantage | idea-level |
| 8 | A new role needs a transition plan: diagnose, early wins, relationships | Expert opinion | watkins2003first | idea-level |
| 9 | Succession research has mostly treated succession as an event; practice treats it as a process | Research finding (review) | berns2017succession | abstract |
| 10 | Knowledge concentration and the truck factor (cited as a pointer to Chapter 12, which owns the topic) | Research finding, open source | avelino2016truck (existing entry) | abstract |
| 11 | In Chrome and a project at Avaya, designated successors reduced expected loss from turnover by up to 15 percent; extending this to management roles is labeled as the book's inference | Research finding, two projects | rigby2016turnover (existing entry) | abstract |
| 12 | Transition-cost model (ramp-up, handoff, management, risk), ramp-up figures, payback arithmetic | This book's recommendation; figures illustrative | — | no research gives engineer ramp-up after a team change |
| 13 | All Northstar facts, the reorganization transition plan, and the succession table | Illustrative | — | fictional; additions in northstar-additions/ch36.md |

Book's own recommendations in the chapter (labeled as such in the text or clearly the author's
reasoning): the three tests for reorganizing; consult on problem, decide names privately; tell each
person before any group; effective within two weeks and handoffs by week six; tier 1 change freeze
during ownership moves; the readiness gates; the four succession readiness levels and the coverage
rule; the quarterly evolution cadence.

## Chapter 37 — The Management Operating System: Cadences and Leadership Meetings

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | At one large company people spent about 300,000 hours a year supporting a weekly executive committee meeting | Expert opinion (consultant, one company) | mankins2014weekly | full text of a short post; method not read |
| 2 | Meetings as the medium of managerial work; process-oriented versus mission-oriented meetings | Practitioner | grove1983high | idea-level (metadata only) |
| 3 | Different leadership meeting types for different horizons; the leadership team as first team; cascading decisions | Practitioner | lencioni2012advantage | idea-level (metadata only) |
| 4 | Time is the executive's scarcest resource; record it before managing it; many meetings signal malorganization | Practitioner | drucker1967effective | idea-level (metadata only) |
| 5 | Meeting time demands relate to well-being depending on interdependence, meeting quality, and accomplishment striving; perceived effectiveness strongly related to attitudes and well-being | Research finding | rogelberg2006not | abstract |
| 6 | Relevance, voice, and time management in manager-led meetings associated with engagement | Research finding (self-report, correlational) | allen2013manager | abstract |
| 7 | Functional meeting interaction associated with satisfaction, productivity, and later organizational success; dysfunctional communication's negative effects stronger | Research finding | kauffeld2012meetings | abstract |
| 8 | Meeting science organized before, during, and after meetings | Research review | mroz2018meetings | abstract |
| 9 | Executives average nearly 23 hours a week in meetings, up from under 10 in the 1960s | Expert opinion | perlow2017stop | official summary (opening only) |
| 10 | Interruptions and collective time use; changing time use improved a software team's productivity | Research finding (one team, qualitative) | perlow1999time | abstract |
| 11 | Remote work in the pandemic raised meeting and coordination time and reduced uninterrupted time | Research finding (one firm) | gibbs2023wfh | abstract (working paper) |
| 12 | Groups discuss shared information more than unique information and decide worse when unique information must be pooled | Research finding (laboratory) | lu2012hiddenprofiles; stasser1985pooling | abstract; transfer to engineering decisions is an inference |
| 13 | Seven meeting jobs; one meeting, one job; four-step audit with a topic-by-forum matrix; horizon table; five design choices for a deciding leadership meeting; 12–16 recurring hours for a director | This book's recommendation | — | reasoning |
| 14 | No study found that compares cadence frequencies or forum counts for leadership teams (research gap) | Research gap | — | searches in this session |
| 15 | All Northstar calendar figures, topic matrix, quarter 3 proposal, and manager hour estimates | Illustrative | Northstar canon; northstar-additions/ch37.md | — |

### Gaps recorded

- Leach, Rogelberg, Warr, and Burnfield (2009), "Perceived meeting effectiveness: The role of design
  characteristics", Journal of Business and Psychology 24(1): no abstract available through OpenAlex,
  Crossref, or Semantic Scholar, and the publisher page required login. Not cited; it would support
  claims about agendas, punctuality, and design features.
- Mankins, Brahm, and Caimi, "Your Scarcest Resource", HBR May 2014: hbr.org returned 404 for the URL
  tried; only the shorter Bain-hosted post was read.
- No research located on the effect of cadence design (weekly versus fortnightly, number of forums) for
  engineering or other leadership teams. Proposed for `research/research-gaps.md`.

## Chapter 38 — Scorecards, Quarterly Planning, and Capacity Allocation

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Developer productivity cannot be captured by a single metric or dimension; used to justify a multi-area organization scorecard | Research finding (argument paper) | forsgren2021space | abstract |
| 2 | Pairing indicators so that pushing one shows in the other; a manager's output is the output of the organization they influence | Practitioner | grove1983high | idea-level |
| 3 | Setting DORA metrics as goals makes gaming more likely; aim is improvement over time, not team comparison | Industry research | dora-metrics-guide | full text, page dated 2026-01-05 |
| 4 | OKRs as a format of a qualitative objective with measurable key results, popularized by Doerr and credited to Grove's practice at Intel | Practitioner consensus | doerr2018measure | idea-level |
| 5 | Goal-setting reviews summarize research on the effectiveness of specific, difficult goals, mediators, moderators, and limits | Research finding | locke2002building; locke2006new | abstract |
| 6 | Critics argue goal-setting benefits are overstated and list side effects (narrow focus, risk distortion, unethical behavior, inhibited learning, culture, intrinsic motivation) | Research (argument), disputed | ordonez2009goals | abstract |
| 7 | Goal-setting researchers reply that the critique is anecdotal and that the pitfalls were already published | Research (rejoinder), disputed | locke2009goal | abstract |
| 8 | In one case study of two teams, OKRs aided knowledge sharing, goal alignment, and inter-team insight; writing key results needed support | Research finding (qualitative, one project) | stray2022okrs | abstract |
| 9 | No controlled study of OKRs' effect on software delivery found | Research gap | — | search in session |
| 10 | Planning sequence, unfunded list, four-question allocation test, triggers, row owner versus data steward | This book's recommendation | — | synthesis |
| 11 | All Northstar quarter 3 figures, the capacity cases, prevention split, scorecard proposal, and case requests | Illustrative | — | fictional; recomputed twice (see research/northstar-additions/ch38.md) |

## Chapter 39 — Reviews, Decision Logs, Escalation, and Executive Reporting

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A manager's output is the output of the organization they lead or influence; reviews inspect that output and its machinery | Practitioner | grove1983high | idea-level |
| 2 | Evidence of a failing course of action in the lower ranks often fails to travel up the hierarchy or is distorted, so decision makers do not know the true status (the mum effect) | Research finding (theory) | smith2003reluctance | abstract |
| 3 | The impact of project failure and observed wrongdoing explain part of the reluctance to report negative project news | Research finding (experiment) | smith2001keeping | abstract |
| 4 | Fault responsibility and time urgency change willingness to report bad news; stressing a narrow correction window may help | Research finding (laboratory experiment) | park2008mum | abstract |
| 5 | In records of 56 experienced software project managers, status reports were biased 60 percent of the time | Research finding (researchers' practitioner summary) | keil2014pitfalls | full-text |
| 6 | Aggressive auditing can backfire into distrust and more misreporting; powerful sponsors reduce candor; reported bad news is sometimes ignored, especially without an official channel; corroborate with several people close to the work | Research finding (researchers' practitioner summary) | keil2014pitfalls | full-text |
| 7 | How messengers are treated distinguishes cultures that pass information well | Industry research | dora-cap-generative-culture | full-text |
| 8 | Decision records keep rationale so successors neither accept nor reverse decisions blindly | Practitioner | nygard2011adr | full-text |
| 9 | A decision is unfinished until action and follow-up are built into it | Practitioner | drucker1967effective | idea-level |
| 10 | Escalate fundamental misalignment early rather than letting debate run until the side with more stamina wins | Documented practice (one company) | bezos2016letter | full-text |
| 11 | Formal authority (right to decide) differs from real authority, which depends on who holds the information | Research finding (formal model) | aghion1997formal | abstract |
| 12 | Main point first, supporting ideas grouped beneath it | Practitioner | minto2002pyramid | idea-level |
| 13 | Narrative six-page memos read silently in place of slides; a great memo can take a week or more | Documented practice (one company) | bezos2017letter | full-text |
| 14 | The engineering executive solves the company's problem rather than advocating for one function | Practitioner (expert opinion) | larson2023balancing | full-text |
| 15 | Practitioner guide to the engineering executive's role | Practitioner | larson2024primer | idea-level |
| 16 | Review rules (data first, presenter names problems, every item ends in a decision), decision log fields, joint escalation with a clock, report structure and color definitions | This book's recommendation | — | synthesis of rows 1–14 |
| 17 | Review system costs about 0.5 percent of organization time at Northstar's size | Illustrative | — | stated assumptions |

## Chapter 40 — The Director's Job: Leading 50 to 150 Engineers

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A manager's output is the output of the organization under their influence; prefer high-leverage work | Practitioner | grove1983high | idea-level |
| 2 | Moving to managing managers means working through other managers | Practitioner | fournier2017manager | idea-level |
| 3 | Engineering management as the design of systems | Practitioner | larson2019elegant | idea-level |
| 4 | Organizational structures distort information reaching decision makers, more so in larger organizations; "control loss" compounds by level | Theoretical model, stated as such | williamson1967hierarchical | abstract; control loss official-summary |
| 5 | In 40 interviews, most employees had withheld a concern from a supervisor; fear of being labeled negatively was the most frequent reason | Research finding (exploratory, small sample) | milliken2003silence | abstract |
| 6 | Research on middle managers' role in strategy spans about 25 years and is diverse in constructs | Research finding (review) | wooldridge2008middle | abstract |
| 7 | 259 middle managers in 25 organizations; Prospector firms' middle managers reported more upward and divergent strategic involvement | Research finding | floyd1992middle | abstract |
| 8 | Boundary-spanning middle managers reported more strategic influence; performance associated with more uniform downward and more varied upward influence | Research finding (correlational) | floyd1997middle | abstract |
| 9 | Interruption, crisis mentality, and rewards for heroics perpetuated a software team's time famine; changing time use raised collective productivity | Research finding (one team, qualitative) | perlow1999time | abstract |
| 10 | Managerial work is brief, fragmented, and mostly conversation, unlike the planning folklore | Expert view, idea-level | mintzberg1990job | idea-level |
| 11 | A documented skip-level practice: written template, purposes, feedback shared with the manager by default, confidential meeting on request | Documented practice | gitlab-skip-level | full text |
| 12 | New leaders should learn deliberately with a plan | Practitioner | watkins2003first | idea-level |
| 13 | The executive's job is to merge the CEO's, peers', and engineering's views into the company's problem | Expert opinion | larson2023balancing | full text |
| 14 | Signal-source table, discrepancy diagram, firsthand-share threshold of about a tenth, calendar cuts by source and horizon, skip-level rule | This book's recommendation | — | reasoning |
| 15 | Skip-level cost table; 0.7 per hop loss example; all Northstar shares, samples, and the quarter 3 proposal | Illustrative | — | arithmetic recomputed in session |

Gaps: Athanassiades (1973) on upward distortion and Roberts and O'Reilly (1974) on upward communication
failures were identified but only truncated abstracts were reachable (AOM returned 403); not cited. No
study found on skip-level meetings' effects or on directors' time allocation and outcomes in software
organizations (extends G22).

## Chapter 41 — Managing and Developing Engineering Managers

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A manager's output is the output of the organization under their influence | Practitioner | grove1983high | idea-level |
| 2 | Idiosyncratic rater effects explained 62 and 53 percent of variance in multi-rater ratings of managers, more than twice the ratee-performance effect | Research finding | scullen2000latent | abstract |
| 3 | Improvement after multisource feedback is generally small (24 longitudinal studies); more likely when change is seen as needed and feasible, goals are set, and action taken | Research finding (meta-analysis plus theoretical review) | smither2005multisource | abstract |
| 4 | People management skills strongly and negatively related to attrition at one firm; not consistently to other outcomes | Research finding | hoffman2021people | abstract |
| 5 | Project Oxygen: teams with highly effective managers had better results and lower turnover | Industry research (company self-report) | rework-great-managers | full text |
| 6 | Managers value delegation for development but withhold important decisions from people seen as inexperienced | Research finding | yukl1999determinants | abstract |
| 7 | Moving decisions to the people with information; leaders who amplify or diminish others | Expert opinion | marquet2013turn; wiseman2010multipliers | idea-level (metadata only) |
| 8 | Leadership training (335 samples) improves reactions, learning, transfer, and results (.63, .73, .82, .72); needs analysis, feedback, practice, spacing, on-site, face-to-face moderate it | Research finding | lacerenza2017leadership | abstract |
| 9 | Systematic study of leader development is fairly young; review emphasizes multisource feedback and longitudinal studies | Research finding (review framing) | day2014advances | abstract |
| 10 | New managers learn the transition mainly from experience; many do not make it | Research finding (qualitative, publisher summary) | hill2019becoming | official summary |
| 11 | Management path level by level; manager's job as purpose, people, process | Practitioner | fournier2017manager; zhuo2019making | idea-level (metadata only) |
| 12 | Firms weight current performance in promotions though other traits predict managerial success | Research finding | benson2019promotions | abstract |
| 13 | Sponsorship differs from mentoring; high-potential women over-mentored and under-sponsored | Industry research | ibarra2010promotions | full text |
| 14 | Six-dimension rubric, four ratings, evidence rule, unset-expectation rule, no composite | This book's recommendation | builds on ch4 | reasoning |
| 15 | Skip-level design, staff-review slot, decision flow for Not yet, bench principles, playbook | This book's recommendation | — | reasoning |
| 16 | Director time model, attrition arithmetic, all Northstar ratings, Priya's quarter 2 hours, quarter 3 plans | Illustrative | — | fictional, recomputed in session |

## Chapter 42 — Cross-Functional Dependencies, Portfolio Management, and Influence Without Authority

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Average work in progress equals throughput times time in system; exact for measured data over a window starting and ending empty; descriptive, not a trade-off rule | Research finding (theorem) | little2011law | full text |
| 2 | Predicting the effect of a lower portfolio limit additionally assumes throughput holds | This book's recommendation | little2011law | full text (caveat) |
| 3 | Sequencing work through a shared specialist delivers value earlier than parallel work | Illustrative | none | arithmetic |
| 4 | DORA associates WIP limits with better delivery performance; failure modes include limits too high and limits raised when idle | Industry research | dora-cap-wip-limits | full text |
| 5 | Multiple team membership negatively associated with unit performance, more so with complex tasks (health care) | Research finding, applied by extension | crawford2019link | abstract |
| 6 | Development queues go unmanaged because they are invisible | Expert opinion | reinertsen2009principles | idea-level |
| 7 | First estimate of a portfolio limit: throughput times acceptable lead time | This book's recommendation | none | reasoning |
| 8 | Number of people involved is strongly related to a work item's calendar time | Research finding (distributed development) | herbsleb2003empirical | abstract |
| 9 | Congruence between coordination patterns and coordination needs shortens modification-request resolution | Research finding | cataldo2008congruence | abstract |
| 10 | Put cross-functional coordination in named intakes and policies rather than escalation | This book's recommendation | inference from rows 8-9 | reasoning |
| 11 | Product teams should be given problems rather than stakeholder feature lists | Expert opinion | cagan2020empowered | idea-level |
| 12 | Principled negotiation: interests over positions; best alternative to agreement | Practitioner (expert opinion) | fisher1981getting | idea-level |
| 13 | Influence among peers as exchange of things the other values | Practitioner (expert opinion) | cohen1990influence | idea-level |
| 14 | Rational persuasion, inspirational appeal, consultation most effective; pressure, coalition, legitimating least; exchange moderately effective with peers, not superiors | Research finding | yukl1992consequences | abstract |
| 15 | Rationality and ingratiation positively related to work outcomes; other tactics situational | Research finding (meta-analysis) | higgins2003influence | abstract |
| 16 | Escalate fundamental misalignment early; disagree and commit | Documented practice | bezos2016letter | full text |
| 17 | Baseline: 9 of 17 committed items cross-team, 1 delivered; lead time 11/24/41 days by dependency count | Illustrative (Northstar canon) | baseline-data | canon |
| 18 | Northstar quarter 3 portfolio, limit, and week 31 request | Illustrative | Chapter 38 draft; northstar-additions/ch42.md | addition |

## Chapter 43 — Leading Organizational Change and Director Failure Patterns

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Kotter's account draws on observing more than 100 companies attempting transformation | Expert opinion | kotter1995leading | official summary (article opening) |
| 2 | Kotter's article is known for a sequence of errors: too little urgency, no guiding coalition, no planned short-term wins, declaring victory too soon, not anchoring the change | Expert opinion | kotter1995leading | idea-level; body of article not read |
| 3 | The "70 percent of change programs fail" figure has no valid and reliable empirical evidence in the five published sources reviewed; a single failure rate is hard to define | Research finding (about the evidence) | hughes2011seventy | abstract |
| 4 | Reactions to change have antecedents before the change and in the change itself (process, perceived benefit or harm, content); how a change is run is a lever separate from what it is | Research finding (review), narrowed | oreg2011recipients | abstract |
| 5 | The hard part of transformation is people, culture, and organization rather than technology | Expert opinion | kane2019technology | idea-level |
| 6 | Strategy starts with a diagnosis, then a guiding policy and coherent actions | Expert opinion | rumelt2011good | idea-level |
| 7 | A cohesive leadership team creates, repeats, and reinforces clarity | Expert opinion | lencioni2012advantage | idea-level |
| 8 | Large problems become tractable as a series of small wins | Expert opinion (essay) | weick1984small | idea-level |
| 9 | Early wins build a new leader's credibility | Expert opinion | watkins2003first | idea-level |
| 10 | Escalation of commitment: committing more to a failing course one chose oneself | Research finding, idea-level credit only | staw1976knee | metadata; no finding reported |
| 11 | In two studies, apology repaired trust better after competence violations and denial after integrity violations; apology worked better when guilt was later shown, denial when innocence was | Research finding | kim2004removing | abstract |
| 12 | Most failed director initiatives are competence failures, so owning them is the fitting repair; explaining them away is a denial | This book's recommendation (inference from claim 11) | kim2004removing | inference stated as such in the chapter |
| 13 | Director failure patterns table (eight patterns) | This book's recommendation | synthesis of claims 1–11 and earlier chapters | no single source |
| 14 | Change-load arithmetic per manager (110-engineer example) | Illustrative | none | worked example with stated assumptions |
| 15 | Northstar Excellence Day and the director's self-assessment | Illustrative | Northstar canon plus research/northstar-additions/ch43.md | fictional |

## Chapter 44 — Working with Product: Discovery and Outcome-Based Roadmaps

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A product idea must survive four risks (value, usability, feasibility, business viability), worked by product, design, and engineering together | Expert opinion | cagan2008inspired | idea-level (metadata-only) |
| 2 | Empowered product teams are given problems to solve; feature teams are given features to ship | Expert opinion | cagan2020empowered | idea-level (metadata-only) |
| 3 | The build trap: measuring output shipped instead of value created | Practitioner consensus (with 2) | perri2018escaping; cagan2020empowered | idea-level (metadata-only) |
| 4 | Build the smallest thing that yields evidence (build-measure-learn) | Expert opinion | ries2011lean | idea-level (metadata-only) |
| 5 | In one large market-driven company, four factors (scale, temporal aspects, common views, decision structures) affected requirements communication; gaps led to unmet customer expectations, quality issues, and wasted effort | Research finding (nine interviews, one company) | bjarnason2011requirements | abstract |
| 6 | Controlled experiments are the best design for establishing causal links between changes and user behavior; the authors' experience is that teams learn more and earn better returns listening to customers than to the highest-paid person's opinion | Documented practice, peer-reviewed | kohavi2009controlled | abstract |
| 7 | At Bing, many ideas moved key metrics by about 1 percent and were not well estimated in advance; experimentation identified negative features not deployed despite stakeholders' excitement | Documented practice, peer-reviewed | kohavi2013online | abstract |
| 8 | A continuous experimentation model, checked in two startups, requires instrumented minimum viable features, managed experiment plans, and linking results to the product roadmap | Research finding (two startups) | fagerholm2017right | abstract (via GI journal-first record) |
| 9 | Randomized experiments transfer poorly to small business-to-business products; weaker evidence types should be named | This book's recommendation | (reasoning from 6 and 7 and Northstar's customer count) | n/a |
| 10 | Working contract clauses, discovery staffing as a capacity line, date classification by origin, five-step conversion | This book's recommendation | builds on 1 to 4 | n/a |
| 11 | Northstar baseline: 7 of 17 items delivered; 5 of 17 dated before sizing; 27 of 212 defects "requirement misunderstood" | Illustrative (canon) | baseline-data.md | canon |
| 12 | Ordering-area quarter-4 numbers, sample findings, contract draft | Illustrative (new) | research/northstar-additions/ch44.md | invented, arithmetic checked |

## Chapter 45 — Business Models, Engineering Economics, and Investment Decisions

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | A business model describes how a firm delivers value, persuades customers to pay, and converts payments to profit; it embodies management's hypothesis about customers | Research (conceptual scholarship) | teece2010business | abstract |
| 2 | Strategy as choices of where to play and how to win, used as a filter on investments | Expert opinion | lafley2013playing | idea-level |
| 3 | Four benefit types (increase revenue, protect revenue, reduce costs, avoid costs) used to triage requirements | Practitioner (case report) | arnold2013blackswan | full text (author-hosted web version) |
| 4 | Cost of delay defined as the value a feature could generate over a period if available now, including information value and decay | Practitioner | arnold2013blackswan | full text |
| 5 | Urgency profiles (long life peak unaffected / affected, short life, external deadline) | Practitioner | arnold2013blackswan | full text; profile table wording is this book's |
| 6 | Maersk Line: about $100M portfolio; one feature about $210,000 a week; 38 weeks in queues cost nearly $8M; outcomes confounded with other practices, no control group | Practitioner case report, caveats stated | arnold2013blackswan | full text; outcome figures deliberately not reported (internal inconsistencies) |
| 7 | CD3 ranking and WSJF as a relative-scoring version | Practitioner / official documentation | safe-wsjf; arnold2013blackswan | full text; Chapter 15 owns the ranking |
| 8 | Cost of delay is widely credited to Reinertsen; origin not established by any source read | Gap G6, partly addressed | reinertsen2009principles; safe-wsjf; arnold2013blackswan | metadata only (book); full text (SAFe, Arnold and Yüce) |
| 9 | Opportunity cost is the value of the next best alternative; sunk costs should be ignored | Standard textbook definition | greenlaw2022economics | full text (section 2.1) |
| 10 | Payback definition and four weaknesses; NPV definition, decision rule, cost of capital as rate, sensitivity profile | Standard textbook definition | dahlquist2022finance | full text (sections 16.1, 16.2) |
| 11 | Irreversibility and the option value of waiting for better information | Research (economics), summary level | dixit1994investment | official summary |
| 12 | Real-options techniques applied to software modularity give results consistent with Parnas's conclusions | Research finding (single worked example) | sullivan2001modularity | abstract |
| 13 | Financial numbers rest on estimates and judgment; know which assumptions carry the result | Practitioner | berman2006financial | idea-level |
| 14 | A dollar of avoided credits is worth more than a dollar of new revenue (margin reasoning) | This book's recommendation | — | reasoning from gross margin definition |
| 15 | Three practitioner rules for real options (buy information, stage, value flexibility only if exercised) | This book's recommendation | — | synthesis of rows 11–12 |
| 16 | Two guards: no sole authorship of decisive numbers; post-decision estimate review | This book's recommendation | — | — |
| 17 | All Northstar figures, investments A–C, the week 34 note | Illustrative | — | canon plus additions in research/northstar-additions/ch45.md; recomputed twice |

### Research gap G6 update (proposed for research-gaps.md)

Searched on 2026-11-19. Arnold and Yüce (2013), read in full in the authors' own web version, cite
Reinertsen (2009) on the importance of measuring cost of delay and Smith and Reinertsen's *Developing
Products in Half the Time* (first published 1991 per Open Library) for related ideas, and describe CD3
as a form of WSJF; they do not establish who coined cost of delay. Black Swan Farming's cost-of-delay
page quotes Reinertsen without attributing the origin. Reinertsen's own site (reinertsenassociates.com)
still failed TLS. Status: origin still unverified from a primary source; "widely credited to
Reinertsen" remains the correct wording. Next step: Smith and Reinertsen (1991) or Reinertsen (2009)
read directly, or a scholarly history of the term.

## Chapter 46 — Stakeholder Management and Negotiation

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | The power-interest grid sorts stakeholders into players, subjects, context setters, and crowd, with suggested handling for each | Expert opinion (scholarly method paper) | eden2021modelling | full text (figure credited by the authors to their 1998 and 2011 work) |
| 2 | Stakeholder positions can be issue-related; low-power stakeholders can become powerful through coalitions | Expert opinion | eden2021modelling | full text |
| 3 | Record negative-avoidance goals; about a third of goals first proposed turn out to be strategies | Expert opinion | eden2021modelling | full text (authors' experience, not a measured rate) |
| 4 | Stakeholders respond to each other's responses; presumptions about them are informed guesses | Expert opinion | eden2021modelling | full text |
| 5 | Stakeholder analysis aims at proposals that are technically feasible and politically acceptable, and at building a coalition to adopt them | Expert opinion (review) | bryson2004what | abstract |
| 6 | Prosocial negotiators were less contentious, solved more problems, and reached higher joint outcomes only when resistance to yielding was high or unknown | Research finding | dedreu2000influence | abstract; lab and student samples, moderators noted |
| 7 | First offers advantage the mover and predict settlements; focusing on the opponent's alternatives, reservation price, or one's own target removes the advantage | Research finding | galinsky2001first | abstract; single-issue distributive negotiations |
| 8 | Principled negotiation and the best alternative to a negotiated agreement | Practitioner | fisher1981getting | idea-level |
| 9 | An error budget is a shared, objective measure that lets product and reliability engineers decide risk without political argument | Documented practice | google2017embracing | full text |
| 10 | Directness with personal care; hard conversations touch feelings and identity | Practitioner | scott2017radical; stone1999difficult | idea-level |
| 11 | A manager's time is the scarcest input and belongs on high-leverage work | Practitioner | grove1983high | idea-level |
| 12 | New leaders should negotiate expectations explicitly with their own boss | Practitioner | watkins2003first | idea-level |
| 13 | The five-part no; floor versus tradeable quality; the two floor tests; never negotiate a forecast | This book's recommendation | none | reasoning in chapter |
| 14 | Payroll-export example and the Northstar case arithmetic (Poisson probabilities 0.587, 0.242, 0.070; 0.587⁴ ≈ 0.119; annual P(≤39 given mean 36) ≈ 0.726) | Illustrative | none | computed; Poisson is a stated simplification |

## Chapter 47 — The VP of Engineering: Managing Directors and the Portfolio

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | The engineering executive is defined by responsibility for all of engineering; CTO, VP, and Head of Engineering titles are used inconsistently | Expert opinion | larson2023executive-job | full text |
| 2 | The executive role is a distinct job with its own guide | Expert opinion | larson2024primer | idea-level |
| 3 | Managers of managers support four to six managers (rough ceiling on directors per VP) | Practitioner opinion | larson2018sizing | full text |
| 4 | Organizational outcomes are partially predicted by top managers' background characteristics; executives' experiences, values, and personalities shape interpretations and choices | Research finding (theory, propositions) | hambrick1984upper, hambrick2007upper | abstract |
| 5 | Specific, difficult goals are effective; goals also narrow focus and cause neglect of non-goal areas | Research finding (review); disputed side effects | locke2006new, ordonez2009goals | abstract |
| 6 | Peers as a leader's "first team"; peers' incentives often conflict; set explicit expectations; test first impressions, then make personnel changes quickly | Expert opinion | larson2023gelling, lencioni2002five | full text; Lencioni idea-level |
| 7 | 56 software project managers' status reports biased 60 percent of the time; seek corroboration; aggressive auditing backfires; trust associated with reporting problems | Research finding (researchers' summary) | keil2014pitfalls | full text |
| 8 | Formal versus real authority; superior's overload raises subordinates' real authority | Theoretical model | aghion1997formal | abstract |
| 9 | A disengaged executive does more damage than a somewhat over-involved one | Expert opinion | larson2023micromanage | full text |
| 10 | Executive planning in three parts; allocate coarsely to area leaders and infrequently, partly to avoid zero-sum competition; rewarded private headcount escalation makes the plan a fiction | Expert opinion | larson2023planning | full text |
| 11 | Firms' internal capital allocations tend toward equality over business units (partition dependence); persists in experiments with experienced managers | Research finding (capital budgets; extension to engineering capacity is this book's) | bardolet2011capital | abstract |
| 12 | Escalation of commitment to one's own failing course | Research finding, idea-level | staw1976knee | idea-level |
| 13 | The executive merges CEO, peers', and engineering views as a company-first problem solver | Expert opinion | larson2023balancing | full text |
| 14 | Role-by-decision table, company-shape table, two-kind goals, operating-review loop, rank-before-map allocation, VP decision table, failure modes, playbook | This book's recommendation | — | reasoning |
| 15 | Halvard Commerce allocation example and all Northstar quarter 4 facts | Illustrative | — | arithmetic recomputed in session |

Gaps: no study found of VP-of-Engineering roles, of engineering leadership team composition and
outcomes, or of capacity allocation across engineering directors; the chapter relies on general
management research (upper echelons, capital allocation) and practitioner writing. The Engineering
Executive's Primer itself was not read (metadata only); its draft chapters on lethain.com were read.

## Chapter 48 — Capacity Strategy, Workforce Planning, and Enterprise Governance

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Headcount planning and organization design are core engineering-executive work done with finance | Expert opinion | larson2024primer | idea-level |
| 2 | Managers should read the numbers finance uses (fully loaded cost, budgets) | Practitioner | berman2006financial | idea-level |
| 3 | New people consume the time of those who teach them; added people help late and cost early | Expert opinion | brooks1995mythical | idea-level (secondary source for the law) |
| 4 | Recent departures associated with higher probability of customer-reported defects in one large project | Research finding | mockus2010volatility | abstract |
| 5 | Turnover-induced knowledge loss can exceed three times the expected loss; successors reduce expected loss up to 15 percent | Research finding | rigby2016turnover | abstract |
| 6 | People management skills strongly negatively related to turnover at one firm | Research finding | hoffman2021people | abstract |
| 7 | Proximity to teammates increased coding feedback, most for newer and younger engineers; experienced engineers wrote less code | Research finding | emanuel2023proximity | abstract (working paper) |
| 8 | Distributed work items took about 2.5 times as long as colocated ones; people involved strongly related to completion time | Research finding | herbsleb2003empirical | abstract |
| 9 | Not enough evidence that offshoring reduced costs | Research finding (review) | smite2015cost (pending) | abstract |
| 10 | Follow-the-sun review: 36 practices, 17 challenges; handovers and allocation make it hard to adopt | Research finding (review) | kroll2013followthesun (pending) | abstract |
| 11 | Requirement keywords should be used sparingly, only where required for interoperation or to limit harm | Standard (analogy) | bradner1997rfc2119 | full text |
| 12 | Heavyweight change approval hurts delivery performance with no evidence of lower change failure rates | Industry research | dora-cap-change-approval | full text |
| 13 | Platforms should not rely on top-down mandates for adoption | Practitioner consensus | cncf-platforms-whitepaper | full text |
| 14 | Exclusive mandated platform use associated with 6 percent lower throughput | Industry research | dora2024accelerate | full text (pp. 47–55) |
| 15 | Formal structures adopted for legitimacy decouple from work | Expert opinion (theory) | meyer1977institutionalized | abstract |
| 16 | Control loss compounds across hierarchical levels | Expert opinion (theoretical model, disputed) | williamson1967hierarchical | abstract plus secondary |
| 17 | One company keeps the same span range at every level to avoid an additional layer | Documented practice | gitlab2026structure | full text |
| 18 | Externality test for enterprise policies; owner, enforcement point, exception path, measure | This book's recommendation | — | reasoning |
| 19 | Level mix bands per domain; no research-backed right mix | This book's recommendation (gap) | — | reasoning |
| 20 | Place whole ownership per site; three vendor tests | This book's recommendation | — | reasoning from rows 8–10 |
| 21 | Halvard and Northstar figures (Halvard groups 130, 110, 100, 90 plus platform 70, per maintainer rule) | Illustrative | — | invented, arithmetic shown |

Research gap: no peer-reviewed evidence found on optimal engineering level mix, or on outcomes of
contractor versus employee staffing in software organizations; the chapter labels both as this
book's recommendation.

## Chapter 49 — Multi-Year Transformation, Executive Communication, and Constructive Politics

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Transformation efforts fail partly by declaring victory too soon | Practitioner | kotter1995leading | official summary; idea-level |
| 2 | Escalation of commitment: further resources committed to a failing course | Research finding (idea credited) | staw1976knee | idea-level |
| 3 | Optimism bias and strategic misrepresentation are distinct causes of bad forecasts needing different remedies | Research finding | flyvbjerg2006nobel | full text |
| 4 | Stage-gate: stages separated by gates with criteria and go/stop decisions | Practitioner (transfer to programs is this book's) | cooper1990stagegate | idea-level |
| 5 | Strategy kernel: diagnosis, guiding policy, coherent actions | Expert opinion | rumelt2011good | idea-level |
| 6 | Transformation is mainly people, culture, and organization rather than technology | Expert opinion | kane2019technology | idea-level |
| 7 | Top management attention is limited; issue selling shapes it early in decision making | Research (conceptual) | dutton1993selling | abstract |
| 8 | Managers' accounts stress packaging, involvement, and timing as issue-selling moves | Research finding (managers' accounts) | dutton2001moves | abstract |
| 9 | Governing point first in executive writing | Practitioner | minto2002pyramid | idea-level |
| 10 | Executive sponsorship can reduce candor; executives sometimes ignore reported bad news | Research summary by the researchers | keil2014pitfalls | full text |
| 11 | Power and influence are how organizations get things done; diagnose whose support is needed | Expert opinion | pfeffer1992managing | idea-level |
| 12 | A cohesive leadership team is the basis of organizational health | Expert opinion | lencioni2012advantage | idea-level |
| 13 | Political skill uncorrelated with general mental ability; predicted managers' performance ratings in two samples | Research finding | ferris2005development | abstract |
| 14 | Political skill relates to productivity, career success, reputation; predicts task performance beyond Big Five and GMA; three of four dimensions predict performance | Research finding (meta-analysis) | munyon2015political | abstract |
| 15 | Perceived organizational politics correlates with strain, turnover intentions, lower satisfaction and performance (values as reported) | Research finding (meta-analysis, correlational) | chang2009perceptions | abstract |
| 16 | Constructive politics defined by transcript, record, and interests tests | This book's recommendation | fisher1981getting (interests) | idea-level for interests |
| 17 | Rational persuasion, inspirational appeal, consultation most effective; exchange not effective upward | Research finding | yukl1992consequences | abstract |
| 18 | Succession better treated as a process than an event; put it in exit criteria | Research review + this book's recommendation | berns2017succession | abstract |
| 19 | Gate rule (mandatory criteria, re-scope, stop) and staged funding | This book's recommendation | — | reasoning |
| 20 | All Northstar and Halvard figures | Illustrative | — | fictional |

## Chapter 50 — What a CTO Actually Does

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Record where executive time goes before deciding where it should go | Expert opinion | drucker1967effective | idea-level |
| 2 | CEO time use is measurable from diary data (1,114 CEOs, six countries); "leader" and "manager" types; performance gaps attributed mainly to CEO-firm mismatch | Research finding (on CEOs; applied to CTOs by analogy only, stated in text) | bandiera2020ceo | abstract |
| 3 | Four CTO roles attributed to Tom Berray: infrastructure manager, visionary and operations manager, external-facing technologist, big thinker; first two manage engineering directly, last two sit near the executive team | Expert opinion | vogels2007ctoroles | full text (post); Berray's original not read |
| 4 | Survey of 25 CTOs of Fortune 100 industrial companies on tasks, backgrounds, and why the position was created; role orchestrates product, process, and information technology | Research finding (old, manufacturing context; stated in text) | adler1990cto | abstract |
| 5 | A CTO's influence rests on business knowledge, networks, and the CEO's style more than on expertise and formal position | Research (conceptual propositions, labeled an informed hypothesis) | medcof2008cto; hambrick2007upper | abstract |
| 6 | The engineering executive is defined by responsibility for all of engineering, regardless of title; the executive job is a craft of its own | Expert opinion | larson2023executive-job; larson2024primer | full text; idea-level |
| 7 | Companies define CTO and VP Engineering very differently; document how technical decisions are really made; many lightly held executive opinions create thrash; learn how the business makes and spends money; build peer relationships before conflict | Expert opinion | larson2020first90 | full text |
| 8 | IT governance as decision rights over five decisions, assigned by archetypes; top performers align governance with performance goals (250+ enterprises, 23 countries) | Research finding (enterprise IT; method transferred, stated in text) | weill2004govern | abstract |
| 9 | The engineering executive as company-first problem solver merging CEO, peer, and engineering views | Expert opinion | larson2023balancing | full text |
| 10 | Formal versus real authority; real authority follows information; superior's overload raises subordinates' real authority | Research (formal model) | aghion1997formal | abstract |
| 11 | An executive who is too disengaged does more damage than one somewhat too involved | Expert opinion | larson2023micromanage | full text |
| 12 | Managerial work is brief, fragmented, and verbal | Expert opinion (idea credited) | mintzberg1990job | idea-level |
| 13 | Peers as the leader's first team; peer incentives conflict | Expert opinion | larson2023gelling; lencioni2002five | full text; idea-level |
| 14 | The management track up to senior executive roles, including CTO | Practitioner (references list only) | fournier2017manager | idea-level |
| 15 | Archetype table with a fifth "organization builder" pattern; three diagnostic questions; CTO/VP/IT decision-rights split; "only the CTO" list; the two-question decision test; the rhythm table | This book's recommendation | — | synthesis |
| 16 | Victor Lindqvist's calendar, the 11 informal requests, the keep, give, stop list, and the IT seam options | Illustrative | — | fictional; arithmetic in research/northstar-additions/ch50.md |

**Gaps.** Empirical research on what CTOs in software companies of 50 to 500 engineers actually do with their
time is thin; the chapter relies on a 1990 manufacturing survey, a conceptual article, a CEO time-use study
applied by analogy, and practitioner writing. The chapter says so ("Research on the role is thin"). Proposed
research-gaps entry: "CTO time allocation and role archetypes in mid-size software companies: no empirical
study found; Chapter 50 uses CEO time-use research by analogy."

## Chapter 51 — Enterprise Technology Strategy and the Three-Year Roadmap

| Claim in the chapter | Source id | Access level | Evidence label |
|---|---|---|---|
| Strategy as a cascade of choices: aspiration, where to play, how to win, capabilities, management systems | lafley2013playing | metadata-only | expert opinion (idea level) |
| Diagnosis, guiding policy, coherent action; signs of bad strategy | rumelt2011good | metadata-only | expert opinion (idea level) |
| Operational effectiveness is necessary but not strategy; strategy is trade-offs; choosing what not to do | porter1996strategy | abstract-only (publisher page highlights) | expert opinion |
| Each new technology spends a scarce budget of attention ("innovation tokens") | mckinley2015boring | full-text | expert opinion |
| Strategic alignment model: four domains, strategic fit, functional integration | henderson1993alignment | abstract-only | conceptual model (expert opinion) |
| Alignment research has disputes and challenges to its value | chan2007alignment | abstract-only | research finding (review) |
| Meta-analysis: alignment dimensions positively correlated with performance; little "alignment paradox" | gerow2014alignment | abstract-only | research finding |
| Alignment associated with agility; effect on performance fully mediated by agility; infrastructure flexibility as strong as alignment (241 firms) | tallon2011alignment | abstract-only | research finding |
| Deliberate and emergent strategies as ends of a continuum | mintzberg1985deliberate | abstract-only | research finding (typology) |
| Three horizons of growth | baghai1999alchemy | metadata-only | expert opinion (idea level) |
| Horizons are not bound by time; model still useful for prioritizing | blank2019flaw | full-text | expert opinion |
| Irreversibility and the option value of waiting | dixit1994investment | official-summary | expert opinion (theory) |
| Plan ventures around assumptions tested at checkpoints | mcgrath1995discovery | metadata-only | expert opinion (idea level) |
| Reversible versus irreversible decisions | bezos2016letter | full-text | documented practice |
| Layered technology roadmap | phaal2004roadmapping | metadata-only | expert opinion (idea level) |
| Premortem surfaces withheld reservations | klein2007premortem (entry in ch55.yaml) | official-summary | expert opinion |
| Optimism bias and strategic misrepresentation in long-range estimates | flyvbjerg2006nobel | (existing entry) | research finding |
| Policies applicable and enforced; coherent actions most important | larson2023engstrategy | full-text | expert opinion |
| Allocate coarsely and change allocations rarely | larson2023planning | full-text | expert opinion |
| Strategy and planning as part of the engineering executive's job | larson2024primer | metadata-only | expert opinion (idea level) |
| Transformation depends more on people and organization than technology | kane2019technology | metadata-only | expert opinion (idea level) |
| Even allocation across units (partition dependence) | bardolet2011capital | abstract-only | research finding |
| Four bins, horizons as kinds of bet, option record fields, seven coherence tests, stress rule, decision rules | — | — | this book's recommendation |
| All Northstar and Halvard figures | — | — | illustrative |

### Gaps (proposed for research/research-gaps.md)

- **No outcome evidence for written technology strategies.** The alignment literature is correlational
  and survey-based; nothing found tests whether writing a technology strategy, or any particular format,
  improves outcomes. The chapter says so.
- **Roadmapping effectiveness.** The roadmapping source was available at metadata level only; no
  evidence on whether layered roadmaps or decision calendars improve decisions was read.
- **Horizon allocation ratios.** No credible evidence was found for any particular split of capacity
  across horizons; the chapter's Northstar split is illustrative and the Halvard 20 to 25 percent figure
  in the X2 solution is labeled a judgment.

### Proposed disputed claim (for research/disputed-claims.md)

- **Are the three horizons time periods or kinds of bet?** Many organizations tie horizons to delivery
  windows; Blank (2019) argues the time element no longer holds while the categories stay useful; one of
  the model's authors disputes the "flaw" framing (comments on Blank's post). The chapter's position:
  horizons are kinds of bet distinguished by what is known about demand and design, and all three start
  in year one.

## Chapter 52 — Technology Investment, Budgeting, and Financial Literacy

Written 2026-11-22 (wave 7). New source entries are in `research/pending-sources/ch52.yaml`.

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Four main financial statements; assets = liabilities + shareholders' equity | Standard | sec2014beginners | full text |
| 2 | Income statement shows revenue and costs over a period; operating profit = gross profit minus operating expenses; depreciation or amortization spreads the cost of long-lived assets | Standard | sec2014beginners | full text |
| 3 | Cash-flow statement has operating, investing, financing sections; cash flow is related to but not equal to net income; non-cash items such as depreciation are added back | Standard | sec2014beginners | full text |
| 4 | Financial figures rest on estimates and judgment; reading them means knowing where judgment enters | Practitioner | berman2006financial | idea level (metadata-only) |
| 5 | SaaS (cloud computing arrangement) development falls under ASC 350-40; software to be sold or licensed under 985-20 | Standard | fasb2025asu202506 | full text (BC13, Summary) |
| 6 | ASU 2025-06 removes project stages because they fit iterative development poorly; capitalization starts at authorized, committed funding plus probable completion | Standard | fasb2025asu202506 | full text (Summary, 350-40-25-12) |
| 7 | Significant development uncertainty (unresolved novel features; requirements not identified or still substantially revised) blocks the threshold | Standard | fasb2025asu202506 | full text (350-40-25-12A) |
| 8 | Capitalizable: direct payroll and payroll-related costs for time on the project, external direct costs, upgrades adding functionality, data-conversion software. Expensed: G&A and overhead, training, maintenance, inseparable minor upgrades, other data conversion | Standard | fasb2025asu202506 | full text (350-40-25-4, 25-5, 25-17A to 17D, 30-1, 30-3) |
| 9 | Capitalization ceases when substantially complete; impairment when completion is no longer probable, uncompleted software presumed worth zero; listed indicators | Standard | fasb2025asu202506 | full text (350-40-25-13, 25-14, 35-3) |
| 10 | Effective for annual periods beginning after December 15, 2027, early adoption permitted; FASB expects little change for most software, possibly less capitalization for CCA software | Standard | fasb2025asu202506 | full text (Summary) |
| 11 | Old stage model: preliminary, application development, post-implementation | Standard | fasb2025asu202506 | full text (superseded text shown in the Update) |
| 12 | IAS 38: research expensed, development capitalized when criteria are met; finite-life intangibles amortized and impairment-tested | Standard | ifrs-ias38 | official summary |
| 13 | Capitalized software figures associated with returns and prices; no support for harm to earnings quality; analysts' errors rise with capitalization intensity; by 1995 amortization roughly offset capitalization's effect on reported profitability | Research finding (correlational; SFAS 86, public packaged-software firms) | aboody1998software | abstract |
| 14 | In steady state, capitalization barely moves operating income but raises EBITDA by the capitalized amount | This book's recommendation (arithmetic), consistent with row 13 | — | derivation shown with Northstar figures |
| 15 | Ticket, project, and role-based tracking; role-based viewed skeptically by auditors; three tests for a method; finance usually prefers compliance to maximization | Expert opinion | larson2023capitalize | full text |
| 16 | Budget definition and purposes; top-down and bottom-up drawbacks; budgetary slack; low targets; zero-based and rolling budgets' costs | Standard (textbook) | franklin2019managerial | full text (section 7.1) |
| 17 | Annual plan as P&L, budget by function, and headcount plan; the engineering executive is a stakeholder in the financial plan; stable plans preferred | Expert opinion | larson2023planning | full text. Note for the maintainer: the existing entry's claims do not include the three-documents point, the stakeholder point, or the expense categories (headcount, production operating costs, development costs); all were verified on the page on 2026-11-22 and could be appended to its claims |
| 18 | Two practitioner responses to budgeting: improve (planning problems) or abandon (performance-evaluation problems) | Research (overview article) | hansen2003budgeting | abstract |
| 19 | Budgeting as most companies practice it should be abolished | Expert opinion | hope2003budgets | official summary |
| 20 | Separate budget, forecast, and target; reward nobody for the forecast | This book's recommendation | synthesis of rows 16, 18, 19 | — |
| 21 | FinOps as an operational framework and cultural practice for financial accountability through engineering, finance, and business collaboration | Industry framework (practitioner foundation) | finops-what-is | official summary |
| 22 | Optimism bias and strategic misrepresentation; reference class forecasting | Research finding (infrastructure, transfer to software is the book's) | flyvbjerg2006nobel | full text |
| 23 | Checklist for a decision maker to test a team's recommendation for bias | Practitioner | kahneman2011bigdecision | idea level |
| 24 | NPV sensitivity to the discount rate; test it | Standard (textbook) | dahlquist2022finance | full text |
| 25 | All Northstar statements, the capitalization policy and history, the FY2 budget draft, and the TR-01 scenarios | Illustrative | — | fictional; every figure derived in `research/northstar-additions/ch52.md` |

Gaps admitted in the chapter or this matrix:

- No research was found on how capitalization policy affects engineering behavior or investment mix
  inside companies (for example, a bias toward capitalizable feature work). The chapter states that
  risk as this book's reasoning, not as a finding. Candidate for `research/research-gaps.md`.
- The capitalization research read (row 13) concerns external-use software under SFAS 86 in the 1980s
  and 1990s; no study of capitalization under ASC 350-40 for cloud software was read.
- The reference-class uplift for software estimates uses Northstar's own canon history; Flyvbjerg's
  uplift data is from transport infrastructure and is not quoted.
- ASU 2025-06 was read from the Update, which is not itself authoritative GAAP; the Codification text
  as amended was not read separately.

## Chapter 53 — Risk, Governance, Regulation, and Security Strategy (with template t11)

| Claim in the chapter or template | Source id | Access level | Evidence label |
|---|---|---|---|
| Cybersecurity risk registers at system and organizational levels, with measures rolled up to the enterprise level and managed against mission and business objectives | nist2025ir8286r1 | abstract-only | Standard |
| IR 8286 (2020) was superseded by Rev. 1 in December 2025 | nist2025ir8286r1 | abstract-only (CSRC page history) | Standard |
| Risk assessments give senior leaders the information to choose responses to risks | nist2012sp800-30r1 | official-summary | Standard |
| Risk matrices have poor resolution, can rate smaller risks higher, can be worse than random with negatively correlated frequency and severity, have ambiguous inputs; use with caution and explained judgments | cox2008risk | abstract-only | Research finding (mathematical analysis) |
| Open FAIR expresses information risk in the same economic terms as other risks; O-RT and O-RA standards | opengroup-open-fair | official-summary | Standard |
| Cybersecurity risk can be measured with calibrated estimates and simple quantitative models rather than ordinal scores (idea only) | hubbard2023cybersecurity | metadata-only | Expert opinion |
| CSF 2.0: six functions, Govern at the center, profiles and gap analysis, Core not a checklist | nist2024csf | full-text | Standard |
| SSDF as secure development vocabulary in four practice groups | nist2022ssdf, nist-ssdf-project | abstract-only; full-text | Standard |
| SLSA Build and Source tracks | slsa-spec | full-text | Standard |
| Security as one of six design pillars, reviewed in conversation, not audit | aws-well-architected | full-text | Standard (vendor guidance) |
| SOC 2 is an examination by an independent licensed CPA of controls relevant to security, availability, processing integrity, confidentiality, or privacy; proposed 2027 criteria and dates | aicpa2026tsc-proposal | official-summary | Standard (official documentation) |
| Trust Services Criteria: control criteria for attestation engagements, five categories | aicpa-tsc2022 | official-summary | Standard |
| PCI DSS purpose, applicability (store, process, transmit, or could affect the CDE), validation set by brands and acquirers | pci-dss | official-summary | Standard |
| SEC 2023 rules: material incident disclosure within four business days of materiality determination; annual description of risk management, board oversight, management's role; registrants | sec2023cyberrule (pending in ch55.yaml) | official-summary | Regulatory requirement (official announcement) |
| Four risk responses (reduce, transfer, avoid, accept) | none | — | Practitioner consensus (stated without a citation) |
| Acceptance rules (accepter level, expiry of at most two quarters, escalation on expiry); appetite in indicator units; design evidence once; reporting rules; attestation tests | none | — | This book's recommendation |
| All Northstar facts, ratings, ranges, quotes, and options | canon plus research/northstar-additions/ch53.md | — | Illustrative |

### Gaps admitted

- **Privacy and data-protection law** is not surveyed (jurisdiction-specific, needs legal advice); the
  chapter says so. Candidate for `research/research-gaps.md`.
- **No outcome evidence** that enterprise risk registers, appetite statements, or SOC 2 attestation
  reduce incidents or losses was found or cited; the chapter presents them as standards and
  recommendations only. Consistent with Ch 26's admitted gap on SBOM and SLSA outcomes.
- **Breach cost** is deliberately not quantified for Northstar; no breach-cost statistic is cited.
- **SOC 2 Type 1 versus Type 2**: not confirmed on any AICPA page fetched; the book does not describe the
  distinction.
- **ISO/IEC 27001 and ISO 31000**: iso.org returned HTTP 403 to automated fetching on 2026-11-22; not
  cited and not mentioned.
- **Thomas, Bratvold, and Bickel (2014), "The Risk of Using Risk Matrices"**: the publisher page returned
  403; not cited.
- Cox (2008) author given names not shown on the page read (Europe PMC lists "Cox LA").

## Chapter 54 — Data and AI Strategy

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | AI acts primarily as an amplifier of an organization's existing strengths and weaknesses; returns come from the organizational system more than the tools | Industry research | dora2025state | official summary |
| 2 | Digital transformation is mainly a matter of people and organization | Practitioner (idea) | kane2019technology | idea-level |
| 3 | Data cascades are pervasive among interviewed practitioners (92 percent), invisible, delayed, often avoidable | Research finding (qualitative) | sambasivan2021data | abstract |
| 4 | ML systems carry specific technical debt: data dependencies, undeclared consumers, hidden feedback loops, external change | Expert opinion | sculley2015hidden | abstract |
| 5 | DORA's seven AI capabilities, including clear AI stance and healthy data ecosystems; both reported to amplify AI's benefits | Industry research | dora2025aicapabilities | official summary |
| 6 | Five-question data readiness test, plus labels for learning models | This book's recommendation | synthesis of 3–5 | n/a |
| 7 | Jagged frontier: AI helps on tasks inside its capability (12.2% more tasks, 25.1% faster) and hurts outside (19% less likely correct), consultants | Research finding | dellacqua2026jagged | abstract |
| 8 | AI-specific buy, build, or wait factors (differentiation in data, option value of waiting, cost of error) | This book's recommendation | builds on Ch 30 | n/a |
| 9 | AI assistance associated with less secure code and higher confidence in its security | Research finding | perry2023insecure | abstract |
| 10 | Package hallucination rates at least 5.2% (commercial) and 21.7% (open-source) in a large sample | Research finding | spracklen2025package | abstract |
| 11 | AI RMF is voluntary with four functions Govern, Map, Measure, Manage | Standard | nist2023airmf | official summary |
| 12 | SP 800-218A is a generative AI community profile augmenting the SSDF | Standard | nist-ssdf-project, nist2022ssdf | full text (project page) |
| 13 | Six-part AI-assisted engineering policy | This book's recommendation | informed by 5, 9, 10 | n/a |
| 14 | Copilot group 55.8% faster on one greenfield JavaScript task | Research finding (preprint) | peng2023copilot | abstract |
| 15 | Three field RCTs, 4,867 developers: 26.08% more completed tasks (SE 10.3%); larger gains for less experienced | Research finding | cui2026effects | abstract |
| 16 | Enterprise RCT, 96 engineers, one task: about 21% less time, wide interval | Research finding (preprint) | paradis2024google | abstract |
| 17 | Experienced OSS developers 19% slower with AI while forecasting 24% and believing 20% faster | Research finding (preprint, small sample) | becker2025metr | abstract |
| 18 | DORA 2024: adoption associated with better documentation, code quality, review speed; estimated 1.5% lower throughput and 7.2% lower stability; 39% little or no trust | Industry research | dora2024announcing | official summary |
| 19 | Acceptance rate tracks perceived productivity better than persistence measures | Research finding | ziegler2022productivity | abstract |
| 20 | Effort, output, outcome, impact chain | Expert opinion | orosz2023measuring | full text (per existing entry) |
| 21 | Indicators relied on for decisions get gamed | Idea attribution | campbell1979assessing | idea-level |
| 22 | Measure at team and system level across several dimensions; DORA delivery measures | Industry research / research | dora-metrics-guide, forsgren2021space, noda2023devex | full text / abstract |
| 23 | Do not bank unmeasured AI gains in headcount; measured trial with decision date | This book's recommendation | D9 | n/a |
| 24 | All Northstar data estate, survey, requests, and arithmetic | Illustrative | northstar-additions/ch54.md | n/a |

**Gaps.** No organization-level causal study of AI-assisted delivery outcomes was found. The DORA 2024 and
2025 reports were read only at official-summary level; the 25 percent adoption basis is stated in the
summary for the quality figures only, so the chapter does not attach it to throughput and stability. The
names of the SPACE dimensions remain unverified (existing caveat), so the chapter does not list them. EU AI
Act (eur-lex returned an empty page) and ISO/IEC 42001 (iso.org returned 403) could not be verified and are
not cited.

## Chapter 55 — Boards, Due Diligence, and Executive Decision-Making

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Boards grew concerned about IT dependence while remaining poorly informed about IT spending and strategy | Expert opinion | nolan2005itboard | official summary |
| 2 | US public companies must describe board oversight of cyber risk and management's role, and report material incidents generally within four business days of a materiality determination | Standard (binding rule for registrants) | sec2023cyberrule | official summary (press release) |
| 3 | CSF 2.0 places GOVERN at the center because it informs the other functions | Standard | nist2024csf | full text |
| 4 | Board cyber-risk reports should be standardized, quantitative, aligned with ERM, at least quarterly, with escalation thresholds and dialogue | Practitioner consensus (directors' association) | nacd2026cyber | official summary (one principle page) |
| 5 | Powerful sponsors reduce candor; bad news is sometimes ignored | Research finding (researchers' summary) | keil2014pitfalls | full text |
| 6 | A practitioner guide covers the engineering executive's job including board reporting | Expert opinion | larson2024primer | idea-level |
| 7 | Reading the numbers a board reads | Expert opinion | berman2006financial | idea-level |
| 8 | Engineering should evaluate acquisitions rigorously, from a written thesis and a base template; one vote, not a veto; named failure modes; integration approach | Expert opinion | larson2023ma | full text |
| 9 | ISO/IEC 5230 defines requirements of an open source license compliance program | Standard | openchain-iso5230 | official summary |
| 10 | SBOM minimum elements | Standard | ntia2021sbom | full text |
| 11 | Yahoo's security team knew of the 2014 breach within days; not disclosed until 2016 during the Verizon sale; disclosure controls failed; $35M penalty | Documented practice (regulator's settled findings) | sec2018altaba | official summary |
| 12 | Verizon purchase price cut by $350M to about $4.48B; incidents disregarded for material adverse effect; liabilities allocated | Documented practice (company filing) | yahoo2017amendment8k | full text (8-K) |
| 13 | People rate decisions better when outcomes are favorable, even with the same information, and despite saying they should not | Research finding | baron1988outcome | abstract |
| 14 | Reversible decisions deserve a light process; about 70 percent of information; disagree and commit | Documented practice | bezos2016letter | full text |
| 15 | Groups fail to pool unique information; such groups reach correct answers less often | Research finding | stasser1985pooling, lu2012hiddenprofiles | abstract |
| 16 | Task conflict more positively related to performance in top management teams and for decision quality | Research finding (correlational) | dewit2012paradox | abstract |
| 17 | Good decisions come from dissenting views | Expert opinion | drucker1967effective | idea-level |
| 18 | Abilene paradox | Expert opinion | harvey1974abilene | idea-level |
| 19 | Premortem: assume failure and list reasons; makes doubts safe to voice | Expert opinion | klein2007premortem | official summary |
| 20 | Explanations of events framed as certain are longer and more episodic | Research finding | mitchell1989prospective | abstract |
| 21 | Checklist for reviewing a team's recommendation for bias | Expert opinion | kahneman2011bigdecision | official summary; idea-level |
| 22 | Fast strategic decision makers consider more alternatives, use counselors, consensus with qualification | Research finding credited at idea level | eisenhardt1989fast | idea-level (metadata only) |
| 23 | Clear decision roles | Expert opinion | rogers2006whohasd | official summary |
| 24 | Board reporting rules (stable definitions, item labels, miss first), diligence triage into price/terms/integration/walk away, surviving-diligence rules, CTO decision record fields, decision placement table | This book's recommendation | none | reasoning shown in chapter |
| 25 | All Northstar and hypothetical diligence figures | Illustrative | none | canon arithmetic in research/northstar-additions/ch55.md |

### Gaps

- No peer-reviewed evidence was found and read on what board technology reporting practices improve
  outcomes; the board-reporting advice rests on a directors' association guide, an HBR summary, a
  regulator's rule, and this book's reasoning. Candidate for `research/research-gaps.md`.
- No empirical study of technology due diligence effectiveness (for example, how often findings change
  price or terms) was read; the diligence section rests on one practitioner essay, two standards, and
  one public case.
- Eisenhardt (1989) could be credited only at idea level; the abstract was not accessible.
- The NACD handbook was read only for Principle Five; the other principles were not read.
- The ICO's Marriott/Starwood penalty (a second diligence-related public case) was considered, but the
  ICO page returned HTTP 403 and secondary accounts disagree on what it found about diligence; not used.

## Templates t05 and t12 — CTO competency matrix and architecture decision record

Same columns as `research/evidence-matrix.md`. For the maintainer to merge.

### Template t05 — CTO competency matrix

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | The engineering executive is whoever is responsible for all of engineering; CTO, VP Engineering, and Head of Engineering titles are used inconsistently | Expert opinion | larson2023executive-job | full text |
| 2 | Four CTO models (infrastructure manager, technology visionary and operations manager, external-facing technologist, big thinker), credited to Berray and Sampath; the role differs with the company and the part technology plays | Expert opinion | vogels2007ctoroles (entry in pending-sources/ch50.yaml; extra claim requested in t05-t12.yaml) | full text of the post; Berray and Sampath not read |
| 3 | The executive's job is the company's problem, not advocacy for engineering | Expert opinion | larson2023balancing | full text |
| 4 | Engineering executives' work as a whole (idea-level credit for the competency list) | Practitioner | larson2024primer | idea-level (metadata-only) |
| 5 | CSF 2.0 places GOVERN at the center of its functions (basis for treating risk accountability as a CTO competency) | Standard | nist2024csf | full text (pages read per bibliography) |
| 6 | The nine competencies, the archetype weighting step, and the rule that the director's results count for the CTO only through the CTO's own action | This book's recommendation | none | reasoning |
| 7 | No study validates any CTO competency model | Research gap | none | stated as a gap in the template |
| 8 | Northstar example: all evidence from canon (index executive context, baseline, first year through quarter 3 results and quarter 4 open items); ratings and weights are illustrative | Illustrative | canon pages | no new facts |

### Template t12 — Architecture decision record

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | ADR fields (title, context, decision, status, consequences), numbered, superseded not deleted; motivation is avoiding blind acceptance or reversal | Practitioner | nygard2011adr | full text |
| 2 | The collection of a project's ADRs is its decision log; the site points to several templates | Practitioner | adr-github-io | full text |
| 3 | MADR 4.0.0 sections, including optional Decision Drivers, Pros and Cons of the Options, and Confirmation | Practitioner | madr-template (new) | full text |
| 4 | Keeping ADRs in source control rather than a wiki | Practitioner consensus | thoughtworks-radar-lightweight-adr | full text |
| 5 | ADR adoption in open source is low and many logs hold few records | Research finding | buchgeher2023adr | abstract |
| 6 | Combined field set (Nygard plus Chapter 13 successor fields plus Chapter 28 governance fields), the ten fill-in steps, "title as the question" | This book's recommendation | none (Chapters 13 and 28) | reasoning |
| 7 | Northstar ADR-0001 example: canon facts plus Chapter 28's case-study estimates and Chapter 39's DL-08 entry; Decision left blank; ADR-0001 stays open | Illustrative | canon pages, Chapters 28 and 39 | no new facts |

### Gaps

- No evidence compares ADR templates or field sets by outcome; the template's additions are reasoned,
  not tested.
- No research validates CTO competency models or archetype classifications; Berray and Sampath's
  original paper was not located.

## Projects 7 and 8 — Twelve-month engineering strategy and CTO technology investment proposal

Projects apply chapters rather than make new claims, so most of their content is Northstar arithmetic
(**illustrative**). The rows below are the claims attributed to sources. No new sources were added; every
id below is already verified in `research/bibliography.yaml`.

### Project 7 — Design a 12-Month Engineering Strategy (project and solution)

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Strategy as explicit choices about where to play and how to win, applied here to where engineering will be excellent and where adequate is enough | Expert opinion | lafley2013playing | idea-level (metadata-only) |
| 2 | Coherent actions are the most important part of a strategy; they sort into enforcements, escalations, and transitions; policies should be applicable | Expert opinion | larson2023engstrategy | full text |
| 3 | People predicting their own task completion are optimistic; plan from the cautious case | Research finding | buehler1994exploring | abstract |
| 4 | Change allocations infrequently so teams can plan | Expert opinion | larson2023planning | full text |
| 5 | Allocations tend toward equal shares across the units a firm is divided into (partition dependence) | Research finding | bardolet2011capital | abstract |

### Project 8 — Build a CTO Technology Investment Proposal (project and solution)

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | The aim of cost-of-delay estimates is accuracy rather than precision; value channels; urgency profiles | Practitioner consensus | arnold2013blackswan | full text |
| 2 | Payback ignores the time value of money and flows after payback; report it only beside NPV | Standard textbook treatment | dahlquist2022finance | full text |
| 3 | Irreversible investment under uncertainty has an option value of waiting for better information | Research (academic book) | dixit1994investment | official summary |
| 4 | Effort estimates are optimistic; use the high end in the downside case | Research finding | buehler1994exploring | abstract |
| 5 | Cost of delay as the central quantity for sequencing product work | Expert opinion | reinertsen2009principles | idea-level (metadata-only) |
| 6 | Decision makers should review a team's recommendation for the team's biases | Expert opinion | kahneman2011bigdecision | official summary, idea level |

### Gaps

- No source in the bibliography covers software capitalization rules; Project 8 keeps accounting to
  questions for the CFO and a single general statement (treatment changes when a cost is expensed, not the
  cash spent), labeled as this book's recommendation. Chapter 52 owns the topic and may add a source.
- The Project 8 counterfactual for the quality continuation (how much unplanned work returns without
  prevention) has no Northstar evidence; the solution states it as an assumption and shows its break-even
  (3.9 points).

## Chapter 56 — Recovering a Failing Engineering Organization (with Project 2)

To be merged into `research/evidence-matrix.md` by the maintainer.

### Chapter 56 — Recovering a Failing Engineering Organization

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | The right transition strategy depends on the situation the leader enters | Expert opinion | watkins2003first | idea-level |
| 2 | Turnaround follows realignment on the downward slope; turnaround's crisis mode invites a more directive approach; realignment calls for engaging people in the diagnosis; people disagree about the stage; not every leader handles every stage equally well | Expert opinion | watkins2014hit | full text (IMD article); one sentence quoted |
| 3 | Turnaround research is fragmented; recent work adds managerial cognition, leadership, and stakeholder management, and finds simultaneous actions beyond the two-stage model | Research finding (review) | trahms2013decline | abstract; one phrase quoted |
| 4 | Cutting improvement time to meet throughput erodes capability (capability trap); managers tend to blame workers | Research finding (case studies and models) | repenning2001nobody | full text |
| 5 | Under threat, information processing narrows and control constricts, at individual, group, and organizational levels | Research finding (multilevel review) | staw1981threat | abstract |
| 6 | Negative status information fails to travel up on troubled software projects | Research finding (theory development) | smith2003reluctance | abstract |
| 7 | Most employees have stayed silent about a concern, most often for fear of being labeled negatively | Research finding (40 interviews) | milliken2003silence | abstract |
| 8 | Westrum's typology distinguishes cultures by treatment of messengers; high-trust, information-flow cultures predict performance | Industry research | dora-cap-generative-culture | full text |
| 9 | Improvement anywhere but the constraint is wasted; an IT turnaround dramatized through constraints and WIP limits | Practitioner (fiction), idea level | goldratt1984goal; kim2013phoenix | idea-level |
| 10 | Ability, benevolence, and integrity as factors of trustworthiness | Research model, credited at idea level | mayer1995integrative | idea-level (abstract read does not state the factors) |
| 11 | Trust repaired better by apology for competence violations and denial for integrity violations | Research finding (experiments) | kim2004removing | abstract |
| 12 | Direct leaders are a particularly important referent of trust (k = 106) | Research finding (meta-analysis) | dirks2002trust | abstract |
| 13 | Small wins make large problems tractable | Expert opinion, idea level | weick1984small | idea-level |
| 14 | Replacing a bottom-decile boss with a top-decile one raises team output more than adding a tenth worker to nine | Research finding (one firm) | lazear2015value | abstract |
| 15 | Managers' people skills strongly reduce turnover, with causal designs | Research finding (one firm) | hoffman2021people | abstract |
| 16 | Coaching effects g = 0.43 to 0.74; organizational outcomes delta = 0.36 (internal or external coaches, excluding manager coaching) | Research finding (meta-analyses) | theeboom2014coaching; jones2016coaching | abstract |
| 17 | Proximity to organizational change and recent departures associated with more customer-reported defects | Research finding (one project) | mockus2010volatility | abstract |
| 18 | One persistently negative member can reduce a group's trust and cooperation | Research finding (review and model) | felps2006bad | abstract |
| 19 | Trust and willingness to engage in conflict at the base of a leadership team | Expert opinion, idea level | lencioni2002five | idea-level |
| 20 | Definition of failing; four kinds of irreversible harm; the four triage outputs; two-track promises; no replacement in the first 30 days except integrity or harm; decision by day 90 | This book's recommendation | — | synthesis from rows 2–18 |
| 21 | All Northstar and Halvard figures; the Halvard Payroll case; the Northstar keep/coach/replace reading | Illustrative | — | fictional; arithmetic in `research/northstar-additions/ch56.md` |

### Project 2 — Diagnose a Low-Performing Engineering Team

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Billing's incident, delivery, capacity, people, and management facts | Illustrative (canon) | — | derived in `docs/projects/data/p2-billing-evidence.csv` |
| 2 | Sprint item counts and interview notes | Illustrative (project-only) | — | invented for the project, marked in page and CSV |
| 3 | Four causes of low performance; peer comparison as a control; arrival versus duration and recurrence | This book's recommendation | — | applies Chapters 9 and 56 |

### Gaps

| Gap | Where it shows | Note for `research/research-gaps.md` |
|---|---|---|
| G-56a | Turnaround evidence is firm-level and financial | No research found on recovering engineering organizations specifically; the chapter labels its triage and keep/coach/replace rules as this book's recommendation |
| G-56b | Coaching evidence measures people who entered coaching, over months | Unknown whether effects hold under a recovery's time pressure, or for leaders coached by their own manager (Jones et al. exclude manager coaching) |
| G-56c | Watkins's STARS framework | Read only through a short IMD article and the book's metadata; the book's own treatment of turnaround was not read |
| G-56d | Mayer, Davis, and Schoorman's three factors | Credited at idea level; the abstract read does not state them. A full-text read would allow a stronger statement |

## Chapter 57 — Crises, Executive Disagreement, and Resistance to Change

Written 2026-11-22 (wave 8). New sources are in `research/pending-sources/ch57.yaml`.

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | US public companies generally report a material cybersecurity incident on Form 8-K within four business days of determining materiality | Standard (regulator's rule) | sec2023cyberrule | official summary |
| 2 | Incident roles separate the commander, operations, communications, and planning; the communications role sends periodic updates | Documented practice | google2017managing | full text |
| 3 | Mann Gulch analyzed as the collapse of role structure and sensemaking; four sources of resilience proposed | Research finding (single qualitative case) | weick1993collapse | abstract; transfer to incident bridges is the book's inference |
| 4 | Failures in complex systems need several contributing faults; hindsight makes signals look obvious | Expert opinion | cook1998complex | full text |
| 5 | Protect stakeholders before reputation; instructing and adjusting information; expressions of concern are not admissions of guilt | Research finding (theory built on experiments) | coombs2007protecting | full text |
| 6 | Crisis clusters by attributed responsibility (victim, accidental, preventable); crisis history and prior reputation intensify | Research finding | coombs2007protecting | full text |
| 7 | Deny, diminish, rebuild strategies; rebuild for preventable crises and accidental crises with history; do not mix deny with diminish or rebuild | Research finding | coombs2007protecting | full text |
| 8 | Over-accommodation costs more without greater reputational benefit and can make the crisis seem worse | Research finding | coombs2007protecting | full text |
| 9 | Mapping a software outage caused by one's own change to the preventable end when there is crisis history | This book's recommendation | coombs2007protecting | inference |
| 10 | Apology repairs competence violations better, denial integrity violations; misleading statements turn an outage into an integrity question | Research finding plus inference | kim2004removing | abstract; transfer is the book's inference |
| 11 | Atlassian 2022: 775 customers, 883 sites, up to 14 days; first broad external message April 7 00:56 UTC; contacts deleted with sites; lessons on earlier and more transparent communication | Documented practice | atlassian2022outage | full text; "about 41 hours" is the book's arithmetic |
| 12 | GitLab 2017: about 18 hours down; public document, live stream, status account; engineer initially named, names to be redacted in future | Documented practice | gitlab2017postmortem | full text |
| 13 | People who expect blame withhold the details needed to prevent recurrence | Expert opinion | allspaw2012blameless | full text |
| 14 | Most of 40 interviewees had stayed silent about a concern, mostly for fear of being labeled negatively | Research finding (exploratory) | milliken2003silence | abstract |
| 15 | Managerial openness relates to voice more consistently than transformational leadership, via psychological safety, most for best performers | Research finding (one company, correlational) | detert2007leadership | abstract |
| 16 | Team psychological safety associated with learning behavior | Research finding | edmondson1999psychological | abstract |
| 17 | Exit and voice as responses to dissatisfaction; loyalty raises the cost of exit | Idea credited | hirschman1970exit | metadata only; "silent compliance" is the book's addition and is labeled as such |
| 18 | Free discussion, clear decision, full support | Idea credited | grove1983high | metadata only |
| 19 | Disagree and commit, including the boss; escalate fundamental misalignment early | Documented practice | bezos2016letter | full text |
| 20 | Task conflict more positively related to performance in top management teams and for decision quality | Research finding (correlational) | dewit2012paradox | abstract |
| 21 | Resistance as partly produced by change agents and as a resource | Conceptual (theory) | ford2008resistance | abstract |
| 22 | Responses to change as multidimensional attitudes; ambivalence | Conceptual (theory) | piderit2000rethinking | abstract |
| 23 | Reactions to change depend on process as well as content | Research finding (review of 79 studies) | oreg2011recipients | abstract |
| 24 | Two-track crisis model; commit-or-escalate test; external communication by phase; six readings of resistance; voice, exit, silence as forms | This book's recommendation | — | synthesis |
| 25 | Halvard Checkout outage and all its figures; Northstar case study readings | Illustrative | — | fictional; arithmetic in `research/northstar-additions/ch57.md` |

### Gaps

- **G57-1.** No empirical study found on software-outage communication specifically (for example, the
  effect of first-notice delay on customer churn). The chapter relies on general crisis-communication
  experiments (Coombs) and two documented public cases, and says so.
- **G57-2.** The evidence on disagreeing upward is about employees' voice to supervisors, not about
  executives disagreeing with executives; the commit-or-escalate test is the book's recommendation, not a
  tested procedure.
- **G57-3.** Resistance-to-change sources used here are conceptual articles read at abstract level; no
  empirical test of "resistance as information" diagnostics was found. The six readings are a synthesis.
- **G57-4.** Piderit (2000) was verified through OpenAlex and Semantic Scholar only (publisher page 403,
  Crossref lookup failed in session).

## Chapter 58 — Layoffs, Reductions, and Mergers and Acquisitions

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | The downsizing literature can be organized into antecedents and individual and organizational effects, with patterns and contradictions | Research finding (review) | datta2010downsizing (pending in ch58.yaml) | abstract |
| 2 | Downsizing predicts voluntary turnover rates, mediated by commitment; embedding and procedural-fairness practices weaken the link, career development practices strengthen it | Research finding | trevor2008downsizing (pending) | abstract |
| 3 | Survivors react most negatively when they identify with those laid off and see them as inadequately compensated (lower performance in lab, lower commitment in field) | Research finding | brockner1987survivors (pending) | abstract |
| 4 | Clear explanations of a layoff are associated with better survivor reactions, especially under high uncertainty and importance | Research finding | brockner1990explain (pending) | abstract |
| 5 | Job insecurity harms attitudes, health, and to some extent behavior toward the organization | Research finding (meta-analysis) | sverke2002insecurity (pending) | abstract |
| 6 | Restructuring mainly harms well-being; communication, information, and procedural justice intervene | Research finding (systematic review) | dejong2016restructuring | abstract |
| 7 | About 65 percent of 133 open-source projects had an estimated truck factor of 2 or less | Research finding | avelino2016truck | abstract |
| 8 | Turnover-induced knowledge loss can exceed expected loss several times; successors reduce expected loss | Research finding | rigby2016turnover | abstract |
| 9 | Proximity to organizational change and recent departures associated with more customer-reported defects in one project | Research finding | mockus2010volatility | abstract |
| 10 | Employers select for reductions by seniority, individual criteria, or eliminating positions or units | Standard (US federal guidance) | eeoc2009waivers (pending) | full text |
| 11 | Group waivers of age claims in the US require 45 days and written disclosure of the decisional unit and the titles and ages of those selected and not selected | Standard (US federal guidance) | eeoc2009waivers (pending) | full text |
| 12 | WARN: 60 calendar days' notice for covered closings and mass layoffs; covered employers broadly 100+ full-time workers; single-site thresholds; 30-day and 90-day aggregation; does not override longer notice laws; not legal advice | Standard (regulatory guidance) | dol2003warnemployer (pending) | full text (2003 guide) |
| 13 | EU: consult workers' representatives in good time with a view to agreement, disclose reasons and selection criteria; redundancies take effect no earlier than 30 days after notifying the authority | Standard (directive) | eu1998collective (pending) | full text, Articles 1-4 |
| 14 | On average acquirers' performance does not improve with acquisitions and is modestly negatively affected; unexplained variance | Research finding (meta-analysis) | king2004metaanalyses (pending) | abstract |
| 15 | Structural integration reduces new product introduction early and for pre-launch firms; effect fades | Research finding | puranam2006organizing (pending) | abstract |
| 16 | Integration impairs acquired inventors' productivity most for those losing status and centrality | Research finding (transfer to software is the book's inference) | paruchuri2006integration (pending) | abstract |
| 17 | Acquired leaders play a key role in expected and serendipitous value | Research finding (case-based theory building) | graebner2004momentum (pending) | abstract |
| 18 | Implementation choices and the nature of acquired knowledge shape technology and capability transfer | Research finding (grounded model, propositions) | ranft2002acquiring (pending) | abstract |
| 19 | Integration approaches depend on autonomy needs and strategic interdependence | Expert opinion (idea level) | haspeslagh1991managing (pending) | metadata only |
| 20 | Run the acquired stack about six months while consolidating where feasible; document the plan | Expert opinion | larson2023ma | full text |
| 21 | System designs copy the communication structure of the organization | Expert opinion (argued essay) | conway1968committees | full text |
| 22 | The engineering executive's job (general further reading) | Expert opinion (idea level) | larson2024primer | metadata only |
| 23 | Structuring a leader's first months (further reading) | Expert opinion (idea level) | watkins2003first | metadata only |
| 24 | Decide work before people; role-based then skill then pre-existing documented performance; ownership check; one notification day; per-dimension integration | This book's recommendation | none | synthesis of rows 2-21 |
| 25 | All Halvard figures (Field Operations reduction, Corvane integration) and the Northstar scenario in X1 | Illustrative | none | canon arithmetic in research/northstar-additions/ch58.md |

### Gaps and limits admitted in the chapter

- No tested recipe exists for running a reduction in a software organization; the procedures are this book's
  recommendation built on general downsizing research and software knowledge-loss research.
- The downsizing and acquisition studies are mostly outside software; the acquisition productivity evidence
  is from pharmaceutical inventors and patent counts.
- Brockner et al. (1994) on procedural justice for victims, survivors, and "lame ducks" was found, but its
  open abstract is truncated, so it is not cited.
- Legal sources are a 2003 US federal guide, 2009 US federal guidance, and the 1998 EU directive's original
  text. State laws, national transposition, and later amendments were not checked; the chapter says it is not
  legal advice and points to counsel per jurisdiction.
- Datta et al. (2010) is cited only for its framework; its conclusions on firm performance were not read.

## Chapter 59 — Transformation Under Budget Constraint and Scaling Without Bureaucracy

| Claim in the chapter | Source id | Access level | Evidence label |
|---|---|---|---|
| A system's output is set by its constraint; improving elsewhere does not raise output | goldratt1984goal | metadata-only (idea level) | Practitioner consensus |
| Most attention goes to parameters, which rarely change behavior; rules and information flows are higher leverage | meadows1999leverage | full-text | Expert opinion (mapping to budget cuts is this book's interpretation) |
| Queues in product development are invisible and so ignored | reinertsen2009principles | metadata-only (idea level) | Expert opinion |
| People default to additive changes and overlook advantageous subtractive ones (eight experiments; worse without a cue and under load) | adams2021subtractive | abstract-only | Research finding |
| Link from additive bias to institutional red tape | adams2021subtractive | abstract-only | Authors' suggestion, stated as such in the chapter |
| Enabling versus coercive formalization; effect on attitudes depends on which | adler1996bureaucracy | abstract-only | Research (conceptual), stated as a conceptual argument |
| Remove destructive friction, keep useful friction | sutton2024friction | metadata-only (idea level) | Expert opinion |
| Heavyweight change approval associated with lower delivery performance; no evidence that formal external review lowers change failure rate; recommends peer review and a coordinating board | dora-cap-change-approval | full-text | Industry research |
| Project Oxygen began from the hypothesis that managers do not matter; teams with effective managers had better results, happiness, lower turnover | rework-great-managers, garvin2013google | full-text; abstract-only | Documented practice |
| Scholarly understanding of radically decentralized (self-managing) organizations is limited; review proposes an agenda | lee2017selfmanaging | abstract-only | Research finding (review) |
| Manager talent matters more than span; for remote and hybrid managers more reports associated with lower engagement | harter2026span | full-text | Industry research |
| Six to eight engineers per manager; four to six managers per manager of managers | larson2018sizing | full-text | Expert opinion |
| Large US firms flattened: wider CEO spans, fewer levels | rajan2006flattening | abstract-only | Research finding |
| Load test, funding-source order, suspend-before-delete, verdict table | none | n/a | This book's recommendation |
| Northstar and Halvard figures | canon and research/northstar-additions/ch59.md | n/a | Illustrative |

### Gaps admitted in the chapter or this matrix

- No research was found that measures the effect of removing organizational process (forums, approvals,
  reports) on outcomes in software organizations, beyond DORA's change-approval findings. The load test
  and the suspend-before-delete method are this book's recommendation, not tested practice.
- The evidence on removing managers is thin and mixed in kind (one company's documented practice, a
  review that reports limited understanding, survey research across occupations). The chapter therefore
  targets management time rather than manager headcount.
- Research on running a technical transformation under a budget cut specifically was not found; the
  funding-source order is synthesis.
- Curriculum source meadows2008thinking is not cited; the chapter uses Meadows's leverage-points essay
  (meadows1999leverage, full text read) instead, which supports the specific claim made.
  larson2019elegant is not cited; its sizing material is cited through the essay larson2018sizing, which
  was read in full.

## Chapter 60 — Capstone: Transforming Northstar Technologies

No new sources. Every source cited is an existing, verified entry in `research/bibliography.yaml`; claims
stay within each entry's recorded `access_level` and `claims`.

| # | Claim | Label | Sources | Basis |
|---|---|---|---|---|
| 1 | Strategy needs coherent actions that support each other, not a list of separately reasonable initiatives | Expert opinion | rumelt2011good | idea-level (metadata only) |
| 2 | Delays between action and consequence make systems hard to steer; stocks change only through flows | Expert opinion | meadows2008thinking | idea-level (metadata only) |
| 3 | Capability trap: cutting improvement time to meet throughput erodes capability; long, hard-to-see delays lead managers to blame effort | Research finding (field case studies and simulation models, mostly outside software) | repenning2001nobody | full text |
| 4 | Escalation of commitment to a course of action one chose oneself | Credited at idea level (no finding reported) | staw1976knee | idea-level (metadata only) |
| 5 | Throughput and stability delivery measures | Industry research, idea level | forsgren2018accelerate | idea-level (metadata only) |
| 6 | DORA guide: speed and stability not trade-offs; setting metrics as goals increases gaming; metrics for services, improvement over time, not team competition | Industry research | dora-metrics-guide | full text |
| 7 | Outcome bias: decisions rated better when outcomes are favorable, despite equal information and despite subjects saying they should not | Research finding (undergraduate subjects) | baron1988outcome | abstract |
| 8 | Managers who read financial statements decide and argue better | Expert opinion | berman2006financial | idea-level (metadata only) |
| 9 | Error budgets convert a reliability target into a rule for change risk | Documented practice, idea level | beyer2016sre | idea-level (metadata only); summarized, not adapted (CC BY-NC-ND) |
| 10 | Team boundaries matched to the flow of change; limits on cognitive load | Expert opinion | skelton2019team | idea-level (metadata only) |
| 11 | Commitment register, hinge review, bridge rule, honor/bridge/revise/retire flow, portfolio integration checks, step-down rule for prevention | This book's recommendation | none | reasoning shown in chapter |
| 12 | All Northstar and Halvard figures and events | Illustrative | none | canon only; derived arithmetic in research/northstar-additions/ch60.md |

### Gaps and limits

- No source in the bibliography studies whether consistency of a leader's documents over a year (the
  capstone's central claim) improves outcomes. The integration method is labeled this book's
  recommendation throughout.
- The count-noise argument in solution X2 (that a per-quarter threshold near 10 can be broken by noise)
  is stated as an assumption, not sourced.

## Templates t01, t02, t06, t19 — 1:1 template, career development plan, team health assessment, leadership succession plan

Wave 8. No new sources; all ids below already exist in `research/bibliography.yaml`. No Northstar
facts added: every example uses canon pages and facts already recorded in the chapter case studies
(Chapters 5, 8, 14, 36, 41, 55). Each template links to the chapter that teaches the topic instead of
re-teaching it.

| Claim in the template | Source id | Access level | Evidence label |
|---|---|---|---|
| **t01.** Meetings rated highest when the report created the agenda; managers' self-ratings of one-on-one skill appear inflated | rogelberg2024unlocking | full-text (researcher's popular summary; underlying studies not read) | Expert opinion informed by survey data |
| **t01.** The one-on-one as the subordinate's meeting | grove1983high | metadata-only (idea-level) | Practitioner consensus |
| **t01.** Fields, five-line record, illustrative decay thresholds, deeper-question rotation | none | — | This book's recommendation (from Chapter 5) |
| **t02.** Pairing care with directness in the "not yet" | scott2017radical | metadata-only (idea-level) | Expert opinion |
| **t02.** Sponsorship distinct from mentoring; a person can be mentored and not sponsored | ibarra2010promotions | full-text | Industry research (MBA graduates, not engineers) |
| **t02.** Plan fields; at most two gaps; dependency and fallback field | none | — | This book's recommendation (from Chapter 8) |
| **t06.** Facilitated workshop rating about ten areas green, yellow, red with a trend; works only with high trust; do not compare teams; support tool, not judgment tool | kniberg2014squad | full-text | Documented practice (one company, no outcome data) |
| **t06.** Survey scores distorted once tied to reviews and manager pressure | orosz2023measuring | full-text | Expert opinion |
| **t06.** Team Diagnostic Survey as a validated instrument of structure, support, and leadership | wageman2005team | abstract-only | Research finding (instrument validation only) |
| **t06.** Area wording, access rule, signal pairing, two-action limit | none | — | This book's recommendation (from Chapter 14) |
| **t19.** Succession research has treated succession as an event; practice treats it as a process | berns2017succession | abstract-only | Research finding (CEOs; framing only) |
| **t19.** Designated successors reduced expected loss from turnover by up to 15 percent (Chrome, Avaya) | rigby2016turnover | abstract-only | Research finding (code; extension to managers is the book's inference, stated) |
| **t19.** Firms promote on current performance though other traits better predict managerial performance | benson2019promotions | abstract-only | Research finding (sales workers) |
| **t19.** Readiness scale, coverage rule, critical-role definition | none | — | This book's recommendation (owned by Chapter 36) |
| All four Northstar examples | none | — | Illustrative (fictional canon) |

Gaps admitted in the templates: no validated study of one-on-one formats (Chapter 5's gap); no outcome
data for facilitated health checks; no research on succession planning for engineering managers
specifically. Nothing could not be verified, because no new source was introduced.
