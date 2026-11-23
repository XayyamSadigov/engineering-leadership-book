# Chapter 18 solutions — Measuring Engineering Productivity: DORA, SPACE, and Their Limits

Worked solutions for the [chapter 18 exercises](../parts/04-execution/18-measuring-engineering-productivity.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Updating an old "four keys" dashboard

**What changed.** DORA's current guide (last updated January 5, 2026) lists five metrics, not four, in
two groups. Throughput: change lead time, deployment frequency, and failed deployment recovery time.
Instability: change failure rate and deployment rework rate. "Time to restore service" has become failed
deployment recovery time, which is narrower: it covers recovery from a deployment that needed immediate
intervention, not every outage. Deployment rework rate is new: the share of deployments that are
unplanned and caused by a production incident.

**Decisions before comparing trends.** A good answer names them. What counts as a deployment (per
service? configuration pushes?). What counts as a failure, and within what window (Northstar uses 72
hours after a release; DORA speaks of immediate intervention). Whether outages not caused by a
deployment, which the old restore metric included, now get their own measure (they should: incident
recovery still matters). How to bridge the series: compute old and new definitions side by side for at
least one quarter, mark the change on the chart, and never draw one trend line across it.

**Decision.** Report the current definitions from next quarter, because they are what the published
benchmarks and any new tooling will use. For the bridging quarter, show old and new values side by side
with the difference explained, then retire the old series and keep it archived for reference. A good
answer commits to a definition and a date rather than leaving both running indefinitely.

**Weak answer.** Renaming the labels and keeping the old calculations, which produces a dashboard that
claims DORA's definitions while measuring something else.

## F2 — "DORA proved that deploying more often reduces failures"

**What the evidence supports.** DORA's findings come from an annual survey of self-selected
professionals (nearly 3,000 in 2023), who report their own delivery performance. Constructs are
validated statistically and relationships are tested with structural equation models that try to
account for confounders. Across many organizations, those reporting faster delivery also tend to report
more stable delivery. That is strong evidence that speed and stability are not necessarily a trade-off.

**What it does not support.** That increasing deployment frequency, by itself, causes fewer failures in
your organization. The data are self-reported and correlational within each year, and the plausible
mechanism (smaller batches, faster diagnosis, easier rollback) depends on practices that usually come
with frequent deployment. A target of daily deployments for every team ignores the guide's warning that
goals invite gaming; the cheapest way to hit it is splitting or empty deploys.

**How to test it locally.** Pick a component where batch size can actually shrink, record a baseline
quarter of deployments, changes per deployment, and change failure rate with event counts, then change the
cadence and compare, alongside a component that did not change. Northstar's Core move to weekly releases
(change failure rate 31 to 22 percent) is consistent with the claim but confounded: contract tests and
flaky-test quarantine arrived in the same quarter.

**Weak answer.** Either accepting "proved", or dismissing DORA entirely because it is a survey.

## F3 — Reporting change failure rate by team

**What one quarter supports.** Very little between individual teams. With 24 to 78 deployments per team
in a quarter, the plausible ranges (95 percent intervals) in the chapter's table are wide (Billing 18 to 53 percent, Data and
Analytics 5 to 27 percent), and every team's interval overlaps every other's. The data are consistent
with the teams that ship through the Core train failing more often, which the incident data and the
mechanism support independently, but the rates alone do not rank teams.

**What it cannot support.** Statements such as "Customer Experience is safer than Payments and
Integrations" or any color-coded ranking. The baseline definition also undercounts: failures are linked
to releases by hand within 72 hours, so unlinked failures are missed, and the four shell-script services
are estimates.

**How to present it.** Show failures and deployments as counts ("8 of 24"), with the rate and an
interval or a rolling two-quarter window. Group teams by delivery path (Core train or independent
services) rather than ranking them. Put deployment frequency beside the rate, so that a team protecting
its rate by deploying less is visible. Footnote the definition and its known undercounting. Ask each team
to compare with its own previous quarters.

**Weak answer.** A sorted bar chart of six percentages with no counts.

## A1 — "Pull requests per engineer, just for visibility"

**Decision.** Do not add it. A per-engineer count shown on a team dashboard is an evaluation whether or
not anyone says so: people see their position and adjust. Daniel's two seniors who review and coordinate
mobile releases would rank lowest while doing some of the most valuable work, and the cheapest way for
anyone to rise is to split changes.

**What to say.** Start with Daniel's problem: "What do you want to see that you can't see now?" Often it
is that work is stuck, someone is overloaded, or reviews are slow. Then: "A per-person count will show the
seniors at the bottom for doing the reviews the team depends on, and it will make pull requests smaller
without making delivery faster. I'd rather we see the system."

**What to offer.** Team-level measures that answer the likely question: median wait for first review,
pull-request size distribution, time from open to merge, and work items open longer than a set age. For
individual concerns, use one-on-ones and the performance process (Chapter 9), where context exists.

