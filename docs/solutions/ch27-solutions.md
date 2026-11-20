# Chapter 27 solutions — Quality Transformation at Enterprise Scale

Worked solutions for the [chapter 27 exercises](../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Classifying the incidents

**Classification.** From `incidents-last-quarter.csv`:

| Trigger | Count |
|---|---|
| Core release train (`monolith-release`) | 9 |
| Third-party dependency or capacity | 6 |
| Configuration change | 5 |
| Latent defect | 4 |
| Database migration | 3 |
| Service deployment | 2 |
| Not determined | 1 |

Detection: 14 by customers, 11 by monitoring, 5 by engineers. Recurrences: 11 of 30.

**The largest single intervention** is the one aimed at the release train: 9 incidents, 30 percent of
the total, with the longest restoration times. If it fully worked it would remove more incidents than
any other single change. A strong answer notes that "fully worked" is generous: shrinking batches and
automating checks will not prevent every release-borne incident, so the realistic gain is some
fraction of nine.

A good answer also separates **incident count** from **incident cost**. Detection work (user-facing
alerts) would not prevent any of the 30 incidents, but it would shorten the 14 customer-detected ones,
whose median detection time is 108 minutes against 6 for monitoring. If the mandate is availability,
that shortening is worth a great deal.

**On extending the manual pass to five days.** The case study records that the existing three-day
pass caught none of the nine train-borne incidents. Extending it lengthens the release cycle, so each
release carries more changes, takes longer to diagnose when it fails, and rolls back more work. The
proposal would probably increase the damage per incident. The weak answer accepts that "more testing"
is always safer without asking what the testing catches and what it costs in batch size.

## F2 — Gaming the proposed scorecard

| Proposed measure | How it is gamed | Replacement or pairing |
|---|---|---|
| Line coverage | Tests that execute code without meaningful assertions; coverage of trivial code | Drop as a target. Track escaped defects by detection point, and review a sample of new tests for assertions |
| Bugs closed per sprint | Close duplicates and trivial bugs; split one bug into several; close without fixing | Defect inflow (new escaped defects per week) and reopened-bug rate |
| Incident count | Reclassify incidents to a lower severity; merge related incidents | Pair with customer-detected share and with a weekly audit of severity decisions against written, impact-based definitions |
| Number of releases | Release empty or trivial changes | Pair deployment frequency with change fail rate and lead time; frequency alone means nothing |
| Postmortems written | Write short, shallow reviews; review only easy incidents | Follow-up action closure rate and recurrence rate of reviewed failure modes |

A good answer is specific: it names the behavior a team would adopt, not just "it can be gamed". It
also notices that four of the five proposed measures count **activity** (things closed, written,
released) rather than **outcomes** (fewer defects reaching customers, faster recovery), and that
activity measures are the easiest to inflate. The weak answer replaces every measure with a different
single number and does not pair anything.

## F3 — Interpreting a fall from 30 to 24

**What the number can tell you.** The count fell. If nothing else had changed, a fall of six would be
mildly encouraging.

**What it cannot tell you.** Incidents are rare events, and quarter-to-quarter counts are noisy. A
rough rule: if incidents arrive independently at a steady rate, a quarter with an expected 30 will
often produce anywhere from the low 20s to the high 30s by chance alone (the standard deviation of a
Poisson count is the square root of its mean, about 5.5 here). A fall to 24 is about one standard
deviation and is well within ordinary variation. The count also depends on classification, which is
exposed to gaming once a scorecard exists.

**Other evidence to ask for:**

- The severity distribution, including Sev3, and an audit of a sample of severity decisions.
- Customer-detected share and service credits, which are harder to reclassify.
- Mechanism measures with many underlying events: Core change fail rate (dozens of releases), main
  branch red time and pipeline failure rate (hundreds of runs), lead time (thousands of changes).
- Recurrence: did reviewed failure modes come back?
- Unplanned work share, which should fall if fewer things are breaking.

A good answer says "encouraging, not conclusive", explains why with a reason about sample size, and
names the faster, higher-volume signals. The weak answer either declares victory or dismisses the
number entirely.

## A1 — The Billing conversation

**Learn first.** Marcus may be right about something you cannot see in the data: which two roadmap
items are behind and why, how burned out the three people carrying on-call are, and whether he
believes the incidents are his team's to fix. Ask what his team spends its unplanned time on and
what he would do with a quarter of capacity if the choice were his.

**Bring data.** Billing had 8 of the quarter's 30 incidents and 58 escaped defects, the most of any
team, and spends 41 percent of capacity on unplanned work. Seven of its eight incidents came through
Core releases or migrations, so prevention work directly reduces the interrupts his team suffers. Put
it in his terms. At 41 percent unplanned, Billing has about 7.7 of its 13 engineers for planned work.
In quarter 1 the 25 percent allocation takes that to about 4.4, which is the cost he is objecting to,
and he is right that it is large. If prevention brings his unplanned work down to 25 percent by
quarter 4 and the allocation falls to a 10 percent maintenance level, Billing has about 8.5 engineers
for planned work, more than today, and his on-call engineers get their nights back. If unplanned work
only falls to 33 percent, he ends roughly where he started on capacity, with fewer incidents.

**Willing to change:** what the allocation is spent on (Marcus and his team choose the specific
prevention work, within the constraint and detection priorities); the ramp (for example 20 percent in
the first month, 25 after); renegotiating one of his two late roadmap items with product on his
behalf.

**Not willing to change:** that Billing takes a larger prevention share than the teams carrying
renewal commitments, because Billing carries the largest share of the inflow; and that his team owns
its incident follow-ups.

A strong answer treats the morale concern as real (low morale and high unplanned work are linked)
and frames prevention as relief rather than as process. The weak answer either concedes or simply
asserts authority.

## A2 — The QA transition

A workable design:

1. **Principle.** The seven QA engineers hold product knowledge that the organization needs; the
   work changes, the people stay.
2. **Target role.** Each QA engineer joins a product team as a quality engineer: owns the team's test
   strategy for its risk areas, leads exploratory testing on risky changes, turns the highest-value
   manual cases into automated checks with the developers, and reviews the escaped-defect
   classification for the team.
3. **Placement.** Match by product knowledge and defect load, as Northstar did (Chapter 19): two to
   Orders, two to Billing (highest defect load), two to Customer Experience, and one to Payments and
   Integrations. Platform Operations and Data and Analytics receive none, which is acceptable
   because the regression pass Platform Operations ran is being retired and the data team's risks
   sit mostly in migrations, which Li Na Zhou's work covers.
4. **Skills.** Pair each with a developer for automation work; fund a short training budget; set
   expectations that automation skill develops over two quarters, not two weeks.
5. **Reporting.** Each moves to the team's engineering manager, with a quality guild led by Tom Becker
   for practice-sharing and career growth.
6. **People who do not want the role.** Offer an internal move (support engineering or product
   operations are common fits), with a decision window of about a month. Be honest that the manual
   regression role itself will not exist in two quarters.
7. **Announcement.** Before the automation work starts, not after. The director announces it to the
   QA group in person first, then to the managers, then to engineering. The case study shows the cost
   of announcing late.

A good answer protects knowledge, gives each person a credible path, is honest about what ends, and
gets the timing right. The weak answer either keeps the manual pass to protect jobs or automates it
and leaves the people to work it out.

## A3 — The memo to the CPO

A strong memo fits on a page and leads with the decision:

> **Decision needed by 15 January:** agree a quarter 1 feature capacity reduction of about 21 percent,
> recovering to baseline by quarter 3 and to about 13 percent above baseline by quarter 4.
>
> **Why.** Thirty Sev1 and Sev2 incidents last quarter, 99.62 percent availability against a 99.9
> percent commitment, $410,000 in service credits, and $9M of renewals at risk. A third of engineering
> capacity is going to unplanned work. That capacity is already lost to the roadmap.
>
> **The trade.** We move 12 engineers' worth of capacity to prevention in quarters 1 and 2, mainly on
> the Core release process, alerting on the order and payment paths, and ownership of unowned
> components. Feature capacity: 41.6 engineers in quarter 1, 45.6 in quarter 2, 54.4 in quarter 3,
> 59.6 in quarter 4, against 52.8 today.
>
> **What you keep.** Both renewal commitments keep their dates; Orders and Payments carry a smaller
> prevention share for that reason.
>
> **If it works less well.** If unplanned work only falls to 26 percent, quarter 4 feature capacity is
> about 53 engineers, equal to today, and incidents are still down. We will show you the model every
> month and stop or resize the allocation if quarter 2 shows no movement in change fail rate or
> customer-detected incidents.
>
> **What I need from you.** Agreement to the quarter 1 dip, and help choosing which three roadmap
> items move to quarter 2.

What makes it work for a skeptic: it admits the cost, gives a pessimistic case, protects what she
cares about most, sets a date at which she can stop it, and asks for a specific decision. The weak
memo argues for quality in general and hides the dip.

## X1 — "Zero Sev1 incidents"

**In the meeting (about 100 words):**

> I understand the intent and I share it: Sev1 incidents are costing us customers and credits. I
> will not accept zero as the target, for two reasons. No organization running software at our scale
> achieves it reliably, so we would be committing to a number we will miss. And when a number cannot
> be met, people learn to classify incidents so that it is met, which would hide exactly the problems
> you want to see. I will bring a proposal to the next meeting for targets we can be held to, and I
> would like to be held to them.

**The follow-up note** should propose tracking:

- Availability on the contractual paths against the 99.9 percent commitment, by quarter, with service
  credits paid. This is the commercial measure.
- Sev1 and Sev2 incidents per quarter, with the trend and an explicit reduction goal (for example
  halving over twelve months, as in the mandate), reported with uncertainty.
- Share of incidents first detected by customers.
- Recurrence: share of incidents that repeat a failure mode already reviewed.
- A short narrative of the largest incident each quarter and what changed as a result.

The rationale: these measure customer impact and organizational learning, they are harder to game
than a count, and they give the board earlier warning than a binary target would. The Google SRE
book's argument that 100 percent reliability is rarely the right target, and that reliability should
match the risk the business is willing to take, is a useful reference for board members who want the
reasoning behind error budgets.

## X2 — Observability platform or CI consolidation

**Recommendation: Option B, CI consolidation, with a cheap detection workstream alongside.**

Reasoning from the baseline:

- The constraint is the Core release train and change safety: 19 of 30 incidents were change-induced,
  9 through Core. CI consolidation addresses the mechanism that produces most of the inflow: it lets
  Core and the four script-deployed services ship through one auditable pipeline with automated
  rollback, and makes pipeline measures comparable.
- Four services deploy through hand-maintained scripts that one person understands, and three of them
  are tier 1 or tier 2 with partial or no alerting. That is concentration risk as well as quality risk.
- Option A addresses detection, which is real (14 customer-detected incidents), but much of the
  detection gain can be captured cheaply in the first month with user-facing alerts on tier 1 paths
  using existing tools. The first-year cost of Option A ($240,000) also consumes almost the entire
  $250,000 discretionary budget.
- Option B costs four engineers for two quarters, about $370,000 of existing capacity at $185,000 per
  year, which is inside the capacity model as prevention work rather than new spend.

**What you give up:** a better investigation experience during incidents, cross-service tracing, and
some speed of diagnosis for the dependency-driven incidents (6 of 30).

**What would change your mind by the end of quarter 1:** if customer-detected share does not fall
after the cheap alerting work, or if time to restore is dominated by diagnosis time rather than
detection or rollback time, the case for a better observability platform strengthens, and it becomes
the quarter 3 investment with a business case to the CFO.

A strong answer ties the choice to the constraint, counts the cost of both options in the same units,
and states a falsifiable condition for revisiting it. Option A is defensible if the answer shows that
diagnosis time dominates restoration time; the weak answer picks either option on general principle.
