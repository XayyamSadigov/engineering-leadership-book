# Chapter 2 solutions — From Individual Contributor to Leader

Worked solutions for the [chapter 2 exercises](../parts/01-foundations/02-from-individual-contributor-to-leader.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — "Not really doing anything"

**What is happening.** She is still being paid by the engineer's feedback loop and starved by the
manager's. Shipped work on time is the fast, clear signal she is used to, and it tells her little
about her own contribution, because a capable team of five would ship for a while under almost any
manager. The management work she is doing (or not doing) shows results in weeks or months, mixed with
noise, and through other people. The longer hours are a symptom: she is probably doing her old job
and the new one at once, and only the old one gives her a sense of progress.

**Three observable indicators**, each something she can count weekly:

- Decisions that waited for her for more than a day, and which of them someone else could have made.
- Areas only one person can handle (including her), and whether the list is shrinking.
- One-on-ones held against scheduled, and whether each produced anything the task tracker did not
  already show.

Other good candidates: delegated outcomes with an explicit level of control; time spent on
hands-on work against an agreed budget.

**Criteria.** A good answer explains the delay, attribution, and filtering properties and picks
indicators she controls and can observe directly. **Weak answer:** "track team velocity" or "ask
for feedback at the end of the quarter", which keep her steering by output or by a signal too slow
to act on.

## F2 — Choosing levels of control

One defensible set of choices, with the reasoning that matters more than the exact numbers:

- **Two-year engineer designing a new internal API: level 3 (intent).** Competent in the area; a bad
  API is costly to change once others depend on it, but the mistake is visible at design time. "Tell
  me your design before you publish it" keeps a checkpoint without taking the decision.
- **Same engineer, production migration rewriting pricing-rules: level 2 (recommend).** Same person,
  different area: a migration on a production table is hard to reverse, and Northstar's baseline
  shows migrations caused 3 of 30 incidents, including INC-419 in this very module (a pricing-rules migration that ran before the code deploy). The engineer writes
  the plan; the manager (or the data standard owner) approves it. This is still delegation, not
  withholding.
- **Staff engineer choosing the team's test framework: level 4 or 5.** Proven competence; the choice is
  reversible at moderate cost. Level 4 if the choice affects other teams.
- **New hire triaging customer-reported defects: level 2 for the first weeks, then 3.** Low context;
  a mis-triaged severity can hide a customer-impacting problem.

**Criteria.** The level is set per area, not per person, and follows both competence and
reversibility. **Weak answer:** one level per person ("she is senior, so level 5 on everything").

## F3 — "50 percent hands-on because Google says so"

The argument has a true premise and an invalid conclusion.

**On the evidence.** Google's re:Work page does list "have key technical skills" among ten behaviors
of effective managers. The same list includes empowering the team without micromanaging. It is
correlational research from one company, published without its data, and it says nothing about what
share of a manager's time should be hands-on. Technical skill can be exercised by reading designs,
asking good questions, and judging trade-offs, without owning the team's work.

**On the kinds of work.** The chapter's table separates work that keeps the manager able to judge
(reading, small off-path fixes, on-call participation) from work that makes the team wait (required
reviewer, owning committed features). Fifty percent is a warning sign mainly if it falls in the
second group. Ask which work it is, and what decisions wait on the manager.

**On respect.** Respect earned by out-coding the team is respect for an engineer. It can coexist with
frustration about blocked decisions, which the manager is the last to hear about.

**Criteria.** A good answer distinguishes skill from time spent, names the evidence's limits, and
proposes a test (decisions waiting, single-person areas). **Weak answer:** "managers should not code",
which ignores the credibility and judgment that technical engagement buys.

## A1 — Priya refuses to hand over the feature

**Learn first.** What exactly worries her: Aisha's competence in the upload path, the customer
relationship, or her own identity as the person who knows the code? What parts of the feature are
truly risky (the parser, pricing for large orders, the API contract)? What would she need to see in
a weekly checkpoint to trust the handover?

**What to accept.** Priya keeps design authority and the weekly checkpoint; Aisha leads implementation
at level 3, telling Priya before API or schema changes. A narrower handover is acceptable too: Priya
keeps one well-defined, off-critical-path component (say, the validation rules spec), while Aisha
owns the integration and the schedule. Pairing for the first two weeks is reasonable. The date
matters to the argument: with the feature due at the end of quarter 2, there are about two quarters
of runway, enough to notice and correct a weak handover. The same handover a few weeks before the
date would be a much worse bet, so the case for doing it now is strongest in week 2.

**What not to accept.** Priya remaining the implementer on the critical path while also managing 14
people, handling incidents, and taking on incident commander training and ownership changes. That
keeps the renewal dependent on the person with the most interrupt-driven calendar.

**If it slips three weeks later.** First diagnose whether the slip comes from the handover or from
scope and dependencies; slips have many causes. If it is the handover, raise support, not control:
more pairing, a narrower scope for Aisha, or Priya taking one bounded task with a handback date. Do
not silently take the work back; say what changed and why. Tell Amara Okafor early if the date is at
risk.

**Weak answer:** overruling Priya by authority, or giving in entirely because the date is important.

## A2 — Delegating to the passed-over candidate

**The delegation.** Give Rafael real ownership: review ownership of core/order-capture at level 4,
with Priya sampling his reviews for a month and then stopping. State the outcome (merge requests get a
first review within a day; review quality holds) and the end of the sampling period up front, so it
reads as a transition, not supervision.

**The history.** Priya should raise it herself, privately, before the announcement: she knows he
applied, she values him, and she wants to talk about what he wants from his career. Then listen. He
may still want management; he may want the staff track; he may be considering leaving. Each needs a
different response, and she cannot know which without asking.

**What not to promise.** A future management role, a promotion date, or that this ownership is a
step toward her job. She can promise honest feedback, real scope, and support in pursuing whatever
he wants, including talking to the director about the staff track.

**What to avoid.** Giving him the delegation as a consolation prize, or avoiding the conversation
because it is awkward. Silence on this topic is itself a message.

**Criteria.** A good answer treats the delegation as real ownership with a defined level, addresses
the history directly, and avoids promises Priya cannot keep. **Weak answer:** "give him more
responsibility so he feels valued", with no level, no conversation, and no question about what he wants.

## A3 — A 90-day plan for a new manager of eight

**Time budget (40 hours).** One-on-ones 4 (30 minutes weekly, all eight), team rituals 3, product and
cross-team 6, incidents 4, hiring 2, coaching delegated work 4, hands-on work capped at 10 (off the
critical path), unallocated 7. A smaller team allows weekly one-on-ones and a little more hands-on time.

**First three delegations.**

1. The first recurring incident pattern: an engineer owns the fix and its follow-up actions at level
   3 (tells the manager the plan before the change).
2. The quarterly deadline: a senior engineer leads implementation at level 3, with a weekly checkpoint.
3. Review ownership of any area where the manager was the required reviewer: two engineers at level 4.

The second incident pattern stays with the manager briefly, explicitly, as a learning item, with a
named second person and a handover date.

**Day-90 criteria agreed with their manager.** Every pre-promotion commitment reassigned or closed;
one-on-ones held at least 90 percent of the time; the single-person-area list shorter than at day 30;
decisions waiting more than a day down; the deadline on track or renegotiated openly; no recurrence of
the patterns, or a recorded interim control.

**How the plan fails.** Criteria can be gamed (one-on-ones held but empty). The manager's manager
should check a few directly in skip-levels.

**Weak answer:** a plan made only of technical goals, or one with no time budget.

## X1 — A program for future promotions

**Proposal, within flat headcount.**

- **Selection:** promotion to management requires evidence of multiplying others (mentoring, leading
  a project through people), not only engineering performance. The Benson, Li, and Shue study suggests
  why; a technical track of equal standing removes the pressure to promote the best engineer.
- **Trial:** a three- to six-month acting period with a defined end and a decision conversation.
- **Support:** each new manager gets an agreed time budget, a monthly check with their director on
  leading indicators, and a peer mentor outside the reporting line.
- **Handover:** pre-promotion commitments reassigned as part of the promotion.
- **Path back:** a stated, respectable return to engineering at the previous level, used without
  stigma. Announce it before anyone needs it.

Budget: mostly time. A small external training budget can come from discretionary spend.

**What to measure.** Share of first-year managers whose teams show improving engagement and stable
retention, measured against their own baseline; one-on-ones held. **Gaming:** managers avoid hard
feedback to protect engagement scores; retention looks good because poor performers are kept.
Pair with skip-level conversations.

**What not to promise the CEO.** A specific reduction in attrition or a delivery improvement.
The evidence is industry research from one company and economic research from sales, not engineering
experiments.

**Weak answer:** a training course alone, with no selection change and no path back.

## X2 — Is Priya a strong manager?

**Evidence to gather.** Orders' results, and how they were produced: how much of the critical work
Priya did herself, how many decisions waited for her, whether the single-person areas shrank, whether
the review ownership held. Skip-level conversations with several engineers. The resignation: the exit
conversation, and whether others say the same. Whether one-on-ones still happen.

**Possible findings and conclusions.**

- **Results were produced by Priya doing the work again.** The good numbers are borrowed from the
  future: the team is not growing, and the resignation is an early cost. She is a strong engineer in a
  management role who needs support and an honest conversation, not a verdict.
- **Results came from the team, and the hands-on time is off the critical path.** The 35 percent is
  less worrying than it looks; the resignation may be specific to that person. Check whether other
  senior engineers have room to grow.
- **Mixed.** Most likely. Reset the budget and the delegations with her, with the evidence on the
  table.

**Recommendation to Victor.** Do not answer from results alone. Report what the evidence shows about
how the results were produced, what you are doing about it, and when you will know more.

**Criteria.** A strong answer separates results from how they were produced and treats one
resignation as a signal to investigate, not proof. **Weak answer:** "results are good, so yes", or
"someone resigned, so no".
