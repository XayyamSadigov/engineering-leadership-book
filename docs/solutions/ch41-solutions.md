# Chapter 41 solutions — Managing and Developing Engineering Managers

Worked solutions for the [chapter 41 exercises](../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Turning impressions into evidence

**"Marcus is defensive about capacity."** Rewrite: "Billing's first response to testing ownership
(Chapter 19), flaky-test fixes (Chapter 22, week 4), and runbooks (Chapter 20) was 'no capacity'; after
the budget rule, Billing deleted 15 and rewrote 23 of its 38 quarantined tests." Dimension: running the
role (escalation judgment) and operational ownership. Note the second half: the evidence includes what
he did after objecting, which a judgment of character hides.

**"Elena is the best manager we have."** Rewrite into several items, each on its own dimension: payment
SLI built in two weeks (outcomes), operations review for two years with a near-miss log of 17 entries
(team health), the configuration-edit blind spot (operational ownership). "Best" is a ranking, which the
rubric forbids.

**"Daniel really cares about his people."** Rewrite: "84 of 90 one-on-ones held in weeks 14 to 19; 55
mainly status; 9 of 15 engineers had no career conversation." Care is real (45 percent of his time on
people); the evidence says the channel carries status.

**"Farah is too technical."** Rewrite: "45 percent of her time is technical as data architect (baseline);
technical direction lives with her." The case rates it "Expectation not set". This one needs a judgment about the role, not
the person: nobody told her which role comes first, so it is an unset expectation.

A strong answer notices that every rewrite names a source and date, and that the weak answer simply
softens the adjectives.

## F2 — Priya's rising hands-on time

**Rating.** "Not yet" on running the role is defensible: the cap of 8 hours was agreed in week 2, so the
expectation was known, and the trend (8, 10, 12) moves away from it as pressure rises, which is exactly
when it matters. A "Solid with a note" is also defensible if the director has explicitly agreed a
temporary exception, but no such agreement is recorded.

**Before the conversation.** Look at what the hours are: coding on the critical path, or answering
review questions (the skip-levels say reviewers are being pre-empted in chat)? Ask Aisha Bello whether
design decisions still come to her. Check whether risks to the week 26 date surfaced before the weekly
checkpoint or at it.

**What to agree for weeks 25 and 26.** Not a lecture on the cap two weeks before a renewal date. A
temporary, named exception (for example up to 12 hours on testing support only, ending week 26), review
questions routed to Rafael Duarte and Aisha Bello, and a reset to 8 hours from week 27 with a check in
week 32. That keeps the rule honest: exceptions are stated and expire.

The weak answer either accepts "it's temporary" with no end date, or insists on the cap regardless of the
date and loses Priya's trust at the worst time. A good answer also notes that Priya's behavior is the
pattern Chapter 2 predicted under pressure, so it is a coaching moment, not a failure.

## F3 — A skip-level round for Customer Experience

**Groups.** Chapter 40's rotation uses groups of three, each from one site and specialty: three web
groups (nine web engineers, Minneapolis and remote, the remote ones by video), the two quality engineers
as a pair, and two mobile groups in Bogotá; six groups, 17 places. Mobile should not be mixed with Minneapolis:
the health check showed that mobile's voice is lost when it shares a room with headquarters. Hold the
mobile sessions in Bogotá's working hours, ideally in person if the director can travel (there is no
travel budget line, so that is the director's decision to fund).

**Questions.** The four standard ones, so themes compare across teams and later rounds, plus none about the
structure decision. This will be the team's first skip-level round (Chapter 40), so open by explaining the rule. The director should not ask "should mobile be a separate team?": it invites lobbying
and implies a decision the director cannot make there.

**What goes back to Daniel.** Under Chapter 40's rule, themes always ("mobile still waits for decisions
made in Minneapolis"), quotes and attributions never; anyone who wants a confidential individual
conversation can ask for one. Hannah Lindgren and Mateo Arango Ríos, who are both informal
leads and development candidates, should not be singled out.

**What the director will not do.** Make or promise decisions, discuss individuals, or tell Daniel who
said what. If a group raises something only the director can fix (the structure, the travel budget), the
director says so and says when it will be decided. The weak answer runs one mixed session over video.

## A1 — Rating outcomes when the integration is late

The recorded result is on time (week 19, Chapter 39); this solution works the counterfactual and then compares.

**Elena.** The rubric rates outcomes in context and asks what the manager did about what she controls.
On the supposition, the slip came from the ledger export, which Billing provided. Elena's controllable
evidence is strong: she lowered WIP limits to protect the four integration engineers, defended them
against a sales request, and accepted contract-test blocking on a condition that caught a defect. A
"Solid" is fair if she surfaced the risk early (the director should check when she first said the date
was at risk); "Not yet" would be fair only if the date slipped silently. On time, the rating would likely
be "Strong". The difference between the two cases is mostly the system, which is why the rubric asks
about the warning, not only the date.

**Marcus.** Billing reserved weeks 1 to 3 for the export. If the export overran, the questions are
whether the reservation was protected from incidents, and whether Marcus told Elena and the director
as soon as he knew. The rating moves on the honesty and timing of the warning more than on the overrun.

