# Chapter 23 solutions — Code Review, CI/CD, and Release Engineering

Worked solutions for the [chapter 23 exercises](../parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Two approvals after INC-427

**Evaluate the proposal against the evidence.** The research on modern code review finds that
defect-finding is the main reason people give for reviewing, but that review delivers fewer defects
than expected and more knowledge transfer, awareness, and alternative designs (Bacchelli and Bird).
Review coverage and participation are linked with fewer post-release defects (McIntosh et al.), so
review is not useless against defects. But INC-427, credit notes applied twice, is a behavior that
depends on data and on the interaction of a batch job with a release. A second reviewer reading a
diff is unlikely to see it.

**Cost.** Core changes already wait a median of 21 working hours for a first review. A second required
approval from a scarce senior group adds a second queue, lengthens branch life, and increases batch
size, which is the mechanism behind the train's failures.

**What to do instead.** Owner-based reviewers for invoicing and ledger (people who understand the
code), a turnaround norm for first response, a size guideline, and the checks review is bad at:
automated tests for credit-note application (Chapter 22), migration ordering checks, and flag rollout
for changes to billing behavior. Expected effect on lead time: turnaround and size reduce it; the
automated checks add minutes to the pipeline, not days.

A good answer separates review's real benefits from the defect-gate expectation and proposes controls
matched to the failure. The weak answer accepts "more review catches more bugs" or, at the other
extreme, argues that review is pointless.

## F2 — Five configuration-change incidents

| Incident | Missing property | Most effective control |
|---|---|---|
| INC-404, token lifetime changed in production config (auth-svc) | Everything as code; staged exposure | Configuration in version control with review, and a staged rollout of the change to a subset of sessions or instances |
| INC-410, flag enabled for all tenants instead of one | Staged exposure for flags | Flag service with default-off and explicit tenant targeting shown in the review; rollout per tenant |
| INC-412, template variable renamed, blank confirmations | Contract between components | A pipeline check that renders every template against the variables the code supplies (a contract check); also a user-facing alert, since a customer found it after 210 minutes |
| INC-416, shared deploy script broke rollback for four services | Everything as code; reversible, exercised | Deploy scripts in version control with review, and an automated test that exercises rollback in a staging environment before the script change ships |
| INC-430, rate limit lowered tenfold by a typo | Validation | Schema and bounds validation on configuration, plus a check that flags changes larger than a set factor for a second look |

**Knight Capital.** The controls that transfer are deployment verification (confirming that every
instance runs the intended version before enabling anything), never reusing a flag, deleting retired
code, second-person review of the deployment, and rehearsed rollback. The SEC order describes a
missed server, a reused flag, retained dead code, no second-person review, and a rollback that made
things worse.

A good answer treats configuration and flags as production changes and picks one control per
incident rather than listing every practice. The weak answer says "be more careful" or "add an
approval".

## F3 — Does a weekly train halve lead time?

**Not quite.** In the chapter's illustrative decomposition, a weekly train with a one-day regression
pass brings the median from about 19 to about 11.5 days, not 9. The colleague's arithmetic assumes
that every part of lead time scales with the interval. Only two parts do: waiting for the cut (7 days
to 3.5) and regression and release (4 days to 1.5). Missed trains shrink as well, because the next
train comes sooner.

**What a weekly train cannot fix** is the roughly five days between first commit and merge: review
waits, rework, and branch life. As cadence improves further, that becomes the dominant component; at
daily deployment it is five of about six days. Fixing it needs review turnaround, smaller changes,
and flags so that work can merge before it is finished.

**Which measure to watch.** Merge requests per release (batch size), which should fall from about 170
to about 85. Watch the lead-time distribution as well as the median: a train that carries a tail of
held-back changes can improve the median while the 90th percentile stays put. Deployment count alone
is the measure that misleads, because it can double while batches stay large if releases are split
artificially.

The weak answer either accepts the halving claim or rejects cadence as irrelevant. A good answer
decomposes lead time, states the assumptions, and names the next bottleneck.

## A1 — Main-branch policy for Core

**Diagnose first.** Before writing rules, show the data: the pipeline runs for 74 minutes on every
merge, 9 percent of runs fail for unrelated reasons, and the rerun calculation suggests flakiness may
explain most of the 22 percent red time. That reframes the problem from discipline to tooling, which
matters for the conversation.

**Policy.**

1. Revert first: anyone may revert a change that turned main red, without asking the author, within
   15 minutes of the red build being attributed to it. Fixes happen off main.
2. Same-day quarantine of nondeterministic tests, with an owner and a two-week deadline; a cap on the
   quarantine list, reviewed weekly.
3. A daily build steward, rotating across the teams that change Core, who watches main and makes the
   revert-or-quarantine call.
4. Red time and quarantine count on the weekly operational review.

**Ownership.** Infrastructure (Tom Becker) owns the pipeline's speed and reliability, including the
split into commit and extended stages. Module owners own their tests, including quarantined ones.
The three unowned Core modules need owners, or their tests will rot in quarantine.

**The conversation.** Introduce revert-first as protection for everyone's merges, not as a verdict on
the author: a revert is cheap, reversible, and says nothing about competence. Say that you expect your
own changes to be reverted too. The weak answer issues the rule by email or assigns ownership of red
main to infrastructure alone.

## A2 — A change process for payments-gateway configuration

**Design.**

- **Routine changes** (new flags, tenant targeting, most settings) go through a merge request in the
  configuration repository, with automated schema and bounds validation and one reviewer from the
  team. Flags roll out per tenant. The pipeline applies the change and records a deploy event.
- **Emergency changes** during partner-bank incidents use pre-approved operational controls: rate
  limits and kill switches with documented safe ranges, changeable by the on-call engineer through an
  audited tool without waiting for review. Anything outside the range goes through the normal path. An
  emergency change is converted into a merge request (or reverted) within one working day.
- **Hygiene:** every new flag has an owner and expiry date; the 23 entries older than a year are
  reviewed and either deleted or reclassified as permanent operational settings.

**How you will know it works.** Configuration-change incidents in payments-gateway (two last quarter)
should fall to near zero; lead time for a routine configuration change should stay within hours;
deployment frequency should not fall from 22 a month; the emergency path should be used rarely, and
each use should appear in the weekly review. Rising emergency-path use is the warning sign that the
routine path is too slow.

A good answer protects incident response speed explicitly. The weak answer either requires review for
everything, which pushes engineers back to editing files on the server, or exempts "small" changes,
which is what INC-430 was.

## A3 — Cutting regression to 600 cases

**How the subset is chosen.** By data, with the QA engineers' knowledge as the main input: cases that
cover components with train-triggered incidents (invoicing, ledger, order capture), areas of recent
change in the train being released, and paths behind the 81 regressions among last quarter's escaped
defects. Cases that have not failed in a long time on stable areas are candidates for automation or
retirement, not for the one-day pass.

**Who is accountable.** Not the QA engineer's signature. Accountability for a release sits with the
teams whose changes it carries and with the release working group that owns the process. QA's role is
to give the best risk information available, not to certify the release. Saying this explicitly
removes an impossible burden from the QA engineer.

**What to say.** Acknowledge the concern as legitimate: one third of the suite does mean less
coverage of rarely changed paths. Then share the evidence: the three-day pass caught none of the nine
train-triggered incidents, and its length is part of why each train carried about 170 changes. Ask
the engineer to lead the selection for their area, and agree a review after four weekly trains,
comparing escaped defects and train incidents with the baseline. Connect this to the role change
Chapter 27 describes (quality engineers in product teams).

The weak answer overrules the engineer with the data alone, or keeps the full pass and abandons the
weekly train.

## X1 — Responding to a request for a change board and a freeze

**In the meeting (short).** "I understand why you want a stop. I'll propose something faster and, I
believe, safer. A freeze makes the next release bigger, and the evidence on approval boards says they
don't lower failure rates; they slow everything down. What I'll do this week: every change to the
order and payment paths goes out behind a flag or canary, rolled out to our largest customer last;
irreversible changes get a named reviewer and a rehearsal; and you'll get a weekly one-page report on
changes, failures, and rollbacks. I'll accept a pause of a few days on Core while we confirm the
cause of this incident."

**Follow-up note.** It explains the batch-size mechanism with Northstar's own data (the two-week train
and its 31 percent failure rate), cites DORA's change approval findings with their correlational
limits, and proposes a change advisory board in the strategic role DORA describes: reviewing the
weekly change report, approving the rare irreversible changes, and resolving cross-team scheduling.
It states what would make Victor support a stricter gate: if progressive rollout fails to reduce
customer impact over the next month.

