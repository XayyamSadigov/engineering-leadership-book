# Project 5 solution: Northstar's quarter 3 organization scorecard

This is one worked answer to [Project 5](../p5-delivery-and-reliability-scorecard.md). It treats the
eight-entry scorecard in [Chapter 38](../../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md)
as a submission to be tested. The conclusion is that its structure is right (paired rows, owners and
stewards, the quality block by reference) but that four of its seven other entries repeat measures
already inside the block, two entries break its own steward rule, and it has no row for the SLOs,
invoice correctness, or security exposure. The scorecard below is this solution's recommendation, one
defensible answer among several. All Northstar facts are fictional; estimates marked as this
solution's are assumptions, not facts from the case.

People named: Victor Lindqvist (CTO), Rajiv Menon (CFO), Amara Okafor (CPO), Sofia Alvarez (VP Customer
Success), Marcus Oyelaran, Tom Becker, and Elena Sokolova (managers of Billing, Platform Operations, and
Payments and Integrations), Kwame Mensah and Li Na Zhou (staff engineers), and Joon Park (IT security
lead). The [cast](../../case-studies/northstar/cast.md) has the details.

## 1. Decisions first

| Decision in quarter 3 | Owner | When |
|---|---|---|
| Does prevention step down again in quarter 4? (Chapter 38's trigger: unplanned share above 26 percent in the week-31 sample) | Director, approved by Victor Lindqvist | Week 31, then the reset |
| Does Core need capacity for contract tests at the remaining tier 1 boundaries? (the week-26 report's checkpoint) | Director asks Victor | Week 32 |
| The quarter 4 allocation and commitment line | Director, CTO, CPO | Weeks 38 and 39 |
| Error budget policy: reporting mode (A) or enforced with Victor arbitrating (B) | Victor Lindqvist | Asked for before week 27 |
| What the renewal customers and the board are told about reliability | Victor, Sofia Alvarez for customers | Monthly |
| Whether Billing's prevention share funds invoice reconciliation first | Director with Marcus Oyelaran | Week 28 |
| Platform roadmap order (event store, environments, CI phase 1) | Tom Becker and Kwame Mensah, director approves | Monthly |
| Rajiv Menon's budget pack request | Director recommends; CTO and CFO agree | Before the budget pack |

Every entry below names one of these. A candidate that informed none was dropped: Core line coverage
(no decision uses it; the template says not to target it), total deployments across the organization
(no owner could act on it), and story points (not comparable across teams).

## 2. Readings, recomputed twice

From [`p5-quarterly-readings.csv`](../data/p5-quarterly-readings.csv). The first column is computed from
counts; the second is the figure Northstar's record reports.

| Measure | Quarter 2 from counts | Record reports | 95% interval (this solution's) |
|---|---|---|---|
| Sev1 and Sev2 incidents | 17 (3 + 14) | 17 | Poisson 9.9 to 27.2 |
| Customer-detected share | 5 ÷ 17 = 29.4% | 29% | Wilson 13% to 53% |
| Recurrences | 3 ÷ 17 = 17.6% | 3 of 17 | 6% to 41% |
| Core change failure rate | 3 ÷ 13 = 23.1% | 23% | 8% to 50% |
| Core change failure rate, baseline | 4 ÷ 13 = 30.8% (26 weeks before arrival) | 31% | 13% to 58% |
| Core change failure rate, quarter 1 | 2 ÷ 9 = 22.2% (weekly releases from week 5) | 22% | 6% to 55% |
| Corrective-action closure | 21 ÷ 27 = 77.8% | 78% | 59% to 89% |
| Tier 1 at the four minimums | 11 ÷ 15 = 73% | 11 of 15 | 11 of 15 (original list, kept for year 1) |
| Availability | 99.86% | 99.86% | Single-region probe; no interval possible |

**Incidents.** For the baseline count of 30 the Poisson interval is 20.2 to 42.8, and for quarter 1's
21 it is 13.0 to 32.1. Quarter 1 to quarter 2 (21 to 17) is indistinguishable from noise: conditional
on 38 incidents, 17 is 0.65 standard deviations below an even split. Baseline to quarter 2 (30 to 17)
is borderline: conditional on 47, 17 is 1.9 standard deviations below an even split, so a split at
least this uneven would occur about 6 percent of the time if the underlying rate had not changed
(normal approximation, this solution's calculation). The direction is encouraging, and the count alone cannot carry the claim. The
mechanism evidence carries more: incidents via Core releases went 9, 4, 2 and recurrences 11, 5, 3.

**Availability.** The director's quarters are 13 weeks, 91 days or 2,184 hours (131,040 minutes). At
99.86 percent, the paths were unavailable for 0.14 percent, about 183 minutes (131,040 × 0.0014 =
183.5). The contract allows 0.1 percent, about 131 minutes. The excess is about 52 minutes. The
baseline is a 90-day quarter: 2,160 × 0.0038 = 8.2 hours, which matches the baseline page; the
scorecard states the quarter length beside every availability figure. Credits fell from $410,000 to $95,000, by $315,000 a quarter.

**Unplanned work.** 28 percent of 80 is 22.4 FTE, about $1,036,000 a quarter (22.4 × $185,000 ÷ 4).
At baseline it was 27.2 FTE, about $1,258,000. The difference, 4.8 FTE or about $222,000 a quarter, is
capacity recovered, assuming the two-week samples are comparable.

**Three definitional notes the scorecard must publish.** None is an error in the data; each is a
place where a reader comparing quarters would be misled unless the window and the denominator are
printed next to the number.

1. **Core change failure rate windows.** Baseline 4 of 13 (the 26 weeks before arrival, on the
   fortnightly train), quarter 1 2 of 9 (weekly releases from week 5 only; the fortnightly releases of
   weeks 1 to 4 are not counted), quarter 2 3 of 13. All three are counts, but the windows differ. The
   scorecard publishes numerator, denominator, and window for every reading and marks the baseline as
   a different cadence. The Wilson intervals (13% to 58%, 6% to 55%, 8% to 50%) overlap almost
   entirely: the fall from 31 to 23 percent cannot be told from noise, and the flat reading between
   quarters 1 and 2 is no evidence of a stall either.
2. **The tier 1 list.** notification-svc moved to tier 2 from quarter 2, but year-1 readings (quarters
   1 to 4) stay on the original 15 so that quarters compare. The scorecard reports quarter 3 over 15,
   switches to the current list of 14 in quarter 5, and shows quarter 4 on both lists once as the
   bridge.
3. **Severity re-rating.** Under the week-3 definitions the baseline is 9 Sev1 and 21 Sev2, not 7 and
   23. The total of 30 is unchanged; any Sev1-only row must say which baseline it uses.

## 3. Reliability: contract, SLOs, and budgets

| Journey | SLO, 28 days | Budget in events | Budget in time |
|---|---|---|---|
| Order submission | 99.9% | 600,000 × 0.001 = 600 failed submissions | 0.001 × 40,320 minutes = 40 minutes |
| Order latency | 99% within 2 seconds | 6,000 slow submissions | about 403 minutes |
| Payment final within 60 seconds | 99.9% | 240,000 × 0.001 = 240 attempts | 40 minutes |
| Invoice correctness | 99.99% once reconciliation exists | Unknown: the case gives no invoice volume | 4 minutes |

**How the contract and the SLOs relate.** A 13-week quarter holds 91 ÷ 28 = 3.25 SLO windows; 3.25 ×
40.3 minutes is about 131 minutes, the contract's allowance for the quarter. In time terms, an order or payment journey that stays
within budget in every 28-day window also meets the quarterly contract, if the probe and the SLI agree.
They do not always: the probe runs from one region, misses the mobile path, and in INC-403 (order submission failed for customers with legacy price lists) would have
seen nothing, while the order SLI counts failures on both web and mobile. The scorecard therefore keeps
contractual availability as the target the contract sets, and budget consumption as the leading
measure that explains it.

**Under either policy.** Budget consumption is the same row under policy A and policy B; what changes
is the decision it feeds. Under A, any incident spending more than a fifth of a journey's budget
triggers a tracked review. Under B, exhausting the order or payment budget also holds non-urgent
releases on that journey until it recovers, with Victor Lindqvist arbitrating. The row's definition
does not depend on Victor's choice, which is the point of building it before he makes it.

**Blind spots.** Correctness failures (wrong amounts or data) were 8 of the 14 baseline
customer-detected incidents, and invoices and the ledger account for several of them; the invoice
correctness SLO has no data. The scorecard carries it as an entry with no reading
and an action (section 5, entry 3) rather than leaving it off: an empty row says what the organization
cannot see. The mobile path is covered by the order SLI at mobile-bff but not by the contractual probe;
adding a mobile synthetic check is costed in the data register.

## 4. Pair and gaming checks

| Measure | Likely gaming | Exposed by |
|---|---|---|
| Contractual availability | Loosening or moving the probe | Budget consumption from real traffic; probe changes need director sign-off |
| Budget consumption | Shipping less to protect the budget | Core releases per quarter and service deployment frequency |
| Sev1 and Sev2 count | Downgrading severity | Customer-detected share and the weekly severity audit |
| Core change failure rate | Not linking failures; fewer releases | Release frequency; incidents with no linked release, audited |
| Corrective-action closure | Closing without doing | Recurrence; monthly sample of closed actions |
| Committed items delivered | Committing less, renegotiating quietly | Forecast calibration and recorded scope trades |
| Capacity against plan | Relabeling feature work as prevention | Unplanned share by team from the same sample |
| Environment wait | Closing requests early | Other teams' requests on Platform Operations, in points |
| After-hours pages | Silencing alerts | Customer-detected share |

Victor Lindqvist's suggested key result, "Sev1 and Sev2 below 10" (Chapter 38), fails the target test
in Chapter 38: hitting it by downgrading would not be welcome. It stays a direction with its pair.

## 5. The scorecard

Ten entries; the quality block counts as one.

| # | Measure and definition | Source and status | Q2 reading | Direction or target | Pair | Row owner | Data steward | Decision |
|---|---|---|---|---|---|---|---|---|
| 1 | Contractual availability: successful synthetic checks ÷ checks, order and payment paths, per quarter | Synthetic monitoring; system, one region | 99.86% ($95,000 credits) | Target 99.9%, set by contract | 2, and customer-detected share | Director | Kwame Mensah | Renewals, credits forecast, reports to Victor |
| 2 | SLO budget consumed per journey (order, latency, payment): bad events ÷ budget, 28-day rolling | Load balancer, mobile-bff, payments-gateway; system | Weekly readings exist; no quarter summary recorded | Within budget | Release frequency (5) | Elena Sokolova | Kwame Mensah | Error budget policy; reviews; holds under B |
| 3 | Invoice correctness: invoices and postings passing reconciliation ÷ all, 28-day | Nightly reconciliation job; status unknown | None | Toward 99.99% once measured | Confirmed correctness defects from support | Marcus Oyelaran | Li Na Zhou | Billing's prevention priorities |
| 4 | Quality block (template rows listed below) | Incident tracker, review records, ownership inventory | As listed | Per row | Within the block | Per template | Kwame Mensah | Monthly quality reviews; prevention step-down |
| 5 | Delivery by component: deployment frequency, change failure rate (72-hour rule and DORA side by side to quarter 4), lead time for changes; Core as its own line | Hand-joined CI logs until the event store runs | Core 13 releases, 3 of 13 failed | Frequency up, failure down, lead time down | Each other | Kwame Mensah | Li Na Zhou | Week-32 contract-test capacity |
| 6 | Capacity by category against plan: unplanned, prevention, platform, product, in FTE | Two-week sample per team; sampled | Unplanned 28% (22.4 FTE) | Unplanned down; others on plan within a fifth | Unplanned share by team | Director | A product manager named by Amara Okafor | Week-31 trigger; quarter 4 allocation |
| 7 | Commitments: committed items delivered, and the share of items delivered by their 85 percent forecast date | Planning tool | Not recorded after baseline (7 of 17) | Up | Recorded scope trades | Director | The same product manager | Commitment line for quarter 4 |
| 8 | Friction: median environment wait; Core review wait | Platform intake queue; code host | About 2 days (week 18); review wait not measured since 21 hours | Down | Other teams' requests on Platform Operations | Tom Becker | Kwame Mensah | Platform roadmap order |
| 9 | Sustainability: after-hours pages per person per rotation, with the share carried by the top three | Paging tool | Not recorded after baseline (54 of 64 by three ledger engineers) | Down, and spread | Survey items on cognitive load when run (teams of five or more) | Marcus Oyelaran | Kwame Mensah | Billing's ledger knowledge plan; rotation design |
| 10 | Security exposure: open critical and known-exploited vulnerabilities past Chapter 26's remediation service levels on tier 1, and exceptions within four weeks of expiry | Scanner results, exception register | 3 open criticals at day 90, all under exceptions; quarter 2 not recorded | Down | Dependency-scanning coverage | Director | Joon Park, IT security lead | Exceptions; renewal security questionnaires |

**The quality block** contains template rows 2 (Sev1 and Sev2 under written definitions), 3
(customer-detected share), 6 (time to restore, 90th percentile), 7 (recurrence), 8 (action closure),
and 10 (tier 1 readiness). Rows 1 (availability), 4 and 5 (Core change failure and deployment
frequency), and 9 (unplanned work) are lifted into entries 1, 5, and 6, so that each measure has one
definition in one place. Time to restore has no reading after the baseline quarter (14 hours at the
90th percentile); its first quarter 3 reading is the baseline for the row.

**Steward separation, checked.** No steward measures their own team: Kwame Mensah and Li Na Zhou sit
in no team; Joon Park is outside engineering; the product manager is outside engineering. Kwame owns the
Core change failure risk in the week-26 report, so he is row owner for entry 5 and Li Na Zhou, who owns
data and configuration standards, is its steward. Tom Becker owns entry 8, which measures his team's
service; its steward is Kwame, not Platform Operations.

**Rules for the scorecard.** A definition changes only through its steward, with the change logged and
the old and new values shown side by side for one quarter. The scorecard is read monthly in the
business review and audited at the reset. A row that changes no decision for two quarters is removed,
and nothing is added without a removal.

## 6. Data quality register

| Entry | How produced | Known weakness | Audit | Action and cost (this solution's estimates) |
|---|---|---|---|---|
| 1 | One-region probe | Misses mobile; INC-403 class invisible | Probe changes signed off | Second region and a mobile check: about 1 engineer-week from the platform line |
| 2 | SLIs from real traffic | Order SLI once counted client errors as good | Replay of known incidents each quarter | None; running |
| 3 | Reconciliation job | Unknown whether it runs | Steward confirms by week 28 | If not running, cost it from Billing's 2.5 FTE prevention share |
| 5 | Four CI systems joined by hand, about two days a month | Shell-script services log nothing; 72-hour links manual | Weekly link review | The event store, about 6 engineer-weeks (platform roadmap) |
| 6, 7 | Two-week sample; planning tool | Teams classify differently | Same sampling rules each quarter | None |
| 9 | Paging tool | Silenced alerts look like relief | Compare with customer-detected share | None |
| 10 | Scanner and register | 4 script services scanned weekly, not in pipeline | Monthly sample of "not affected" closures (two of seven were unanalysed in week 8) | CI consolidation phase 1 |

## 7. Executive view

For Victor Lindqvist and the board, five numbers, each with its pair beside it: contractual
availability against 99.9 percent with credits (entry 1); Sev1 and Sev2 with customer-detected share
(block); committed items delivered (entry 7); capacity by class, run, grow, improve, with dollars
(entry 6); and after-hours pages concentration as the one people measure (entry 9). Invoice
correctness is named as a blind spot in the report's risks until it has data. These are the measures a
board can act on; the rest stay in the director's monthly review.

## 8. Reply to Rajiv Menon

> Rajiv, you asked for output per engineer by team. I recommend we do not publish it, and I want to
> answer the question behind it: is the money going to the right places, and is it improving?
>
> A per-engineer figure would measure our architecture, not our people. Orders and Billing ship through
> the Core release, so their counts describe the train. Seven of Platform Operations' twelve people at
> baseline were QA engineers who did not deploy. The rates are too noisy to rank: every team's baseline
> change failure interval overlapped every other's. Once the figure is in a budget pack, teams raise it
> by splitting work, and we lose the measure.
>
> What I can show, quarterly from now: in quarter 2 we spent about 22.4 FTE ($1.04M) on unplanned work,
> down from 27.2 FTE ($1.26M) at baseline, and 12 FTE ($555,000) on prevention. Credits fell from
> $410,000 to $95,000. On those two lines alone, about $537,000 a quarter came back against $555,000
> spent, before the $9M of renewals. For quarter 3, prevention falls to 8 FTE ($370,000) and unplanned
> work is planned at 17.6 FTE ($814,000). If the week-31 sample shows unplanned work above 26 percent,
> prevention does not fall again. The first report on this basis comes with the quarter 3 close.

Check: 22.4 × $185,000 ÷ 4 = $1,036,000; 12 × $185,000 ÷ 4 = $555,000; $222,000 + $315,000 = $537,000;
8 × $185,000 ÷ 4 = $370,000; 17.6 × $185,000 ÷ 4 = $814,000.

## 9. Evaluation of Chapter 38's eight-entry scorecard

**Strengths.** Every row has a pair, a row owner, and a data steward; the quality block is included by
reference; the only target (availability) has a contractual reason; the hand-joined delivery data
carries a caveat; it stays at eight entries.

**Weaknesses, checked against the chapter's own rules.**

1. **Four of the seven other entries repeat the block.** Entry 1 is template row 1 and its pair is row
   3; entry 3 is rows 4 and 5; entry 6 is rows 7 and 8; entry 5's pair is row 9. "Do not copy the
   quality rows" is the chapter's own instruction. Copies drift: the template measures Core change
   failure, entry 3 measures it by component.
2. **Steward separation is broken twice.** Entry 7's steward is Platform Operations and its owner Tom
   Becker; entry 5's steward is Tom Becker, whose team's work is most of the 4.5 FTE platform category it
   measures.
3. **The owner of entry 3 cannot explain most of it.** Elena Sokolova's team does not ship through
   Core, and the week-26 report names Kwame Mensah, entry 3's steward, as owner of the Core change
   failure risk.
4. **Reliability is the contract alone.** No SLO row, though budgets are published weekly and a policy
   decision is pending; no invoice correctness; no security exposure, though a renewal customer asked
   for SBOM and SSDF evidence in week 3.
5. **No definitions, readings, or data status.** Entry 8's survey may not have run; entry 4's steward is
   a role nobody holds by name.

**Scored as a submission:** decision linkage 9 of 15; definitions 9 of 20; pairing 10 of 15; reliability
7 of 15; readings 4 of 15; ownership 5 of 10; executive view and Rajiv 3 of 10. Total 47, weak. That is
fair to a chapter case that sketches a structure for the reader to finish, and it shows what the
project adds: definitions with counts, the reliability section, and the separation rule applied.

**Other defensible answers.** Keeping change failure and deployment frequency inside the block and
using entry 5 only for lead time works if the block's definitions are by component. Dropping entry 10
and carrying security inside the quality block is defensible if the monthly quality review owns
exceptions. A scorecard that uses DORA's change failure definition only, from quarter 3, is defensible
if the break in the series is shown and the 72-hour figures are kept for two quarters.

## What a weak submission looks like

> "Northstar quarter 3 scorecard: deployments per engineer by team (target +20 percent), Sev1/Sev2
> below 10, change failure rate below 15 percent, availability 99.9 percent, line coverage 60 percent,
> story points per sprint, eNPS. Owners: each team's manager. We improved incidents by 43 percent
> from baseline."

Against the rubric: no decisions named (linkage weak); no definitions or sources, and hand-joined numbers
presented as fact (definitions weak); targets on mechanism measures with no pairs (pairing weak);
availability alone, no SLOs or correctness (reliability weak); "43 percent" from 30 to 17 with no
interval (readings weak); managers own and define their own numbers (ownership weak); a per-engineer
league table is exactly what the reply to Rajiv should decline (executive weak). It fails acceptance
criteria 2, 3, 4, 5, 6, 7, and 9.

**An adequate submission** adopts Chapter 38's eight entries, adds definitions and quarter 2 readings,
and declines Rajiv's request politely, but keeps the duplicated rows and the steward conflicts and
copies the percentages without counts. It scores in the 60s. **What separates excellent from adequate**
is starting from decisions, recomputing every number from its counts until the differing windows and denominators show,
and putting the blind spots on the scorecard as rows with no data instead of leaving them off.
