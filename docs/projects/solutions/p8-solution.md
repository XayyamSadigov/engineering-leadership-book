# Project 8 solution: Northstar's year-2 technology investment proposal

This is one worked answer to [Project 8](../p8-cto-technology-investment-proposal.md), written in the seat of
Victor Lindqvist (CTO) in week 47. Its main finding is uncomfortable and, for that reason, the one to put in front
of the executive team and, through the operating plan of Helena Marsh (CEO), the board: on counted benefits alone, the
recommended package has a three-year NPV of about −$70,000 in the base case, and the quality continuation at its center breaks even only if it keeps unplanned work about
4 points lower than it would otherwise be. The package is still recommended, because migrating the unsupported Core framework is
cheaper than the realistic alternative of paying for extended support, and because the renewal protection it
buys has to be worth little to close the gap. It asks for no cash beyond the continuation's $150,000. The case says so in those words. All Northstar facts are fictional;
the figures marked invented come from the project's data files, and estimates marked as this solution's are
assumptions, not facts from the case. Also named: Rajiv Menon (CFO) and Greg Tanaka (VP Sales).

## 1. The decision in board terms

**The board (week 50)** approves the year-2 operating plan and budget envelope, which Helena Marsh presents.
The engineering content of that envelope is 87 seats with no additions and no cash beyond the continuation's
$150,000 of tooling, offset inside the $4.2M cloud and tooling budget. The board does not approve projects.
My own agenda item that week is the three-year technology strategy, for discussion; this proposal is its
year-2 investment layer, not a separate approval item.

**The executive team (week 49, decisions by week 51)** decides the quality continuation (6 FTE, or 4 FTE plus
two engineers on deal features) and the order in which engineering capacity outside product work is spent.

**The CTO** decides the technical sequence inside that capacity: when the framework migration starts, when
the bank route is built, and who decides the CI target. I recommend; the executive team and the board decide
their parts.

## 2. Conventions

| Convention | Value | Why |
|---|---|---|
| Effort rate | $3,558 an engineer-week ($185,000 ÷ 52) for every candidate; engineer-days converted at five a week | One rate for all candidates. At Chapter 30's $800 an engineer-day, a five-day week would cost $4,000, so mixing the two inflates day-based estimates by about 12 percent |
| FTE-quarter | $46,250 | $185,000 ÷ 4 |
| Timing | Year 1 is quarters 5 to 8; all flows at the end of each year | Simple and stated; quarterly timing would move each NPV by a few thousand dollars |
| Discount | 10 percent; factors 0.9091, 0.8264, 0.7513 (sum 2.4869) | Finance's rate (Chapter 45) |
| Horizon | Three years | Chapter 45's guard against benefits counted for ten years |
| Two ledgers | Capacity (engineer time, paid either way) and cash (money leaving the company) shown separately; "economic" NPV adds them with capacity at cost | The board can see which number is which |

