# Chapter 36 solutions — Reorganizations, Organizational Evolution, and Succession

Worked solutions for the [chapter 36 exercises](../parts/07-organization-design/36-reorganizations-evolution-and-succession.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Four complaints, four diagnoses

**Billing and Orders blaming each other after a Core release incident.** Not structural evidence by
itself. The baseline describes the friction and the absence of a manager response; the cheaper levers
are the blameless review practice of Chapter 25, recording which team's change triggered each Core
release incident, and a contract or ownership agreement at the ledger boundary. What would change the
diagnosis: the dependency map showing a large share of Orders' and Billing's items needing the other
team (Orders → Billing 9 links, Billing → Orders 6 at baseline), concentrated on a few components. Then
a boundary move between the two teams, not a reorganization, is the next step.

**core/permissions without an owner.** Structural, but narrow: one component, the smallest possible
fix is assigning it (Chapter 13 frames the Orders or Platform Operations choice). A reorganization
would be grossly oversized.

**Daniel Cho with 17 reports.** Structural (a span problem, Chapter 34), and narrow: a lead role or a
web and mobile split (Chapter 14). Data that would change the answer: if the health check showed
problems unrelated to span, such as one-on-ones that are mostly status, coaching comes first.

**Data and Analytics' low contact.** Not necessarily a problem: low dependency links (4 received at
baseline) may mean good boundaries. Check whether requests to it are slow or whether its work is
disconnected from what other teams need before touching anything.

A good answer refuses to bundle the four into one reorganization. The weak answer treats the number of
complaints as evidence that "the structure is broken".

## F2 — Pessimistic transition cost

Recompute with the new assumptions:

| Part | Calculation | Engineer-weeks |
|---|---|---|
| Ramp-up, Mobile | 5 × 1 | 5 |
| Ramp-up, core/permissions | 2 × 5 | 10 |
| Ramp-up, search-svc | unchanged | 1 |
| Handoff | both fractions for twice as long: 7.4 × 2 | 14.8 |
| Management | unchanged | 3.8 |
| Total | 5 + 10 + 1 + 14.8 + 3.8 | 34.6, about 35 |

Share of a quarter: 34.6 / 1,040 ≈ 3.3 percent, against about 2 percent in the base case. Check: the
increases are +2.5 (Mobile), +4 (core/permissions), and +7.4 (handoff), totaling +13.9, and
20.7 + 13.9 = 34.6.

Numerically the handoff duration matters most, because it multiplies across the most people (23
engineers in the base case: 7 plus 16). A strong answer adds that the core/permissions assumption matters most
for **risk**: if taking on the module takes longer, the period in which a tier 1 component is moving
to a new owner and a first-ever rotation stretches too, which is where the Mockus finding locates
defects. The decision should hold at the pessimistic end, and here it does: about 3 percent of one
quarter is modest for fixing an unowned tier 1 module and a 17-person span. The weak answer reports a
number without saying which assumption drives it, or treats 21 as precise.

## F3 — Breaks in the succession table

Against the rule (at least one ready-now or interim cover and at least one in development; the cover
holds no other critical role and is not primary cover for one):

- **No cover at all:** Billing manager, Data and Analytics manager, core-domain staff role, data and
  integration staff role.
- **Cover holds another critical role:** Platform Operations (Kwame Mensah), director (Elena Sokolova).
- **No development candidate:** Platform Operations, infrastructure staff role (Bram covers only the
  Jenkins pipeline).
- **Fragile even where the rule is met:** Orders and Payments and Integrations each rest on one person
  in both columns; the Payments informal tech lead also appears under Li Na Zhou's role.

A defensible priority order: first **Billing manager**, because Billing had the highest incident count
and the ledger engineers' load; losing Marcus with nobody to hold the team would hit the area of the
reliability mandate most exposed. Second, the **core-domain staff role**: Ines Carvalho's knowledge is
the broadest and her retention is an open question (Chapter 10). Some readers will put the **director**
second, because the chain (Elena to director, Payments to its tech lead) breaks two roles at once; that
is defensible if they explain why it outranks Ines. The weak answer lists gaps without ranking them by
the cost of a vacancy, or counts "interim" covers as solved.

## A1 — Announcement day

A strong schedule for the Tuesday of week 51 (Bogotá is in the same or an adjacent hour as Minneapolis):

1. **Before the day:** Mateo has accepted, and the director and Daniel have told the mobile engineer
   who wanted to lead, one-on-one, why Mateo was chosen and what development they will get (for
   example, running Mobile's planning, which also starts covering Mateo's role).
2. **Morning, Bogotá:** the director and Daniel, in person, meet each of Mateo's five engineers one to
   one with Mateo present: new manager, effective date (week 53), what happens to their on-call and
   the board, whom to ask.
