# Chapter 59 solutions — Transformation Under Budget Constraint and Scaling Without Bureaucracy

Worked solutions for the [chapter 59 exercises](../parts/13-advanced-problems/59-transformation-under-constraint-and-scaling-without-bureaucracy.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is
fictional.

## F1 — The pull request checklist

**The load test.**

| Question | Answer for the checklist |
|---|---|
| What failure, decision, or information flow does it serve? | Stated intent: that authors check tests, documentation, and similar items before merging. Nobody can name a failure it prevented |
| Evidence in the last two quarters? | The only evidence is against it: 38 of 40 sampled requests ticked every box, and 11 of those 38 ticked "tests added or updated" falsely |
| What would we see if it stopped? | Nothing measurable; the reviewers' behavior does not depend on the boxes |
| Cheaper mechanism? | For the one item that matters most, test changes for production code, a pipeline warning when production code changes without a test change is cheaper and truthful |

**Verdict and replacement.** History: retire it. Replace only the test item, with a review-time warning
rather than a gate, because some production changes legitimately need no new test (Chapter 20's ladder:
a check that is sometimes wrong should warn, not block). The other nine items either duplicate the 14
mandatory standards, which have owners, or are guidance.

**Watch signal.** During a one-quarter suspension, watch regressions among customer-reported defects
and the share of Core merge requests that change production code without tests, as reported by the new
warning. Neither should rise because of the checklist's absence, since the checklist did not change
behavior.

**Criteria for a good answer:** uses the baseline sample as evidence; separates the checklist's
intent from its mechanism; names a watch signal. Also notices the second cost: a false attestation
cheapens every other attestation. **The weak answer** keeps the checklist "because it does no harm",
or adds a rule that reviewers must verify the boxes, which adds a process to prop up one that carries
history.

## F2 — Meeting the in-year measure

The in-year gap is $1,800,000 − $1,313,200 = $486,800. Additional sources, each with its cost:

| Source | In-year saving | What it costs |
|---|---|---|
| Withdraw 2 approved but unfilled requisitions at the start of the year (assumed to exist): 2 × $205,800 | $411,600 | Two engineers' work must stop as well; either a second roadmap item, or slower migration support for the 23 legacy-tool services, which lengthens the period of running two deployment paths |
| Bring the legacy tool's retirement forward by one quarter (end of quarter 1 rather than mid-year): $350,000 × 0.25 | $87,500 | The 46 engineer-weeks of migration land on the product groups in one quarter instead of two, competing with their own plans |
| Total | $499,100 | Covers the gap with $12,300 to spare |

Check: $1,313,200 + $499,100 = $1,812,300, above $1.8M. If no unfilled requisitions exist, the first
source is a reduction in force, and [Chapter 58](../parts/13-advanced-problems/58-layoffs-reductions-and-mergers.md)'s
method applies instead.

Alternatives that are defensible: deferring a license renewal or cutting internal cloud environments
(cheap if they are idle, damaging if product teams depend on them); asking finance to count a one-time
saving. A good answer shows that the in-year measure forces either earlier seat loss or a compressed
migration, both of which raise risk, and states that trade to the CFO; it does not pretend the money
comes free. **The weak answer** takes 2.7 percent off every team, which meets the number while making
none of the work stop, or quietly counts the freed process capacity as cash.

## F3 — What "41 of 3,000" does and does not show

A low rejection rate can mean the board carried no load, or that its existence improved the requests
before they arrived (people prepared more carefully because a board would look). The first is history;
the second is a deterrent load, and the rate alone cannot tell them apart.

Other evidence to want:

- **Outcomes, not decisions:** all 19 change-triggered Sev1 and Sev2 incidents in platform components had
  passed the board, so whatever deterrence existed did not catch the changes that hurt. This is the
  stronger evidence.
- **What the sent-back requests had in common:** 35 of 41 were missing form fields, which is a load on
  the form, not on production. The 6 clashes are a real load.
- **The cost side:** a median wait of 3 working days, which by DORA's reasoning produces larger, less
  frequent batches.
- **The research base:** DORA found no evidence that more formal external review is associated with
  lower change failure rates.

**How the replacement kept the load.** Peer review in the pipeline replaced the approval; an automated
change calendar replaced the board's only demonstrated load, clash detection, and flagged 9 clashes in
the first quarter. The watch signal, change-triggered incidents, showed 5 and 4 against about 4.75 a
quarter, which is not a detectable change.

**Criteria for a good answer:** names deterrence as the alternative explanation; turns to outcome
evidence; identifies clash detection as the load to preserve. **The weak answer** treats 1.4 percent
as proof of uselessness without asking what the board deterred or coordinated.

## A1 — Replying to Elena Sokolova on migration rehearsals

**What to agree with.** The week 9 Sev1 is strong evidence that tier 1 data migrations are dangerous,
and the cost of an unrehearsed failure (a schema change that defeats rollback, a forward fix under
pressure) is much larger than the cost of a rehearsal. The rehearsal rule is not on the list because
it looks like history; it is there because nobody can show what it does.

**What to ask for.** No change to the rule during the period. For one quarter, each rehearsal records
three things: the migration, whether the rehearsal found anything, and what it found (a lock, a timing
problem, data the migration did not expect). That costs minutes per rehearsal.

**How to decide.** If rehearsals find problems, the rule is load-bearing and the record becomes its
evidence; consider whether part of what they catch can move into the week 11 pipeline check, which is
cheaper. If a quarter of rehearsals finds nothing, the decision is still not automatic: migrations are
infrequent and high-consequence, so a rule that rarely catches anything can still be worth its cost.
Then the question becomes whether the rehearsal can be cheaper (a smaller data sample, an automated
dry run), not whether it should exist.

A possible reply: "I agree the rule stays. I'm asking for one line per rehearsal for a quarter, so that
next year we can say what it catches instead of defending it from memory."

**Criteria for a good answer:** keeps the rule during the period, asks for cheap evidence, and treats
low-frequency high-consequence loads differently from frequent cheap ones. **The weak answer** either
suspends the rule to "test" it or exempts it from the inventory because a senior manager objects.

## A2 — Reviewing the compliance pack removal

A short review in blameless form (Chapter 25's format applies to process changes too):

**What happened.** The monthly compliance pack was replaced by a dashboard generated from the four
tools. The data stayed complete. Findings past their service level across Halvard rose from 12 to 31 in
quarter 2, because nobody looked at them.

**The missed load.** The pack carried two loads: compiling evidence, which the dashboard does better,
and a monthly moment at which each VP saw their group's breaches next to the others'. The second load
was social: comparison and attention. The inventory priced the compilation (0.4 FTE) and treated
reading as free.

**Why the load test missed it.** The test asked the pack's owners what it was for, and they described
the document. It did not ask the readers what they did with it, and it did not name a watch signal on
the outcome the pack existed to protect. Had "findings past service level" been the watch signal, the
rise would have triggered a restore within a month rather than a quarter.

**What changes.** Every removal names a watch signal on the outcome, not just on the process's cost;
the readers or attendees of anything removed are asked what they use it for; and the restored meeting
stays small (a 20-minute monthly review of breaches with each VP's delegate) without the manual
compilation.

**Criteria for a good answer:** distinguishes the document from the meeting; owns the miss in the
removal method rather than blaming the VPs; changes the method. **The weak answer** restores the full
pack, which brings back 0.4 FTE of manual work to recover a 20-minute meeting.

## A3 — A hypothetical 5 percent cut at Northstar

This is a scenario for the reader, not canon. Five percent of the FY2 personnel draft of $16.73M is
about $0.84M; of the whole $20.93M (personnel plus $4.2M cloud and tooling), about $1.05M. Agree first
which base and whether it is in-year or run-rate.

A defensible order:

1. **Cloud and tooling waste** inside the $4.2M: cash, fast, and the same place Rajiv Menon already
   wants the $150,000 offset. Requires an analysis Northstar has not done.
2. **Spend consolidation**: the four CI systems. The running-cost saving is capacity (about 1.0 FTE),
   but consolidating also retires licenses and hosts; the cash part depends on the target chosen at week
   78, so it may not arrive in time.
3. **Process removal** from the quarter 4 inventory: small, mostly capacity.
4. **Seats left unfilled** with named work that stops: Northstar's attrition was about 10 percent (8 of
   80) before the director arrived, so about 8 departures a year; leaving 4 unfilled for half a year
   saves about 4 × $185,000 × 0.5 = $370,000 in-year.

**The source to refuse first:** cutting the prevention allocation. It is the only source that grows,
the year-2 board headline depends on it, and Victor's draft stress rule says an overrun comes out of
horizon 2, never prevention. Cutting it converts a 5 percent budget cut into a reversal of the
reinforcing loop.

**Criteria for a good answer:** asks for the base and measure; orders sources by safety and lag;
protects the self-funding loop; names the work that stops with each seat. **The weak answer** spreads
5 percent over the six teams.

## X1 — Victor Lindqvist in week 52

**What to tell the executive team.** Year 2 is funded mainly by unplanned work that prevention
returns: 34 percent at baseline, 25 percent in quarter 3, a draft target of 22 percent. That is about
7.2 FTE returned so far, against 8 FTE of prevention in quarter 3: approaching the prevention spend but
not yet self-funding in capacity. Separately, service credits avoided are about $1.4M a year at the
quarter 3 rate; that is money, not capacity, and should not be presented as paying for the engineers. Process
removal is a supplement, not the main source: the inventory finds about 1 FTE, from build consolidation,
and that depends on the week 78 decision.

**On Rajiv's offset.** The inventory does not cover cloud and tooling, so commission a review of the
$4.2M with a named owner and a date before the $150,000 is spent, rather than promising an offset nobody
has found.

**What to rule on.** The expired portfolio trial and the exemption expiry rule both concern cross-team
authority and Victor's own arbitration role, so rule on them or name a decider with a date. Leave the
checklist, the rehearsal instrumentation, and the standards mechanism to the director and the standard
owners; they are inside the director's authority.

**To Samuel Osei.** "Flat headcount carries the roadmap if unplanned work keeps falling. It fell from 34
to 25 percent this year; each point is 0.8 engineers. We also identified what we will stop, so that the
board sees subtraction as part of the plan, not only additions." This avoids promising the
quarter 4 result, which is not yet measured.

**Criteria for a good answer:** separates capacity from cash; refuses to invent an offset; rules on the
cross-team items and delegates the rest; gives the board a falsifiable answer. **The weak answer**
claims the inventory funds year 2 or promises the 22 percent as a certainty.

## X2 — Halvard's Sev1 review policy

**Do not allow abolition.** The tracked review for every Sev1 is one of six enterprise policies, the
company's encoded lessons. "Most reviews find nothing new" is a claim about the mechanism's cost and
yield, not about the load: Sev1s are rare, high-consequence events, and the review is how recurrences
are found and how the company learns across groups. Abolishing it to save process cost would cut the
policy rather than its paperwork.

**What to allow instead.** Cheapen the mechanism. Options: a lighter format for Sev1s whose cause
matches a known, already-tracked failure mode, with a full review for new ones; reviews that end with
fewer, owned actions rather than long lists (Chapter 25); a quarterly cross-group review of themes, so
that "nothing new" is checked across groups rather than inside one. Measure recurrences as the watch
signal; if recurrences rise after the lighter format, the format was too light.

**Preventing cost shifting.** Require each VP's process cut to state any work it moves to another
group, and have the platform organization, which runs the shared tooling, confirm it. Review all groups'
cuts together in one company-level session, because no single VP sees the transfers. A cut that saves
one group's hours by adding to the platform's queue is not a saving.

**Criteria for a good answer:** keeps the policy and changes the mechanism; names a watch signal;
builds a cross-group check against cost shifting. **The weak answer** either refuses any change (which
teaches VPs that policies cannot be improved) or allows abolition because the platform's removals went
well, generalizing from a different kind of process.
