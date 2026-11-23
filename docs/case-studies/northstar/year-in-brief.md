# The year in brief

!!! warning "Fictional"
    Everything on this page is invented for the book. See the note on the
    [Northstar overview](index.md).

This page tells the Engineering Director's first year at Northstar as a story: what was tried, what
worked, what failed, and why the year ends with its biggest decisions still open. It takes about six
minutes. Read it after the [overview](index.md) and before any chapter that starts in the middle of the
year. The numbers behind it are on the [timeline](timeline.md) and in the
[year 1 record](first-quarter.md); the people are on the [cast](cast.md) page.

You are the director. Each quarter below is 13 weeks, counted from your first day.

## Quarter 1: ownership, severity, and a faster release train

You arrive with a mandate from Victor Lindqvist (CTO): within a year, halve serious incidents and meet
the availability promised in customer contracts. You may not add headcount, and you must keep the two
customer commitments that two large renewals depend on. In the quarter before you came there were 30
[Sev1 and Sev2](../../glossary.md#severity-sev1-sev2-sev3) incidents. Most were caused by Northstar's
own changes, and customers reported almost half of them before any alert fired.

Your diagnosis is that the bottleneck is the Core release train: a fortnightly release of the main
application, preceded by days of manual regression testing. You attack it from several sides at once.
With Kwame Mensah (staff engineer, reliability) and Sofia Alvarez (VP Customer Success) you write
severity definitions, so that an incident's rating no longer depends on who is asked. Orphaned modules
and services get owning teams. Managers, staff engineers, and senior engineers are trained as incident
commanders. Each team reserves capacity for prevention work, 12 FTE in all, instead of hoping for
slack. Within a month Core ships weekly, and flaky tests are quarantined with named owners.

Two things go wrong, and both teach something. A run of incidents is rated Sev3, although one of them
delayed customers' payments for hours; you re-rate it and add a severity audit to the weekly review. A
pipeline check promised after an earlier ledger incident slips past its date, and in week 9 a Billing
release applies credit notes twice and cannot be rolled back. An interim rule follows, and the check
lands soon after. Follow-up actions from incident reviews are triaged, and every one that is kept gets
a manager as its owner.

Late in the quarter you announce that the QA engineers will join product teams as quality engineers.
At day 90 serious incidents are down to 21, and both renewal commitments are on track. One ownership
question, the shared permissions module in Core, is deferred under a recorded exemption.

## Quarter 2: the renewals and the operating system

The renewals come first. The accounting-system integration goes live for its customer in week 19.
Bulk ordering is complete by the end of the quarter and forecast to ship that week.

Around the delivery work you build the habits of running an organization rather than a rescue. A
decision log records who decided what. A published escalation path gives disagreements a clock and a
written case. Li Na Zhou (staff engineer, data and integration) opens Northstar's first architecture
decision record, ADR-0001, on how integrations should read ledger data. It stalls: Victor had told a
manager in passing to "read the tables now", and nobody's decision rights are mapped.

The people side shows what you had not been watching. When you measure your own week, only 4.7 percent
of it goes on seeing the work first-hand. You hold no skip-level conversations until mid-quarter. Your
first conversation with a mobile engineer, Mateo Arango Ríos in Bogotá, reveals that he has done a
lead's job for over a year without the title. Priya Raman (Orders manager) agreed to cap her own coding
time; by the end of the quarter she is well past the cap.

The numbers keep improving: 17 serious incidents, and availability of 99.86 percent against the 99.9
percent contract. But meetings fill about half your week, and your written reports to Victor stop after
the first quarter's results and resume only at the quarter's end.

## Quarter 3: capacity, portfolio, and the first quarter at target

With the renewals delivered, you plan capacity in the open. The quarterly plan has a planned case and
a cautious case for unplanned work, commits only what the cautious case can absorb, and shrinks the
prevention allocation. A portfolio rule allows at most three cross-team initiatives at once, as a trial
for the quarter. It is tested within weeks, when Greg Tanaka (VP Sales) asks for a further feature for
an open deal. The portfolio forum meets on it, and its decision is not recorded.

Your clearest failure of the year comes here. You launch an Engineering Excellence Day on your own,
without the managers or Amara Okafor (CPO). Participation falls at each session, none of the merged
work touches the debt the organization had priced, and you stop it before the quarter ends. The lesson
is about how change is led, not about the idea.

Two other things slip. The permissions module's exemption reaches its limit and lapses with no owner
chosen. And after Orders sizes a pricing feature, Greg gives a customer a date for it.

The results are the best of the year. Serious incidents fall to 14, the first quarter at or below the
mandate's target. Availability reaches 99.89 percent, still just short of 99.9. Unplanned work is 25
percent, between the planned and cautious cases. These are the latest measured figures; the last
quarter has none.

## Quarter 4: drafts, positions, and open decisions

The last quarter produces proposals, not outcomes. Three decisions drive it.

The **year-2 organization**: you propose splitting Customer Experience into a Web team under Daniel Cho
and a Mobile team under Mateo, giving the permissions module to Orders, and running Platform
Operations as an internal product. Victor decides, and alternatives sit beside the main proposal.

The **quality continuation**: staged prevention work through year 2 at a smaller allocation, with no
headcount request. Each executive takes a position. Rajiv Menon (CFO) wants the tooling cost found
inside the existing budget. Greg wants the prevention engineers on deal features and privately offers
his support in exchange for two of them; you decline and write the offer into the proposal as an
option.

The **board headline**: Victor proposes promising fewer than 10 serious incidents a quarter. You
counter with a rolling total over year 2, reported with the severity audit. The draft board page
carries both. The board meets in week 50 to approve the year-2 plan and budget, and its response is not
recorded.

Around these sit smaller open items: whether Northstar needs a VP of Engineering, a SOC 2 report that a
prospect requires, AI tools in use without a policy, and a first enterprise technology risk register.

The decisions are open on purpose. The later chapters and the capstone put you in the director's or the
CTO's seat to make them. They are also hard because they draw on the same fixed 87 seats: a VP takes
one, every prevention engineer is one Greg cannot have for deals, and your headline counter assumes the
continuation is funded. The [quarter 4 briefing](quarter-4-briefing.md) sets out each decision and what
is at stake.
