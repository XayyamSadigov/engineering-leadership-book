# Chapter 8 solutions — Career Development, Promotion, and Compensation

Worked solutions for the [chapter 8 exercises](../parts/02-people-management/08-career-development-promotion-and-compensation.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.
Nothing here is legal advice; where an answer touches pay law, it says where local advice is needed.

## F1 — Rewriting a Senior Engineer description

**What each phrase does.** "Five or more years" becomes a gate: managers wait for the anniversary, a
fast grower with three years is refused on a technicality, and a slow one with seven is promoted on
time served. "Expert in Java, Spring, Kafka" rewards depth in the current stack, ages with it, and
excludes people from other stacks. "Strong communicator" cannot be checked, so it is decided by
impression, which is where bias enters. "Mentors junior engineers" is close to useful but counts
activity, not result.

**One rewrite.**

- Owns the design and delivery of a system or major feature, including its operation in production,
  without needing day-to-day direction.
- Makes trade-offs that others can follow from the written record; designs are reviewed and adopted,
  not just approved.
- Prevents classes of failure in their area, shown by incidents or defects that stopped recurring.
- Raises others' ability: at least one engineer can now do work in the area they could not before.

**Testing.** Place twenty current engineers, across teams, against old and new text, and ask whether
their peers would agree with each placement. Disagreements show vague cells. A strong answer also
checks that the scope required is available on every team.

**Weak answer:** replacing the tools with other tools, or keeping years as "guidance".

## F2 — Explaining different promotion rates

The rates are 6 of 15 (4.0 per 10 engineers) and 1 of 13 (0.8 per 10). Alternative explanations:

1. **Different meanings of Senior.** Daniel Cho's bar ("owns features end to end") is lower than a
   bar that requires design others build on. This is the leading hypothesis from the chapter's case.
2. **Different starting mix.** If Customer Experience had more engineers close to the bar two years
   ago, it would promote more. Look at level mix and time at level at the start of the period.
3. **Scope availability.** Customer Experience works on two platforms with many features; Billing's
   work is dominated by incidents (41 percent unplanned), which leaves little room for visible scope.
4. **Manager advocacy.** Some managers nominate; others wait to be asked.
5. **Real growth.** Customer Experience may in fact develop people better.

**Data:** the cases themselves (what evidence was cited), level mix and tenure at level, nominations
per team, and promotion outcomes for transfers between teams.

**Calibration settles** whether the same evidence is judged the same way across teams. It does **not**
settle whether opportunities were equal, or whether the past promotions were right; re-leveling past
promotions is a separate, costly decision. **Weak answer:** "Customer Experience inflates" or
"Customer Experience grows people better", stated without the data.

## F3 — A usable "not yet"

**Message (spoken, then sent in writing).** "Your case was not approved this cycle. I want to go
through why and what would change it. The committee agreed that your work on the export service is at
Senior level for technical judgment and delivery. The gap is scope: Senior means owning a system whose
design other people rely on, and all of your impact so far sits inside one service only our team
touches. What would close it: lead the design of the change the reporting API needs from your service,
take it through review by the team that consumes it, and support their first integration. My part:
I will assign you that design this quarter and ask a staff engineer to review it with you. We will
check progress in three months, and the case goes back to calibration next cycle."

The five parts are present: decision, gap tied to a dimension, evidence, the manager's commitment,
and a date.

**What makes it useless.** First, an unachievable or vague evidence request ("show more leadership",
or "lead a cross-team initiative" when none exists). Second, no commitment from the manager: if the
role offers no cross-team scope, telling the person to find it shifts the manager's job onto them.
Also weak: softening the decision so much that the person leaves believing they were nearly promoted
and only the committee's mood stood in the way.

## A1 — Running a lopsided calibration

**In the meeting.** Stop presenting by the nominating manager: an independent reader summarizes each
case against the dimensions, and Daniel Cho answers questions. Reorder so that the two Billing cases
are not left to the tired end; if their packets are too thin to judge, defer them to a short session
within two weeks with Marcus Oyelaran present, rather than declining them. Deferral is not a "no", and
saying so prevents the Billing engineers from paying for an incident week. Take a break before the
remaining cases. Apply the decision rule out loud for each case: every dimension at the next level,
sustained.

**For the next cycle.** Packets due a week before the meeting, with a minimum standard and help for
managers with bad weeks; independent readers assigned in advance; a cap on cases per session; random
or rotating order.

**Checking fairness afterwards.** Compare approval rates by team against nomination rates; look for
order effects (late cases declined more often); check whether decisions changed after a senior voice
spoke; ask two readers to re-score a sample of packets blind.

**Criteria for a good answer:** acts during the meeting, not only after; protects absent managers'
cases without lowering the bar. **Weak answer:** "let each manager present and trust their
judgment", which is the manager lottery.

## A2 — An outside offer and a request for Staff

Treat the two questions separately; joining them is the failure mode "promotion as retention".

**Promotion.** Her work is strong at Senior, and the staff criteria are new. Farah Haddad should say
that a promotion is decided by the evidence against the criteria in the next cycle, and that an offer
does not change the evidence. If her work already shows staff scope, help her build the packet now
and, if the organization allows out-of-cycle cases, take it through the same calibration. If it does
not, give a "not yet" with the five parts and a real opportunity.

**Pay.** The offer is market evidence. Check where she sits in the Senior band and against comparable
peers; if the offer shows that the Senior band has fallen behind the market, the fix is the band for
everyone at that level, funded properly. A pay adjustment within Senior can be justified on those
grounds. Chapter 10 owns whether to counter at all.

**What not to say:** "I'll get you Staff if you stay" (it promises what calibration decides), anything
disparaging the other employer, or a matching number before checking internal equity, which would
create a new gap with her peers.

**Defensible alternatives:** letting her go with goodwill, if the market evidence shows the offer is an
outlier and the gap cannot be justified.

## A3 — Hiring above existing peers

Senior midpoint is $152,500. The recommended offer of $165,000 is compa-ratio 1.08; the three Billing
seniors at $136,000, $139,750, and $141,000 are at 0.89, 0.92, and 0.92.

**The offer.** Verify the market data: if several sources and recent offer outcomes support $165,000,
the band itself may be stale. A reasonable offer is near the top of what the data supports, perhaps
$155,000 to $160,000, if candidates accept at that level.

**The existing seniors.** Adjust them in the same cycle. Taking them to 0.95 ($144,875) costs $8,875,
$5,125, and $3,875, total $17,875 in base salary. Without that, the hire creates a $20,000 to $30,000 gap
with people who will train the newcomer and share the same Billing on-call rotation, which is the compression the
chapter warns about.

**To the CFO.** Present the hire and the adjustments as one decision: the cost of the hire plus
$17,875, compared with losing one of three experienced Billing seniors (only one of them, Teodora Vasquez-Lund, a
ledger expert at baseline), whose replacement took a median of
15 weeks at baseline while the on-call load fell on the remaining few. The money is small against the
risk.

**Weak answer:** paying the new hire market and doing nothing for the existing seniors, or refusing the
hire's rate and leaving the role open while on-call load grows.

## X1 — Funding six equity adjustments

**The cost.** The 0.95 target is $144,875. The six (fictional) salaries are $132,000, $134,500, $136,000,
$137,000, $138,000 (Sunil Varghese), and $139,750. Gaps: $12,875, $10,375, $8,875, $7,875, $6,875, and
$5,125, total $52,000 in base salary, about $73,000 fully loaded if loading is 1.4 times base. That is
about 0.3 percent of Northstar's $16.1M engineering personnel budget.

**Funding.** Argue for a separate equity line, not a share of the merit budget: taking it from merit
would cut other people's raises to fix a gap they did not cause. If Rajiv Menon will not fund it this
year, sequence: the largest gaps first, and anyone whose retention risk is high or whose knowledge is
concentrated (Sunil designed the warehouse pipelines). A dated plan to close the rest within two cycles
is defensible; an open-ended "next year" is not.

**What to tell people.** The six: that the review found their pay below where comparable work should
be, the amount, and the date. Their peers: that a pay equity review now runs every cycle. Do not
present the adjustment as a reward; it is a correction.

**Risk of waiting.** Resignations from the most experienced internally grown seniors, and, where
equal pay law applies, a gap that could be challenged if it correlates with a protected characteristic.
**When to involve HR and counsel:** before finalizing, to check whether the gaps show any pattern by
protected group and what the law in each jurisdiction requires.

## X2 — Publishing pay bands

**Recommendation.** Publish bands internally, in sequence, within a year; do not publish first and
clean up later.

**Sequence.** (1) Finish the ladder and calibrate levels, so that everyone is in the right band. (2) Run
an equity review in each market (United States and Colombia separately) and fund the corrections. (3)
Agree with HR and employment counsel in both countries what must and may be disclosed, and how
pay-information requests will be answered. (4) Train managers to explain a person's position in the
band. (5) Publish bands and the criteria for movement, with a channel for questions.

**What must be true first:** every placement can be explained on job, equity, or market grounds;
level definitions are the same in both countries even though bands differ; managers can answer "why am
I here?".

**What to expect.** Fewer one-off deals; more requests for explanations; pressure from people low in
their band; less room for individual counter-offers. The equilibrium research
(Cullen and Pakzad-Hurson) suggests transparency can compress pay and weaken individual bargaining,
so expect complaints from strong negotiators.

**What not to claim.** That transparency will improve retention or engagement (no evidence verified
for this book shows that), or that it brings Northstar into compliance with any particular law;
counsel in each country decides that. **Weak answer:** "publish next month" or "never publish", without
a sequence.
