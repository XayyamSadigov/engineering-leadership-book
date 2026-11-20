# Chapter 1 solutions — What Engineering Management Actually Is

Worked solutions for the [chapter 1 exercises](../parts/01-foundations/01-what-engineering-management-is.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Classifying Priya's week

| Block | Hours | Job | Mark |
|---|---|---|---|
| Four one-on-ones | 2 | People | Necessary |
| Design review, bulk ordering | 2 | Technical | Leveraged if Priya is the only person who can judge the design; otherwise substitutable |
| Writing code on order-capture | 6 | Technical | Substitutable |
| Planning with product | 1 | Delivery | Leveraged |
| Meeting with Billing about core/customer | 1.5 | Delivery or technical (cross-team) | Leveraged: core/customer has no owner and four teams change it |
| Email | 3 | Other | Partly necessary |
| Canceled career conversation | 0 | People | The most telling entry |

Four one-on-ones for fourteen reports in one week means most engineers see her fortnightly at best,
and the one career conversation was the block that gave way. Six hours of coding is the largest
single block.

Before recommending anything, a good answer asks: is there anyone on Orders who could own technical
direction, or is Priya the only one? Is the code on the bulk-ordering path (a renewal commitment),
where her involvement may be a deliberate, temporary choice? What did Priya agree with her manager
when she was promoted eight months ago? The weak answer says "stop coding" without asking whether
anyone else can carry the work or what Priya's role definition says. The transition from engineer to
manager is Chapter 2's subject; here the point is that the calendar and the role disagree.

## F2 — The advertisement

The advertisement assigns all three jobs: technical direction ("own the architecture of our payments
platform"), delivery ("run sprint ceremonies"), and people management ("manage a team of nine"), and
then adds 80 percent individual coding on top. At 80 percent coding, the role has about eight hours a
week for everything else. Nine weekly 30-minute one-on-ones alone take four and a half of those.

What is underweighted is people management, and in practice delivery too: "run sprint ceremonies"
describes meetings, not managing dependencies or renegotiating commitments. The risk for the team is
the super-engineer failure mode by design: the team's output depends on one person's calendar, career
conversations are the first thing to slip, and nobody else grows into technical ownership because the
manager owns the architecture.

A revised split depends on the company's intent. If it wants a technical leader for payments, it
should advertise a staff or tech lead role without reports. If it wants a manager, a defensible split
is: manager owns people and delivery, with perhaps 10 to 20 percent hands-on time; a named tech lead
or staff engineer owns payments architecture. A tech lead manager shape could work only for a smaller
team than nine. The weak answer adjusts the percentage without noticing that the advertisement asks
one person to own all three jobs for a team too big for that shape.

## F3 — "Seventy-five percent more productive"

The figure most likely comes from a misreading of Lazear, Shaw, and Stanton, whose abstract says that
under one normalization the average boss is about 1.75 times as productive as the average worker. That
compares a supervisor's contribution with a worker's. It does not say good managers make teams 75
percent more productive. The same abstract's team-level finding is that replacing a bottom-10-percent
supervisor with a top-10-percent one raised team output by more than adding one worker to a team of
nine, roughly an 11 percent gain or more on that comparison.

What the evidence supports: in the settings studied (one firm of technology-based service workers;
one high-tech firm; US and British survey data; Google's internal study), manager quality is
associated with output, retention, and satisfaction, and two studies have designs pointing to causal
effects. What it does not support: anything about software teams specifically, which of the three
jobs produces the effect, or that more managers produce more output. All of the studies concern the
quality of a manager, not the number of managers.

So the conclusion inverts the evidence. If manager quality matters, the implication is to select and
develop managers well, and perhaps to avoid stretching good managers too thin. A strong answer also
notes the reading level: the studies were read at abstract or summary level, so precise magnitudes
should not be quoted beyond what the abstracts state. The weak answer either accepts the claim or
dismisses all the evidence as "soft".

## A1 — The conversation with Marcus

**Ask first.** Start with his view, not the audit: what does he think his job is, which part does he
think he is neglecting, and why he joins incidents. There may be a reason (the three engineers who
carry the pages are exhausted; he is the only one who knows core/ledger). Learning the reason
determines whether the fix is in his calendar or in the team's on-call design.

**Bring.** The audit split (55 percent delivery, 15 percent people), the 20 hours of incident calls,
and two team facts: Billing has the highest incident count (8 of 30) and three people carry most
pages. Frame the issue as the system: his time on calls treats symptoms, and nothing in the calendar
addresses why three people carry the load.

**Propose.** Stop joining incidents as a responder unless it is Sev1 or crosses teams; instead spend
a fixed weekly block on the on-call design (widening the rotation, pairing, runbooks). Raise people
time to at least weekly one-on-ones with the three on-call carriers and fortnightly with everyone else.

**Not yet.** Do not ask him to drop delivery commitments or hand technical direction to someone while
nobody on Billing is ready for it. Changing everything at once removes his footing.

**Evidence in two months.** Rerun the audit; check how many pages the top three engineers carry and
whether incident calls without him restored more slowly. A weak answer presents the audit as a
verdict, or measures success by his hours rather than by the team's on-call load.

## A2 — Daniel's fifteen engineers

**Criteria.** Is technical direction owned by named people with time for it? Can Daniel's people work
be done well at fifteen reports? What is the coordination failure between web and mobile, and which
option fixes it? What does each option cost in transition?

**Options.**

- *Name two tech leads* (web and mobile). Cheapest and fastest: it makes existing informal roles
  explicit. It does not fix the API conflict unless one of them, or a written agreement, owns the
  shared API (mobile-bff and the web contract). It leaves Daniel with fifteen reports.
- *Split under two managers.* Fixes span (eight or nine and six or seven) but needs a second manager,
  under flat headcount, by converting an engineer or backfilling. It can make the API conflict worse by
  putting the two clients in different teams; team design is Chapter 33's subject.
- *Daniel takes technical direction.* At 45 percent people time already and 5 percent technical,
  adding the third job to a fifteen-person team is the least realistic option.

**A defensible answer.** Name the two tech leads now, in writing, with one of them owning the shared
API contract, and plan a team split for the following half-year if span remains the bottleneck. The
transition cost: two engineers lose some feature time, and Daniel has to stop being the tiebreaker on
technical disputes. The weak answer picks the reorganization first because it looks decisive, without
fixing ownership of the API that caused the conflicts.

## A3 — Advising Ines Carvalho

Start by separating what Ines wants (influence over Core's direction) from the means she proposes
(direct reports). On the three-jobs map, influence over Core is technical direction, which does not
require people management. Becoming a manager would add people and delivery work to her week, likely
reduce the time she has for Core, and give her authority over one team's engineers rather than over
the four teams that change Core.

Her complaint is still legitimate. At baseline, Northstar's staff engineers have no mandates; Ines is
consulted on Core changes but owns no decision. In Larson's terms she has no recognized archetype,
only a solver role by default. "Nobody listens" is an accurate description of a role without decision
rights.

What the director would have to change for her choice to be real: a written mandate for Core (for
example, owner of Core module boundaries and the Core code standards, with decision rights and an
escalation path when managers disagree), visibility in the director's operating cadence, and a career
path on which a staff engineer can progress without reports. The canon later gives her such a mandate
during the quality transformation. If she still wants to manage after that, the choice is then about
the job, not about influence. A weak answer either talks her out of management without fixing the
mandate or encourages her into it as the only route to influence.

## X1 — The tech lead manager proposal

**Response.** The tech lead manager model works for small teams with technically strong managers.
Northstar's teams have 11 to 15 engineers, well beyond the four to six where one person can do all
three jobs. Applied now, it would push people management aside, since the calendars already show
technical and delivery work crowding it out, or it would leave technical direction undone.

Retiring the staff role removes the only owners of cross-team technical direction. Core has three
modules changed by four teams and owned by none; the reliability mandate depends on release,
detection, and migration safety that cross every team. No single team's manager can own those.

**Saving.** Three staff engineers at roughly Northstar's average loaded cost of $185,000 is about
$555,000 a year (an assumption; staff engineers usually cost more). Set that against $1.64M a year in
service credits at the baseline rate and $9M in at-risk renewals that depend on cross-team technical
work.

**Conditions under which it would work.** Teams of about six, managers selected for technical depth,
and little cross-team architecture. Data and Analytics, where Farah already holds technical direction,
is closest.

**Alternative.** Keep the staff engineers and give them written mandates (as the transformation
later does); name tech leads in the large teams; allow a tech lead manager shape only as a recorded
exception for small teams. The weak answer argues from principle ("staff engineers are important")
without numbers or the conditions under which Victor would be right.

## X2 — Four managers instead of six

**Span.** 80 engineers across four managers is 20 each, against 11 to 15 today. Weekly 30-minute
one-on-ones would take 10 hours a week, a quarter of a 40-hour week, before any hiring, feedback, or
delivery work. In practice one-on-ones would become fortnightly or less, and technical direction would
leave the manager's calendar entirely.

**Saving.** Two managers at an assumed cost close to the $185,000 average is about $370,000 a year,
roughly 2.3 percent of the $16.1M personnel budget. State the assumption; manager cost may differ.

**Evidence.** The manager-effect research concerns manager quality, not count, so it does not directly
predict the effect of a wider span. It does suggest where the cost would surface: Lazear and colleagues
and Hoffman and Tadelis both link manager quality to whether people leave, and a stretched manager is
unlikely to perform at the same level. Span-of-control evidence for software teams is a gap (G8), so
the analysis should say so.

**Where the cost would show up.** Attrition among engineers with the most product knowledge;
slower delivery from merged teams relearning each other's components; and risk to the reliability
mandate and the two renewal commitments if Orders or Billing is merged during the transformation.
Losing two or three experienced engineers would cost more than the saving once replacement time is
counted (an estimate the CFO can check against Northstar's own hiring data).

**Recommendation.** Decline for the next two quarters; offer to revisit team boundaries after the
reliability work, as part of a deliberate team-design review rather than a cost cut. The weak answer
either accepts the arithmetic or refuses without numbers.
