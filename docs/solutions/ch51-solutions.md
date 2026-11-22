# Chapter 51 solutions — Enterprise Technology Strategy and the Three-Year Roadmap

Worked solutions for the [chapter 51 exercises](../parts/12-cto-leadership/51-enterprise-technology-strategy.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional.

## F1 — Rewriting a generic first paragraph

| Sentence | Genericity | Trace | Says no |
|---|---|---|---|
| "Reliable, secure, and modern" | True of every competitor's strategy | Traces to nothing specific; reliability is a contract term, not a choice | Rules nothing out |
| "Use data to drive decisions" | Generic | No business choice named | Nothing |
| "Invest in our platform and our people" | Generic | No capability named | Nothing |

All three sentences describe operational effectiveness, which Porter's essay separates from strategy.
A rewrite that passes uses the case's facts:

"Northstar's customers, mid-market wholesale distributors, choose us because we can be trusted with their
money. Our technology must therefore be excellent at three things: correct orders, invoices, and payments;
available order and payment paths; and clean integration with customers' accounting systems and banks.
We will hold our ordering screens and internal reporting at parity, buy tax content and delivery tooling,
and not rewrite Core, run multi-region active-active hosting, or maintain customer-specific code branches."

The genericity test now fails for a competitor that sells, say, warehouse software: the bins and the
"not doing" list are Northstar's. A good answer keeps at least one "not doing" item that a named person
wants (customer-specific branches, which Greg Tanaka wants). The weak answer replaces the slogans with
longer slogans ("world-class, resilient, cloud-native platform") and still rules nothing out.

## F2 — Placing items in horizons

| Item | Placement | Why |
|---|---|---|
| Core framework migration (120–180 engineer-days) | Horizon 1, committed in year 2 | Demand is certain (community support has ended, TR-01) and the work is understood; it sits in the estate-currency line |
| Idempotent order submission | Horizon 1, committed | Ordering correctness is now in the excellent bin; 70 of 340 sampled ordering errors were duplicate submissions; small and well understood |
| CI consolidation | Horizon 1, with an open decision | Demand is known (four systems cost about 1.5 FTE a year against about 0.5 for one); the target is not chosen, so the strategy books it for week 78 |
| Ledger posting events | Horizon 2, staged | Demand exists (integrations are part of how Northstar wins); design and size depend on ADR-0001 |
| Higher availability tier for top accounts | Horizon 3, probe | Neither demand (will renewals ask?) nor design is known; a 4 engineer-week costing study |
| Ordering API for distributors' largest buyers | Horizon 3, probe | An option on a future channel; no demand evidence yet |
| Multi-region active-active hosting | Drop ("not doing") | The contract is 99.9 percent, and nothing in the record attributes the misses to a regional failure: at baseline almost two thirds of serious incidents came from Northstar's own changes |

A good answer justifies each placement by what is known about demand and design, not by when the work
might happen. CI consolidation is defensible as horizon 2 if you argue the design is genuinely unknown;
say so. The weak answer sorts by date ("the API is far off, so horizon 3") or places the framework
migration in horizon 2 because it is large, which confuses size with uncertainty.

## F3 — Year 3 under two scenarios

Planned year 3 (79 engineers): unplanned 14.2 FTE (18 percent), horizon 2 14.0 FTE.

**Unplanned work at 22 percent.** 79 × 22% = 17.38, about 17.4 FTE, which is 17.4 − 14.2 = 3.2 FTE more
than planned. The stress rule takes the shortfall from horizon 2: 14.0 − 3.2 = 10.8 FTE, barely above
year 2's 10.0. Horizon 3 stays at 4.0 and prevention at 3.0. Implication for week 78: the stage 2 gate
will already show unplanned work not falling, so the multi-currency option, even if its assumption
holds, meets the "no capacity" branch of the decision diagram. Victor must name what it would displace
(probably ledger posting events, if ADR-0001 chose them) and take the choice to the executive team, or
hold the option with a new decision date.

**Unplanned work at 15 percent.** 79 × 15% = 11.85, about 11.9 FTE, releasing 14.2 − 11.9 = 2.3 FTE.
The draft has no upside rule, which is itself a finding. A sound rule: the released capacity goes first to
horizon 2 only if an option has passed its decision point, otherwise to product work for today's
customers for that year, so it is not spent on unexamined items. Horizon 2 could reach 16.3 FTE.

A good answer shows the arithmetic, applies the rule mechanically, and links the result to a specific
decision. The weak answer cuts prevention to protect horizon 2, which the policy forbids and which would
make the next year's unplanned work worse.

## A1 — The multi-currency option record

**Assumption, testable.** "By week 78, at least three of the largest 40 customers, or at least three
qualified prospects, state in writing that invoicing and settling in more than one currency is a
condition of renewal or purchase within year 3." The threshold is a judgment; what matters is that it is
written now.

**Probe, 6 engineer-weeks (about $21,000).** Two engineer-weeks with Greg Tanaka's and Sofia Alvarez's
teams to collect the evidence above; three engineer-weeks by a Billing ledger engineer and Li Na Zhou
to map what multi-currency requires in core/ledger and invoicing (currency per posting, revaluation,
rounding rules); one engineer-week to size a first stage.

**Evidence by week 78.** The customer statements; the design sketch with its dependency on the ledger
read path; a first-stage size in FTE-quarters.

**Decider.** Victor Lindqvist, with Helena Marsh, because it is tied to her year-3 growth question.

**Kill criterion.** Fewer than three written demands by week 78, or a first stage above 10 FTE-quarters
that cannot fit horizon 2 without cutting prevention.

**First stage if exercised.** Multi-currency posting in the ledger behind a contract, for one pilot
customer, gated at the end of the stage.

**Why ADR-0001 matters.** Every integration that reads ledger tables directly would break or mislead
once postings carry several currencies. If ADR-0001 is still open at week 78, the honest move is to make
its decision a condition of the first stage, not to start multi-currency on top of table reads. The
weak answer writes "decide at week 78" with no evidence named, or treats the probe as the first stage.

## A2 — Year-2 inputs for Victor's strategy

| Proposal | Horizon and calendar | Effect on the strategy |
|---|---|---|
| Year-2 organization (decision week 46) | Organization lane; review week 64 | Sets the planning basis: 79 engineers (main), 80 (B), 78 (C), 77 (D) |
| Quality continuation (executive team week 49) | Horizon 1 prevention; gates weeks 56, 78, 104 | Prevention of 5.5 FTE average in year 2, or 4 FTE plus 2 on deal features under Greg's option |
| Workforce plan (draft week 49) | Organization lane | Option C would need an exception to the 87-seat rule, changing the envelope |
| VP question (week 48) | Organization lane | A VP takes a seat: 78 engineers under the main proposal |
| CI target | Horizon 1 platform; week 78 | Stage 3's $100,000 of tooling depends on it |
| ADR-0001 | Policy 2; week 60 | Two horizon 2 options depend on it |

Two couplings matter most. First, the VP question and the organization proposal together move the
planning basis between 77 and 80 engineers; at 78 instead of 79, the year-2 total loses 1 FTE, and under
the stress rule that comes out of horizon 2 (10.0 to 9.0). Second, if the continuation goes with Greg's
4 FTE option, prevention falls by 2 FTE in quarters 5 and 6 and the risk that unplanned work stalls rises,
which threatens the whole reliability dividend.

**How to present them while open.** One planning basis (79), a sensitivity line for each open decision,
and the decision dates in the calendar. A good answer finds at least two couplings and quantifies one.
The weak answer lists the proposals without showing that their outcomes interact.

## A3 — Replying to Greg Tanaka

A worked reply from Victor:

"Greg, I am keeping 'no customer-specific code branches' in the draft, and I want you to see why. Our
customers trust us with their money; every branch is a second version of invoicing or ordering that we
must test, release, and support, and the incidents we have spent a year reducing came mostly from our
own changes. What we will offer instead: the custom behavior those two deals need, built as configuration
within the product where the portfolio forum agrees it serves more than one customer, with an engineering
estimate and a named owner before any date is given. I will revisit the policy if, within the next two
quarters, we lose a deal of top-40 size that configuration could not have won, and I will record your
objection with the draft so the executive team and the board see it."

The policy protects the excellent bin: correctness and safe weekly change. A good answer offers a real
alternative, names the evidence that would reopen the policy, and records the dissent rather than
burying it, consistent with Chapter 49's record test. It also routes the request through the existing
portfolio forum rather than a private agreement. The weak answer either drops the policy to win Greg's
support, which makes "not doing" decorative, or refuses without an alternative, which makes the policy
look like engineering convenience.

## X1 — The board document

**Order.** (1) The business choices, stating that the CEO confirmed the first two and placed growth
into larger distributors in year 3. (2) What technology must be excellent at, and what Northstar will
not do. (3) The three-year allocation by horizon, with the reliability dividend and the bad-year rule.
(4) The decision calendar, with the open decisions named. (5) What the strategy does not ask for: no
headcount, no spending beyond the $150,000 the continuation already proposes.

**First paragraph.** "This is a discussion item, not a request for approval. Northstar's technology
strategy for the next three years follows from one business choice: distributors buy from us because
they can trust us with their money. We will be excellent at financial correctness, availability of the
order and payment paths, and integration with our customers' accounting systems and banks, and we will
not rewrite Core or build customer-specific versions. Growth work is funded by reducing unplanned work
from 25 percent of capacity, not by adding headcount; if unplanned work does not fall, growth slows and
reliability does not."

**Open decisions named.** The year-2 organization, the continuation, ADR-0001, the CI target, and Helena's
year-3 growth question. Whether to name the VP question is a judgment; naming it as "management structure
under review" is defensible because it moves the capacity basis.

**What not to show.** Executives' private positions from one-on-ones and Greg's objection in his words
(record it, but present it as "a commercial objection to policy X, under discussion"); detailed option
records, which belong in the appendix. A good answer leads with choices and the ask (discussion), keeps
reallocated capacity separate from new money, and admits the dependency on unplanned work. The weak
answer presents a three-year Gantt chart for approval.

## X2 — A company-level strategy at Halvard

**The request in numbers.** 31 percent of 500 engineers is 155 for horizon 2, and 9 percent is 45 for
horizon 3, leaving 300 (60 percent) for horizon 1, including the 70-engineer platform organization and
each group's run work. Commerce alone assumes 32 FTE of run work; if the other groups are similar in
proportion, a 60 percent horizon 1 is probably too thin, so the first finding is that the sum of group
roadmaps exceeds what the company can carry.

**Structure.** One company document: business choices confirmed by the CEO, company-wide excellent and
"not doing" bins, three or four company policies (including the six existing enterprise policies where
they fit), the company horizon split, and the platform mandate. Beneath it, one group strategy per vice
president, derived from the company choices and tested with the same coherence tests.

**Allocating horizon 2.** Set the company total first (say 20 to 25 percent, a judgment), then allocate
it by option records that pass their decision points, ranked by cost of delay (Chapter 45), not by group.
A group with no passing option gets no horizon 2 that half-year.

**Avoiding partition dependence.** Bardolet and colleagues report that allocations tend toward equal
shares across however many units the firm is divided into. Countermeasures: allocate to options, not
groups; publish the ranking rule before submissions; show each group's share against the previous year,
so an even split is visible as a choice.

**The platform policy.** Converge, but stage it: adoption by tier 1 components first, with a decision
point after a year, rather than a two-year mandate for everything. A good answer quantifies the request,
separates company from group strategy, and names the even-allocation bias. The weak answer averages the
four requests or gives each group a quarter.
