# Chapter 35 solutions — Designing Organizations of 20, 50, 100, and 500 Engineers

Worked solutions for the [chapter 35 exercises](../parts/07-organization-design/35-designing-organizations-at-four-scales.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — The 22-engineer startup

**The breakage** is the classic one of the 20-engineer band: one person is the review, decision, and
approval point for everything. Two days of review wait on every deployment, and a single approver for
schema changes, are symptoms of a structure with no ownership below the founder.

**The cheaper answer first.** Before adding anyone, move review to the team: two reviewers per area,
with the CTO reviewing a sample for a month, and a written rule for schema changes that names two or
three engineers who may approve them. This costs nothing in headcount and can be reversed.

**The structure.** Split into three teams by product area or system boundary, for example 8, 7, and 7
(8 + 7 + 7 = 22). Promote or hire two or three first-line managers or working leads. A VP of Engineering
is a manager of managers; at 22 engineers there are no managers to manage yet, so the hire answers a
breakage that has not arrived, unless the CTO wants to leave people management entirely, which is a
different argument.

**Criteria for a good answer:** names the breakage with evidence, tests the cheaper fix, does the
arithmetic, and explains why a VP is premature or under what conditions it is not. **Weak answer:**
"hire a VP to take the load off the CTO", which adds a layer above a structure that does not exist.

## F2 — Counting crossing links under alternative C

**The count.** All 86 baseline links are between existing teams, so they cross a boundary today and
still cross one under alternative C. The three transfers to the platform team move people, not
components, so they change no link. The split adds the work that used to stay inside Orders. Chapter
34's recount puts that at 4 work items of a week or more that touched both order capture and pricing,
catalog, or search. Under the matrix's rules the answer is about 90 links: 86 plus 4.

**The assumption.** Orders' 23 requested and 18 received links must be divided between Order Capture
and Catalog and Pricing. A reasonable assumption is that each link follows the component involved: the
order-to-invoice mapping and order-status links go with Order Capture, pricing-rules and search-svc
links with Catalog and Pricing. That split does not change the total; it changes which new team carries
each link.

**What the count tells you, and what it cannot see.** The 4 is a floor, not the cost. The matrix only
counts items of a week or more, so it misses the smaller coupling: about 58 merge requests a quarter
changed both pricing-rules and order-capture (Chapter 31), and each would need cross-team review and a
coordinated release after the split. Two more blind spots: Orders' internal work was never classified
beyond those 4 items, and the proposal's own Web and Mobile split has no measured links, because the
matrix counted Customer Experience as one team. The action is to sample Orders' and Customer
Experience's internal items for a quarter before deciding either boundary.

**Criteria:** sees that existing links all cross already, uses Chapter 34's 4 items, states the
assumption, and explains why the count understates the split's cost. **Weak answer:** a precise number
presented as the whole cost, or "86" with no account of the work the split creates.

## F3 — "Never more than seven"

The formula is arithmetic, not evidence. n(n−1)/2 counts possible communication paths if everyone
needs to talk to everyone; real teams use far fewer, and the formula does not identify a size at which
anything breaks. Going from 7 to 8 people adds 7 paths (21 to 28); nothing in the formula makes that
step special.

The chapter's evidence points the same direction as the colleague (more people involved and more
diffuse ownership go with slower work and more failures), but none of it measures an optimal team size.
Herbsleb and Mockus related people involved to calendar time for work items, in a distributed setting.
Nagappan and colleagues related ownership diffusion to failures in one system. Neither tests a cap.
The book records that no validated team size exists; the evidence is thin.

A good answer accepts the direction, rejects the cap, and replaces it with a test: does the team's
work hold together, can one manager support the people, and is coordination inside the team rather than
across teams? It might note that a team of nine owning one coherent component can be healthier than two
teams of five that change the same module. **Weak answer:** accepting seven because it sounds familiar,
or rejecting the formula without acknowledging the direction it points.

## A1 — The platform team's product statement

**Product statement (one worked answer).** "Developer Platform gives every Northstar team one way to
build, test, and deploy, and a test environment on request without a ticket. In year 2 we move the
four script-deployed services and the Jenkins services onto one pipeline with automated rollback, and
retire one CI system per half-year."

**Two adoption measures.** First, the share of components deploying through the common pipeline,
starting from the four-system baseline; it is gamed by moving easy components first, so report
tier 1 components separately. Second, the median wait for a test environment, which Chapter 16's
re-sample put at about 2 days in week 18; it is gamed by redefining "ready", so define it with the users.

**What to refuse.** Feature work in other teams' services; on-call for components the platform does
not own (core/permissions goes to Orders under the proposal; the platform team has no Core Java
engineer); and bespoke pipelines.

**On alternative C's transfers.** With two of five on the interrupt rotation, three engineers build
the product. A strong answer argues for the transfers only with evidence: the measured 1.5 FTE a year
spent running four CI systems, and the environment waits, set against what the three losing teams
would give up. It also accepts that the director may defer them until the first product shows adoption.

