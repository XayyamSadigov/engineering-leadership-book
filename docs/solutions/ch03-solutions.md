# Chapter 3 solutions — Managerial Leverage and Systems Thinking

Worked solutions for the [chapter 3 exercises](../parts/01-foundations/03-managerial-leverage-and-systems-thinking.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — The stock of safe ledger responders

**The map.** One stock: engineers who can safely respond to a ledger incident. Inflow: engineers who
become safe responders (through pairing, shadowing, runbooks, and practice). Outflow: safe responders
who leave the team or the rotation. Upstream of the inflow sits a second stock, Billing engineers who
are not yet safe responders, fed by backfills with a 15-week delay.

**The history.** Four at the start of the year; one resignation about nine months before the director
arrived leaves three. The backfill started 15 weeks later and was not on the rotation by the end of the
baseline quarter.

**Assumptions and prediction.** Say, as an assumption, that without pairing a new engineer needs about
nine months to become safe, because the experts have no time to teach, and that with deliberate pairing
and runbook time it takes about four months. Without pairing, the stock is still three at the end of
two quarters, perhaps reaching four just after, and it falls to two if one expert leaves. With pairing
started now, the backfill and two of the other ten engineers could be safe within two quarters, giving
five or six.

**The fastest flow** the director controls is the inflow through teaching time, not hiring, which is
limited by flat headcount and the backfill delay; the second fastest is the outflow, by reducing the
experts' load. The weak answer models only hiring and concludes that nothing can change for a year.
A good answer states its ramp assumptions and shows how sensitive the prediction is to them.

## F2 — Classifying eight responses

| Response | Level | Effect on the concentration loop |
|---|---|---|
| Higher stipend | Parameter | None on concentration; may delay a departure |
| Second weekly incident review | Delay or information, depending on design | Could shorten feedback; could also add load to the experts |
| Hiring request | Stock inflow | Small and late |
| No-action page purge | Inflow to the loop | Removes about a third of pages, most from the experts |
| Pages-per-person chart | Information flow | Makes the concentration visible to managers |
| Escalation-only rule for experts | Rule | Reverses the loop |
| Award for best incident response | Rule (incentive) | **Strengthens** the loop |
| Protected runbook time | Loop gain | Slows concentration |

**The hardest two.** The award looks like recognition, and recognition is good. But an award for best
incident response goes to whoever fixed the worst outage, which will usually be one of the three
experts. It rewards the behavior that produces concentration; Perlow's study found that rewards for
individual heroics helped sustain a team's crisis pattern. A better award recognizes the runbook that
let a non-expert restore service. The second review depends on who attends and what it looks at: if
it reviews pages per person and asks why non-experts escalated, it is an information flow; if it is
another meeting the three experts must attend, it consumes the resource the loop is short of.

A good answer catches the award. The weak answer ranks all eight by cost alone.

## F3 — The constraint is a person

**The constraint** is Ines Carvalho's decision time on Core module boundaries: every such decision
waits for her. The pipeline is not the constraint for this work. Shaving 20 minutes from a 74-minute
pipeline may be worthwhile on its own merits, but it does not raise the rate at which boundary
decisions are made, so it does not improve the flow the working group cares about. This is the
classic non-constraint optimization: a real local gain and no system gain.

**Getting more from the constraint without longer hours:**

1. **Stop spending her time on work others can do.** The chapter's baseline shows about eight hours a
   week of unscheduled Core questions. Replace them with written module boundary rules and a weekly
   office hour, so most questions are answered once.
2. **Subordinate the rest of the process to her.** Batch boundary decisions into a fixed weekly slot
   with written proposals prepared by the requesting team, so her time goes to judgment, not to
   gathering context.
3. **Relieve the constraint over time.** Delegate decisions within the written rules to two senior
   engineers, with Ines reviewing a sample afterwards.

The weak answer asks Ines to prioritize better, or approves the pipeline work as "flow improvement".
A strong answer names what will be measured: decision wait time and the share of decisions made
without her.

## A1 — Redesigning the director's week

**Ranking, lowest leverage first:** joining incident calls (the director adds a person to the call
without changing the structure; Chapter 25 separates coordinating from fixing), personally approving
technical changes (makes the director a constraint), status meetings (information that could flow in
writing), email and chat (mostly reactive). Highest leverage: one-on-ones with managers and staff
engineers, hiring (it sets the stock of capability for years), and the parts of product meetings where
goals and trade-offs are set.

**One redesign:**

| Category | From | To | Freed | Risk |
|---|---|---|---|---|
| Status meetings | 9 | 3 | 6 | Lost situational awareness; mitigate with a written weekly update |
| Incident calls | 5 | 1 | 4 | Looks absent; attend Sev1s as communicator only |
| Approvals | 4 | 0.5 | 3.5 | Early mistakes; delegate within written decision rules |
| Email and chat | 8 | 6 | 2 | Slower replies; set expectations |

The 15.5 freed hours go to: writing decision rules and staff-engineer mandates (4), coaching managers
and skip-level conversations (4), designing what the weekly review shows (2), mapping the
organization's loops and checking them against data (3), and unscheduled slack (2.5), because a week
with no slack turns every surprise into overtime.

A good answer protects the new hours on the calendar and says what will be checked in a month. The
weak answer cuts one-on-ones because they are "not urgent", removing the director's best information
flow.

## A2 — Ines and the designs nobody proposes

**Frame.** Ines is responding sensibly to the system: questions arrive, she knows the answers, and
answering is fast and valued. The effect is that others stop thinking, which concentrates knowledge
further. This is a structure problem, and the conversation should say so.

**Ask first.** Which questions does she answer most often? Which does she wish people would decide
themselves? What would she do with eight more hours a week? How does she feel about the Orders
engineers' comment? (Report it without names, and only if they agreed.)

**Bring data.** The two-week sample of unscheduled time (about eight hours a week), the number of
design proposals from outside her in the last quarter, and how long decisions wait for her.

**Offer a mandate.** Ownership of written Core module boundary rules, which is also where her
judgment has the most reach, with an explicit expectation that she reviews others' proposals rather
than writing the answer. In multiplier terms, her job becomes raising the quality of other people's
decisions.

**Measure in a quarter.** Hours of unscheduled questions (target: falling), proposals from others
(rising), and decisions made within the rules without her.

The weak answer tells Ines to "let others speak", which treats a structural pattern as a personality
flaw and will feel like a demotion to someone with eleven years on Core.

## A3 — The stipend request

**Decision: approve, with conditions.** The retention risk is real and immediate, and out-of-hours
on-call work should be compensated, as the SRE Workbook's on-call chapter states. Refusing would cost
trust when Marcus is asking for the one thing he can do this week. Approving it alone repeats what the
previous management did, and the loop would be unchanged in a quarter.

**The reply, in substance:**

- Approved, effective this month.
- This week: take the expert who is close to leaving off primary for a fixed period, say for how
  long, and keep them as a business-hours escalation contact by agreement.
- Within a month: delete or demote the no-action pages (about a third of the quarter's 180), and put
  pages per person on the weekly review.
- Within the quarter: experts become escalation-only, with pairing, and get protected time to write
  runbooks for the recurring ledger failure modes.
- Review in the monthly meeting: pages per expert, escalations, and Billing restore times.

**Avoiding drift.** Tie the stipend's review date to the structural plan's review, so the
conversation about money is also a conversation about load. Chapter 24's rotation design gives the
details.

The weak answers are a flat refusal ("money will not fix this") and an unconditional approval.

## X1 — Delaying backfills

**Capacity cost.** At the chapter's attrition rate (8 a year, about 2 a quarter), delaying each
backfill by a quarter (13 weeks) adds about 26 empty seat-weeks per quarter, half an engineer-year.
Over a year that is about 2 engineer-years, roughly $370,000 at $185,000 per engineer-year. That is
also the saving, and it is a timing saving: once the policy ends, the cost returns.

**The loops it strengthens.** Workload on the remaining engineers rises while their number falls,
which raises attrition risk, which creates more vacancies: a reinforcing loop. Every concentration
loop gets worse, because the people who leave take knowledge and the people who stay have less time to
teach. A departure from Billing's three ledger experts would leave two, at the moment the team is
trying to spread the load.

**Recommendation to Helena Marsh.** Do not delay backfills for roles on tier 1 paths or for people who
hold scarce knowledge; delay only where the team can absorb it, case by case. To meet the CFO's goal,
look for saving that does not drain the experience stock, such as consolidating the four CI systems
(about 1.5 FTE of infrastructure time a year) or reviewing tooling spend. State the risk plainly: the
saving is small against $9M of renewals that depend on reliability.

A good answer quantifies both sides and names the loop. The weak answer argues only from morale.

## X2 — A rule or a dashboard

**Placement.** The rule sits at the rules level of Meadows's list; the dashboard is an information
flow, one level lower. Both are well above parameters.

**Recommendation: the rule, with the dashboard's on-call measure as its means of enforcement.** The
rule directly reverses the concentration loop, and enforcing it requires measuring first-responder
share anyway, so most of the information flow comes with it. The dashboard alone relies on managers
acting on what they see; at Northstar, the concentration in Billing persisted for most of a year in
plain sight of the people closest to it.

**Costs of the rule.** Slower restores while others learn; exceptions requested for every specialist
system; and gaming, such as routing pages through a nominal first responder who immediately escalates.
Guard against the last by counting escalations, not only first responses.

**What would make you switch after two quarters:** restoration times that are worse and not
improving, evidence of routing games, or teams that comply on paper while experts still do the work
at night. In those cases the rule is not being absorbed, and transparency plus manager coaching may do
more.

The dashboard is also defensible for an organization with poor data, where the first problem is that
nobody can see the load at all. The weak answer picks one without saying where each sits or what
evidence would change the choice.