3. **Same morning, Minneapolis by video:** Daniel speaks with Hannah Lindgren first. Her informal
   leadership of web becomes more important, not less, and the conversation should say whether a
   formal role follows. Then the web engineers, the two remote ones in their own calls at the same
   time.
4. **Managers and staff engineers,** with the ownership table (core/permissions to Orders, search-svc
   to Data and Analytics) and handoff dates.
5. **All-engineering call,** everyone on their own screen, then the written rationale and FAQ.

The FAQ answers: why Customer Experience is splitting (span, the shared board, the mobile boundary
incidents); what does not change (pay, levels, other teams); how Web and Mobile will coordinate on
mobile-bff and shared releases; how core/permissions changes are handled while Orders takes it over;
and what it means that a manager is now based in Bogotá. The weak answer announces to the group first,
or forgets Hannah, whose informal role the split changes most.

## A2 — Succession for Billing

The constraint is that the obvious candidate may not want the job and the ledger experts cannot be
spared from the rotation. Two quarters of work could be:

- **Quarter 1:** Marcus delegates two management tasks with an explicit level of control (Chapter 2):
  running sprint planning, and owning the on-call schedule and its fairness. Rotate them between two
  senior engineers, including at least one who is not a ledger expert, so the development list has
  more than one name. Ask Teodora directly, without commitment, whether she wants to try management;
  accept "no" as an answer and keep investing in her technical path.
- **Quarter 2:** whoever showed interest acts as manager for two weeks during a planned absence of Marcus's, with the
  director as backstop. Revisit the table at the six-month review.

Separately, the ledger knowledge gap (period close and currency and rounding have one or two people
who can change them safely) is knowledge succession and belongs in the knowledge map work of Chapter
12, not in the management table. A good answer separates the two and avoids naming one heir publicly.
An acceptable alternative is to state that an external hire would be the backfill if Marcus left, and
to prepare the interim arrangement only; that is honest if said explicitly. The weak answer nominates
Teodora without asking her.

## A3 — The leak in week 48

The rumor is accurate, and Mateo has accepted, so denial would damage trust in all three people. The
plan's logic says to shorten the uncertain period, and here that is possible: the decisions are made,
and only the communication remains. A good answer moves the announcement earlier, to the next
available day on which the director and Daniel can be in Bogotá or, failing that, can hold the
mobile engineers' one-on-ones by video the same morning. Effective dates stay at week 53; only the
telling moves.

Until then, Hannah should not confirm details she was not given; she can say truthfully that a
structural proposal exists, that nobody's pay or job is at risk, and that everyone affected will hear
directly within days. Daniel should tell Hannah herself what is happening that same day, since she
has been carrying the question. The weak answers are asking Hannah to deny it, searching for the
source, or waiting for week 51 because "that is the plan".

## X1 — Delay or proceed

The argument for delay is real: the Mockus finding links organizational change to customer-reported
defects, and Northstar's renewals depend on reliability. But the plan already prices and limits the
risk: about 21 engineer-weeks (2 percent of a quarter), with only core/permissions and the mobile
rotation as tier 1 exposure, each with a readiness check, shadowing, and a freeze in the handover
week. Delay has its own costs. Mateo has been asked and has accepted, Daniel's span stays at 17, and
core/permissions stays unowned for another quarter, which is itself a reliability risk the Mockus
finding does not speak to.

A defensible answer proceeds on the plan's dates with two concessions to Victor: core/permissions
on-call starts only after an explicit go or no-go at the readiness check, and the 90-day review
reports incidents on the moved components separately. To Rajiv Menon: the budget can reflect the new
teams from week 53, but the benefit is a forecast and should not be booked as savings. An equally
defensible answer delays the Mobile split alone while moving core/permissions now, if Mobile's
five-person rotation cannot be made safe in time. The weak answer chooses based on which executive is
more senior.

## X2 — Director-level succession

The honest finding is that the director's succession is a chain: Elena covers the director, her
informal tech lead covers Payments and Integrations, and nobody covers the tech lead. A one-year plan
under flat headcount could include: making the Payments informal tech lead a formal role (a title and
mandate, not a new seat), so Elena can step up without breaking her team; giving Elena and one other
manager (Priya or Daniel are candidates for development) director-level work now, such as chairing the
operations review, owning the capacity model for a quarter, and representing engineering in one
executive meeting; and agreeing with Victor that he holds the role above if two people are absent at
once.

Does this change the view of Chapter 35's alternative with two group leads (managers of managers)? It adds an argument for it: two group leads would
be natural director successors. It does not settle the question, because it costs two engineering seats
and a layer to solve a breakage the director does not yet observe. A strong answer says that
succession is one of the triggers for revisiting that option, alongside headcount growth, and that development
of two managers with director-level assignments achieves much of the succession benefit without the
layer. The weak answer adopts the extra layer for succession alone, or treats "Victor would cover it" as a plan.
