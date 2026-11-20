# Chapter 29 solutions — Staff and Principal Engineers

Worked solutions for the [chapter 29 exercises](../parts/06-technical-leadership/29-staff-and-principal-engineers.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Classifying Northstar's staff engineers

| Staff engineer | Baseline | First quarter | Draft standing scope |
|---|---|---|---|
| Ines Carvalho | Solver by default: consulted on most Core changes, owning nothing | Moving toward architect (Core boundaries, contract tests, Core code standard) | Architect for Core |
| Kwame Mensah | Solver, pulled into the largest incidents | Architect for delivery (release working group, pipeline standards), with solver residue | Architect for delivery and reliability |
| Li Na Zhou | Solver, answering integration questions first-come | Architect for migration and configuration safety | Architect for data integrity, with a capped solver share |

**Evidence from the time sample.** Each spends 18 to 23 hours a week on mandated program work, which
looks like architect work, and 7 to 9 hours on unscheduled questions and pulls, which is the solver
pattern continuing. Ines's 5 unexplained rejections out of 8 add a critic signature that the archetypes
do not name. The gap between need and practice is largest for Li Na, whose nine unscheduled hours are
the highest of the three.

**Criteria.** A good answer uses the archetypes as descriptions of work, not of people, and notes that
the solver share is not wrong in itself; unbounded, it was. None of the three is a right hand, which
Larson associates mainly with very large organizations. **Weak answer:** labels by personality ("Ines
is an architect type") without the time evidence.

## F2 — Every design, every incident

**Diagnosis.** Both failure cases at once. Reviewing every design with nothing of one's own is the
roaming-critic shape; being in every major incident is the overloaded hero. The manager's praise is part
of the structure: it rewards the visible fix and the fast opinion.

**The structure.** No owned decisions, no stop list, and a manager who measures value by presence. The
loop in the chapter's first diagram: the more the engineer reviews and fixes, the more others route to
them.

**First three changes.** (1) Write a scope with one class of decision the engineer owns outright, for
example the area's boundary or data rules, and make the next quarter's outcome a design they author
and others adopt. (2) A stop list: reviews of routine designs go to named senior engineers, with the
staff engineer consulted on request; incidents only on a defined escalation. (3) Change what the
manager praises: problems that no longer reach the staff engineer, and designs others make against
their rules.

**Criteria.** Fix structure before the person; name what stops and who takes it. **Weak answer:**
"delegate more" or "set boundaries", with no named decision or receiving person.

## F3 — Measuring Li Na Zhou's impact

| Measure | Shows | How it is gamed | Pair with |
|---|---|---|---|
| Share of tier 1 data migrations rehearsed and passing the pipeline ordering check | Her migration rules are used | Classifying risky changes as non-tier 1 | Quarterly sample of three unclassified changes |
| Data, migration, and configuration standard decisions within ten working days | Her domain decides on time | Fast easy decisions, hard ones deferred or sent back | Count of reopened or escalated decisions |
| Integration contracts with versioning and contract tests (starting with the ledger export) | Her contract rules reach other teams | Contracts written but not run in the pipeline | Contract-test failures caught before release |

**Why not questions answered.** It rewards the hero pattern: the number rises as others depend on her
more, and falls when her rules work. If anything, unscheduled hours should fall, paired with a check on
who now answers and how well.

**Criteria.** Each measure is observable without asking her, has a named gaming route and a pair, and
reflects other people's behavior changing. A strong answer notes that domain outcomes (migration-related
incidents) are few and slow, so they support, not replace, the leading measures. **Weak answer:**
activity counts such as reviews done or meetings held.

## A1 — Ines blocks an Orders interface change

**Who decides.** Apply the rule. The core/customer boundary rules are inside Ines's draft owned
decisions, so whether the change conforms to the boundary is hers. Whether Orders spends capacity on an
alternative, and the bulk-ordering date, are Priya's. The conflict is between the two: a boundary
decision with a delivery consequence. That is the case the rule sends to the sponsor.

**What each writes, within days.** Ines: why the change conflicts with the extraction, what it would
cost to undo, and the smallest change she would accept (an adapter, a deprecated path with a removal
date). Priya: what the alternative costs bulk ordering against the week 26 date, and the risk to the
renewal. Both: the condition that would reopen the decision.

**If both appeal.** The director decides within the ten working days, in writing. A defensible
decision: allow the change behind an adapter Ines specifies, with a removal date inside the extraction
plan, because the renewal commitment is a constraint and the undo cost is bounded. If the adapter
cannot be specified in time, the renewal date wins and the extraction plan absorbs the rework, recorded
as debt.

**Criteria.** Uses the rule rather than seniority; protects the renewal; keeps Ines's ownership of the
boundary visible. **Weak answer:** the director rules on the technical merits personally, which
erases the scope a week after granting it.

## A2 — Ines's week 20 checkpoint

**Assessment.** Mixed and early. Reasons on rejections improved most (3 of 8 to 5 of 6), the behavior
she directly controls. One Orders proposal on a base of zero is a start, not a trend; six weeks is short
against a pattern that took years. Unscheduled hours fell from about eight to five, but the private
messages show part of the fall is displacement, the gaming route the plan predicted.

**Changes to the plan.** Keep the structure. Ask the two Billing engineers what the office hours do not
give them (timing, depth) and adjust the slots rather than forbid messages. Make the co-review with
Rafael Duarte produce a written boundary rationale Orders can reuse. Add one measure: proposals from
Orders that were accepted or accepted with changes.

**What to say to Ines.** Start with the specific improvement: "Five of your six rejections said why and
what would change your mind. Orders sent a design for the first time this year." Then the open issue,
framed as a design problem: "Some questions moved to private messages. What would make office hours
work for them?" Agree the week 26 targets with her.

**Criteria.** Reads small numbers honestly, spots the displacement, reinforces progress specifically,
keeps feedback on the task. **Weak answer:** declares success on the reasons measure, or treats the
private messages as Ines's failure.

## A3 — Kwame asks for principal

**Answer.** Not now, with reasons and a path. His results are real and staff-level: the weekly Core
release and pipeline failures unrelated to the change falling from 9 to 4 percent came from a working
group he led with owners from the teams. Principal, as this chapter defines it, is justified by a
company-critical domain over one to three years, usually with a VP or CTO sponsor. Northstar has had no
principal role since its principal architect left in 2021; it has 80 engineers, one product, and a
director sponsoring all three staff engineers. Recreating the level for one person is the
title-as-retention failure mode.

**What a principal role would need.** A domain larger than one staff scope and longer than the quality
program: for example, consolidating Northstar's four build and deploy systems into one, with
operational readiness for all tier 1 components, over several years, sponsored by Victor Lindqvist. A
written level definition through Chapter 8's process, and parity with the management track.

**Keeping him engaged.** Tell him what evidence would support principal if the role is created; give
him the standing scope with the build-system direction inside it; check his pay against the Staff band
now. Ask what he wants: some people asking for a title want scope or recognition.

**Weak answer:** yes because he is valuable, or no with no path.

## X1 — An external principal architect

**Advice.** Do not hire it now. Under flat headcount the hire uses a backfill, so a team loses an
engineer. The role would own "architecture" above three staff engineers whose domains together cover
most of it, so it would either take their owned decisions, undoing the scopes just written, or have
nothing to own and become a roaming critic with a higher title. The board's expectation is a reason to
explain the structure, not to add a layer. Northstar has tried this shape: when its principal
architect left in 2021, the monthly architecture review they chaired stopped and nothing replaced it
(Chapter 28), the concentration risk in its purest form.

**What it would cost beyond salary.** The backfill's lost capacity; months of context-building in an
11-year-old monolith; authority conflict with Ines, whose retention is already a concern; and the
signal to the three staff engineers that the top of their track is filled from outside.

**Instead.** Publish the three standing scopes and the fortnightly staff review, so the board sees
named owners for each technical risk. Name the gap honestly: no staff scope covers the frontends. If
a multi-year domain emerges (build consolidation, a Core boundary program), define a principal role
against it and consider internal candidates first.

**Criteria.** Uses the headcount constraint, the overlap test, and the retention risk; offers an
alternative that answers the board's concern. **Weak answer:** accepts the role because large
companies have chief architects.

## X2 — Rajiv asks what the staff engineers are for

**Answer structure.** Cost first, honestly: at the Staff midpoint of $195,000 against the Senior
midpoint of $152,500, three staff engineers cost about $127,500 a year more in base salary than three
Senior Engineers (3 × $42,500), less than one additional engineer. The real comparison is not three
staff engineers against four seniors; it is whether the cross-team problems they own would be owned by
anyone else.

**Evidence after two quarters.** For each, the owned decisions made on time and the pair measures; the
domain outcomes the first quarter recorded (Core change failure rate, pipeline failures unrelated to the
change, the migration check); and the fall in unscheduled hours, from 24 of 120 at week 13.

**What you cannot yet show.** That the outcomes would not have happened without them: most were team
efforts, and incident trends rest on few events. Say so.

**What would change the roles.** If after two quarters a staff engineer's owned decisions are rare or
routinely reopened, and unscheduled hours have not fallen, the scope is wrong: rescope or convert the
role, for example into a tech lead for one team.

**Criteria.** Correct arithmetic, honest limits, and a stated condition for change. **Weak answer:**
claims credit for the whole first-quarter improvement, or counts reviews and meetings.