**Criteria.** A good answer refuses the metric, explains the mechanism (invisible work, gaming), and
offers a substitute tied to Daniel's actual need. **Weak answer:** allowing it "with a caveat", or refusing
without asking what problem Daniel is trying to solve.

## A2 — Designing the first developer-experience survey

**Structure (about 15 questions).** Feedback loops: how often waiting for review blocks you (pair: median
first-review wait, 21 working hours at baseline); how often the Core pipeline or a broken main branch
blocks you (pair: 74-minute pipeline, main-branch red time); how much you trust test failures (pair:
failures unrelated to the change). Cognitive load: whether you know who owns the code you change (pair:
components with clear owners); whether you can find how to operate a service (pair: runbooks); how hard
it is to make a safe Core change. Flow: how often unplanned work interrupts planned work (pair: unplanned
work share, 34 percent at baseline); after-hours interruptions (pair: paging data). Satisfaction: tools,
sustainability of workload, whether you would recommend the team. One open question: the one friction to
remove first.

**Rules.** Anonymous; results reported only for groups of five or more, so the three staff engineers are
combined with another group and the seven former QA engineers, now spread across four teams, are never
reported as a group. Teams see their own results; the director sees team-level results; executives see
organization-level results. Results return to teams within two weeks with one or two chosen actions.
Commitment in writing: results are never used in performance ratings or managers' objectives.

**Criteria.** Every question maps to a dimension and, where possible, a system measure; anonymity rules
handle small groups. **Weak answer:** a long satisfaction survey with no pairs and no commitment about use.

## A3 — Deployment frequency doubled, lead time unchanged

**Probable explanation.** The deployment count has become a target, formally or informally, and teams
are deploying more without changing more: splitting changes, redeploying unchanged artifacts, or pushing
configuration-only deployments. Lead time per change unchanged and a rising share of deployments with no
code change point that way. There are innocent explanations to rule out first: automated dependency
updates, a pipeline that now redeploys on every configuration change, or a new flag system whose
toggles are counted as deployments.

**Confirming without accusation.** Treat it as a measurement question, not a conduct one. Break the
deployments down by type (code change, configuration, redeploy of the same version) and by trigger
(human, automation). Then ask the two teams what changed in how they ship. If someone has been telling
them their numbers matter, that is the finding, and it is a leadership problem, not theirs.

**Design changes.** Count deployments that carry at least one new change separately from other
deployments; report changes per deployment beside frequency; make lead time per change the headline
throughput measure; remove deployment frequency from any team goal; add the pattern to the metric's
documented gaming paths.

**Weak answer.** Reprimanding the teams, or celebrating the doubling in the next executive update.

## X1 — Reply to the CFO's request

**One worked answer (outline).**

*Your question:* whether 80 engineers are being used well, given 41 percent of committed roadmap items
delivered on time in the baseline quarter and flat operating expense.

*What I will provide, from the end of quarter 2:* (1) where engineering capacity goes, by category:
features, prevention (12 FTE), unplanned work (34 percent at baseline, 31 percent after the first quarter);
(2) delivery trends at organization level (Core releases, change failure rate, recovery time);
(3) commitments delivered against plan; (4) outcomes of the largest investments, including the two
renewal commitments and service credits.

*Why not a per-engineer number:* it would mostly measure which teams ship through the Core release train,
not how well people work; it would reward splitting work and penalize reviewing and incident response; and
once in the budget pack, it would rise without any change in output, so finance would be paying for a
number that misleads.

*What I need from you:* agreement on the format; the six engineer-weeks to build the shared
deployment-event store; and which cost categories finance needs, so the capacity view maps to the budget.

**Criteria.** A good reply takes the board's question seriously, answers it with something usable, gives
reasons in business terms, commits to a date, and asks for something specific. It acknowledges the CEO's
support without arguing with her. **Weak answers:** a lecture on Goodhart's law, or providing the number
"with caveats".

## X2 — Buying an engineering-analytics platform

**Numbers.** Building: about six engineer-weeks, roughly 6/52 × $185,000 ≈ $21,000 of Platform Operations
time, plus ongoing maintenance. Buying: $90,000 a year, recurring, from a $250,000 discretionary budget
that also has to fund other tooling. Neither option makes the four shell-script services emit events; that
needs pipeline work either way.

**A defensible recommendation: build, with a time box.** The organization needs one deployment event from
every pipeline regardless, the build cost is a fraction of one year's licence, and a tool whose default
views rank developers carries a cultural risk that a contract clause only partly removes. Buying is also
defensible if Platform Operations has no capacity this quarter; then set conditions: per-person views
disabled at the administrative level and audited, data retention and access rules agreed with HR, a
one-year term with exit, and no use of its outputs in performance management.

**What would show you were wrong after one quarter.** For building: the store is not producing trusted
numbers for most deployments by the end of the quarter, or the work has taken more than twice the
estimate. For buying: per-person views reappeared or were requested by managers, or the data still needed
hand correction.

**Weak answer.** Choosing on the feature list alone, without the cost comparison or the culture risk.