Payback is reported only next to NPV, because it ignores the time value of money and everything after the
payback date ([Dahlquist and Knight, 2022](../../references/bibliography.md#dahlquist2022finance)).

## 3. Priced register

| Candidate | Options | One-time | Run cost | Displaces |
|---|---|---|---|---|
| C1 Quality continuation | Do nothing (prevention to 0 from week 53); 4 FTE plus 2 on deal features; stage 2 now and stage 3 at the gate | 22 FTE-quarters, $1,017,500 capacity; $150,000 cash (stage 2). Stage 3's $100,000 belongs to C3 | None stated | Product work; Greg Tanaka's deal features |
| C2 Core framework (TR-01) | Do nothing (patch under exceptions; one open Core critical already waits on TR-01); extended support ($60,000 a year, the assumption Chapters 30 and 52 use); support for a year then migrate; migrate | Migrate: Finance's scenarios of 120, 190, and 243 engineer-days, 24, 38, and 48.6 engineer-weeks: $85,385, $135,192 (base), $172,904 at $3,558 a week (Finance's $800 a day gives $96,000, $152,000, $194,400) | Support: $60,000 a year cash | The estate-currency line in my week 47 draft, or prevention, in quarters 5 to 7 |
| C3 CI consolidation after phase 1 | Do nothing (four systems); decide the target only; full consolidation | About 80 engineer-weeks, $284,615, plus $100,000 tooling | Falls from about 1.5 to about 0.5 FTE a year | The platform roadmap, or C1 capacity |
| C4 Second bank route (TR-08) | Do nothing; a manual fallback (queue and notify, about 4 engineer-weeks, this solution's estimate); build the route | 26 engineer-weeks, $92,500 (range 20 to 36), in quarters 7 and 8 | $36,000 a year fee from go-live in week 104, so from year 3 (invented) | Payments and Integrations product work |
| C5 Invoice reconciliation | Do nothing; monthly sampled reconciliation by Data and Analytics (about 2 engineer-weeks, this solution's estimate); nightly job for all customers | 12 engineer-weeks, $42,692 (range 8 to 20) | 0.1 FTE a year, $18,500 capacity | Billing product work |
| C6 Two engineers on deal features | Do nothing; through the forum as the 4-plus-2 option | 4 FTE-quarters, $185,000 capacity | None | Stage 2 prevention (6 to 4 FTE) |

## 4. Valuation and scenarios

**C1, the counterfactual first.** The continuation's value is the difference between year 2 with it and
year 2 without it. This solution's assumptions, written so that they can be attacked:

| | Without the continuation | With it |
|---|---|---|
| Unplanned work | Drifts from 25 to 28 percent (quarter 2's level); average 27 | Falls from 25 toward 20; average 22.5 |
| Credits a quarter | Drift back toward quarter 2's $95,000 | Average $40,000 (between quarter 3's $60,000 and stage 2's criterion of $25,000) |

Base benefit in year 1: 4.5 points of 80 engineers = 3.6 FTE, $666,000 of **capacity**; credits $55,000 a
quarter, $220,000 of **cash**. Benefits halve in year 2 and stop in year 3 (prevention then becomes a normal
line in the quarterly plan, as the continuation proposal says). Downside: 2 points (1.6 FTE, $296,000) and
$20,000 a quarter ($80,000). Upside: 7 points (5.6 FTE, $1,036,000) and $70,000 a quarter ($280,000).
Renewal protection is not counted.

Base economic flows: year 1 = −$1,017,500 − $150,000 + $220,000 + $666,000 = −$281,500; year 2 = 0.5 ×
($220,000 + $666,000) = $443,000. NPV = −$281,500 × 0.9091 + $443,000 × 0.8264 = about **+$110,000**.
Payback about 1.6 years (281,500 ÷ 443,000 of year 2). Cash only: year 1 = −$150,000 + $220,000 = +$70,000,
year 2 = +$110,000, NPV about +$155,000; the cash case looks strong because the engineers are paid either way,
which is why it is not the decision-relevant number.

**All candidates, three-year NPV at 10 percent.**

| Candidate | Base | Downside | Upside | Counted benefit and its source |
|---|---|---|---|---|
| C1 continuation (economic) | +$110,000 | −$564,000 | +$679,000 | Capacity and credits under the counterfactual above |
| C2 migrate, against doing nothing | −$123,000 (190 days) | −$157,000 (243 days) | −$78,000 (120 days) | None counted; risk avoided |
| C2 migrate, against extended support | +$26,000 | −$8,000 | +$72,000 | Support PV $149,211 ($60,000 × 2.4869) less migration PV |
| C3 full consolidation, fast schedule | −$58,000 | not computed | +$33,000 if the $100,000 is not needed | $185,000 a year capacity from year 2; the template's slower schedule gives about −$182,000 |
| C4 bank route | +$11,000 | −$65,000 (0.5 outages a year) | +$162,000 (2 a year) | 0.8 × outages × $120,000 credits, less the $36,000 fee |
| C5 reconciliation | −$68,000 | −$94,000 (20 weeks) | −$55,000 (8 weeks) | None counted |
| C6 deal features | not computable | | | Revenue value not supplied |

C4's base flows: year 1 = −$92,500 (built in quarters 7 and 8, live in week 104, so no fee and no
protection in year 1); years 2 and 3 = $96,000 − $36,000 = $60,000. NPV = −$92,500 × 0.9091 + $60,000 ×
(0.8264 + 0.7513) = about +$11,000. C5: −$42,692 × 0.9091 − $18,500 × 1.5777 = about −$68,000. C2 against
support: $149,211 − $135,192 × 0.9091 = about $26,300; at Finance's pessimistic 243 days migration costs
about $8,000 more than support in present value. The partial C2 option (support for a year, then migrate)
costs $60,000 × 0.9091 + $135,192 × 0.8264 = about $166,000 in present value, the most expensive of the three
because it pays for both.

## 5. Cost of delay and sequencing

| Candidate | Cost of delay a week | Urgency profile | Duration | CD3 ($ a week of delay, per week of duration) |
|---|---|---|---|---|
| C1 | About $17,000 ($886,000 ÷ 52, base year-1 benefit) | External deadline in effect: six top-40 renewals in quarters 5 to 8 | 52 weeks | 328 |
| C2 | About $1,154 if waiting means buying support ($60,000 ÷ 52); unpriced risk if it means doing nothing | Long life, peak unaffected, with a security tail | 38 weeks | 30 |
| C4 | About $1,154 ($60,000 ÷ 52) | Long life, peak unaffected | 26 weeks | 44 |
| C3 | About $3,558 after completion | Long life, peak unaffected | 80 weeks | 44 |
| C5 | Not priced; information | Long life | 12 weeks | not ranked |

C1 runs first and is scheduled backward from the renewals, not ranked. C5 is cheap and its information
changes what the strategy measures, so it runs in quarter 5. C4 ranks slightly above C2 on CD3, but C2 starts
first: its downside is an unpatchable vulnerability with no workaround (one Core critical already waits on
TR-01 under an exception), which the ratio does not price. C4 follows in quarters 7 and 8, after the stage 2
gate, which also keeps its fee out of year 2. C3 is deferred: the target is chosen at the week 78 gate, as my
week 47 strategy draft says, and that choice decides whether the $100,000 is needed.

## 6. The package

| Quarter | C1 prevention | C2 migration | C5 reconciliation | C4 bank route | Total FTE | Envelope 8 |
|---|---|---|---|---|---|---|
| 5 | 6 | 0.97 (12.7 weeks) | 0.92 (12 weeks) | | 7.90 | 0.10 spare |
| 6 | 6 | 0.97 | | | 6.97 | 1.03 spare |
| 7 | 5 | 0.97 | | 1.0 (13 weeks) | 6.97 | 1.03 spare |
| 8 | 5 | | | 1.0 | 6.00 | 2.0 spare |

**Funded:** C1 stage 2 now and stage 3 at the week 78 gate; C2 migration; C4; C5. **Deferred:** C3; the target
is chosen at the week 78 gate, and the $100,000 is a later request triggered by that choice. **Declined as a private arrangement, offered as an option:** C6, priced in section 10. Spare
capacity (about 1 FTE in quarters 6 and 7, 2 in quarter 8) returns to product through the portfolio forum.
At Finance's pessimistic 243 days the migration needs about 1.25 FTE a quarter, which breaks the envelope in
quarter 5 (8.17 FTE); it then runs into quarter 8 instead.

The package uses absolute FTE, so it holds at 78, 79, and 80 engineers; product capacity absorbs the
difference. The continuation proposal does not itemize what its 6 FTE buy, so this solution treats C2, C4,
and C5 as additions. My week 47 draft carries a separate estate-currency line of 2.0 FTE in year 2, which is
where C2 naturally sits. Funding them inside the 6 FTE, as the [Project 7 solution](p7-solution.md) does with the
migration and reconciliation, is defensible and frees about 1 to 2 FTE a quarter, but must then name the
prevention work it displaces.

**Cash against offsets.**

| Year 2 cash | Amount | Offset, year-2 saving (annual rate) | Confidence |
|---|---|---|---|
| Stage 2 tooling, tranche 1 (week 53) | $85,000 | O1 duplicate licenses, about $75,000 from renewal in week 59 ($85,000) | Medium |
| Stage 2 tooling, tranche 2 (week 65) | $65,000 | O2 environment shutdown, about $46,000 from week 65 ($60,000) | Low |
| **Total** | **$150,000** | **About $121,000 ($145,000)** | Year-2 gap about $29,000 if both land; about $75,000 if O2 fails |

Nothing beyond the continuation's $150,000 is asked for in year 2. The year-2 savings are prorated: O1 saves
from its renewal (assumed week 59, 46 of 52 weeks) and O2 from week 65 (40 weeks). The gap is a timing
difference at the annual rates, which cover the $150,000 in a full year; tranche 2 is spent only up to the
savings O1 and O2 have shown by week 65, and the rest slides into year 3. Two later requests are named now
with their triggers: C4's $36,000 a year fee from week 105, triggered by go-live, and C3's $100,000,
triggered by a CI target at the week 78 gate (with O3, $25,000 a year once the last Jenkins unit moves).

## 7. Decisive inputs and break-evens

| Item | Decisive input | Base | Break-even | Reading |
|---|---|---|---|---|
| C1 | Unplanned-work difference the continuation makes | 4.5 points | 3.9 points | Fragile: a modest overestimate turns it negative. The week 78 gate must test it |
| C2 | Migration effort | 38 engineer-weeks (190 days) | About 46 engineer-weeks (about 230 days) against support | Thin: Finance's pessimistic 243 days is past it. The scoping at week 60 decides |
| C4 | Partner outages over two hours a year | 1 | 0.93 a year; at 36 engineer-weeks of effort the base case turns to about −$22,000 | Near zero on expected credits; see the 99.9 percent argument below |
| C5 | Value of seeing invoice correctness | Not counted | About $27,000 a year ($68,000 ÷ 2.4869) | One prevented incident like INC-409 (duplicate invoices from a retried batch job) every few years plausibly covers it |
| Package | Renewal protection | Not counted | About $28,200 a year ($70,120 ÷ 2.4869): a 3.3-point lower annual chance of losing one top-40 customer ($28,200 ÷ ($1.17M × 72%)) | Small against $7.0M of ARR renewing |

The package NPV is the sum of C1 (+$110,207), C2 against doing nothing (−$122,902), C4 (+$10,575), and C5
(−$68,000): about −$70,100. Downside about −$880,000; upside about +$708,000. Against the extended-support
baseline for C2, the base becomes about +$79,000.

**C4 beyond expected value.** One 150-minute payment outage exceeds a whole quarter's 99.9 percent
allowance (about 131 minutes) by itself, and 99.9 percent in every quarter is a mandatory stage 2 exit
criterion. The expected-credit arithmetic misses that: the bank route also protects the continuation's own
gate. The case states this as an uncounted benefit rather than adding a price for it.

## 8. Accounting note

Under Northstar's policy (ASC 350-40; coding and testing on budget-authorized projects that add functionality
is capitalized at $157,250 per FTE-year and amortized over three years; maintenance, incident work,
prevention, and refactoring are expensed), the package books as follows. C1 is prevention: expensed. C2 adds no
functionality: expensed, as Finance's TR-01 scenarios already state. C4 adds a capability, so its coding and
testing could be capitalized if the project is budget-authorized: at most 26 ÷ 52 × $157,250 = about $78,600,
then about $26,200 a year of amortization over three years. C5 is a new job but arguably a control rather than
functionality; at most about $36,300 (12 ÷ 52 × $157,250). I will ask Rajiv Menon to confirm C4 and C5 before
the budget is final, and how amortization would sit in year-2 operating expense
([Chapter 52](../../parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md)
explains how each shows up in the statements). The recommendation does not depend on the answers: the case is
built on cash and capacity, and the accounting treatment changes when a cost is recognized as expense, not
how much is spent (**this book's recommendation**, consistent with Chapter 45's warning that booking can make
work look cheaper without changing its economics).

## 9. Engineering input to the operating plan

> **Engineering input to the year-2 operating plan (for Helena Marsh's week 50 envelope)**
>
> **What the envelope needs to contain.** 87 engineering seats with no additions, and no cash beyond the
> continuation's $150,000 of tooling, offset inside the $4.2M cloud and tooling budget.
>
> **What it buys.** (1) Reliability held through the six top-40 renewals in quarters 5 to 8 (about $7.0M
> ARR): prevention at 6 then 5 FTE, down from 8, with gates in weeks 78 and 104. (2) The Core framework,
> past free support, replaced by week 91 for about $135,000 of engineering time, less than three years of
> extended support ($180,000), with the risk removed rather than rented. (3) A second payment route by week
> 104: one partner outage like the 150-minute Sev1 in the quarter before the director arrived would break a
> quarter's 99.9 percent on its own. (4) Invoice reconciliation, so that the correctness of what we bill can
> be measured.
>
> **What it does not buy.** CI consolidation (the target is chosen at the week 78 gate; any funding is a
> later request). Deal-feature capacity from prevention, which the executive team may choose instead as a
> priced option.
>
> **The numbers, honestly.** Capacity 7.9, 7.0, 7.0, and 6.0 FTE by quarter. Counted three-year NPV about
> −$70,000 in the base case (−$880,000 to +$708,000). It pays if it lowers by about 3.3 points a year the
> chance of losing one top-40 customer. The weakest assumption is how much unplanned work would return
> without prevention; the week 78 gate tests it.
>
> **Report back.** Estimates against actuals at weeks 78 and 104.

## 10. The ask, and the replies

**The ask.** Decision: the executive team approves C1 stage 2, C2, C4, and C5 inside the envelope by week 51;
the board approves the envelope in the operating plan Helena Marsh presents in week 50. Decider for the technical sequence: the CTO. Funding: the
prevention line and the two cash tranches. Checkpoints with stop conditions:

| When | Evidence | Stop or change if |
|---|---|---|
| Week 56 | Stage 1 gate (the continuation's criteria) | The gate fails: stage 2 is re-scoped before tooling tranche 1 is spent |
| Week 60 | TR-01 scoping complete; ADR-0001 decided (as my draft proposes); reconciliation producing data | Scoped migration above about 46 engineer-weeks: buy support instead |
| Week 65 | O1 and O2 savings visible | Tranche 2 is spent only up to the savings shown; the rest waits for year 3 |
| Week 78 | Stage 2 gate; unplanned work against the 3.9-point break-even; CI target chosen | Unplanned no better than 27 percent: the continuation's value is re-estimated before stage 3. No target: C3 stays unfunded |
| Week 91 | Migration complete; bank route integration on track | Migration more than a quarter late: C4 is not started until reviewed |
| Week 104 | Stage 3 gate; look-back on every estimate in this proposal | Report variances, misses included |

**Reply to Greg Tanaka.** Two engineers for quarters 5 and 6 cost about $185,000 of capacity. To pay back
their salary cost, the deal features they build must add expected new ARR of about $163,000 from year 2
($185,000 ÷ (0.72 × 1.5777)); to beat the prevention they displace, valued at the continuation's average of
about $53,000 of present value per FTE-quarter, expected new ARR of about $188,000. At a win probability of 0.5 that is deals worth
about $375,000 of ARR. If you write down the deals, their value, and the probability, I will put the option
to the executive team in week 49 with those numbers; it is a legitimate choice through the forum, and the
proposal lists the stage 2 criteria that would move to stage 3. Average value probably overstates what the
fifth and sixth prevention engineers return, so the true bar may be lower.

**Reply to Rajiv Menon.** Nothing beyond the continuation's $150,000 in year 2. The named offsets run at
$145,000 a year, $85,000 of duplicate licenses (medium confidence) and $60,000 of environment shutdown (low),
but save only about $121,000 in year 2 because they start in weeks 59 and 65. Tranche 2 is spent only up to
the savings shown by week 65, so a shortfall delays tooling rather than adding cost. The bank route's $36,000
a year and any CI tooling are year-3 requests with stated triggers, not part of this envelope. The program ends after stage
3 in week 104; prevention then becomes a normal line in the quarterly plan. Credits have fallen from $410,000
to $60,000 a quarter, so this case is no longer about credits; it is about renewals and the capacity
returned, and I have shown where it fails.

## 11. Other defensible answers

- **Fund C2, C4, and C5 inside the 6 FTE.** Defensible, and cheaper in capacity, if the submission shows the
  prevention work displaced.
- **Buy extended support for one year and migrate in year 3.** Defensible if Core changes in year 2 are judged
  too risky with 41 percent line coverage; it costs about $43,000 more in present value than migrating now
  ($166,275 against $122,902) and must say so.
- **Buy extended support and do not migrate.** Defensible if scoping at week 60 lands near Finance's
  pessimistic 243 days, where support is about $8,000 cheaper in present value; the risk is then rented, not
  removed, and the open Core critical stays under exception.
- **Decline C4.** Defensible on expected value if the submission addresses the 99.9 percent argument directly
  and names who accepts the risk.
- **Recommend the 4-plus-2 option.** Defensible if Greg Tanaka supplies a value above the break-even and the
  moved criteria are listed.

## What a weak submission looks like

> "We request $1.4M for reliability and modernization: quality program $1.0M, framework upgrade $150K,
> CI consolidation $385K, bank redundancy $130K. ROI: 300 percent from avoided outages, saved engineering
> time, and protected renewals of $7M. Payback under six months. Approve all items."

Against the rubric: projects put to the board instead of an envelope (framing weak); one option per item,
mixed rates (pricing weak); capacity counted as cash and $7M of renewals counted as certain benefit
(valuation weak); everything funded with no quarter-by-quarter fit and no offsets (portfolio weak); no
break-even or stop condition (staging weak); a return figure with no assumptions that the board will
remember next year (communication weak); Greg Tanaka's alternative not mentioned (replies weak). It fails
acceptance criteria 2 to 9.

**An adequate submission** prices each candidate with three options, computes base-case NPVs correctly, and
fits the package within the envelope in total, but counts the continuation's cash case as its value and
gives the board a list of projects. It scores in the 60s. **What separates excellent from adequate** is
stating the counterfactual, separating capacity from cash, putting the fragile break-even on the one-page input,
and tying the cash to offsets that stop the spending if they fail.
