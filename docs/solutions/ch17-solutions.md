# Chapter 17 solutions — Predictability and Managing Uncertainty

Worked solutions for the [chapter 17 exercises](../parts/04-execution/17-predictability-and-managing-uncertainty.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — The eight-week promise

**The single-point plan.** The 26 weeks sum to 133 items, a mean of 5.1 a week. Forty divided by 5.1
is 7.8, rounded to "eight weeks."

**The simulation.** Drawing weeks at random from the 26, with 10,000 trials, gives a median of 8
weeks, an 85th percentile of 9, and a 95th percentile of 10 (reruns may differ by a week). The
eight-week date is met in roughly 60 percent of trials. So the product lead's date is not wrong; it
is a coin flip with slightly better odds, presented as a plan. The honest statement is "eight weeks
is about 60 percent likely; nine weeks is about 85 percent likely."

**Assumptions most likely to fail for Orders.** A strong answer names specific ones. The system is
changing: Orders takes on core/customer in week 4, receives two quality engineers, and gives 10
percent to prevention work, so history overstates future planned throughput. Weeks are not
independent: a release-train regression tends to cost more than one week. And 40 items is the current
breakdown; Orders' features have grown 15 to 35 percent after starting.

**Weak answer.** Running the simulation and reporting the 85th percentile as the answer without
questioning whether the history still describes the team.

## F2 — Forecast, target, or commitment

**Amara Okafor to the board: "bulk ordering ships by the end of quarter 2."** A commitment, and it
should be one: a renewal depends on it. What is missing is the scope. A good answer says the
commitment should name the contractual scope (the 44 items, or whatever was agreed with the
customer) so that growth beyond it does not silently become part of the promise.

**Greg Tanaka to a prospect: "we expect the export feature in quarter 3."** Worded as a forecast,
received as a commitment. A prospect hears a date. Unless engineering has forecast it, it is not even
a forecast; it is a target in forecast's clothing, made by someone who does not own the work.

**Priya Raman to her team: "let's aim to finish the upload rework in four weeks."** A target, and
legitimately so: internal, motivating, owned by the manager. It becomes a problem only if it is
reported upward as a date.

**The engineer: "probably two weeks, if the pricing service holds up."** A forecast with an explicit
risk, which is good. It lacks a probability and a plan for retiring the risk; a spike on the pricing
service would turn the condition into knowledge.

**Weak answer.** Labeling everything with a date a commitment. The criterion is who relies on it and
what happens if it is missed.

## F3 — Four engineers from Data and Analytics

**Assess against the mechanisms, not the slogan.** Brooks's law is commonly stated as a law, but the
useful part is its mechanisms: ramp-up time, communication overhead, and indivisible work.

- **Ramp-up.** Data and Analytics engineers work on reporting-api, export-svc, and warehouse
  pipelines. Bulk ordering lives in core/order-capture and pricing-svc. They do not know the code,
  the Core release train, or the bulk-upload failure history (INC-421). With ten weeks left, a
  three-to-four-week ramp-up consumes a large share of the remaining time.
- **Overhead.** Orders' most experienced engineers would onboard them, and those engineers are
  likely on the critical path.
- **Divisibility.** Some work may divide well: test data generation, export of bulk orders to
  reporting, load-test harnesses. That is where outside help can go.
- **Cost elsewhere.** Data and Analytics loses a third of its engineers for a quarter; its own
  commitments move.

**What to do instead or in addition.** First, find out why the forecast slipped: scope growth (cut or
move it to a follow-up release), a technical surprise (a focused spike), or throughput (look for
interrupts to shield the team from). Second, if help is needed, take one or two people who already
know order-capture, if any exist elsewhere in the organization, and give them
divisible work. A good answer ends with a decision rule, not a blanket yes or no.

**Weak answer.** "Brooks's law says no." It is expert opinion, and late help to divisible work by
people who know the code can work.

## A1 — Retiring risk on the accounting integration

**The uncertainties.** Can erp-sync talk to this customer's accounting system at all (authentication,
API limits, data model)? Do Northstar's invoice and payment records map onto the customer's chart of
accounts without manual steps? What will the customer's finance team actually do with the integration
(nightly batch or near real time)? Only after these is "how long will it take" a sensible question.

**Week 1: spikes.** One spike against the customer's sandbox: authenticate, post one invoice, read it
back, measure limits. A second, smaller one on the data mapping, done with Li Na Zhou, the staff
engineer for data and integration. Output of each: a written decision, not code.

**Weeks 2 and 3: walking skeleton.** One invoice flows from core/invoicing through erp-sync into the
customer's sandbox and a confirmation flows back, deployed through the real pipeline with a contract
test at the erp-sync boundary. Nothing is complete; everything is connected.

**Experiment with the customer.** Show the customer's finance team the skeleton's output for ten real
invoices in week 3 and ask them to reconcile it. Their reaction tests the assumption about how the
integration will be used.

