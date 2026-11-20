# Chapter 13 solutions — Decision-Making in Teams

Worked solutions for the [chapter 13 exercises](../parts/03-high-performing-teams/13-decision-making-in-teams.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Choosing the method

| Decision | Method | Decider | Reason |
|---|---|---|---|
| Rename an internal library | Delegate | The engineer or pair doing the work | Reversible, low stakes, information sits with the people using it |
| New message broker for three teams | Consult, with written input first | One named decider above the three teams (a staff engineer or director) | Hard to reverse once data flows through it; three teams carry it |
| On-call swap policy within a team | Consent with an objection window | The team | A team agreement; everyone must live with it, and nobody has a conflict of interest |
| Ship a reversible flag change today | Delegate, or decide quickly | The owning engineer, informing afterward | A two-way door: the flag makes being wrong cheap |
| Retire a public API version | Consult widely, owner decides, with a dated record | Product and engineering owner of the API | One-way door for customers; stakes outside the team |

A good answer explains each choice by reversibility and stakes rather than by importance alone, and
notices that the broker and API decisions are where reversibility can be bought (a parallel run,
a long deprecation period). It also names a person, not a group, wherever one person decides. The weak
answer gives consensus to the two big decisions because they are important; that hands three teams a
veto over the broker and lets the most persistent team choose. Another weak answer delegates the API
retirement to the team because "they own the code", ignoring that the people who carry the cost are
customers outside the team.

## F2 — The consensus team

**Diagnosis.** The team uses consensus as its only method. Inside the team it feels pleasant because
most decisions are uncontested. For contested decisions it becomes a veto, which is the "consensus as
veto" failure mode: the two cross-team decisions stalled because consensus across teams gives every
participant a veto, and there is no named decider. The engineer's remark is a false-consensus signal:
she has stopped objecting, not started agreeing. The team is happy partly because conflict is being
suppressed, which is exactly when apparent agreement is least reliable.

**First change.** Name the method for the two stalled decisions: one decider each, consult the
people affected, set a date. That is the change with immediate value, and it shows the team that
"consult" is not autocracy. Second, introduce consent for team agreements, with an explicit rule that
an objection must state a harm, so that objections are welcomed but bounded. Third, talk privately
with the engineer and invite her objections in writing before meetings.

A good answer separates the two problems (no decider across teams; suppressed dissent within the team),
protects the engineer's confidence, and does not abolish consensus by decree. The weak answer tells the
lead "you are too slow, decide yourself", which fixes speed and worsens the suppressed dissent.

## F3 — The silent design review

**Why it happened.** The junior engineer held unshared information (knowledge of the downstream
consumer). Hidden-profile research finds that discussion dwells on information members already share
and on information that supports existing preferences, and that groups often fail to pool unique
information (Stasser and Titus; Lu, Yuan, and McLeod). Three features of the review made it worse:
the most senior person presented and spoke first, comments were requested in the open with no
structure, and silence was read as agreement. The person with the decisive fact was also the person
with the least status, so offering it carried the most risk.

**Redesign.**

1. Circulate the proposal two days before, and ask every reviewer for written comments, including
   "what do you know about consumers or dependencies that others may not?"
2. Name the decider and the method at the start ("I decide after consulting you").
3. In the meeting, ask the people closest to affected systems first, and the senior presenter last.
4. Replace "any objections?" with a round: each person states one risk or says they have none.
5. Record the decision with its assumptions, and send it for objections within a day.

A good answer explains the mechanism, not just "make people speak up", and notes the research limit:
laboratory tasks with correct answers, so the transfer is a warning, not a measurement. The weak answer
blames the junior engineer for not speaking.

## A1 — The decision brief for core/permissions

A strong brief, one page, contains:

**Decision.** Which team owns core/permissions (tier 1), and on what interface and review terms.

**Method and roles.** Consult; the director decides. Driver: someone without an ownership stake who can
keep the date; Ines Carvalho is a defensible choice because she leads the quarter's permissions
extraction and owns Core code standards, but the brief should say that she has an interest in the
extraction's success. Contributors: Priya Raman, Tom Becker, Kwame Mensah (owner of the on-call
minimum and of the exemption's domain). Informed: the other four managers and the staff engineers.

**Deadline.** A date in the first weeks of quarter 2, well before the extraction lands, stated in the
brief. The exemption's two-quarter maximum is an outer limit, not the target.

**Options and costs.**

| Option | For | Against |
|---|---|---|
| Orders now | 17 of 38 changes; owns core/customer; Core review skills | Bulk ordering due week 26; notification-svc arriving |
| Platform Operations | Next to auth-svc; identity coherence | No Core Java skills among five engineers; zero changes |
| Orders after week 26, interim named reviewer pair | Respects the renewal | Keeps the exemption alive through the extraction |
| Split: Orders owns code, staff engineer owns interface | Separates the skills | Two owners; the review gap the X2 scenario describes |

**Information still needed.** Expected change volume from the extraction; who would be on call for the
module and at what load; what the 21 changes from other teams were.

The weak answer takes the decision in the brief, or lists options without costs, or leaves the date
open, which reproduces the avoidance it is meant to end.

## A2 — The decision record

One defensible record, choosing Orders with a staged start (other choices are equally acceptable if
argued):

- **Decision and date.** core/permissions owned by Orders from the start of quarter 2; on-call joins the
  Orders rotation after bulk ordering ships in week 26. Decided by the director after consulting Priya
  Raman, Tom Becker, Kwame Mensah, and Ines Carvalho.
- **Options rejected.** Platform Operations: no Core Java capability among its five engineers and no
  changes in the baseline quarter. Deferring the whole decision to week 26: leaves the extraction landing
  in an unowned module.
- **Assumptions.** Orders' change share stays near the baseline 45 percent; review load from other teams
  stays below an agreed number of merge requests a week; the extraction narrows the interface.
- **Consequences, including negative.** Orders' load rises during the renewal; Orders reviews the
  majority of changes, which come from other teams; the exemption is closed when on-call starts.
- **Review trigger.** If Orders' review wait for core/permissions changes exceeds a stated threshold for
  two consecutive months, or another team's share of changes passes Orders', reopen.

Criteria: the assumptions are testable from data Northstar already collects, the trigger names a signal
and a threshold, and the negative consequences are stated. The weak record says "Orders owns it because
they make most changes" with no assumptions and no trigger, which a successor can only obey or reverse
blindly, the outcome Nygard's format was designed to prevent.

## A3 — Kwame's fast queue

**What is happening.** The ten-working-day rule works, so people route decisions to the one place that
answers. Ownership questions are not in Kwame's domain: component ownership is assigned at the
director's level. If Kwame answers them, he acquires decision rights nobody gave him, and his
operational queue slows. If he refuses without a route, the questions go back to drifting.

**What Kwame should do.** Accept each request into a log, answer the standards part if there is one
(for example, whether a compensating control is acceptable while ownership is open), and forward the
ownership question to the director's open-decisions list with the requester copied. He should not
decide ownership, and he should not let the exemption register become the place ownership questions
wait.

**The design change.** Give ownership decisions their own owner (the director) and their own service
level, for example ten working days to a decision or to a dated plan, and publish it beside the
standards owners. Add a rule that an exemption tied to an open decision carries a fixed date, not
"until the decision". Review the list weekly.

A good answer sees that the fast queue is a symptom of a missing queue, not of Kwame's helpfulness.
The weak answer tells him to say no, or makes him the owner of ownership decisions, which moves the
bottleneck to a person without the authority to move engineers between teams.

## X1 — Cross-team decision rights at Northstar

**Design.** A one-page decision-rights map for recurring cross-team decisions:

| Decision class | Decider | Consulted | Service level |
|---|---|---|---|
| Standards and exemptions | Domain staff engineer (existing) | Requesting team | 10 working days (existing) |
| Component ownership | Director | Candidate managers, relevant staff engineer | 10 working days to a decision or dated plan |
| Interface changes to shared modules | Owning team's manager | Consuming teams | 5 working days |
| Roadmap conflicts between teams | Director with the CPO | Managers involved | Next weekly leadership meeting |
| Architecture across teams | Left to Chapter 28's design | | |

Plus an open-decisions list reviewed weekly, and a shared decision log.

**Reporting to Victor Lindqvist.** Monthly: open cross-team decisions past their service level, which
commitments they block, and exemptions tied to open decisions with their dates.

**Gaming.** Deciders meet the service level with a "dated plan" that is itself deferral; count plans
that slip. Teams avoid filing requests and decide informally; sample merge requests for undeclared
cross-team changes. Managers frame decisions as reversible to avoid consultation.

**Cost.** Perhaps a few hours a week of the director's time in the first quarter, and some friction
as managers find informal authority written down.

**Deliberately undefined.** Architecture decision rights (disputed; owned by Chapter 28), and decisions
inside teams, which stay with managers.

A good answer is small, names deciders not committees, and includes its own failure modes. The weak
answer creates an architecture review board that approves cross-team changes, which Chapter 20 shows
becomes a queue.

## X2 — The Sev1 and the unchecked trigger

**Evidence.** The incident review (blameless, per Chapter 25): which change, who reviewed it, what each
team believed about review responsibility. The decision record: what it said about review terms, the
review trigger, and who was meant to check it. The change history: how the share of changes by team had
moved since the decision. Whether the trigger's threshold had in fact been crossed.

**Answer to Helena Marsh.** Be precise. The decision was made, recorded, and assigned an owner, so the
process did not fail at deciding. It failed at follow-through: a review trigger with no named person
and no cadence is a wish. If the record also left review responsibility for other teams' changes
ambiguous, say so; that is a defect in the decision itself. Do not claim the decision caused the
incident without the review's evidence.

**Changes.** Give every review trigger an owner and a place on a recurring agenda (the open-decisions
review); add an explicit review rule for changes from non-owning teams to shared modules, enforced by
code-owner configuration rather than belief; reopen the ownership decision if the trigger had fired.

A good answer separates decision quality from outcome, owns the follow-through gap, and changes a
mechanism. The weak answer either defends the process because a record existed or concludes that
recording decisions does not work.
