# Chapter 54 solutions — Data and AI Strategy

Worked solutions for the [chapter 54 exercises](../parts/12-cto-leadership/54-data-and-ai-strategy.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional.

## F1 — Readiness test on two datasets

| Question | Order and ledger data in the warehouse | The 400 labeled corrections |
|---|---|---|
| Owner of meaning | Not ready: no dataset has a named owner; Data and Analytics owns the pipelines | Partly: Data and Analytics wrote the corrected-order definition in week 40 |
| Definition | Partly: 38 of 212 tables described; revenue differs from Finance's close by 0.3 to 0.6 percent | Ready for its purpose: the week 40 definition is written and specific |
| Quality measured | Not ready: load failures found by inventory, not by monitoring (11 of 91 nights in quarter 3) | Partly: hand-classified once; no second classifier, no agreement check |
| Lineage and contract | Not ready: 29 pipelines read Core tables through read replicas; ADR-0001 open | Ready: derived from known sources in a known window |
| Permitted use | Not ready: personal data in 14 unclassified tables | Partly: the sample contains customer orders and has not been classified |

**First fixes.** For the order and ledger data, the ledger read contract that ADR-0001 is about, owned by
Li Na Zhou as standard owner for data, with a Billing owner for the meaning of ledger fields: it removes
the largest cause of broken loads (7 of 11) and is useful whatever happens to AI. For the labeled
corrections, make the corrected-order measure continuous and classify causes on a rolling sample, owned
by Farah Haddad, so labels accumulate.

A good answer cites the chapter's evidence for each rating and picks fixes with value beyond AI. The weak
answer rates everything "not ready" and proposes a company-wide data governance program, which has no
first step and no owner.

## F2 — Replying to the 55 percent slide

A model reply:

"Rajiv, the 55 percent comes from a controlled experiment in which developers wrote one small new program
(an HTTP server in JavaScript) from scratch; the group with the assistant finished 55.8 percent faster.
It is real evidence, for that kind of task. The largest randomized study, at three large companies with
4,867 developers, found about 26 percent more completed tasks, with a wide margin and bigger gains for
less experienced developers. A trial with experienced developers working in their own large, mature
codebases found them 19 percent slower, although they believed they were faster. Northstar's Core is a
1.4-million-line, 11-year-old system worked on by people who know it well, which is closer to the last
setting. None of these measured delivery to customers; DORA's survey associates rising adoption with lower
delivery stability. Before planning on any gain, we would need our own team-level delivery and stability
measures over a trial quarter. I propose one, with a decision date you can put in the plan."

Criteria: names the task and setting, places it among the other studies, distinguishes output from
delivery, and ends with an action and a date. The weak answer says "studies disagree" and stops, which
gives the CFO nothing to plan with; the other weak answer accepts the number because it is published.

## F3 — The 83 percent figure

34 of 41 is 83 percent of weekly users, not of engineers: 41 of 63 respondents use AI weekly, and 63 of
80 engineers responded, so the figure describes 34 of 80 engineers (43 percent) and a self-selected
group. More importantly, it measures perceived speed. In the one trial that compared perception with
measurement, developers believed they were about 20 percent faster when they were 19 percent slower, and
acceptance rates track perceived productivity rather than delivered output. The figure shows that
engineers like the tools, which matters for adoption and retention. It does not show that delivery
improved.

Report instead, by team:

| Measure | Pair |
|---|---|
| Median lead time for changes | Change failure rate (Core reported separately from the other services) |
| Median wait for first review on Core merge requests | Escaped defects confirmed per quarter |

Optionally add a developer experience survey across several dimensions, reported as such and never as a
productivity result. A good answer catches the denominator, names the perception gap, and pairs every
speed measure with a stability or quality measure. The weak answer replaces the survey with acceptance
rate or lines of code, which measures use, not value.

## A1 — Policy for analysis work

**Data rules.** No customer personal data, credentials, or production logs containing them enter any
external AI tool, including the approved one. Schema and SQL text may enter the approved tool; query
results may not, unless drawn from tables classified as containing no personal data. Personal chat
accounts are not used for Northstar data.

**What must happen first.** Classify the warehouse: tag the 14 tables holding personal data, create
views without the personal columns for analysis, and restrict raw tables to named roles. Until
classification is done, analysts may use the approved tool for SQL drafting only against schema, never
pasted results.

**Owners.** Li Na Zhou owns the data classes and their exemptions (decisions within 10 working days, as
her standard requires). Farah Haddad owns the warehouse classification and the views. Joon Park reviews
vendor terms. Marta Kowalczyk's IT team updates the acceptable-use policy for the analysts outside
engineering, who are not bound by an engineering policy.

**The six respondents.** The survey was anonymous and promised as a baseline; identifying people would
end honest answers. Instead, ask Joon Park to assess the exposure by tool (what the providers' consumer
terms say about retention), announce a one-time amnesty with a confidential route to report specific
incidents, and treat any customer data confirmed in a provider's retention as a security matter under the
normal process. Criteria: the answer covers analysts outside engineering, sequences classification before
permission, and protects the survey's integrity. The weak answer bans chat tools for analysts, which moves
the use to personal phones.

## A2 — The order assistant

**Analysis.** Data readiness: customers' emailed orders are not in any Northstar system today, so there
is no evaluation set; order and customer data fail on owner of meaning and permitted use. Differentiation:
turning an email into an order is likely to become a commodity feature of bought tools; what differentiates
is Northstar's catalog, pricing, and customer history, which the feature would draw on. Error cost: high.
A wrong order becomes a wrong invoice, a customer-visible financial record that Northstar's severity
definitions rate Sev1, and ordering errors are already the subject of a top-40 customer's complaint.
Evaluation: impossible until real emailed orders are collected with consent. Verdict: wait, with a
trigger, and a discovery step that builds the evaluation set.

**What to say to Greg.** "I want to help you win these deals, and I won't put a date on something we
can't test. Here is what I can offer: a two-week discovery with Keiko Ashworth and one of your customers to
collect real emailed orders and measure how often a draft would be right. A written statement for the two
prospects that we are evaluating assisted order entry, with the order-error work we are doing now, which
addresses the errors their peers complain about. And the order assistant goes on the portfolio forum's
list with a decision date after discovery, so it is sized against everything else, not slipped in."

Criteria: applies the readiness test and the error cost explicitly, offers something concrete without a
date, and keeps the request inside the portfolio process. The weak answer either refuses ("AI isn't
ready") or concedes a date "for the deals", which is the demo-driven commitment the chapter warns about.

## A3 — A better trial

**Rollout.** Randomize at team level within pairs matched on how they ship: Orders with Billing (Core
release train), Payments and Integrations with Customer Experience (services and frontends), Data and
Analytics with Platform Operations. One team of each pair starts in week 53, the other in week 60. Because
the year-2 reorganization, if approved, changes reporting lines in week 53 for both arms at once, its effect
hits both arms; the
comparison is within pairs, between arms, not before and after. If the proposal is approved, teams affected by moves (search-svc in
week 54, the Customer Experience split) are analyzed both with and without the moved components.

**Measures and pairs.** Lead time with change failure rate; first-review wait with review comments per
merge request; deployment frequency with escaped defects; blocked dependency findings on AI-assisted
changes as a security signal. A developer experience survey at weeks 52, 59, and 66.

**Decision rules, written in advance.** Full rollout if no pair shows a worse change failure rate or
escaped-defect count in the AI arm and at least two of three pairs show shorter lead time or review wait.
Stop or redesign if two pairs show worse stability. Decision date week 68.

**Detectable effect.** Three pairs over seven weeks can detect only a large effect, roughly a change
comparable to the quarter-to-quarter swings in Northstar's record (for example a Core failure rate moving from about
a quarter of releases to well under or well over), not a 5 percent gain. Say so in the proposal, so nobody
reads "no significant difference" as "no effect". A good answer handles the reorganization, writes the
rules first, and states the detection limit. The weak answer randomizes individuals within teams, which
contaminates both arms through shared code review.

## X1 — Victor's decisions

One defensible set of decisions:

| Proposal | Decision | Review trigger |
|---|---|---|
| Interim policy | Approve, adding a section for analysis work and IT's acceptable-use update for analysts | Six-month review; any confirmed customer data in an external tool |
| Trial | Approve with paired team randomization and decision rules written before week 53 | Decision date week 68 |
| Order checking | Approve stage 1 through the portfolio forum; stage 2 decided after a quarter of the corrected-order measure | Corrected-order rate after stage 1 |
| Order assistant | Wait; fund a two-week discovery to build an evaluation set | Evaluation set exists; a signed deal makes it a requirement |
| Support summaries | Approve, subject to Joon Park's review of terms | Terms review complete |
| Backfills | Accept: no backfills held on AI in the year-2 plan | Trial result at week 68 |

**To Rajiv.** "The backfill question comes back at week 68 with our own trial results, and if two of three
team pairs deliver faster with no loss of stability, I will bring you a revised plan that holds backfills
open from quarter 7. Until then, holding them would bet two engineers' work on a number we have not
measured."

**Questionnaire answer.** "Northstar permits the use of one approved AI coding assistant under an
enterprise agreement that prohibits the provider from training on Northstar data. Our policy prohibits
customer data, credentials, and production logs in any AI tool not covered by a reviewed enterprise
agreement, and in the coding assistant in all cases. AI-assisted code passes the same review and pipeline
controls as all other code. Customer Success's support ticketing system includes a summarization feature
provided by its vendor; it processes the content of support tickets, which can contain customer data, and
is enabled only after our security review of the vendor's data terms (retention, no training on customer
data, data location). Northstar's product does not currently include generative AI features." The answer
is true only after the policy is approved, the tool procured, and the support-tool review complete; until
the review is done, the support sentence must say the feature is not enabled. Before the policy exists the
honest answer is that a policy is being put in place, with the date. Answering "no customer data reaches AI
providers" while approving the support summaries would be exactly the overstatement the criteria warn
against.