**What separates contribution from system.** Dated evidence of when each manager knew and said; whether
the plan was sized against Billing's unplanned load; whether ADR-0001's open decision (which this
exercise does not resolve) delayed the work. The weak answer gives both "Not yet" because the date
moved, which teaches managers to hide risk.

## A2 — Marcus's quarter 3 plan

**The plan.** Focus: operational ownership. The objection is real (two experts critical, one with an
offer), so the plan must reduce risk now rather than ask for a large program.

- Delegated decision: Teodora Vasquez-Lund leads the TR-07 pairing plan at level 3, choosing which two
  non-ledger engineers pair on credit notes and posting rules, the two areas with the most changes.
- Marcus joins ledger incidents only as incident commander, which frees about the hours he spent as an
  additional responder at baseline and models the rotation.
- Check in week 38: a recount of the knowledge map; success is at least one new person able to respond
  alone in one area, not a target across all five.

Pairing during incidents costs little extra time, because the experts are already there; the cost is a
slower response in the first weeks, which should be stated to Elena and the director.

**If he declines.** Ask what he would do instead to reduce concentration this quarter; his alternative
is evidence for the running-the-role dimension. If there is no alternative, the director states the
expectation in writing and rechecks next quarter; after two quarters of "Not yet" despite a plan, the
Chapter 9 process applies. Tomasz's offer remains a separate decision (Chapter 10). The weak answer
removes the plan because Billing is busy, which keeps it busy.

## A3 — Tom contests his rating

**Keep the rating, change the record.** The evidence for "Not yet" on people growth is a nine-month
pattern: 31 of 74 tickets moved without a conversation, a "meets expectations" review, two colleagues
covering. His quarter 2 proposal is good evidence of his response and belongs in the same cell, dated.
Raising the rating because the response is good would erase the pattern the rating exists to show.

**How to record it.** "Not yet; response strong. Baseline quarter: gap managed around rather than raised.
Quarter 2: specific, fair expectations proposal drafted after reconstructing Bram's time." Was the
expectation known? Raising performance problems with the person is a basic part of managing at any
company, and Northstar's annual reviews existed, so the unset-expectation rule does not apply. That
judgment is open to argument, and a good answer says so.

**What Tom shows by week 38.** That any new performance gap was raised with the person within two weeks,
that nobody in the skip-level reports work being moved silently, and that Bram's plan, whatever the
director decides about it, is run as written with weekly checks. On HR: tell Tom honestly how the rating
will be used; if this cycle feeds pay, the director should say how the response is weighed.

The weak answers are to soften the rating to avoid conflict, or to treat the rating as a verdict on the
Bram decision, which is still open.

## X1 — A ranking and a successor

**The ranking.** Refuse to produce a single ordinal ranking, and offer what pay decisions actually need:
for each manager, the six ratings with evidence, a statement of performance against stated expectations,
and the director's recommendation. Reasons to give Victor: the teams sit in different places in the
system (two ship through the Core train), five cells are "No evidence", two "Not yet" ratings
are against expectations the director never set, and rater effects are large enough that an ordering of
six people by one rater would be mostly noise. If Victor insists on a pay distribution, the director can
place managers in bands (for example, above or at expectations) with evidence, which is a judgment the
director can defend.

**Payments and Integrations.** The evidence says its only cover is the informal tech lead, who is
interim cover and holds the team's technical direction. Chapter 36's coverage rule calls that inadequate.
The honest answer: nobody is ready now; the informal tech lead could keep it running for weeks; the
quarter 3 plan starts building that person's management evidence. If Elena moves soon, the director
should plan a period of closer support for the team rather than promise a successor.

**What to refuse.** A ranking, and naming a successor who has not been asked. The weak answer produces
the ranking with Elena first and Marcus last, which reproduces the activity scorecard Chapter 4 warns
against.

## X2 — External program or internal cohort

**Recommendation: the internal cohort**, possibly with an external facilitator for one session. The
meta-analysis (abstract level) favors needs analysis, practice, spaced sessions, on-site location, and
face-to-face delivery. The internal option has all five: the rubric gaps are the needs analysis, the
sessions can be built around practice on real Northstar decisions, they are spaced three weeks apart
with a job assignment between them, and they are on site. The external program is face-to-face but
massed into one block, off-site, and generic.

**Cost, illustrative.** External: 6 × $8,000 = $48,000, plus 30 manager-days away (6 × 5) in one week,
which is a real risk with a renewal date and Billing's on-call load. Internal: 12 manager-days (6 × 4
half-days) spread over about three months, 4 director-days of preparation plus 2 days of delivery, and
little cash. Rajiv Menon wants flat operating expense, which also favors the internal option. A
defensible alternative is to send one manager (for example the bench candidate for director cover) to an
external program for the peer network, alongside the cohort.

**Knowing in two quarters.** Re-rate the dimensions the cohort targeted against the week 24 baseline,
read the next skip-level round for the same themes, and check whether each manager made the delegated
decision the session prepared them for. The weak answer measures only satisfaction with the sessions
(the research's "reactions" criterion), which is the furthest of the four criteria from behavior on the job.
