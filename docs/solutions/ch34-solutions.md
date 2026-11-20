# Chapter 34 solutions — Spans, Layers, and Dependency Mapping

Worked solutions for the [chapter 34 exercises](../parts/07-organization-design/34-spans-layers-and-dependency-mapping.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Scoring Northstar's spans

**One worked scoring, week 14:**

| Manager | Span | Factors that matter | Target range | Inside? |
|---|---|---|---|---|
| Priya Raman, Orders | 16 | First year as manager; still 8 hours a week hands-on; renewal work in flight | 6–8 | No, far above |
| Marcus Oyelaran, Billing | 15 | High incident load, three-person ledger expertise, heavy unplanned work | 7–9 | No |
| Elena Sokolova, Payments and Integrations | 13 | Experienced; strong practices; an informal tech lead; two sites | 9–11 | No, moderately above |
| Daniel Cho, Customer Experience | 17 | Two platforms, two sites, all mobile in Bogotá, mostly-status one-on-ones | 6–8 | No, far above |
| Farah Haddad, Data and Analytics | 11 | Acts as data architect (45 percent technical time), two sites | 7–9 | No |
| Tom Becker, Platform Operations | 5 | People work does not fill the job after the QA move | 8–10 | No, too small |

**Tom's span** is the one too small. A good answer does not invent work for him. Options: give him a
scope that grows his people work (for example the interrupt rotation's intake and self-service
roadmap, next to the auth-svc ownership he already holds), combine the manager role with
technical leadership deliberately, or plan for Platform Operations to grow back through platform work
rather than headcount.

**Criteria:** each range is justified from canon facts, not from a single number; the answer notices
that ranges differ by manager. **Weak answer:** "everyone should have eight", or treating Elena's 13 as
fine because her team performs well today.

## F2 — Removing the senior-manager layer

**Gains.** Using the chapter's illustrative model (about three and a half working days per hop), every
escalation that previously climbed engineer, manager, senior manager, director now stops one level
lower: about three to four working days saved per escalation. Information passes one fewer summary: at
80 percent per level, the director sees about 64 percent of what matters instead of about 51.

**Losses.** Fourteen managers is far above four to six. One-on-ones with each manager shrink or become
fortnightly; new managers lose their coach; the director's calendar becomes the queue. The latency
model assumes the decider has time: a director with fourteen reports and a weekly staff meeting may
add more wait per hop than the layer did.

**What would change the answer.** The dependency map. If the senior managers each covered a group of
teams that mostly depend on each other, removing them moves those frequent decisions up to a busier
person and the organization gets slower. If the groups were drawn arbitrarily, so that most links
crossed them anyway, the layer was adding a hop to most decisions and removing it is right. Also: how
many of the fourteen managers are experienced, and whether staff engineers or tech leads own technical
decisions.

**Weak answer:** treating flatter as faster without checking where the decisions actually go.

## F3 — Recounting a data-export move

**Assumptions (state them).** The canon matrix has Data and Analytics → Billing 2 and Billing → Data
and Analytics 2. Assume both Billing → Data links were month-end reporting changes Billing needed, and
one of the Data → Billing links was a ledger field the export needed; the other was unrelated.

**Recount.** If month-end export work moves to Billing, the 2 Billing → Data links become internal
and the 1 related Data → Billing link disappears: 3 removed. New links: the warehouse pipelines still
read the export, so any export format change now becomes Billing → Data or Data → Billing; assume 1
per quarter. Net about −2.

**Is it worth it?** On links alone, no: two links a quarter do not justify a boundary change. And it
adds work to a team at 41 percent unplanned with concentrated ledger expertise. What else to know:
whether the month-end path is a reliability risk (it was built by one engineer who moved on, a
key-person risk), whether Billing's customers of the report care about lead time, and whether a
contract on the export would remove the waiting more cheaply.

**Criteria:** assumptions explicit, recount includes created links, and the answer weighs span and
load, not just links. **Weak answer:** "it removes links, so do it."

## A1 — Talking to Priya about splitting Orders

**What to share.** That splitting Orders is one option in an analysis, not a decision; why it is on the
list (her span at 16 in her first year, more if web order-entry work or core/permissions moves to her);
that nothing changes before bulk ordering ships in week 26; and that whatever happens, she keeps a team
built around her domain depth. Say what the recount found: a split creates links between order capture
and pricing (about 4 items, and about 58 co-changing merge requests a quarter in Chapter 31's data), so it
is not obviously right.

**What to ask.** Where she thinks the natural seam is; which work last quarter crossed order capture
and pricing (she will know better than the matrix); what her span costs her today, in her own words;
who on the team might be ready to lead, and how she would handle the person not chosen.

**What not to promise.** That Orders will or will not be split. Who would manage a new team, before a
fair process (Rafael Duarte has asked about management; others may be interested). A team size.

**Criteria:** the answer treats Priya as a co-designer, separates analysis from decision, and keeps the
choice of any new manager out of a private conversation. **Weak answer:** presenting the split as done,
or reassuring her so fully that a later split feels like betrayal.

## A2 — Marcus objects to the contract

**Take the objection seriously.** It is partly right: a contract owned by Billing means Billing writes
and maintains the provider side, reviews changes to it, and is consulted when Orders needs a new field.
At 41 percent unplanned work, that is real load.

**Respond with a cost split, not a reversal.** Orders writes the consumer-side contract tests for its
own needs (the consumer-driven pattern); Billing owns the contract's definition and the provider
verification. Fund the first version from the prevention allocation, as a named piece of work, rather
than assuming Billing absorbs it. Agree a review rule: contract changes need a Billing reviewer within
an agreed response time.

**Should the choice change?** Compare with M3, moving the mapping to Orders. M3 removes more links but
moves invoice correctness away from the team that answers for the ledger, after a Sev1 in Billing in
week 9. Marcus's objection is about cost, not about correctness, so it argues for funding the contract
properly, not for M3. If Billing cannot staff even the provider side, the honest alternative is to
defer, not to move the mapping by default.

**Weak answer:** overruling Marcus because "contracts are best practice", or accepting M3 to make the
objection go away.

## A3 — Projected 4 links, actual 11

**Likely causes.** The projection used the baseline quarter's work mix; year-2 work (new pricing for bulk
orders, for example) may touch both sides far more. The seam may be wrong: pricing-rules may change
whenever order capture does, as Chapter 31's 53 percent co-change already warned. Orders' informal practice may persist (people still ask the colleague they
used to sit with, counted now as a cross-team link). Or the count changed: items that were internal are
now logged as links because the board split.

**First data.** The 11 links themselves, classified by component and reason, as in the chapter.
Whether they cluster on one interface (pricing-rules called by order-capture) or spread. The lead time
of items with these links compared with the previous quarter. Whether the matrix was built the same way.

**Decide.** If most links sit on one interface that changes for order capture's reasons, move that interface
to the order capture team (adjust). If they are spread and caused by one project, a one-off, wait one more quarter
with the recount scheduled. Reverse only if lead time and incidents are worse and the cause is the
seam itself; a reversal has its own transition cost.

**Weak answer:** reversing immediately on one quarter's count, or ignoring the gap because the span
problem was fixed.

## X1 — Victor at week 44

**One defensible decision.** Approve the recommended option of Chapter 35's proposal: it fixes the
worst span (Customer Experience at 17) for one seat, resolves two ownership questions, and adds no
layer. Approve it with named triggers rather than leaving the open items implicit:

1. **Orders.** Reopen the split (alternative C) if, two quarters after core/permissions arrives, Orders'
   span is above 16, its on-call load or lead time rises, or Priya's one-on-ones fall below every two
   weeks.
2. **Web and Mobile.** Require the matrix to count them as separate teams from week 53, so their links
   become visible; review after one quarter.
3. **Orders and Billing.** Require evidence that the order-to-invoice contract shortened waits (lead
   time of items crossing the pair, before and after). If not, the pair is a candidate for a shared
   manager or a boundary move.
4. **Layer.** No layer in year 2 unless the director's reports grow past about ten or the order-to-cash
   group's internal disputes keep reaching the director; the 27-inside, 48-outside count says a layer
   there would slow more links than it speeds.

**Evidence required.** The span table and dependency matrix rebuilt each quarter; one-on-one measures
for Orders and the two new teams; Rajiv's seat count kept current.

**Criteria:** each approval names its seat cost and each open item a trigger; the layer decision rests
on the matrix, not on the chart's look. Approving alternative B or C is defensible if the trade-offs are
stated. **Weak answer:** approving everything at once, or deferring everything because the evidence is
incomplete.

## X2 — "Why so many managers?"

**The answer.** Seven managers for 79 engineers is about 1 to 11.3, already above the range this book
and the practitioner sources cite for engineering managers (Larson's six to eight; this book's eight to
ten by default). Before the change, one manager had 17 people, with effects already visible
(one-on-ones mostly status, a lead without recognition), and three others are still above range. The
one new manager came from an engineering seat, not a new hire: headcount is still 87.

**What the flattening evidence says.** Rajan and Wulf found large US firms widened spans and removed
levels at the top, between division heads and the CEO. It says nothing about first-line spans of
engineers, and Gallup's data suggest that large spans hurt most where managers are less experienced,
work hybrid, or carry heavy hands-on work, which describes several Northstar managers.

**Signs of too many managers.** Spans below five without a reason; managers whose one-on-ones and
reviews leave most of their week empty; decisions that pass through a manager without being made there;
a layer that only forwards. Offer to report spans quarterly with these signs.

**Criteria:** answers with numbers, uses the evidence within its limits, and gives the CEO a test
rather than a defense. **Weak answer:** "engineering is different" with no data, or promising to
flatten to match a headline.
