# Chapter 52 solutions — Technology Investment, Budgeting, and Financial Literacy

Worked solutions for the [chapter 52 exercises](../parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#exercises).
Several exercises have more than one defensible answer. Each solution gives one worked answer, the
criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard figures are
fictional, and nothing here is accounting advice: classifications are what a finance team would
probably conclude under Northstar's policy (coding and testing on budget-authorized projects that add
functionality, inside the current stage-based guidance Finance applies) and under the amended standard
Finance is assessing, to be confirmed with the company's own finance team and auditors.

## F1 — Reading the FY1 latest estimate

**The ratios.**

| Measure | Arithmetic | Result |
|---|---|---|
| Gross margin | 104.4 ÷ 145.0 | 72.0 percent |
| Operating margin | 21.0 ÷ 145.0 | 14.5 percent |
| EBITDA margin | 23.9 ÷ 145.0 | 16.5 percent |
| Free cash flow as a share of revenue | 17.5 ÷ 145.0 | 12.1 percent |

**The explanation for an engineering manager.** "Net income counts costs when they are incurred, even
if no cash moves, and cash flow counts money when it moves. Amortization and depreciation (2.9) are
costs on paper for things we paid for in earlier years, so cash flow adds them back. Customers also
prepaid a little more service than last year (deferred revenue up 1.0), which is cash in hand before it
is revenue. Part of the gap is also presentation: the 2.4 of capitalized engineering is a real cash
outflow, shown under investing instead of operating. Free cash flow, 17.5, counts it, and it is close to
net income, so nothing is hidden."

**Criteria.** A good answer computes the four ratios correctly, names the non-cash add-back and the
working-capital effect, and points out that capitalized engineering moves cash from the operating to
the investing section. The weak answer says operating cash flow is "real profit" and net income an
accounting fiction, which is the misreading the chapter warns against.

## F2 — Classifying Northstar work

| Item | Likely treatment | Reason |
|---|---|---|
| New erp-sync connector (accounting integration) | Capitalize coding and testing once requirements were settled | Authorized renewal commitment, completion probable, new functionality |
| 140 quarantined flaky tests and their fixes | Expense | Maintenance of existing software; no new functionality |
| Contract tests on tier 1 boundaries | Expense, in practice | Testing that protects existing behavior; testing is capitalizable only as part of a project that adds functionality |
| Self-service test environments | Depends, ask finance | Internal-use software for Northstar's own operations; capitalizable if authorized as a project and it adds capability, but much of it may be configuration of subscribed services, which is operating expense |
| Proposed deployment-event store | Depends, ask finance | New internal capability, but small (about six engineer-weeks from the prevention allocation); Northstar's policy capitalizes only budget-authorized projects, so it is probably expensed |
| Hypothetical six weeks defining bulk-ordering scope | Expense under both | Preliminary project stage under the current guidance; under the amended standard, significant performance requirements still being substantially revised, so the probable-to-complete threshold is not met |
| Hypothetical one-off data conversion | Expense, except any software built to convert the data, which is capitalizable | The standard expenses data conversion and capitalizes conversion software |

**Criteria.** A good answer applies Northstar's policy and the amended standard's threshold (authorized,
probable, uncertainty resolved), the functionality test, and the cost-type rules, and is comfortable writing "depends" with the question
it would ask finance. It notices that a company's own policy (for example, capitalizing only
authorized projects above a size) narrows what the standard would allow. The weak answer classifies by
team ("Platform Operations work is expense, Orders work is capital") or by importance, neither of which
the standard uses.

## F3 — Stopping capitalization in FY2

Assume the FY2 work resembles FY1, so about $2.5M would otherwise have been capitalized (about 15.3
FTE-years at $157,250, raised 3 percent for merit, is about $2.48M).

| FY2 measure | Keep capitalizing | Stop capitalizing | Change |
|---|---|---|---|
| Engineering labor expensed | all except about 2.5 | all of it | +2.5 expense |
| Amortization | 2.3 ((2.1 + 2.4 + 2.4) ÷ 3) | 2.3, unchanged in FY2 | none |
| Operating income | baseline | about −2.5 | −2.5 |
| EBITDA | baseline | −2.5 | −2.5 |
| Operating cash flow | baseline | −2.5 | outflow moves from investing to operating |
| Free cash flow | baseline | unchanged | none (ignoring tax) |

The trap is the year of transition. In the chapter's steady-state comparison, always expensing cost
only 0.3 of FY1 operating income. Switching costs the full 2.5 in FY2, because the amortization of
earlier years' capitalization continues (2.3 in FY2, 1.6 in FY3, 0.8 in FY4) while current work is
expensed. Operating income recovers only as that tail runs off.

