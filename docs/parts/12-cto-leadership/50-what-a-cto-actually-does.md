# Chapter 50 — What a CTO Actually Does

The title Chief Technology Officer (CTO) names a seat, not a job. One CTO runs every engineer in the
company; another has no reports and spends the year with customers. This chapter defines the role by the
decisions it owns. It covers the archetypes, the split with the head of IT and the VP of Engineering, the
CTO's own team and rhythm, and the short list of things only the CTO can do. The running example puts you in the seat
of Victor Lindqvist, CTO of Northstar Technologies, the book's fictional
[case study](../../case-studies/northstar/index.md), in quarter 4 of the director's first year.

Related chapters: the VP role (47) and Part XII's strategy, finance, risk, data, and board chapters
([51](51-enterprise-technology-strategy.md) to
[55](55-boards-due-diligence-and-executive-decision-making.md)).

## Why This Matters

At team scale, engineers feel the CTO through technical decisions: a hallway ruling that overrides a
team's design, or a strategy that explains why their service is being retired. A CTO who rules informally
makes every team's decisions provisional.

At organization scale, the CTO decides what the engineering leaders below are accountable for and what
stays at the top. When that split is unwritten, directors and VPs either wait for permission they already
have or take decisions that were never theirs.

At executive scale, the CTO is the only technologist at the table where the company's money, risk, and
direction are decided. A CTO who spends that seat advocating for engineering, or who spends the week
inside engineering, leaves the company without technical judgment. Most CTO failures are failures in how
CTOs spend their own time.

## Learning Objectives

After this chapter you will be able to:

- Distinguish the common CTO archetypes and diagnose which one a company needs, given who else sits at
  the top.
- Divide responsibility among the CTO, a CIO or head of IT, and a VP of Engineering by decision rights,
  and find the seams where nobody owns a decision.
- Audit a CTO's calendar against the decisions only the CTO can take, and design a delegation plan with
  named receivers.
- Design the CTO's own leadership team and operating rhythm, including forums the CTO attends rather than
  chairs.
- Recognize the role's failure patterns (the shadow architect, the absent executive, the engineering
  advocate) and detect them early.

## The Mental Model

> **Mental model:** The CTO's job is the set of technology decisions that only the company's top
> technologist can take. Everything else is delegated, in writing, to a named person. The CTO's
> calendar is the evidence of which job is actually being done.

Two ideas organize the chapter.

First, **the role is a residual.** What a CTO does depends on who else is at the top. If a VP of
Engineering runs the organization, the CTO's job is what is left: strategy, external trust, company-level
bets. If IT reports to the CFO, the CTO's territory ends at the product's boundary, and the seam between
them needs an owner. Archetypes describe what was left over in a given company; they are not personality
types.