**When to report confidence.** At the end of week 3, with the risks retired or named, run a
throughput forecast on the broken-down backlog and tell Amara Okafor the 85th and 95th percentile
dates against week 19. Before then, report progress on risks, not a date.

**Weak answer.** A plan that starts with building the full mapping layer and reaches the customer's
system in week 12.

## A2 — Quarterly planning for quarter 3

**Start from the reference class.** Open planning with the record: 28 of 66 committed items delivered
in quarter over the last four quarters, and why the 10 baseline misses happened (growth, dependencies,
incidents). The point is not blame; it is to make the outside view the default.

**Capacity first.** Each team brings its throughput history and current unplanned share. Plans are
built on demonstrated throughput after unplanned work and the prevention allocation, never on nominal
headcount.

**Forecasts, not estimates.** Each candidate item is sliced and forecast with Monte Carlo, including
historical growth. Items with unretired technical or integration risk enter as discovery work with a
time box, not as dated items.

**Two lists.** External commitments: few, each at the 85th or 95th percentile, each owned by a named
person (the director for engineering, Amara Okafor for the customer promise). Targets: everything
else, published as such.

**Who may commit externally.** Only Amara Okafor or the director, and only from an engineering
forecast.

**The "our work is unique" objection.** Grant what is true: if the work really is new, history is a
weak guide, and the answer is a wider range and early risk work, not a confident estimate. Then ask for
the team's own record on its last "unique" items. Most teams' unique work is unique in content and
ordinary in how it slips.

**Weak answer.** A better estimation template. The problem was never the quality of estimates.

## A3 — The week 18 update

**Order matters.** Lead with the commitment, because that is what Amara is accountable for: "The
contractual scope, the 44 items agreed with the customer, is forecast at 93 percent by week 26." Then
the news: "The full 60-item version is now 62 percent likely by week 26. The extra 16 items came from
splitting and discovery after we started; here is what they are."

**Options, each with a forecast.**

1. Ship the contractual scope in week 26 and the remaining items in a follow-up release, with its own
   forecast (for example, week 29 at 85 percent).
2. Cut the lowest-value of the 16 items now; for example, dropping 6 raises the chance for the rest.
3. Keep everything and accept the risk; say plainly that this is a 62 percent bet.

**Recommendation.** Option 1, plus an early conversation with the customer about what the follow-up
contains, led by Amara with engineering present. A customer told in week 18 about a planned
follow-up is in a different position from one told in week 25 about a slip.

**For someone burned before.** Show her the weekly trend of the forecast since the start, so she can
see this is the forecast moving, not a surprise. Commit to the next update date.

**Weak answer.** Reporting "on track" because the 44 contractual items are on track, and letting the
extra 16 surprise everyone at the end.

## X1 — A dated annual roadmap for the board

**What to present.** Three tiers on one page. Commitments: the few items the company has promised
externally or that the strategy cannot do without, each with a date at 85 to 95 percent confidence
and a defined scope. Forecasts: the remaining roadmap items as quarter ranges ("most likely Q2, 85
percent by Q3"). Targets: ambitions that the plan does not yet support, labeled as such.

**How to express confidence.** Give the board the organization's own track record: four quarters of
42 percent delivered as committed, the change in planning method, and from then on, calibration: "of
the forecasts we made at 85 percent, 9 of 11 came true." Calibration is what makes a range
trustworthy.

**Handling the wish for certainty.** Acknowledge it: boards need to plan cash, hiring, and customer
messaging. Offer certainty where it can honestly exist (the short commitment list) and a quarterly
update cadence for the rest. Point out that twelve dated commitments at Northstar's historical rate
would mean about seven missed, and that each miss would cost more credibility than a range does now.

**Criteria for a good answer.** It neither refuses the request nor accepts it as framed, it uses
numbers, and it gives the board something it can track.

**Weak answer.** Twelve dates with private padding. The board will discover the padding or the
misses, and either one costs trust.

## X2 — A policy for external dates

**Who can commit.** Product leadership (Amara Okafor) commits on the company's behalf; sales may
communicate commitments but not create them. Engineering's director signs off that a forecast exists.

**On what evidence.** A Monte Carlo or reference-class forecast that includes historical scope growth,
made after the item's technical and integration risks are retired or explicitly accepted.

**At what confidence.** 85th percentile for ordinary deal-related dates; 95th for contractual or
renewal-critical dates. Before the evidence exists, sales may say "we are actively working on it and
will have a date by" a stated day, which is itself a small commitment the team can keep.

**When a forecast crosses a committed date.** The owning manager raises it within a week, with
options; product decides; sales tells the customer early.

**How to know it works.** After two quarters: share of external commitments met (expected near the
confidence level, not 100 percent), calibration of forecasts, time from deal request to forecast, and
sales' view of whether deals stalled for lack of dates. Watch for gaming: if commitments are met at
100 percent while few are made, the confidence bar is too high or sales has stopped asking.

**Weak answer.** Banning external dates. Deals that need dates will get them from someone, without
a forecast.