**What Calder Ridge would care about.** EBITDA, if the firm values its stake or plans an exit on a
multiple of it: a 2.5 drop is about 10 percent of FY1 EBITDA. It would also note that cash is unchanged,
so the business is no worse; the question is how buyers would read the series.

**Criteria and weak answer.** A good answer separates the transition effect from the steady-state
effect and says cash does not change. The weak answer reports a 0.3 effect, carrying the steady-state
figure into a transition year.

## A1 — Offsetting $150,000 inside cloud and tooling

| Option | Assumptions | Statement effect | Risk |
|---|---|---|---|
| Production hosting review ($3.1M) | About 5 percent removable by rightsizing idle capacity and committing the stable baseline; owner Kwame Mensah with Tom Becker | Cost of revenue down, gross margin up about 0.1 point (0.15 ÷ 145) | Commitment locks in load you might move; rightsizing a tier 1 path can hurt latency |
| Development tooling review ($1.1M) | About 14 percent from unused seats and duplicate tools; CI consolidation cannot be counted because no target is chosen | R&D expense down | Cuts tools engineers use; 14 percent is a large share of a small line |
| Expected vacancy | Use $150,000 of the forecast $427,000 vacancy underspend | Personnel line under forecast; cloud and tooling not offset as Rajiv asked | Vacancy is capacity lost; if attrition falls, the money is not there |

**Recommendation (one defensible version).** The hosting review, because it is the largest base, it
improves gross margin, and it gives engineering a variable-cost owner, with vacancy as a declared
fallback. Paragraph to Rajiv: "We will offset the $150,000 inside production hosting: Kwame Mensah and
Tom Becker will remove about 5 percent of the $3.1M through rightsizing and a commitment on the stable
baseline, reported monthly from week 53. If by the end of quarter 5 the saving is tracking below
$100,000, the shortfall comes from personnel vacancy, which you will see as a variance line rather than
a hidden saving."

**Criteria and weak answer.** A good answer states assumptions, names an owner, shows which statement
line moves, and is honest that vacancy is not an offset inside the line Rajiv named. The weak answer
proposes cutting development tooling without saying which tools or what productivity it costs, or
counts savings from a CI target that has not been chosen.

## A2 — tax-svc through the statements

Year 1, with the exercise's assumptions (the build-out's upfront work is capitalizable and goes into
service at the end of year 1, so its amortization starts in year 2; integration work is not
capitalizable; engineer time is existing payroll, so only subscriptions are new cash):

| Option | Year-1 operating expense | Year-1 EBITDA effect | New cash in year 1 | Three-year TCO (Chapter 30) |
|---|---|---|---|---|
| A. Build out | $92,500 upkeep (0.5 FTE); the $96,000 upfront is capitalized and amortized from year 2, when it is in service, about $32,000 a year | −$92,500 | $0 | $373,500 |
| B. Buy engine | $64,000 integration + $150,000 subscription + $27,750 (0.15 FTE) = $241,750 | −$241,750 | $150,000 | $597,250 |
| C. Hybrid | $56,000 integration + $45,000 subscription + $46,250 (0.25 FTE) = $147,250 | −$147,250 | $45,000 | $329,750 |

**Who likes what.** Rajiv Menon, on these figures, prefers A: least operating expense, best EBITDA, no
new cash; C is his second choice; B breaks his flat cloud-and-tooling line. Greg Tanaka cares about
Billing capacity for his deals and may prefer B, which leaves only 0.15 FTE of upkeep. Victor Lindqvist's
strategy policy (buy what changes for outside reasons) points to B or C.

**Why the figures should not decide.** A looks best only because capitalization moves its main cost off
the year-1 income statement and because existing payroll is treated as free. The decisive issues are
elsewhere: who maintains rate content (A keeps it with one person, the concentration that caused
INC-414), the vendor on the order path (B), the cheapest three-year TCO (C), and that a wrong tax line is
a Sev1 under the week 3 definitions. **Criteria:** correct arithmetic, a clear split between capacity and
new cash, and the explicit point that the accounting ranking differs from the economic one. **Weak
answer:** recommending A because it "costs nothing in year 1".

## A3 — "Costs nothing and improves profit"

**Assessing the claim.**

- *"Costs nothing."* False. Moving 2 FTE for two quarters is 4 FTE-quarters, $185,000 of capacity
  (2 × 2 × $46,250, Chapter 49), and stage 2 then runs at 4 FTE, moving some exit criteria to stage 3.
  Cash does not change because headcount is flat, but the prevention work not done is the price.
