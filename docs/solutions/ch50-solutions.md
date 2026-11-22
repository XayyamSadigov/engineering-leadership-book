# Chapter 50 solutions — What a CTO Actually Does

Worked solutions for the [chapter 50 exercises](../parts/12-cto-leadership/50-what-a-cto-actually-does.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer, the
criteria a good answer meets, and the weak answer to watch for. All Northstar and Halvard data is fictional.

## F1 — Diagnosing the founding CTO's archetype

**The three questions.** Technology is the product. Nobody runs the engineering organization day to day
except the CTO, who manages four managers directly. The top technical problem with no owner is the one the
CEO names: customers want to hear from technology leadership and nobody below the CTO can speak for it.
Underneath it sits a second unowned problem: the CTO personally approves every schema change, so the
organization's technical throughput is capped by one calendar.

**Archetype.** The company is moving from visionary and operator toward either organization builder or
external-facing technologist. The CEO's request points to the second, which only works if something exists
elsewhere: someone who runs engineering (a director or VP, from the four managers or hired) and technical
direction carried by senior engineers.

**First thing to give away.** Schema approval. It binds nothing beyond engineering, is reversible with
effort, and the information sits with the teams. Replace it with a standard owner and a migration check
(Northstar's quarter 1 equivalent is Li Na Zhou's data standard and the pipeline check for unfinished
migrations). Design reviews come next, moved to a forum the CTO samples.

**Criteria.** A good answer names what must exist elsewhere, not only the archetype, and gives away the item
where others hold the information. **Weak answer:** "the CTO should become strategic" with no receiver for
the work, which produces the absent executive.

## F2 — Victor's calendar in a typical quarter 5 week

**Assumptions added.** The week stays at 48 hours. Board preparation falls from 4.0 to an average of 1.0 hour
a week (one board item a quarter, prepared over about three weeks). Year-2 decision reviews fall from 4.5 to
1.0 hour a week (the stage 1 gate in week 56 and follow-up). The keep, give, stop list has not yet been
applied. Freed hours go to strategy work.

**Arithmetic.** Seasonal rows: 4.0 + 4.5 = 8.5 hours before, 1.0 + 1.0 = 2.0 after; 6.5 hours freed. Strategy
work rises from 2.0 to 8.5 hours. Work only the CTO can do: 3.0 + 1.0 + 0.5 + 5.0 + 1.0 + 1.0 + 8.5 = 20.0
hours, the same total as before, about 42 percent of 48. What changes is composition: non-seasonal work only
the CTO can do (executive team, peers, director, customers, strategy) goes from 3.0 + 1.0 + 0.5 + 5.0 + 2.0 =
11.5 hours (24 percent) to 18.0 hours (37.5 percent).

**If the delegation list is also applied**, a further 7.0 hours move: strategy work 15.5 hours, work only the
CTO can do 27.0 hours, about 56 percent.

**What grows unless managed.** Email and the unrecorded rulings: freed time is the most likely to be absorbed
by requests nobody redirects.

**Criteria.** States assumptions, shows the sum, distinguishes seasonal from structural. **Weak answer:**
treating weeks 44 to 46 as Victor's normal week and concluding that 42 percent is healthy, when 8.5 of its 20 hours are seasonal.

## F3 — A decision-rights table for a 90-engineer company

| Decision | Owner | Seam? |
|---|---|---|
| Product technology direction | CTO | No |
| Allocation across engineering teams | VP of Engineering, inside the CTO's envelope | No |
| Engineering managers' hiring and staffing | VP of Engineering | No |
| Internal business systems | Head of IT | No |
| Production access and identity | Head of IT runs the directory; VP owns production role grants | Yes, split by layer |
| Vendors serving product and internal systems | Budget holder, with written technical sign-off from the other | Yes |
| Customer security questionnaires | CTO accountable; evidence owners named per control | Yes |
| Product security tooling | VP of Engineering | Shared controls with IT |

**First dispute.** Customer security evidence. Customers address the CTO, the controls sit partly in IT
(identity, devices, logging) and partly in engineering (pipeline, dependencies), and the head of IT reports to
the CFO, so neither side can instruct the other. The questionnaire deadline forces the question within weeks.
Vendor contracts are a defensible second choice because renewals arrive on fixed dates.

**Criteria.** One owner per row, seams marked explicitly, and the dispute prediction tied to who reports to whom.
A good answer also says how the split of a seam is written (by layer, by budget, or by accountability versus
operation). **Weak answer:** "shared" in a cell, which assigns the decision to nobody.

## A1 — Accepting the sales-call work

**Decision.** Accept the principle, not the proposal as written. Staff engineers on deal calls is a sensible
receiver: they hold the technical information, and customer exposure develops them. But all three have standing
scopes and quarter 4 commitments, and Northstar's quarter 3 portfolio work already shows how unsized requests
erode capacity.

**What to say.** "I agree the deal calls should come off your calendar, and staff engineers are the right people
for the technical questions. I can't name one per deal without knowing the load. Can you give me the last six
weeks of calls: how many, how long, which accounts? If it is about two hours a week, I will rotate it among the
three staff engineers and take it out of their quarter 4 scopes explicitly, and I will tell Greg Tanaka the
rule: you join for top-40 accounts and roadmap-changing deals, a staff engineer for the rest. I need you to back
that rule the first time Greg asks for you anyway."

**Criteria.** Sizes the work, names what is displaced, puts the rule in front of the stakeholder who will test
it, and asks the CTO for the support only the CTO can give. **Weak answer:** accepting silently, which moves the
cost from Victor's calendar to unrecorded staff engineer time; or refusing, which leaves the 3.5 hours where
they are.

## A2 — Redirecting the eleven requests

**Genuinely the CTO's (three).** Decide, and log the decision in the organization decision log with a reason. Say
so: "This one is mine because it binds the company; here is the decision and where it is recorded."

**Under the escalation path (six).** "That is a decision for the two teams, then the director under the
escalation path. I am not going to decide it, and if I give a view now it will be read as a decision. Take it
to the director." Log the request as redirected.

**With the standard owners (two).** "Kwame Mensah owns pipeline standards; he decides within ten working days.
Ask him." The same for Li Na Zhou on data.

**Second ask.** Repeat the redirect word for word and tell the director, so the pattern is visible. If the person
argues urgency, ask whether the owner has been told it is urgent; if not, that is the next step.

**Did it work?** After a quarter, count again over three weeks: total informal requests, share redirected, and
whether repeat askers dropped. Corroborate with the decision log: do decisions in those classes now appear with
the owners as deciders? Watch for one countersign: requests disappearing entirely may mean people stopped telling
Victor things, which is the absent-executive failure.

**Weak answer:** a memo announcing that Victor will no longer give informal rulings, with no redirect script and
no measure.

## A3 — Transferring the previous CTO's forums

**Quarter 1.** Attend all three forums as they are, in their current format, for four to six weeks to learn them (this solution's judgment), in the spirit of Larson's advice to limit
concurrent changes. Then hand the operational review to
the two directors (alternating chair, or each for an area), the architecture review to the senior engineers who
own technical standards, and the incident review to the incident process owner. Announce each transfer with the
decisions the new chair now owns and what still comes to the CTO.

**Quarter 2.** Attend a sample: one operational review a month, the architecture review when a company-level
decision is on the agenda, any review of a Sev1. Chair two new forums: a monthly business review with both
directors and a monthly technical direction review.

**Avoiding the disengagement signal.** Transfer forums one at a time, explain the reason (decisions belong with
the people holding the information), keep skip-level conversations, and show up unannounced to a sample.
Continue to read every Sev1 review.

**Criteria.** Learns before changing, names a receiver and the decisions transferred, keeps a sampling presence,
and adds forums for the CTO's own loops. **Weak answer:** dropping all three in week one, or keeping all three
"for now", which in practice means permanently.

## X1 — Choosing an option for the IT and security seam

**One defensible choice: option 1, written narrowly.** Keep the structure, write the table, and leave the security
questionnaire row undecided until after the audit committee's week 50 technology risk session
([Chapter 53](../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md)). Moving IT is a large
structural change made in the same month as three other open structural questions; it would cost Rajiv an
organization and give Victor work his own audit says to shed.

**Sequencing.** Do not send it before the board. Week 48 is the VP recommendation; week 50 is the board. Raise the
table in the first Rajiv one-on-one after week 50, as a working page, not a proposal.

**The note (draft).** "Rajiv, after the board I'd like 30 minutes on a page I have drafted: five decisions our
organizations share, with a proposed owner for each. Two are housekeeping (internal systems stay with Marta;
pipeline security tooling stays with engineering). Two need your view: production access, which I propose to split
by layer (IT runs the directory, the director owns production role grants), and vendor contracts that serve both
of us, where I propose the budget holder decides with the other side's written sign-off. The fifth, customer
security evidence, has a proposal in the director's security strategy draft (an evidence library owned by Joon,
with Kwame Mensah as engineering evidence owner); I suggest we decide it after the audit committee's technology
risk session, and until then I will keep answering questionnaires with Joon. I am not proposing to move IT."

**What would make option 2 right.** Evidence that the seam is causing customer or audit harm that a table cannot
fix: repeated contradictory answers to customers, a control failure between the two organizations, or the CFO
wanting to hand IT over.

**Weak answer:** choosing option 2 on tidiness, or option 3 as indefinite waiting with no date.

## X2 — The "more strategic CTO" request (hypothetical)

**What it implies.** Half of 48 hours is 24 hours a week on customers and the board. Today those rows are 5.0
(customers) plus 4.0 (board, seasonal): Victor would move toward the external-facing archetype. The archetype table
says this works only if someone runs engineering, and the condition is a written split of decisions. At Northstar the
director runs the 87 seats already; what is unwritten is which decisions are the director's.

**What must move and to whom.** The delegable rows (sales calls, rulings, incident bridges, questionnaire drafting:
up to 7.0 hours on the chapter's plan) go to the receivers in the keep, give, stop list. Year-2 reviews still need
Victor until week 51. The extra customer and board time beyond that, roughly 24 − 5 − 1 (board, steady state) = 18
hours a week more than the steady-state rows, would come mainly from strategy work and from Victor's presence in
engineering, which is the absent-executive risk.

**What to tell Helena.** That an outward CTO needs either a director with written VP-level decision rights or a VP,
that the choice is the open week 48 question, and that the request should wait for it. If the answer is a VP, the
cost is one of 87 seats (engineers 79 to 78 under the main proposal) and a new layer. If the director grows into
the role, the cost is a span of 10 and a written delegation. Either way, Victor keeps the strategy row; "strategic"
cannot mean customers instead of strategy.

**Criteria.** Converts the request into hours, names the condition for the archetype, makes the dependence on week
48 explicit without answering it. **Weak answer:** agreeing to 50 percent on customers without saying who takes the
inside, or deciding the VP question inside this answer.
