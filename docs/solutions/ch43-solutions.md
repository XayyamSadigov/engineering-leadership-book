# Chapter 43 solutions — Leading Organizational Change and Director Failure Patterns

Worked solutions for the [chapter 43 exercises](../parts/09-engineering-directorship/43-leading-change-and-director-failure-patterns.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — A diagnosis for a single sprint cadence

**Outcome with a number.** The proposal names none. The closest real outcomes in the Northstar record are
reporting effort (delivery numbers assembled by hand, about two days a month) and the baseline roadmap
record (7 of 17 committed items delivered, 8 of the 10 misses cross-team). A diagnosis must pick one.

**Candidate mechanism.** If the outcome is cross-team misses, the mechanism the record supports is
dependencies (lead time 11 days with none, 41 days with two or more), not cadence mismatch. If the
outcome is reporting effort, the mechanism is the four CI systems and the absence of a deployment-event
store.

**Disconfirming evidence.** Cross-team items that missed while both teams already shared a cadence
would show cadence is not the cause. Orders and Billing already ran the same two-week Scrum aligned
to the release train, had the heaviest dependency link between them (9 links), and delivered 1 of 7
committed items between them at baseline; the first check is how many of those misses were items
shared by the two teams.

**Who sees it.** Elena Sokolova, whose Kanban team has the best delivery record, and Tom Becker, whose
interrupt rotation would be broken by sprints.

**Verdict.** The diagnosis does not support the proposal. A strong answer says what it would support
instead (shared planning dates and a common event store) and notes that Chapter 15 owns method choice.
The weak answer argues for or against sprints in general without stating a mechanism.

## F2 — Two misuses of the 70 percent figure

Both colleagues treat the figure as a known base rate. Hughes reviewed five published sources of it
and found no valid and reliable empirical evidence in any; he also argued that a single failure rate is
hard to define, because what counts as failure depends on context, perception, timing, and
measurement. So the figure supports neither "keep it small" nor "hire consultants".

The first colleague may still be right that the change should be small, but for a different reason: a
small pilot makes failure cheap and informative. Argue that from the change's own risk, not from an
unsupported statistic. The second inference is weaker still, since even a true failure rate would say
nothing about whether outside help lowers it.

What to define instead, for a Northstar change: the outcome measure (for example register entries
closed, or a fall in a named incident category), the checkpoint date, the threshold that counts as
failure, and who declares it. A strong answer also notes that defining failure in advance protects
against redefining it later. The weak answer replaces 70 with another number from memory.

## F3 — Assessing a director against three patterns

There is no single answer; the solution is judged on method. Take three patterns where evidence can be
observed, for example change by announcement, promise inflation, and decision vacuum.

For each pattern, evidence for and against must be events, not traits. Change by announcement: for,
"the on-call policy was first presented at the all-hands"; against, "the planning template went through
two drafts with managers' comments". Promise inflation: for, "three of the eight commitments made in
the last quarter slipped without notice"; against, "the two that slipped were renegotiated in writing
before their dates". Decision vacuum: for, "the dispute over the shared module waited six weeks";
against, "a decision log names a decider for each cross-team decision".

What would settle it: a count over a defined period rather than recollection, and a second person's
view (a manager reviewing the commitments list). A strong answer notices which evidence is missing and
says how to collect it. The weak answer uses adjectives ("decisive", "collaborative") or assesses only
patterns where the person looks good.

## A1 — Re-planning the Excellence Day intent

**Diagnosis.** Outcome: no priced register entry moved in quarter 3 through Excellence Day, and
register entries need more than a day of continuous work. Mechanism: ownership and continuity, not
free hours. Disconfirming test: if an entry with a named owner and two protected weeks still does not
move, the mechanism is something else (skill, a blocking decision).

**Carriers.** The leadership team meeting chooses which register entries matter most and which team
holds each. Amara Okafor agrees the capacity in quarter 4 planning, since it comes out of the 8 FTE
prevention allocation, not on top of it. The staff engineer for the domain reviews the scope.

**Pilot.** One volunteering team takes one register entry, one named owner and a second engineer, for
four weeks inside its prevention allocation. Measure: the entry closed or reduced to a stated
remainder, and no Sev2 caused by the work. Thresholds: closed, scale to two more teams; half done with
a known reason, adjust; untouched, stop and re-diagnose.

**Reinforcement.** If it works, the planning template gains a line for register entries with owners,
and the monthly managers' review reports them.

The weak answer reschedules the organization-wide day to avoid period close.

## A2 — The week 37 note

A strong note, under 400 words, has five parts. **What I intended:** keep debt and test-health work
moving as prevention fell from 12 to 8 FTE. **What happened:** participation 64, 41, then 23; 118 items
started, 71 merged, 52 of them under a day; 9 flaky-test fixes; no register entry touched; one Sev3 from
a day-1 refactor. **What I got wrong:** I diagnosed capacity when the register needed owners; I
launched without you; I picked a date without checking period close; I set no success measure at all.
**What stops and what replaces it:** the organization-wide day ends; teams may schedule fix-it time
inside their prevention allocation, which 29 of 52 pulse respondents preferred. **Two commitments:**
the next organization-wide practice change comes to this meeting and runs as a one-team pilot first;
one of you reviews my commitments list each quarter.

Two damaging sentences a weaker draft would include: "Participation fell because teams did not
prioritize quality", a denial that blames the people who exempted their teams for good reasons; and
"Overall the day was a success: 71 improvements", a redefined measure that the managers will recognize
as such. Both make the next proposal harder to believe.

## A3 — Responding to Marcus Oyelaran

**To Marcus.** Thank him and treat it as information, not disloyalty. Ask what would make the managers
act sooner: which past announcements they waited out and why. Do not ask him to name the two managers.

**What changes in how you propose.** Proposals come to the leadership team meeting as a diagnosis first, with the
solution designed there. Every proposal carries a stopping rule and a named person who calls it. The
change register is shared, so managers can see their load before anything is added. You make fewer
promises, and you keep them visibly: report each commitment's status at the monthly review.

**Evidence that credibility is returning.** Managers propose changes to your drafts (a sign they expect
to be heard). The lag between a decision in the leadership team meeting and action in teams shortens. A manager
raises a failing initiative before its checkpoint. The quarterly commitments review shows few slips.

A strong answer accepts that recovery takes at least a quarter and is shown, not claimed. The weak answer
holds a meeting to "reset trust" or asks managers to commit to acting faster, which is another
announcement.

## X1 — The account for Victor Lindqvist's staff meeting

**Structure:** one paragraph each for intent, result, cost, what was learned, and what changes.

**Concede.** The launch did not involve Amara Okafor or the managers, the date collided with period
close, and there was no measure. Those are the director's errors and should be stated as such.

**Defend with numbers.** "A lost week of roadmap" overstates it. Actual use was 128 engineer-days, 25.6
engineer-weeks, about 2 FTE over the quarter, about half the 48 engineer-weeks planned; it produced 71
merged improvements and 9 flaky-test fixes. The cost was real but bounded, and the initiative was
stopped after three days rather than defended.

**Ask of Amara.** That the next practice change is agreed with product before launch, with its capacity
inside the prevention allocation she already approved, and that product managers raise conflicts
through the leadership team meeting rather than by asking teams to skip. Offer her a seat in the
design of the pilot.

A strong answer keeps the account short and factual, separates the concession from the defense, and
turns the disagreement into a process agreement. The weak answer either apologizes for everything,
which invites the executives to discount the next proposal, or argues that roadmap impact was zero.

## X2 — A rule for directors' changes

**The rule.** Any organization-wide practice change carries a one-page card before launch: diagnosis,
affected managers with estimated weekly hours, outcome measure, checkpoint, stopping threshold, and a
named caller who is not the sponsoring director. Cards go into one shared change register across
directors. A change that pushes any manager's summed load above an agreed ceiling (for example, half
of a stated weekly slack) waits until another finishes.

**Detecting failure without fear.** Reward stopping: the CTO's review asks each director which change
they stopped or reshaped this quarter and what they learned, and treats "none" as a question, not a
virtue. Signals independent of the directors: a short quarterly pulse to managers on change load, and
the register's checkpoint results. A missed checkpoint triggers the decision diagram, not a blame
conversation.

**Fourteen managers under three changes.** Sequence them: the CTO and the three directors rank the
three, pilot the top one, and hold the others.

A strong answer makes the rule light enough to be used and places the stopping call outside the
sponsor. The weak answer adds an approval board for all changes, which turns the CTO into the
bottleneck the chapter warns directors against.