- *"Improves profit because feature work is capitalized."* Partly true on paper and irrelevant to the
  decision. If all the time qualified, about $157,000 more would be capitalized in FY2 (2 × 0.5 ×
  $157,250); if three quarters is coding and testing after the threshold, about $118,000. FY2 operating
  income and EBITDA rise by that amount; then about a third of it returns as amortization in each of the
  next three years. Cash is identical, and whether deal features pass the threshold depends on whether
  their requirements are settled, which for a prospect's feature often they are not.

**Sentences for the proposal.** "Option B moves 2 of the 6 prevention engineers to deal features in
quarters 5 and 6. It adds no cost in cash and costs $185,000 of capacity, and the following exit criteria
move to stage 3: [list]. Because some feature work may be capitalized, option B can show about
$0.12M to $0.16M more operating income in year 2, offset by amortization in later years; we compare the options in
cash and capacity, where they are equal in cost and differ in what they deliver."

**Criteria and weak answer.** A good answer separates capacity, cash, and accounting, quantifies each,
and refuses to let the booking decide. The weak answer either accepts Greg's claim or dismisses it
without the arithmetic, which leaves him the last word.

## X1 — TR-01 in the year-2 plan

**One defensible decision.** Fund TR-01 from Core capacity in quarters 5 and 6, with a checkpoint after
the first 40 engineer-days. Under the base scenario (190 days), 40 days should deliver about a fifth of
the scoped work; if the checkpoint shows progress at or below the pessimistic pace (243 days in total),
decide whether to buy a year of extended support while continuing, and re-plan. Request a real support
quote now, because the case currently rests on an assumed $60,000; buying information is cheap.

**The alternative** (also defensible): buy extended support first and migrate in quarters 7 and 8, if
quarters 5 and 6 of Core capacity are already committed (permissions work, ledger work, the year-2
organization's handoffs). Its cost is new operating expense inside the line Rajiv wants flat, and the
migration still comes.

**Two sentences for the board.** "Core's framework is past community support; we will migrate it in the
first half of year 2 using existing engineers, at an expected cost of about $150,000 of capacity and no
new spending, with a checkpoint that triggers extended support if the work runs long. Until then, any
known-exploited or internet-facing critical without a patch is mitigated within our 7-day rule, other
criticals within 30 days, or escalated to me."

**Reversal evidence.** A checkpoint at the pessimistic pace; a support quote far below $60,000 a year,
which makes deferral cheap; or a critical, unpatched framework vulnerability, which makes the migration
urgent and may justify displacing more Core work.

**Criteria and weak answer.** A good answer chooses, uses the scenarios, names the checkpoint and its
trigger, and keeps the board version in cash, capacity, and risk. The weak answer presents the three
scenarios to the board without a decision, or promises a fixed date from the optimistic scenario.

## X2 — Halvard and the EBITDA refinancing

This is a hypothetical scenario, not Halvard canon.

**Quantification.** Payroll about $102.9M. At 18 percent, $18.5M is capitalized (0.18 × 102.9); at 28
percent, $28.8M (0.28 × 102.9). The difference is about $10.3M.

| Effect | Year 1 | Later years |
|---|---|---|
| EBITDA | +$10.3M | +$10.3M each year the policy holds, since capitalized labor never appears above EBITDA |
| Operating income | +$10.3M, less amortization of the increment if any starts in year 1 | Shrinks as amortization of about $3.4M a year per year's increment accumulates; near zero after three years at steady state |
| Cash, free cash flow | none (ignoring tax) | none |

**Assessment against the standard.** Platform and reliability work is mostly maintenance or work that
keeps existing functionality; the standard expenses it. Reclassifying it as enhancements without new
functionality, authorized projects, and resolved uncertainty is not supported. It also creates risks the
CFO bears with the CTO: auditor challenge, lender diligence that adjusts EBITDA back down, and an
impairment trail if reclassified projects never "complete".

**Response to the CFO (one version).** "I can't support reclassifying platform and reliability work: it
does not meet the capitalization criteria and our records would not survive the auditor or the lenders'
diligence. What I can do in four weeks is check whether our tracking misses genuinely capitalizable
work, for example new platform capabilities funded as projects, and give you a defensible figure, which
may be a few points rather than ten. I'd also suggest we show the lenders EBITDA with free cash flow
beside it, which is the number they will test."

**Criteria and weak answer.** A good answer quantifies the effect, separates EBITDA from cash, applies
the standard's criteria, and offers a legitimate alternative instead of a flat refusal. The weak answer
either agrees ("it's finance's call") or refuses without offering the review, which loses the CFO and
the argument.