Criteria: decisions with triggers, a dated answer to the CFO, and a questionnaire answer that does not
overstate. The weak answer approves everything as written or answers the customer as if the policy already
operated.

## X2 — Halvard's four assistants

**Governance.** One company AI stance, owned by the CTO and operated by the platform organization: a short
list of approved tools under enterprise terms (consolidate from four to one or two, which also gives
negotiating power), company data classes, and pipeline controls enforced by Halvard's existing enterprise
policy of an auditable pipeline. Each product group keeps choice inside the approved list. A principal
engineer in the technical direction function owns the AI policy, as other Halvard policies have an owning
principal engineer.

**Evaluation.** A company evaluation design, not four: team-level delivery and stability measures already
collected for the platform, staggered rollout where groups have not yet adopted, and difference-in-
differences comparisons where they have. Acceptance rate and survey data are reported as adoption and
experience, never as productivity.

**The vendor contract.** Tell the VP that acceptance rate and surveys measure perceived productivity, and
that the evidence includes a setting where experienced developers believed they were faster while being
slower. Ending one of the two contracts (about 30 engineers if the two are equal in size, an assumption Halvard's record does not fix) on that basis would remove capacity that cannot
be restored quickly. Offer a path: the contract's next renewal decision uses the measured result for that
group over two quarters, and the contract can be resized rather than ended.

**Avoiding a contest.** Report AI measures by group only alongside delivery and stability, never ranked;
set no AI adoption targets; compare each group with its own baseline. Criteria: consolidation with
ownership, one evaluation design, and a contract answer tied to measurement and reversibility. The weak
answer lets each group keep its tool and its metrics, which guarantees four incompatible success stories.
