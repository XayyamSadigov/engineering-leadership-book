# Chapter 6 solutions — Feedback, Conflict, and Difficult Conversations

Worked solutions for the [chapter 6 exercises](../parts/02-people-management/06-feedback-conflict-and-difficult-conversations.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Rewriting vague feedback

**"Be more of a team player."** Rewritten: "In Monday's planning, when Lee asked for help with the
export job, you said it wasn't your area and went back to your ticket. Lee spent the afternoon stuck.
What was going on for you at that point?" To say this you need to have seen or reliably heard about one
concrete event. If you only have a general impression, the honest move is to watch for an instance, or
to ask others what they have seen, not to deliver the impression.

**"Your code quality has slipped."** Rewritten: "Your last three merge requests on invoicing went out
without tests for the error paths, and two needed follow-up fixes after release. What's changed?" You
need the merge requests in front of you. The question may reveal a cause (deadline pressure, unclear
standards) that changes what you ask for.

**"Great work on the migration."** Rewritten: "Running the migration against a production-sized copy
first found the table lock before customers did. That's what I want on every ledger migration." Positive
feedback needs the same specificity, or the person cannot repeat what worked.

A good answer keeps each rewrite to one event and its effect and ends with a question or a clear
request. The weak answer replaces one adjective with a gentler adjective ("collaboration could improve").

## F2 — Feedback after every sprint

The practice gets the timing right and the target wrong. Kluger and DeNisi's meta-analysis found
feedback improved performance on average but decreased it in more than a third of interventions, and
their theory, supported by moderator analyses, is that effectiveness falls as attention moves from the
task toward the self. Feedback "on attitude and commitment" is aimed squarely at the self: it asks the
person to defend who they are rather than change what they did.

What to change: keep the frequency, but restrict the content to observed behavior and its effect on the
work. Replace "you don't seem committed" with the event that produced the impression ("you missed the
last two refinement sessions without notice, and the estimates went ahead without your input"). Drop
routine feedback where there is nothing specific to say; a fixed ritual produces generic content.

A strong answer also states the limits: the meta-analysis pools many settings, dates from 1996,
and does not give a number for software teams. What it supports is the direction, not a dose. The
weak answer either endorses the practice because "research says feedback works" or rejects frequent
feedback altogether, which throws away the part the manager got right.

## F3 — Classifying disputes

**Event sourcing for the ledger: task conflict.** Both engineers argue about the content of a design;
the evidence they bring is technical. Response: a written comparison, a named decider, a deadline.

**Who fixes flaky tests in a shared suite: process conflict.** The dispute is about ownership of a
shared system. No amount of goodwill settles it, because neither team owns the suite. Response: assign
ownership (Northstar's release working group gave each quarantined test an owning team and a fix-or-
delete deadline).

**The senior engineer whose design was presented by a junior colleague: status conflict.** The evidence
is about credit and recognition. It may hide a process question (who presents designs to the CTO), but
the hurt is about standing. Response: private conversations first; then fix the norm on attribution.

**Shipping a known rounding error for a renewal date: values conflict.** Both sides can agree on the
facts and still disagree, because they weigh customer trust in financial correctness against a
commercial commitment differently. Response: make the trade-off explicit (who is affected, how
detectable, how reversible), decide at the level that owns the risk, and explain it. At Northstar,
wrong financial records visible to customers are Sev1 under the week 3 definitions, which partly
settles it.

A good answer names the evidence that decided each classification and notes mixtures. The weak answer
labels everything "communication".

## A1 — Preparing Marcus for the conversation with Teodora

**Purpose.** Teodora understands that naming another team as the cause, in public, before the facts
are known, is not acceptable, and agrees what she will do instead. Separately, she hears that the
on-call load is being addressed, with specifics.

**Facts and story.** Facts: the post after INC-417; the opening statement in the INC-427 review; the
recorded contributing factors, which do not name a team. Not known: whether an Orders change did
contribute (nobody recorded attribution), how many nights she was paged that week.

**Her view.** She has been paged at night for a year by failures arriving through a process she does
not control, and management's responses were a stipend and "document as you go". Her anger is
evidence of a real problem. Marcus should say so before anything else.

**Non-negotiables and negotiables.** Non-negotiable: no public blame of a team before a review has the
timeline. Negotiable: how she raises concerns about other teams' changes (directly with Marcus, in the
review's contributing-factor discussion, through the release working group).

**If it goes badly.** If she says management ignored the load for a year, Marcus should agree where it
is true, not defend past decisions, and name what changes now: the 25 percent prevention allocation,
the release working group, and a date for getting the ledger backfill onto the rotation. Then return to the behavior: "Both are
true. The load is real, and the post still did damage." If she is too angry to continue, pause and
resume within two days.

A good answer separates the grievance from the behavior and addresses both. The weak answer either
skips the behavior because she is overloaded (ruinous empathy) or lectures her without acknowledging
the load.

## A2 — The first joint session

**Attendees.** Engineers from both teams who work on Core boundaries (including Teodora and the Orders
engineer from the thread), both managers, a staff engineer (Ines Carvalho for Core, or Kwame Mensah who
leads the release working group) as facilitator. Not the director as chair: the director's presence
turns it into an escalation.

**Evidence on the table.** The incident list for Billing (seven of eight through releases or
migrations), the contributing factors from the reviews, the fact that nobody recorded which team's
change triggered each incident, and the release changes now under way.

**Output.** A short list of boundary agreements: which tests at the invoicing and ledger boundary each
team owns, how a team is told when another team's change touches its tables, and a rule that incident
reviews record the triggering change before discussing cause.

**If it turns into grievances.** Do not suppress it entirely; some of it needs to be heard. The
facilitator writes each grievance on the shared screen, asks "what in the system made this possible?",
and moves it into the process column. If one person attacks another personally, the facilitator stops
that exchange and takes it offline with each manager.

A strong answer designs the session around the process layer, because that is where the conflict
started. The weak answer is a "team-building" session with no evidence and no output.

## A3 — Feedback about feedback

Start with evidence, not culture. Collect two or three specific examples from the skip-levels (with
permission, and without identifying who said what) where engineers did not realize they had been
criticized. Then, in a one-on-one: "In three recent cases, engineers didn't realize you were asking them
to change something. For example, you told one that their design 'might benefit from another look'; they
heard approval. What did you intend them to take away?"

The aim is not to make the manager adopt a different style, but to make the message arrive. Offer the
two techniques from the chapter: ask each engineer how they prefer to hear criticism, and end each
conversation by asking what they will take away. The second gives the manager immediate evidence of
whether the point landed, without changing their personality.

Evidence of change: in the next round of skip-levels, engineers can name something their manager asked
them to change, and the manager's written reviews contain nothing the engineer hears for the first time.

A good answer adapts its own delivery to this manager, treats national culture as a hypothesis rather
than a diagnosis, and holds the standard (people must know where they stand). The weak answer either
tells the manager to "be more direct" (unusable) or excuses the gap as cultural and changes nothing.

## X1 — The CPO and CTO disagree

**Diagnosis.** This is a values conflict layered on a task question. The task part (how long the
reconciliation work takes, what risk remains without it) can be estimated. The values part (how much
risk of wrong financial records is acceptable to keep a customer date) cannot be settled by data.

**Structure of the recommendation.** One page. The decision being made. The facts both sides agree on.
The options (delay three weeks; ship on time with a mitigation such as daily manual reconciliation;
ship on time and accept the risk), each with its cost and its risk stated in the same units where
possible. Your recommendation and the reasoning. What would change your recommendation. Wrong financial
records visible to customers are Sev1 at Northstar, which is a fact the recommendation should state.

**If the CEO splits the difference** (for example, a one-week delay), ask what the one week buys. If it
buys nothing that reduces the risk, say so, in writing, once, and then execute the decision. Record the
risk explicitly as accepted by the CEO. Do not relitigate it in every meeting.

A good answer separates the estimable part from the value judgment and makes the trade-off explicit for
the person who owns it. The weak answer picks a side and argues it as if the data alone settled it.

## X2 — Blame at the start of cross-team reviews

**Diagnosis.** A 40 percent rate of reviews opening by naming another team is a symptom of process
conflict at team boundaries turning into relationship conflict, and of a review process that lets
attribution precede the timeline.

**Review process.** Require the timeline and the triggering change before any discussion of cause (see
Chapter 25 on blameless review). Make the triggering change a recorded field, so that attribution
becomes data rather than argument. Rotate facilitators from outside the involved teams.

**Measurement.** Track the share of cross-team reviews where the first contributing factor names a
team, and the share where the contributing factors include a system or boundary factor. It is gamed
easily: people stop naming teams in writing while continuing in private channels. So pair it with
skip-level questions about inter-team trust and with recurrence at the same boundaries, which is harder
to fake.

**Director behavior.** Directors should treat recurring blame at one boundary as a design question for
their own staff meeting, not as a behavior problem for engineers. They should model it by naming the
system factor first when they speak in reviews.

**What not to do.** Do not ban naming teams (it drives the conflict underground), do not punish
individuals for one review (it teaches silence), and do not run organization-wide conflict training as
the main response. A strong answer works on the review process and the boundaries first; the weak
answer starts with a values statement.
