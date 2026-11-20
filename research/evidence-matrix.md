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
