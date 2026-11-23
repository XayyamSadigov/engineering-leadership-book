# Chapter 12 solutions — Team Charters, Working Agreements, and Knowledge Sharing

Worked solutions for the [chapter 12 exercises](../parts/03-high-performing-teams/12-team-charters-working-agreements-and-knowledge-sharing.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Replacing a charter nobody uses

**What the existing charter does.** A long mission and a list of values describe the team's identity.
They may help in hiring conversations. They do not help anyone decide anything: no request can be
checked against them, no neighbor learns where to send work, and no decision is assigned. The direct
messages are the team's real interface, and the real charter is "whatever the person you know agrees to".

**A replacement, headings and first lines.**

| Section | First line |
|---|---|
| Mission | Two sentences: who the team serves and what result they get |
| Owns | Components, data, and processes, by name |
| Does not own | The things people assume the team owns, and who does |
| Disputed | Each disputed item, with a proposal and a date to resolve it |
| Interfaces | Where requests go (one queue), first-response time, what is self-service |
| Decision rights | The five or six recurring decisions, each with who decides and who is consulted |

Session one drafts mission, owns, and does not own from a sample of last quarter's work; session two
does interfaces and decision rights and plans how to tell requesters about the queue. Keep two or three
of the values only if they become observable working agreements.

**Criteria.** The answer explains that the old charter has no decision moment, puts boundaries and
interfaces first, and starts from actual work. **Weak answer:** rewriting the mission more crisply and
keeping everything else.

## F2 — Testing working agreements

| Agreement | Observable? | Rewrite or drop |
|---|---|---|
| We value quality | No | Drop, or replace with a specific one, such as "a tier 1 change without a test change needs a written reason in the review" |
| Reviews within 24 hours | Mostly; ambiguous about working hours | "First response to a review request within one working day"; checkable from review timestamps |
| No meetings on Wednesdays | Yes | Keep; say whether incidents and customer calls are exempt |
| Everyone documents their work | No: what, where, for whom? | Replace with "after a paired page, the learner updates the runbook the same week" |
| Be kind | No | Drop as an agreement; kindness is managed through feedback and behavior, not a rule nobody can check |

**Which to check first.** The review agreement. It is the one with data (review timestamps), it is the
one most likely to be broken by the most senior people, including the manager, and checking it in the
retrospective shows the team that agreements bind everyone. A strong answer may instead pick the
documentation agreement because it is the vaguest, which is defensible if the team has a knowledge
problem.

**Criteria.** Each agreement gets a test of how the team would know it was broken. The answer drops
some rather than rewriting all. **Weak answer:** keeping all five with better wording, which keeps the
list long and unenforced.

## F3 — Reading the truck factor from the map

**Whole ledger.** By headcount the ledger looks like a truck factor of three: three people can do
almost everything. But that hides the per-area picture. Per area, taking "change safely" as the test:

| Area | Respond alone | Change safely | Truck factor (change) |
|---|---|---|---|
| Posting and journal rules | 3 | 3 | 3 |
| Credit notes and adjustments | 4 | 2 | 2 |
| Period close and month-end | 2 | 1 | 1 |
| Ledger schema migrations | 2 | 2 | 2 |
| Currency and rounding | 1 | 1 | 1 |

The ledger as a whole is only as safe as its weakest tier 1 area, so for practical purposes its truck
factor is 1: one departure leaves period close and currency handling with nobody who can change them
safely.

**Why "three experts" overstates resilience.** It counts people, not coverage, and the three do not
know the same things equally. It also counts on availability: three people also take holidays and get
paged at the same time.

**Why a value of 1 does not give the cost.** Rigby and colleagues found that simple truck-factor
estimates exaggerate the potential for loss: the other experts could learn currency handling from the
code, more slowly and with more risk. The cost depends on how often the area changes (three times in
two quarters), how bad a mistake would be (customers' money), and how long relearning takes. The
truck factor tells you where to look.

**Weak answer:** "the truck factor is three" or treating 1 as certain disaster.

## A1 — Making the ledger two-deep

**Plan for one quarter (Marcus Oyelaran).** Areas and mechanisms:

| Area | Gap | Mechanism | Learners |
|---|---|---|---|
| Posting and journal rules | None for depth; all three are experts | Route reviews to learners | 2 |
| Credit notes and adjustments | Change: 2 | Learners drive the next changes; expert reviews | 2, including Tamsin Achterberg |
| Period close | Respond 2, change 1 | Monthly rehearsal of close in test; learner drives | 2 |
| Schema migrations | Change 2 | Learners write the next migrations with the migration check (Chapter 23) | 1 |
| Currency and rounding | 1 and 1 | Paired walk-through, then one planned change driven by a learner | 2 |

**Hours.** Each of the three experts pairs about four hours a week: 12 hours a week, about 156 in the
quarter. Learners spend roughly the same plus their own reading, say 200 to 250 hours across five or six
engineers. Rehearsals of period close: three half-days. In total about 370 to 440 hours, roughly 0.7 to 0.85 of an engineer-quarter,
which should be named in Billing's share of the prevention allocation.

**Restoration times.** Expect them to rise on low-severity pages routed to learners, and plan to keep an
expert first on Sev1 ledger incidents for the quarter. Say this to the director before the quarter
starts, so a rise is read as planned cost, not failure.

**Evidence of success.** Count who restored ledger incidents in the quarter, by area, and whether they
escalated; check that each area has two people who have actually done a change or a rehearsal; check that
Tamsin is on the rotation. Not evidence: the number of runbook pages written.

**Weak answer:** "write documentation for each area", or a plan with no hours.

## A2 — The script expert's leave

**In the six weeks.** Two things, in this order. First, try to pull retirement forward for at least
one service: if auth-svc, the tier 1 service, can move to the standard pipeline before the leave, the
risk during the leave falls most. This depends on Platform Operations' plan (Chapter 23); ask, do not
assume. Second, for whatever remains on the script, a second infrastructure engineer drives every
script deploy in the six weeks with the expert as navigator, including at least one rollback rehearsal
in a test environment (INC-416 showed rollback is the fragile path). The learner writes the checklist
after each deploy; the expert corrects it.

**Risk to accept during the leave.** Deploy only what must ship for the four script services, and freeze
changes to the script itself. Agree a way to reach the expert for a genuine emergency only if they are
willing, and do not plan on it.

**Avoiding the long untested page.** The output is a short checklist that the second engineer has used
successfully at least three times, plus one rehearsed rollback. If the page has not been used by
someone other than the expert, it does not count.

**Criteria.** The answer prefers removal where possible, uses doing over writing, and names the rollback
path. **Weak answer:** asking the expert to write everything down in their last week, or cancelling the
leave.

## A3 — The urgent direct message

**How the team responds.** The engineer does not do the work on the spot and does not refuse rudely.
They reply that requests go through the queue, put it there themselves to make it easy, and flag it to
Farah as urgent. Farah decides within a working day whether it jumps the queue, since accepting work out
of order is her decision under the charter's decision rights.

**Exception process.** The charter should say who can accept an exception (Farah, or her named delegate
when she is away), that every exception is recorded with the requester and reason, and that exceptions
are reviewed at the quarterly charter review. If the sales request is genuinely tied to a deal, Farah may
accept it; the point is that the decision and its cost are visible, not that the answer is no.

**Is the interface working after a quarter?** Measures: share of requests that came through the queue;
number and source of exceptions; first-response times against the two-day promise; points of capacity
spent on requests from other teams compared with the baseline 12. Each can be gamed: engineers can
quietly do direct-message work without logging it, so ask the team in the retrospective how much
off-queue work they did. Also ask Greg Tanaka's people whether the queue worked for them.

**Weak answer:** "tell sales to follow the process" with no exception route, or quietly doing the work
and leaving the charter untested.

## X1 — Should search-svc move to Data and Analytics?

**What the case says.** search-svc is nominally owned by Orders, disputed because its authors moved to
Data and Analytics. It is tier 2, has no runbook, partial alerts, and no on-call rotation, and INC-407 was
a search cluster node loss with nobody on call.

**Case for moving it.** The knowledge is in Data and Analytics, and ownership should follow the people
who can change the system safely. Orders, carrying the bulk-ordering commitment, loses a component it
does not understand.

**Case against.** Data and Analytics has little operational practice: its own export-svc has no runbook,
no alerts, and no on-call rotation. Search is a product-facing service rather than reporting, so moving
it adds an on-call surface, new consumers to manage, and a broader mission to a team whose draft charter
says it serves reporting and exports.

**What you would need to believe.** To move it: the team will take on-call and readiness work (runbook,
alerts, rotation) within a quarter, and the mission can grow to include search without becoming vague.
To leave it with Orders: Orders will fund learning it, with the original authors as reviewers, and the
dispute closes.

**Transition cost of moving.** Readiness work (runbook, alerts, rotation), perhaps three to four
engineer-weeks, plus a rewrite of both teams' charters and the on-call training. One defensible answer
is to move it with a dated readiness plan and a recorded exemption until it is met, as Northstar did for
core/permissions. Another is to keep it in Orders with named Data and Analytics reviewers for two
quarters. **Weak answer:** deciding by who complains least, or moving it without the readiness work.

## X2 — A truck-factor target for the operational review

**What the number would tell Victor.** Where to look: components or areas with only one capable person.
It would not tell him the size of the risk, since Rigby and colleagues found simple truck-factor
estimates exaggerate the potential for loss, nor which departures would hurt most, since loss is uneven.
It also depends heavily on how it is measured: from commit authorship (Avelino and colleagues' method,
validated on open source) or from managers' judgement.

**How it would be gamed.** Managers would list more names as "capable" than can actually respond or
change; a second reviewer added to a component would count without having done anything; components would
be split or merged to move the number. A target of 2 for every tier 1 component would turn a screen into
a score.

**What to report instead.** A short register of single-person tier 1 areas, each with its remedy
(retire, spread, or accept), a date, and evidence of progress: who actually restored or changed the area
last quarter. Report how many entries closed and how many are overdue. Keep the per-area maps in the
teams.

**Decision it should inform.** Backfill priorities, funding for retiring special tooling (the script
deploys), and the knowledge plan in any reorganization. If no decision changes with the number, it
should not be in the review.

**Criteria.** The answer separates screening from measuring, names gaming, and ties reporting to a
decision. **Weak answer:** accepting the target, or rejecting any reporting.