**Criteria:** a product with users and an adoption measure, an honest count of capacity (three
building, two on interrupts), a first product small enough for three people, and explicit limits. **Weak answer:** a list of
tasks, or "we will support all teams", which is the dumping-ground failure mode.

## A2 — Priya's objection to the split

The facts matter, and they come in two units. In work items, the split would have made about 4 of
Orders' items of a week or more cross-team in the baseline quarter (Chapter 34's recount); the baseline
associates one dependency with lead time rising from 11 days to 24, so each costs about two weeks. In
merge requests, about 58 a quarter (53 percent of pricing-rules' 110) also touched order-capture; under
the split each would need cross-team review and a coordinated release. The first cost is small and
visible; the second is larger and appears in no matrix. Chapter 31 calls high co-change across owners a
problem.

Before deciding, ask for: the 58 merge requests themselves (how many were small, and whether they
cluster in a few kinds of change that a contract or an interface on pricing rules could absorb);
whether year-2 work such as bulk-order pricing will add more; and what the alternative is. Keeping Orders whole, as the proposal does,
leaves one manager with 16 reports and core/permissions added, which Chapter 34 would challenge.

Defensible outcomes include: drawing the boundary differently (pricing rules stay with Order Capture,
catalog and pricing-svc form the new team); keeping one team with two tech leads and revisiting in two
quarters; or keeping the split and funding an interface on pricing rules first. A good answer treats
Priya's objection as evidence, not resistance, and asks for data. **Weak answer:** overruling her
because the design "looks cleaner", or dropping the split without addressing the 16-report span.

## A3 — Staff mandates

**Ines Carvalho, architect (Core).** Decides the module boundaries and interfaces inside Core,
including the permissions extraction; advises on team-internal design. Reports to the director.

**Kwame Mensah, architect or solver (reliability).** Decides the operational minimums and their
exemptions (his Chapter 20 mandate) and the reliability architecture of tier 1 paths; advises the
platform team on its product. Reports to the director.

**Li Na Zhou, architect (data and integration).** Decides data, migration, and integration contracts
between teams, such as the ledger-export contract; advises Data and Analytics on its own pipelines.
Reports to the director.

**"Advises" rather than "decides".** Ines Carvalho on the platform team's pipeline design: her
expertise is Core code, and the platform team owns its product. Another good example: Kwame on any
team's on-call rotation design, beyond the minimums.

**Criteria:** an archetype per person with reasons, decision scope in a sentence, reporting line
justified (Chapter 29's trade-off between leaf managers and senior leaders), and a boundary between deciding
and advising. Facts from the case about each person (Ines's rejected-design history, for instance) may inform the
"advises" choices. **Weak answer:** mandates that list topics with no decision scope.

## X1 — Responding to the CTO's preference for alternative D

**Cost of D now.** Two engineering seats become management seats (79 to 77 engineers), about 2.5
percent of engineering capacity. A layer between the director and the teams carrying the reliability
mandate adds decision latency (Chapter 34). Two new group leads are learning a new job during the
second year of the reliability program.

**Cost of moving to D later.** One more structural change: the teams stay, and only a reporting
layer is added above them, which disturbs far fewer people than a boundary change (Chapter 36). The
expensive part of reorganizing twice is redrawing team boundaries, and adding a layer later does not
redraw them.

**Triggers to commit to.** Approved headcount growth; a third team split; the director's assessment of
manager development falling behind, checked each quarter against named evidence (development time held,
hiring load, decisions waiting).

**Response.** Agree with the destination, disagree with the timing, and prepare D: identify and
develop two candidate group leads during year 2 so that D can be filled from inside. **Criteria:** a
cost for each path, triggers that can be observed, and a preparation plan. **Weak answer:** accepting D
to avoid conflict, or rejecting it without a path to it.

## X2 — Halvard's duplicate platforms

**First, diagnose.** Forty percent adoption with two parallel platforms says the platform organization's
product does not meet those groups' needs, or did not exist when they needed it. Gather: what the two
group platforms do that the central one does not; their cost (people, cloud); incidents attributable to
each; and what the groups' engineers say in interviews.

**Then decide.** Mandating the platform raises adoption without fixing the product, and the measure
then stops meaning anything. A better sequence: the platform organization treats the two group
platforms as requirements; it agrees with each group a migration with dated milestones, funded from the
group's own platform staff, who move into the platform organization; and a mandate applies only to new
services, after the product meets stated needs.

**Design consequence.** Platform engineers move from product groups into the platform organization,
the platform gets user representatives from the two groups, and adoption becomes a product measure the
platform VP owns. **Criteria:** diagnosis before decision, an honest view of mandate as a measure-gaming
risk, and an organizational move that follows the work. **Weak answer:** mandate immediately, or let
the groups keep their platforms indefinitely with no cost accounting.