A good answer gives the CEO something concrete and visible, accepts a short targeted pause, and
avoids a standing gate on routine changes. The weak answer either agrees to the board and freeze to end
the meeting or dismisses the request with theory.

## X2 — One CI system now, or properties first?

**Recommendation: properties first for tier 1, with one exception.** Mandate the six properties for
all 15 tier 1 components within two quarters, and retire the shell scripts now. The shell-script
services are the exception because they fail the properties worst: they log nothing, one person
understands three of them, and INC-416 showed a shared script breaking rollback for four services.
Moving them onto one of the existing systems is the cheapest large risk reduction.

**What you give up.** Jenkins remains a shared single point of failure for a while (INC-428 stopped all
Jenkins deploys and its cause was never found), and the platform team keeps supporting three systems,
which costs effort and keeps metrics harder to compare. A full migration now would remove that cost
sooner, but it competes for the same engineers as the release-train work, which is the constraint.

**Budget.** Using existing licenses, the main cost is engineer time, not the $250,000 discretionary
budget. A paid tool beyond that needs the CFO's approval and a business case.

**What would change your mind after one quarter.** If teams on Jenkins cannot meet the properties
(automated rollback, deploy events) without disproportionate effort, or if another Jenkins-wide
failure occurs, consolidation should move forward. The weak answer chooses on tool preference instead
of on incident evidence and on the release-train constraint.
