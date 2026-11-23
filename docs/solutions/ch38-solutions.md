# Chapter 38 solutions — Scorecards, Quarterly Planning, and Capacity Allocation

Worked solutions for the [chapter 38 exercises](../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Rebuilding a peer's scorecard

**Remove** lines of code per engineer (rewards volume, measures individuals, says nothing about
outcomes; Chapter 18 explains why individual productivity scoring is refused), story points per team
(points are a team's private estimating unit and inflate when compared), and test line coverage as an
organization row (it says how much code runs, not whether tests would fail; it belongs, if anywhere, in
a team's diagnostic view).

**One rebuilt version, seven entries:**

| Measure | Pair | Owner role |
|---|---|---|
| Contractual availability or main customer outcome | Customer-detected share | Director (row), reliability staff engineer (data) |
| Quality block, by reference to the quality scorecard | As defined there | As defined there |
| Deployment frequency | Change failure rate | A manager (row), platform team (data) |
| Committed items delivered | Forecast calibration | Director |
| Capacity by category against plan | Unplanned share by team | Director (row), time-sampling owner (data) |
| Sev1 and Sev2 count (in the quality block if it exists) | Customer-detected share and a severity audit | Incident process owner |
| Engagement or survey items on feedback loops | After-hours pages, regretted attrition | A manager (row), survey administrator (data) |

eNPS can stay if it has changed a decision; most organizations find team-level survey items on
specific friction more actionable. **Criteria:** every row has a pair and two named roles; removals are
explained by what the measure rewards, not by taste. **Weak answer:** keeping all seven and adding
owners, which leaves three rows that invite gaming.

## F2 — Sensitivity of the commitment line

Start from the cautious case: 44.5 FTE of product capacity after the bulk-ordering reserve, divided by
1.25, gives 35.6 FTE-quarters of committable estimated effort.

**Growth allowance 1.35:** 44.5 ÷ 1.35 = 33.0. The commitment falls by 2.6 FTE-quarters (about 34
engineer-weeks). The planned-case ceiling falls from 39.4 to 49.3 ÷ 1.35 = 36.5.

**Cautious unplanned 30 percent:** 0.30 × 80 = 24.0 FTE; product = 80 − 24.0 − 8 − 4.5 = 43.5; after
the 0.6 reserve, 42.9; ÷ 1.25 = 34.3. The commitment falls by 1.3.

**Both:** 42.9 ÷ 1.35 = 31.8.

The growth allowance matters about twice as much here: a 0.10 change in the allowance moves the line as
much as about four points of unplanned work. The lesson is that estimate growth, which most plans
ignore, deserves as much measurement as unplanned work. A strong answer proposes measuring growth per
team from completed items, since the 15 to 35 percent range is Orders' history, not the organization's.
**Weak answer:** recomputing correctly but drawing no conclusion about which input to improve.

## F3 — A key result on deployment frequency

Goal-setting research suggests a specific, difficult goal will focus effort on it; that is the point.
The risk, which both sides of the Ordóñez and Locke and Latham exchange accept as a mechanism, is
neglect of what lies outside the goal. Here the likely distortions are smaller but emptier releases,
releases with no change counted, or pressure to skip checks to keep the cadence, so change failure rate and
recurrence could rise while the key result is met. DORA's guide also warns that using its metrics as
goals makes gaming more likely.

**A better version:** make the objective the outcome ("Core changes reach customers faster and more
safely"), with key results such as median Core lead time below an agreed figure, paired with change failure
rate and with deployment rework. If deployment frequency stays as a key result, count only releases
with at least one change and publish it beside change failure rate. **Criteria:** names a concrete gaming
path, adds a pair, moves the key result toward an outcome. **Weak answer:** "daily is too ambitious",
which argues about difficulty rather than what the goal will distort.

## A1 — Replying to Amara on the target band

A good reply agrees with her premise and holds the line on evidence. Sketch:

"Amara, you're right that the planned case is our projection, and I think it is the likelier outcome.
The commitment line is about what we promise customers, and our record is that a committed item has
landed in its quarter about four times in ten. Quarter 2 unplanned work was 28 percent; the planned
case assumes 22. Until we see that fall, I would rather promise 35.6 and deliver 39 than promise 39 and
explain a miss. Here is what I can offer: the 3.8 FTE-quarters of targets are ranked now, staffed first,
and visible to you weekly; at the week 31 time sample, if unplanned work is at or below 24 percent, we
convert the top targets to commitments, and you can tell customers then."

**Criteria:** a stated reason (the measured cautious case), a concrete path for her to get more (a
dated trigger), and nothing promised to customers before sizing. **Weak answers:** conceding to keep the
peace, which repeats the baseline; or refusing without a path, which loses an ally. Moving the line is
defensible only with new evidence, for example an early unplanned-work sample.

## A2 — Marcus's request for 25 percent

Billing at 25 percent of 15 engineers is 3.75 FTE, 1.25 more than proposed.

**Option 1, take it from Orders:** Orders back to 0.75 FTE (about 5 percent). Cost: Orders has just
finished bulk ordering and takes on post-launch risk; its recurrences were second highest. **Option 2,
spread it:** 0.5 from Orders, 0.25 each from Customer Experience, Payments and Integrations, and Data
and Analytics. Cost: smaller teams' work gets thinner, and fragments below about one FTE tend to vanish.
**Option 3, change the work, not the share:** keep 2.5 but direct 1.0 of it explicitly at ledger
knowledge spreading (pairing, runbooks for period close), since the argument is concentration, not
volume. Option 3 answers his actual reason at no cost to others, and is the recommended answer, with
option 1 as fallback if Billing's recurrences do not fall.

**Rows that tell you in quarter 4:** Billing's recurrence and corrective-action closure, after-hours
pages handled by the three ledger engineers, and the knowledge map counts. **Weak answer:** granting 25
percent by reopening the 8 FTE total without saying what product loses.

## A3 — The paper allocation in week 33

Prevention received 5.1 of 8 FTE: 2.9 FTE (36 percent) went elsewhere without a recorded trade. This
quarter: do not claw it back abruptly, which would sink the product item too; record the trade now,
with the item's owner and the CPO, and decide explicitly whether the remaining weeks restore the
allocation or the shortfall is accepted and carried into the quarter 4 trigger review. Ask which
prevention work was displaced and whether any of it was on Billing's ledger risk.

Next plan: allocation spent against plan becomes a monthly row with the director as owner; borrowing
from prevention requires the same sign-off as changing a commitment; the slipping item's cross-team
dependency gets examined (8 of 10 baseline misses were cross-team).

**Note:** "Prevention received 5.1 of 8 FTE this quarter; 2.9 FTE went to the cross-team item without a
recorded trade. From now on any borrowing from prevention is agreed and logged like a change to a
commitment." **Criteria:** names the process failure, not the person; fixes the mechanism. **Weak
answer:** blaming the item's owner, or quietly accepting the loss.

## X1 — Three OKRs for Victor

**Decline his key result as written.** A count of Sev1 and Sev2 below 10 invites reclassification
(in week 7 of quarter 1 a two-hour payment delay was rated Sev3 and had to be re-rated), and incident counts are small numbers that move
by several between quarters by chance. Offer an outcome instead, paired with the count.

1. **Customers can rely on ordering and payment.** KR: contractual availability at or above 99.9
   percent for the quarter. Pair: customer-detected share and the weekly severity audit.
2. **We keep what we promise.** KR: at least 85 percent of committed items delivered. Pair: forecast
   calibration and the size of the target band, so the line is not lowered to hit the number.
3. **Fewer of our own changes hurt customers.** KR: Core change failure rate below an agreed figure from
   quarter 2's measured baseline. Pair: deployment frequency and recurrence.

**Criteria:** three objectives tied to the allocation, every KR paired with a scorecard row, no KR that
can be met by reclassification alone, and a clear, respectful no to the CTO with an alternative.
Several sets are defensible, for example one platform OKR on environment waits. **Weak answer:**
accepting his KR because he is the CTO, or writing five OKRs that cover every row and focus nothing.

## X2 — Rajiv's two-category reporting

**CFO's view:** two categories are simple for the board and match how many companies present
spending. **CPO's view:** "roadmap" capacity looks larger, which she may like until prevention and
platform vanish into it. **Director's view:** folding prevention (8 of 80 FTE, 10 percent) and platform
(4.5, about 6 percent) into larger lines removes exactly the categories whose effect is delayed; once
invisible, they are the first to be borrowed, which is the paper allocation failure.

**Agree to:** a two-line summary for the board pack. **Refuse:** abolishing the categories internally
or a size threshold for visibility, because small categories are where trade-offs hide. **Offer:** the
run, grow, improve view with the four internal categories underneath, quarterly trend, and the scorecard
rows that show each investment's return; and a dollar figure per category (for example, unplanned work
in the quarter 3 planned case is about $814,000 for the quarter) so the CFO sees the tax that prevention
is meant to reduce. **Criteria:** takes the CFO's need seriously, keeps the investment categories
visible where decisions are made. **Weak answer:** rejecting the proposal as "finance not understanding
engineering".
