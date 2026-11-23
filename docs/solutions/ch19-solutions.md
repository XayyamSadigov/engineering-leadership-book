# Chapter 19 solutions — Defining, Measuring, and Owning Software Quality

Worked solutions for the [chapter 19 exercises](../parts/05-engineering-quality/19-defining-measuring-and-owning-quality.md#exercises).
Most of these exercises have more than one defensible answer. Each solution gives one worked answer,
the criteria a good answer meets, and the weak answer to watch for. All Northstar data is fictional.

## F1 — Three people, three meanings

**Classification.** The head of customer success holds an **external**, user-based view: quality is
what customers experience. The QA lead holds a **conformance** (manufacturing-based) view, which is a
narrow slice of external quality: the product matches its specified behavior. Ines Carvalho (staff
engineer, Core domain) holds an
**internal** view: quality is how safely the system can be changed. Garvin's transcendent strand is
also present in "code we can change without fear", which is easier to feel than to measure.

**Why each is incomplete.** "Fewer angry customers" lags by weeks and mixes product quality with
support quality and expectations. "The regression suite passing" misses everything the suite does not
describe, including the 27 escaped defects built exactly as specified and the 81 regressions that
escaped despite the pass. "Code we can change without fear" is real but invisible to customers and
slow to show results.

**Measures each could accept.** For customer success: customer-detected share of Sev1 and Sev2
incidents (47 percent today), because it counts problems customers found first. For the QA lead:
regression share of escaped defects (38 percent), because it tests the claim the suite exists to
make. For Ines: change failure rate for Core changes (31 percent), paired with deployment frequency,
because it shows whether changes are safe.

A good answer finds measures that each person would recognize as fair. The weak answer declares one
view correct and dismisses the others.

## F2 — A payment-path quality profile

One defensible profile, with invented thresholds marked **illustrative**:

1. **Availability.** The payment path is available at least 99.9 percent of each quarter, measured by
   synthetic checks (the contractual commitment; current 99.62 percent). Owner: Payments and
   Integrations for the gateway and connectors, Billing for invoicing and ledger. Chapter 24 turns
   this into an SLO.
2. **Correctness of money.** Payments are applied to the right invoice exactly once; duplicate or
   missing applications stay below an illustrative 1 per 10,000 payments. Owner: Billing, with
   Payments and Integrations at the boundary.
3. **Timeliness of reconciliation.** Payment status reaches the customer's accounting system within
   an illustrative 15 minutes for 99 percent of payments. Owner: Payments and Integrations.
4. **Not verifiable by conformance testing:** a distributor's finance staff can reconcile a day's
   payments without contacting Northstar support. Owner: the product manager for payments with the
   two teams; measured by support contacts tagged to reconciliation.

**Left out deliberately:** latency below a strict threshold (customers have not cited it, and
availability and correctness matter more), maintainability (internal, kept on the separate list),
and accessibility of payment screens (important, but owned on the web and mobile paths).

A good answer states properties a team could observe this month, names owners at component
boundaries, and admits which thresholds are invented. The weak answer lists ISO characteristics
without thresholds or owners, or writes "the payment path is reliable".

## F3 — Ranking teams by defects per engineer

**The ranking.** Escaped defects per engineer last quarter: Platform Operations 0.75 (9/12), Data and
Analytics 1.7 (19/11), Payments and Integrations 2.6 (31/12), Customer Experience 2.9 (44/15), Orders
3.6 (51/14), Billing 4.5 (58/13). The "best" team is Platform Operations.

**Why it misleads.**

- **Exposure.** Platform Operations' changes rarely reach customers directly, so customers rarely
  report its defects. Customer Experience owns the web and mobile apps, the surfaces customers touch
  most. The ranking measures distance from the customer.
- **Architecture.** Orders and Billing ship most of their work through the Core release train, whose
  large batches produce more defects per release whoever writes the code. Their position partly
  reflects the train.
- **Attribution.** Defects in shared, unowned Core modules (customer, permissions, scheduler) are
  attributed by whoever triaged them, so counts depend on the triage.
- **Behavior.** Rewarding a low count rewards arguing defects into feature requests and slowing triage.

**A better use.** Compare each team with its own baseline over time, broken down by detection point,
and use the breakdown to decide which checks each team should own. Use cross-team views only to find
shared causes, such as the train or the unowned modules. The weak answer adjusts the normalization
(per deployment, per line of code) and keeps the ranking; every normalization still measures
something other than discipline.

## A1 — Responding to Tom Becker on independence

**What is supported.** Tom Becker (Platform Operations manager) is right that independence is a real
property: testers without a stake in the change find
things authors miss, and specialized testing skills exist. The research on testing roles also shows
that domain knowledge is a testing asset (Mäntylä, Itkonen, and Iivonen, 2012), and Northstar's QA
engineers have years of it. Concede both.

**What is not supported.** No study shows that removing a central QA group raises escaped defects;
the evidence on the question is thin and unresolved. And the baseline undercuts the claim that the
current model is protecting customers: 212 escaped defects last quarter, 81 of them regressions, and
14 of 30 incidents found by customers, all with the three-day pass in place. Chapter 27 records that
the pass caught none of the nine train-triggered incidents.

**Data to bring.** The detection-point breakdown: 106 of 212 defects at unit or contract level,
which the authoring team's tests are best placed to catch; 41 end-to-end defects, where Tom's
engineers add the most. The cost of the pass: about $440,000 a year in QA time.

**What to concede.** Embedded quality engineers keep the knowledge and an independent eye inside each
team; a narrow independent check can remain for irreversible migrations. Do not concede keeping the
manual pass as the main gate. The weak answer treats it as a debate to win; the strong one treats Tom
as the person who knows most about what the pass actually finds and asks him for that data.

## A2 — An embedded quality engineer's mandate in Billing

**Owns.** The team's test strategy for invoicing, ledger, and tax: which risks are tested at which
level (with Chapter 22's vocabulary); exploratory testing of new invoicing and credit-note behavior;
coaching developers on test design for financial rules; the team's escaped-defect analysis by
detection point, presented at the monthly quality review.

**Does not.** Execute regression cases on behalf of developers; act as the release gate; write all
of the team's automated tests; own incidents.

**Time split.** First quarter, illustrative: 40 percent automating the highest-value manual cases
for Billing's areas (they know which ones matter), 25 percent exploratory testing of in-flight work,
20 percent pairing with developers on tests, 15 percent defect analysis. After two quarters:
automation falls to about 15 percent, coaching and exploratory testing rise, analysis stays.

**Collapse signals at six months.** Most of their time is spent executing tests; developers' merge
requests wait for them; Billing's developers write fewer tests than before; the engineer is paged for
defects. Any two of these call for a reset with the manager. Because Billing has three people carrying
most on-call pages, the manager must protect the role from becoming a fourth incident responder.

The weak answer describes a tester embedded in a team: same job, different seat.

## A3 — Elena's team and its boundaries

**Decision.** One defensible choice: do not impose an embedded quality engineer on Elena Sokolova's
Payments and Integrations team if its ownership is working, but do make the boundary defects owned. The detection-point
data says the problem is at the contracts between teams, not inside the team.

**How.**

- Name the boundaries: invoicing to payments-gateway, payments-gateway to webhooks, and erp-sync to
  customers' accounting systems. For each, name the provider and consumer teams.
- Ask Elena's team to lead contract tests on the boundaries it consumes and provides, with Billing
  as the counterpart; make Platform Operations' infrastructure engineers responsible for making the
  tooling cheap.
- Resolve the webhooks ownership (currently orphaned, assigned by default to Payments and
  Integrations) explicitly, because an orphaned component on the boundary will absorb defects.
- Offer, rather than assign, a quality engineer for the accounting-integration renewal commitment,
  where domain risk is high.

A strong answer respects existing ownership as an asset and fixes the gap with a boundary mechanism.
The weak answers are uniformity ("every team gets one") or deference ("they're fine, leave them").

## X1 — Keeping quality specialists

**Recommendation.** Tell Victor Lindqvist (CTO): keep quality specialists, change what they do. Embed most of the seven in product
teams as quality engineers; automate the manual regression pass over two quarters; keep a narrow
independent check for irreversible data migrations on the payment path.

**Evidence and limits.** "No QA" at admired companies usually means no separate QA department, with
heavy investment in engineer-owned testing and shared infrastructure; *Software Engineering at Google*
describes that model at one very large company, and it is documented practice, not proof it
transfers. No study directly compares the models; the evidence is thin. The best research available says domain
knowledge matters for validation and that defects raised inside teams are fixed more often (Mäntylä,
Itkonen, and Iivonen, 2012). Northstar's data say the current central pass is expensive ($440,000 a
year) and is not preventing customer-visible failures.

**Why not zero.** Northstar has a 99.9 percent contractual commitment, money-handling logic, and
teams that have never owned testing. Removing specialists now would remove the knowledge needed to
automate what the pass covers and to teach teams.

**What would change my mind.** If after two quarters embedded engineers are mostly executing manual
tests, or escaped end-to-end defects rise in teams with embedded engineers, revisit the model. If
teams with no embedded engineer show the same improvement, reduce specialist roles over time through
attrition and career moves, not layoffs. The weak answer argues philosophy without the commitment and
the money.

## X2 — A single number for the board

**Instead of one number,** offer four or five measures in business terms:

1. Availability of the order and payment paths against the 99.9 percent commitment, quarterly.
   Distortion: excluding "planned" windows or measuring from one region; Northstar's checks already
   miss the mobile path. Defense: publish the measurement method and its gaps.
2. Service credits paid. Distortion: commercial concessions given outside the credit mechanism.
   Defense: report credits and goodwill concessions together.
3. Customer-detected share of Sev1 and Sev2 incidents. Distortion: rating incidents below Sev2.
   Defense: severity defined by customer impact and audited.
4. Revenue in accounts where reliability is a stated concern. Distortion: the sales team stops
   recording reliability as the reason. Defense: customer success owns the field, not engineering.
5. Optionally, change failure rate on Core, as the leading indicator. Distortion: fewer releases.
   Defense: report it with release frequency.

**Protecting team measures.** Detection-point breakdowns, regression share, coverage, and team-level
scorecards stay inside engineering. The board sees organization-level outcomes and trends with stated
confidence, never team rankings. Explain to the board that the measures teams use for learning stop
working once they become targets for judgment.

A good answer gives the board fewer, business-level measures with their distortions and a firewall
between board reporting and team improvement. The weak answer supplies a composite "quality index",
which hides the trade-offs and invites the gaming the chapter warns about.