Second, **delegation is the CTO's main design tool, and the calendar is its audit.** The week is fixed.
Peter Drucker is known for the advice to record where time actually goes before deciding where it should
go ([Drucker, 1967](../../references/bibliography.md#drucker1967effective)); **expert opinion**. Diary
studies of CEOs suggest that how a leader's time fits the firm matters
([Bandiera et al., 2020](../../references/bibliography.md#bandiera2020ceo)); applying that to CTOs is an
analogy.

The loop: every decision that reaches the CTO is kept, returned to its owner, or given a newly named owner
in writing. A quarterly calendar audit checks whether returned decisions have drifted back. A decision
returned once is a favor; a decision class returned every time changes the organization.

## Deep Conceptual Explanation

### Archetypes: what the company needs at the top

The best-known taxonomy comes from Tom Berray, as summarized by Werner Vogels
([Vogels, 2007](../../references/bibliography.md#vogels2007ctoroles)). It has four roles:

- the **infrastructure manager**, who runs infrastructure and operations where technology supports the
  business;
- the **technology visionary and operations manager**, who decides how technology carries out the strategy
  and also runs it, typical of founders;
- the **external-facing technologist**, who works between key customers and the product organization;
- the **big thinker**, who studies how technology could create new business, often with an
  advanced-development group.

The first two usually manage engineering directly; the last two sit close to the executive team. This is
**expert opinion**: a vocabulary, not a tested model. Research on the role is thin; Medcof argues that a
CTO's influence rests more on business knowledge and networks than on expertise
([Medcof, 2008](../../references/bibliography.md#medcof2008cto)).

This book adds a fifth pattern seen in software companies of 50 to 400 engineers: the **organization
builder**. This CTO runs engineering as its top manager and delegates technical direction to staff and
principal engineers. Will Larson defines the engineering executive by responsibility for all of
engineering, regardless of title ([Larson, 2023a](../../references/bibliography.md#larson2023executive-job);
[Larson, 2024](../../references/bibliography.md#larson2024primer)); **expert opinion**.

| Archetype | Owns | Typical company | What must exist elsewhere |
|---|---|---|---|
| Infrastructure manager | Operations, infrastructure, internal systems | Technology supports a non-software business | An owner for product technology, if any |
| Visionary and operator | Strategy and the engineering organization | Startup to about 50 engineers | Nothing yet; the risk is the CTO's span |
| Organization builder | The engineering organization through managers | 50 to 400 engineers without a VP | Technical direction carried by senior engineers |
| External-facing technologist | Customer and partner technical trust | Enterprise software with large accounts | Someone who runs engineering (a VP or director) |
| Big thinker | New technology bets, long horizon | Large firms with funded exploration | A VP who runs delivery; a strategy that funds bets |

The archetype is diagnosed, not chosen by taste (**this book's recommendation**). Ask three questions:

1. Is technology the product, or does it support the product?
2. Who runs the engineering organization day to day?
3. Which of the company's top problems is technical and has no owner?

The third answer names the archetype the company needs this year, and it changes. A CTO who was right as
operator at 40 engineers is wrong as operator at 150 if nobody else is setting direction.

### CTO, CIO, and VP of Engineering: splitting by decision rights

Split the roles by decision, not by title, because companies define the CTO and VP roles very
differently ([Larson, 2020](../../references/bibliography.md#larson2020first90)). The CIO (chief
information officer) or head of IT usually runs internal systems. Weill's study of more than 250
enterprises treats IT governance as assigning [decision rights](../../glossary.md#decision-rights)
([Weill, 2004](../../references/bibliography.md#weill2004govern)), a **research finding** whose method
transfers: list the decisions, then assign each one.

For a software company with all three roles, a typical split (**this book's recommendation**):

| Decision | CTO | VP of Engineering | CIO or Head of IT |
|---|---|---|---|
| Product technology direction and major bets | Decides | Advises | Informed |
| Allocation of engineering capacity across areas | Sets envelope | Decides | n/a |
| Engineering leaders below the top | Approves VP picks | Decides directors | n/a |
| Internal business systems (finance, HR, CRM) | Informed | n/a | Decides |
| Employee devices, identity, office networks | Informed | n/a | Decides |
| Security of the product and its pipeline | Accountable (unless a CISO) | Implements | Shares controls |
| Customer and board technical trust | Decides | Supports | Supports on internal controls |

A CISO (chief information security officer) is a dedicated security executive; where one exists, the
security row moves to that person. Where there is no VP, the CTO holds the VP column too, or gives it
explicitly to a director (Chapter 47's first company shape). Where IT reports to the CFO, the CTO and the
CFO share seams: identity, security, vendors that serve both, and evidence for customer security reviews.
The table's job is to make each seam somebody's decision. A blank cell is acceptable only if it is
written down as blank.

### What only the CTO can do

Keep the list deliberately short (**this book's recommendation**):

1. **Merge the company's view and engineering's view into one problem.** Larson describes the engineering
   executive as a company-first problem solver, not a functional advocate
   ([Larson, 2023b](../../references/bibliography.md#larson2023balancing)).
2. **Own the technology strategy's fit with the business strategy.** Others draft it; only the CTO can
   commit the company to it ([Chapter 51](51-enterprise-technology-strategy.md)).
3. **Take or ratify company-level, hard-to-reverse technical bets**: a platform the company will run for a
   decade, an acquisition's integration, an exit from a vendor. Team-level choices, even expensive ones,
   belong to the teams and the architecture process
   ([Chapter 28](../06-technical-leadership/28-architecture-decision-making-and-governance.md)).
4. **Design the technology leadership structure and choose its top people**, including whether a VP
   exists (Chapter 47).
5. **Hold the technical trust of the largest customers and the board.**
6. **Set decision rights at the seams** with product, IT, security, and finance.
7. **Be accountable at the top for technology risk**, whoever operates the controls
   ([Chapter 53](53-risk-governance-regulation-and-security-strategy.md)).

Everything else can be done by someone else, often better. Aghion and Tirole separate formal authority
(the right to decide) from real authority, which follows information
([Aghion and Tirole, 1997](../../references/bibliography.md#aghion1997formal)). A CTO who keeps formal
authority where others hold the information either decides badly or rubber-stamps.

### Delegation that holds

Delegation fails in two directions. The CTO keeps answering questions that have an owner, or disappears
from decisions that needed the top. Larson argues the second does more
damage than the first ([Larson, 2023c](../../references/bibliography.md#larson2023micromanage)); **expert
opinion**.

The fix for both is a published list of decision classes, each with an owner. The CTO then redirects
every request that arrives at the wrong door, every time, for a quarter. It must be a habit because
managerial work is brief, fragmented, and verbal
([Mintzberg, 1990](../../references/bibliography.md#mintzberg1990job)). Most decisions reach a CTO as a
two-minute question in chat, and each answer teaches the organization to ask again.

### The CTO's own team and operating rhythm

A CTO has two teams. The **first team** is the executive team. Larson, following Lencioni, treats a
leader's peers as the first team, and notes that peers' conflicting incentives make this harder than
managing ([Larson, 2023d](../../references/bibliography.md#larson2023gelling);
[Lencioni, 2002](../../references/bibliography.md#lencioni2002five)); **expert opinion**. The **second
team** is the CTO's direct reports: VPs or a director, perhaps a technical direction group.

Design the second team by the decisions it must make together (**this book's recommendation**). If the CTO
decides allocation, everyone whose area competes for capacity is on it. If technical direction is the main
job, the senior engineers who carry it join a standing forum with the CTO, even if they report elsewhere.

The rhythm follows Chapter 37's rule that every loop has one home
([Chapter 37](../08-management-operating-system/37-cadences-and-leadership-meetings.md)). The CTO's loops
are longer than a director's.

```mermaid
flowchart TD
    Y["Annual: strategy and plan"] --> Q["Quarterly: board and reset"]
    Q --> M["Monthly: business review"]
    M --> W["Weekly: executive team"]
    W -->|"exceptions"| M
    M -->|"evidence"| Q
    Q -->|"revisions"| Y
```

| Loop | CTO chairs | CTO attends, does not run |
|---|---|---|
| Weekly | One-on-ones with direct reports | Executive team, as a member; a sample of engineering forums |
| Monthly | Business review with engineering leaders; technical direction review | Largest-customer executive reviews |
| Quarterly | Strategy check; calendar audit | Board item; engineering's quarterly reset |
| Annual | Technology strategy and investment plan ([Chapter 51](51-enterprise-technology-strategy.md), [Chapter 52](52-technology-investment-budgeting-and-financial-literacy.md)) | Operating plan with the CFO |

Attend engineering forums by sampling, not chairing. A CTO who chairs engineering's weekly operational
review has taken the director's meeting; one who never attends loses unfiltered signal.

## Engineering Organization Example

!!! info "Northstar so far"
    Week 47 of the director's first year. Sev1 and Sev2 incidents fell from 30 a quarter to 14 in quarter 3,
    and availability reached 99.89 percent. Several year-2 decisions are open, among them the
    organization proposal and whether to hire a VP of Engineering. See the
    [quarter 4 briefing](../../case-studies/northstar/quarter-4-briefing.md) and the
    [timeline](../../case-studies/northstar/timeline.md).

This example is **illustrative** and fictional.

**You are Victor Lindqvist (CTO) in week 47.** You have one direct report, the Engineering Director, who
runs 87 seats (engineers, managers, and the director). Corporate IT reports to Rajiv Menon (CFO): 14 people
under Marta Kowalczyk (Head of IT), including the two-person security function of Joon Park (IT security
lead). In week 45 you asked the director whether Northstar needs a VP of Engineering in year 2. The
recommendation is due in week 48, and you have decided nothing. Whatever the answer, you want to know
which part of your week no structure would change. You export your calendar for weeks 44 to 46 and sort an
average week.

**The finding first.** 20 of your 48 hours are work only the CTO can do under any structure. Another 7 are
recoverable without a VP. Only 2 hours, about 4 percent, go to strategy, which is the complaint behind your
week 45 question.

| Activity | Hours a week | Class |
|---|---|---|
| Executive team meeting and one-on-one with Helena Marsh (CEO) | 3.0 | Only the CTO |
| Fortnightly one-on-ones with Amara Okafor (CPO), Rajiv Menon, Greg Tanaka (VP Sales), Sofia Alvarez (VP Customer Success) | 1.0 | Only the CTO |
| One-on-one with the director | 0.5 | Only the CTO |
| Largest customers' technical relationships | 5.0 | Only the CTO |
| Board preparation (week 50 item, board pack figures) | 4.0 | Only the CTO, seasonal |
| Year-2 decision reviews (organization, continuation, workforce plan) | 4.5 | Only the CTO, seasonal |
| Strategy work, uninterrupted | 2.0 | Only the CTO |
| Customer security reviews (Joon Park drafts, you join calls) | 2.0 | Shared seam |
| Sales calls on open deals with Greg Tanaka's team | 3.5 | Mostly delegable |
| Sev1 bridges and customer calls during incidents | 2.0 | Partly delegable |
| Technical rulings asked in chat or the corridor, unrecorded | 3.5 | Should have an owner |
| Engineering forums attended (monthly review, quarterly reset) | 1.5 | Keep |
| Recruiting and external | 1.0 | Keep |
| Email, administration, travel | 14.5 | Overhead |
| **Total** | **48.0** | |

The first seven rows total 20.0 hours; the four delegable rows total 11.0.

**The rulings.** In the three weeks, 11 technical questions reached you outside any process. Three were
genuinely yours:

- a top-40 customer's request for a dedicated environment, which would change how Northstar runs its
  platform;
- the technical terms of a vendor renewal affecting both product and IT;
- a top-40 customer's request to review Northstar's architecture direction before renewing.

Six had an owner under the director's [escalation path](../../glossary.md#escalation-path), published in
week 15. It gives the parties five working days, then the director, and reaches you only for customer
commitments or the director's budget authority. Two belonged to the standard owners: Kwame Mensah (staff
engineer, infrastructure) for pipelines and Li Na Zhou (staff engineer, data and integration) for data.

Answering those eight repeats an old mistake. In week 14 you told a team in passing to "read the tables
now", that is, to read ledger tables directly. That remark pre-empted [ADR-0001](../../glossary.md#adr-0001), the architecture
decision on how integrations read ledger data, which Li Na had just opened
([Chapter 39](../08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md)).

**Your draft keep, give, stop list.**

| Item | Now | Draft | Receiver |
|---|---|---|---|
| Sales calls | 3.5 | 1.5: top-40 accounts and roadmap-changing deals only | The director names a staff engineer per deal |
| Technical rulings | 3.5 | 1.0: the "only the CTO" list only | Escalation path and standard owners; you redirect every time |
| Incident bridges | 2.0 | 1.0: customer executive calls only | Incident commander runs the bridge |
| Security reviews | 2.0 | 0.5: final call with top-40 customers | Joon Park's evidence library, Kwame Mensah proposed as engineering evidence owner (draft, Chapter 53) |
| **Reclaimed** | | **7.0** | |

Moved to strategy, the 7 hours would raise that row from 2 to 9 hours, about 19 percent of the week.
That is an upper bound: delegation costs time in its first quarter. None of this answers the VP question.

## Decision Framework

The archetype table answers which role the company needs. The recurring decision is the single request:
does it stay with the CTO? Use this test (**this book's recommendation**).

```mermaid
flowchart TD
    A["Decision arrives"] --> B{"Binds the company?"}
    B -->|"no"| C{"Owner named?"}
    B -->|"yes"| D{"Needs top trust?"}
    C -->|"yes"| E["Redirect to owner"]
    C -->|"no"| F["Name an owner"]
    D -->|"yes"| G["CTO decides"]
    D -->|"no"| H["CTO ratifies"]
```

| Question or outcome | Meaning |
|---|---|
| Binds the company? | Beyond engineering, for more than about a year, or hard to reverse |
| Needs top trust? | The CEO, board, or a top customer will hold the CTO personally accountable |
| CTO ratifies | Someone else prepares and recommends; the CTO signs or sends it back with a reason |
| Name an owner | The decision class has no home: the CTO assigns one in writing and logs it |
| Redirect to owner | Say who decides and where it is recorded; give no view that could be read as a ruling |

## Trade-offs

**Inside or outside.** An inward-facing CTO keeps technical judgment close to delivery but gives
customers and the board a thinner technology voice. An outward-facing CTO needs someone who runs
engineering, which costs a seat or a written delegation (Chapter 47).

**One report or several.** A single direct report, as at Northstar, gives a clear chain and time for the
outside, at the cost of depending on one person for nearly all signal about engineering. More reports
widen the signal at the cost of management time.

**Owning IT or not.** Owning corporate IT removes the product-IT seam, at the cost of attention on
laptops and finance systems. Leaving IT with the CFO keeps the CTO focused, but every shared decision
becomes a negotiation unless decision rights are written.

**Ruling or redirecting.** An informal ruling saves days on one decision and costs a process people can
trust. Redirecting is slower the first time and cheaper by the third.

## Failure Modes

**The shadow architect.** The CTO gives rulings in conversation that override the architecture process.
Early sign: teams quote "the CTO said" for decisions nobody can find in a log. Detection: count requests
reaching the CTO outside any process for three weeks, as Victor did.

**The absent executive.** The CTO moves outward and stops looking inside, knowing engineering only through
one report's summaries. Early sign: the CTO learns of a serious incident or a
resignation from the CEO.

**The engineering advocate.** The CTO argues for engineering's share instead of the company's answer. Early
sign: peers pre-negotiate with the CTO's reports, and the CEO stops asking the CTO about anything outside
engineering.

**The archetype lag.** The CTO keeps doing the job that was right three years ago: still writing code at
150 engineers, or still running every manager after a VP arrived. Early sign: the VP or director cannot name
a decision that is fully theirs.

**The orphaned seam.** Security, identity, or customer evidence falls between the CTO and the head of IT,
each assuming the other owns it. Early sign: a customer questionnaire answered differently by two functions.

## Enterprise Application

In an organization of 50 to 150 engineers the CTO usually looks like Northstar's: one director, or a few
managers of managers, and no VP. Two things are specific to this size.

First, the staff engineers report through the director, so the CTO has no direct line to technical
direction. A monthly technical direction review chaired by the CTO, with the director and the staff
engineers, gives direction a home without a second reporting line
([Chapter 29](../06-technical-leadership/29-staff-and-principal-engineers.md) covers the staff role).

Second, without a VP, the split with the director is the whole delegation. Write down which VP-level
decisions the director holds: allocation with the product leader, manager staffing, the operating rhythm.

A rough guide for the calendar at this size (**illustrative**): at least a fifth of the week on
non-seasonal work only the CTO can do. No standing chair of an engineering-internal weekly forum. A
quarterly audit that is actually run.

## CTO Perspective

This section looks at how the role changes past Northstar's size. At Halvard Systems, the fictional 500-engineer company of
[Chapter 35](../07-organization-design/35-designing-organizations-at-four-scales.md), the CTO has five vice
presidents (four product groups and a platform organization). The second team is the five VPs, and the
archetype is organization builder: allocation across groups, the choice of VPs, and cross-group bets.
Technical direction runs through seven principal engineers and six enterprise policies. An informal
ruling from Halvard's CTO crosses group boundaries and does damage at six times the scale.

As the company grows, the CTO's time moves from deciding to designing who decides. The "only the CTO" list
stays short while each item gets heavier. The first team matters more than the second, because influence
on capital and risk is exercised among peers and with the board. The first-90-days advice below (learn
the money, build peer relationships early) becomes the job, not the onboarding.

### The executive's own sustainability

Nobody above a CTO watches the CTO's load, so the CTO has to (**this book's recommendation**). The
calendar audit is also a health check: Victor's 48-hour week had 14.5 hours of overhead and 2 of
strategy, the profile of someone running on reaction. Three signals deserve attention: weeks that stay
above about 50 hours for a quarter, strategy time that keeps losing to the inbox, and decisions you
now postpone because you are tired rather than because you lack evidence. Three habits help. Delegate
for capacity as well as for development, since every item on the keep, give, stop list returns hours.
Protect one block a week that no request can take. Keep a peer network outside the company (other CTOs,
a former manager) for problems you cannot discuss with your own team or the CEO. An exhausted CTO
makes the decisions this chapter reserves for the top worse, and the organization copies the hours.

## Practical Playbook

1. **Write the "only the CTO" list**: at most seven decision classes, each with the reason it stays.
2. **Name the archetype the company needs this year** from the three diagnostic questions, and what must
   exist elsewhere for it to work.
3. **Write the decision-rights table** with the VP or director and the head of IT: one owner per row,
   deliberate blanks marked. List the seams with IT (identity, security tooling, customer security
   evidence, shared vendors) and give each an owner before considering moving IT.
4. **Audit three weeks of calendar** into only the CTO, seasonal, delegable, and should have an owner.
5. **Count informal requests** in the same weeks: who asked, what, and who should have decided.
6. **Draft a keep, give, stop list** with a named, briefed receiver for every item given away.
7. **Redirect every misrouted request for a quarter**, naming the owner, and log decision classes with no
   owner.
8. **Design the rhythm**: what you chair, what you attend without running, one home per loop.
9. **Repeat the audit quarterly**, and revise the list when the archetype the company needs changes. To
   assess the CTO against the role rather than the calendar, use the
   [CTO competency matrix](../../templates/cto-competency-matrix.md).

### A CTO's first 90 days

A new CTO's first quarter should produce understanding and a few written agreements, not a program of
change. Larson's advice for new CTOs and VPs of Engineering is to learn how the business makes and
spends money, build peer relationships before conflict arises, get the manager's expectations in
writing, and limit the number of changes in flight. He also warns that many lightly held opinions from
a new executive create thrash ([Larson, 2020](../../references/bibliography.md#larson2020first90);
**expert opinion**). This book's sequence turns that advice into the chapter's tools:

| Days | Aim | Output |
|---|---|---|
| 1 to 30 | Listen and measure | One-on-ones with every executive peer and direct report; skip-levels; the company's financial plan read with the CFO; three weeks of your own calendar recorded |
| 31 to 60 | Write down what exists | How high-impact technical decisions are actually made today; the implicit technology strategy; the archetype the company needs (three questions); a draft decision-rights table |
| 61 to 90 | Agree and start | The CEO's expectations in writing; the decision-rights table agreed with peers; the "only the CTO" list; your operating rhythm (one-on-ones, written updates, a recruiting review, perhaps a weekly operational review); at most two changes started |

Two traps are specific to the first quarter. The first is ruling early: in the first month every
question reaches the new CTO, and each answer given then becomes precedent before you know who should
own it. Say "who decides this today?" and write the answer down. The second is inheriting the
predecessor's calendar. A CTO who walks into the previous CTO's forums becomes that archetype by
default; attend for a month, then decide which to keep (exercise A3).

## Case Study

This case is **fictional**, set in quarter 4 at Northstar. The outcome is open.

**The seam.** Northstar has no CISO. It holds no [SOC 2](../../glossary.md#soc-2) report, the independent
accountant's examination of controls that large customers often require. Joon Park's security function sits
in Corporate IT under Marta Kowalczyk, who reports to Rajiv Menon. Product security runs through
engineering's pipeline: dependency scanning, remediation service levels, and the security share of the
[prevention allocation](../../glossary.md#prevention-allocation)
([Chapter 26](../05-engineering-quality/26-security-and-software-supply-chain-quality.md)). Customers send
security questionnaires to the CTO. In weeks 44 to 46 Victor spent about 2 hours a week on them: Joon Park
drafted answers from IT's records, engineering supplied evidence ad hoc, and Victor joined the calls.

**The shared decisions.** Victor's week 47 list of decisions touching both him and Rajiv's organization:

| Decision | Who decides today | Victor's draft owner |
|---|---|---|
| Identity and access for production systems | Unclear: IT runs the directory, engineering grants production roles | IT runs the directory; the director owns production role grants |
| Vendor contracts serving product and internal systems | Whoever signs first | The budget holder, with the other side's written technical sign-off |
| Customer security questionnaires and evidence | Victor, by default | The director's week 47 security strategy draft proposes an evidence library owned by Joon Park, with Kwame Mensah as engineering evidence owner; not decided |
| Product security tooling in the pipeline | Engineering | Engineering, unchanged |
| Internal business systems | IT | IT, unchanged |

**What Victor considers.** Three options, none chosen:

1. **Keep the structure and write the table.** IT stays with the CFO; the seams get owners; Victor raises
   the table with Rajiv. Cheapest, and depends on two executives honoring a page.
2. **Move IT under the CTO.** This removes the seam. It also adds 14 people and corporate systems to a CTO
   trying to reclaim time for strategy, and takes from Rajiv an organization he did not offer.
3. **Wait for the risk and security design.** Leave the questionnaire row undecided until after the week 50
   technology risk session of the [audit committee](../../glossary.md#audit-committee) (the board committee
   that oversees risk). Wait also for the open decision on where security reports
   ([Chapter 53](53-risk-governance-regulation-and-security-strategy.md)), and keep answering meanwhile.

**What makes it hard.** Victor already has three structural questions open this month. The VP
recommendation arrives in week 48. The board meets in week 50. The year-2 organization proposal, if
approved, is announced in week 51 (all are on the
[quarter 4 briefing](../../case-studies/northstar/quarter-4-briefing.md)). Raising IT's reporting line with
the CFO now adds a fourth. Not raising it leaves Victor answering questionnaires by default, the work his
own audit says he should not be doing.

**The reader decides:** which option Victor should take, what he says to Rajiv Menon and when relative to
the other open decisions, and what evidence would change his course.

## Exercises

Worked solutions are in the [Chapter 50 solutions](../../solutions/ch50-solutions.md).

### Foundational

**F1.** A 120-engineer software company has a founding CTO who manages four engineering managers directly, a
CPO, and IT under the CFO. The CTO spends most mornings in design reviews and is the only person who approves
database schema changes. The CEO wants the CTO to meet more customers. Using the three diagnostic questions,
name the archetype the company needs, what must exist elsewhere for it to work, and the first activity to
give away.

**F2.** Using Victor Lindqvist's week 44 to 46 calendar, reclassify every row for a typical quarter 5 week,
with the year-2 decisions and the week 50 board meeting behind him. State which hours disappear, which grow,
and what share of the week is then work only the CTO can do. Show the arithmetic and every assumption you
add.

**F3.** Write a decision-rights table for a 90-engineer company with a CTO, a VP of Engineering, and a head of
IT reporting to the CFO, with at least six decisions. Mark the seams where two roles share a decision, give
each seam one owner, and identify the row you expect to be disputed first, and why.

### Applied Leadership

**A1.** You are the Engineering Director at Northstar in week 47. Victor Lindqvist shows you his draft keep,
give, stop list and asks you to name a staff engineer per open deal for sales calls. Ines Carvalho (Core
domain), Kwame Mensah, and Li Na Zhou already have standing scopes and quarter 4 commitments. Decide whether
to accept the work as proposed, and write what you say to Victor, including what you need from him.

**A2.** Of the 11 informal requests Victor counted, three were his, six belonged under the director's
escalation path, and two with the standard owners. Design Victor's redirect for each group: the words, what
he logs, and how he handles someone who asks a second time. Explain how you would know after one quarter
whether the redirect worked.

**A3.** A new CTO joins a 150-engineer company where the previous CTO personally chaired the weekly
operational review, the architecture review, and the incident review. Two directors run the organization.
Design the new CTO's rhythm for the first two quarters: what to chair, what to attend without running, what
to stop, and how to transfer each forum without signaling disengagement.

**A4.** You join a 70-engineer software company as its CTO. There is one engineering director, no VP,
a CPO, and a CFO who owns IT. Your predecessor left suddenly; the CEO says only that "engineering needs
to be more predictable" and that a large customer renewal is due in month five. Two staff engineers ask
in your first week whether you will approve a database migration they have argued about for a year.
Write your 90-day plan as a one-page table, say what you answer the staff engineers, and name the two
changes you would allow yourself to start, and why those two.

### Executive Decision-Making

**X1.** You are Victor Lindqvist in week 47, with the case study's three options for the security and IT seam
in front of you. Choose one and write the half-page note you would send Rajiv Menon. Address the sequencing
problem: the VP recommendation is due in week 48 and the board meets in week 50. The year-2 organization is
still undecided, with an announcement planned for week 51 if it is approved. State what you would need to
believe for moving IT under the CTO to be right.

**X2.** Suppose, hypothetically (this is not part of Northstar's record), that Helena Marsh (CEO) tells
Victor the board wants "a more strategic CTO" next year and asks him to spend half his week on customers and
the board. Using the archetype table, explain what this implies for who runs engineering, what it costs,
which of Victor's activities must move and to whom, and what you would tell Helena about the risks. A VP
would take one of the 87 seats. Do not decide the week 48 VP question; show how your answer depends on it.

## Reflection Questions

1. If you exported the last three weeks of your calendar, what share would be work only your seat can do?
   What would you have guessed before looking?
2. Which decisions do people bring to you that already have an owner, and why do they keep bringing them?
3. Which archetype was your current role designed for, and is it the one the company needs this year?
4. Where does a decision in your area fall between two executives, and has either of you written it down?
5. When did you last argue in an executive meeting for an answer that cost engineering something?

## Key Takeaways

- Define the CTO role by the decisions it owns; the title tells you almost nothing.
- Diagnose the archetype from who else is at the top and which top problem has no owner; expect it to
  change as the company grows.
- Split CTO, VP, and IT responsibilities by decision rights, with one written owner per seam.
- Keep the "only the CTO" list short: the company's technology problem, strategy fit, company-level bets,
  the leadership structure, top customer and board trust, seams, and technology risk.
- Audit the calendar quarterly; a CTO with 4 percent of the week for strategy has delegated strategy to
  nobody.
- Redirect every misrouted decision to its owner, every time; informal rulings make every team's decisions
  provisional.
- The executive team is the first team and the direct reports the second; forums can include people without
  moving them.
- Chair few forums, attend a sample of the rest, and never confuse distance with delegation.

## References and Further Reading

- [Drucker, 1967](../../references/bibliography.md#drucker1967effective). *The Effective Executive*. Knowing
  where an executive's time goes.
- [Bandiera et al., 2020](../../references/bibliography.md#bandiera2020ceo). CEO time use from diary data,
  and the fit between executive and firm.
- [Vogels, 2007](../../references/bibliography.md#vogels2007ctoroles). The four CTO roles attributed to Tom
  Berray.
- [Medcof, 2008](../../references/bibliography.md#medcof2008cto). Sources of a CTO's influence beyond
  expertise and position.
- [Weill, 2004](../../references/bibliography.md#weill2004govern). IT governance as decision rights.
- [Aghion and Tirole, 1997](../../references/bibliography.md#aghion1997formal). Formal and real authority.
- [Larson, 2024](../../references/bibliography.md#larson2024primer). The engineering executive's job.
- [Larson, 2023a](../../references/bibliography.md#larson2023executive-job). The executive defined by
  responsibility, not title.
- [Larson, 2023b](../../references/bibliography.md#larson2023balancing). The company-first executive.
- [Larson, 2023c](../../references/bibliography.md#larson2023micromanage). Disengagement as the worse
  failure.
- [Larson, 2023d](../../references/bibliography.md#larson2023gelling). The executive team as the first team.
- [Larson, 2020](../../references/bibliography.md#larson2020first90). The first 90 days as CTO or VP
  Engineering.
- [Mintzberg, 1990](../../references/bibliography.md#mintzberg1990job). The fragmented reality of managerial
  work.
- [Lencioni, 2002](../../references/bibliography.md#lencioni2002five). *The Five Dysfunctions of a Team*.
  Peers as a first team.
- [Fournier, 2017](../../references/bibliography.md#fournier2017manager). *The Manager's Path*. Known for
  following the management track up to senior executive roles, including the CTO.
