# Engineering strategy template

**Used in:** Chapter 30 (technical strategy and technology selection), Chapter 51 (the CTO's
technology strategy).
**Owner:** the engineering director or CTO, written with the staff engineers; each guiding policy has
a named owner who decides exceptions to it.
**Cadence:** written once and kept to about two pages; the diagnosis is re-read quarterly against the
technology risk register, and the whole document is revised when a review trigger fires.

An engineering strategy is a diagnosis of what makes the situation hard, a few guiding policies that
decide many later choices in advance, and the actions that make the policies real. The structure is
Rumelt's strategy "kernel" ([Rumelt, 2011](../references/bibliography.md#rumelt2011good)), which Will
Larson applies to engineering, arguing that coherent actions are the most important part
([Larson, 2023](../references/bibliography.md#larson2023engstrategy)). Both are **expert opinion**.
This template adds two sections the kernel leaves implicit: what the organization will not do, and
the conditions that reopen the strategy.

A document with a vision, a list of goals, and a target architecture diagram is not a strategy under
this definition. If nothing in it would have changed a decision made last quarter, it is decoration.

## How to fill it in

1. **Collect evidence before writing.** Incidents by trigger, components by owner and runtime
   version, the debt and risk registers, and the cost of the estate. The diagnosis cites numbers from
   these, not impressions.
2. **Write the diagnosis first, and keep it to three findings or fewer.** Each finding names a cause,
   gives one or two numbers, and says why it matters to the business. "Our platform is legacy" is not
   a finding; "63 percent of our serious incidents are triggered by our own changes" is.
3. **Write two to four guiding policies.** Each one must be applicable (a team can tell whether a
   proposal complies), must cost something (name the freedom it removes), and must trace to a
   finding. Test each against one real decision from last quarter: would the policy have decided it?
4. **List coherent actions in three kinds.** *Enforcements* (how compliance is checked), *escalations*
   (who decides exceptions, within what time), and *transitions* (work that moves the estate toward
   the policy). Every action has an owner and a date.
5. **Write "What we will not do".** Name the attractive options the strategy rules out, so that
   nobody spends a quarter proposing them again. Include at least one that a senior person wants.
6. **Write review triggers.** Observable conditions, each with a check date or a data source, that
   reopen the diagnosis. Without them a strategy is revised only when its author leaves.
7. **Workshop before circulating.** Take the draft one-on-one to the staff engineers and to each
   manager whose team the policies constrain most, then to the CTO or executive sponsor.

## Template

| Section | Contents | Test |
|---|---|---|
| Scope and horizon | Which systems and teams it covers; the period (usually 12 to 24 months) | Could a team tell whether its component is in scope? |
| Diagnosis | Up to three findings, each with evidence and business consequence | Would a skeptical peer accept each number? |
| Guiding policies | Two to four rules, each with its cost and the finding it answers | Would it have decided a real past decision? |
| Coherent actions | Enforcements, escalations, transitions; owner and date each | Does every policy have at least one enforcement? |
| What we will not do | Options ruled out, with the reason | Does it disappoint someone with influence? |
| Review triggers | Conditions that reopen the strategy, with where each is observed | Can each be checked without a meeting? |
| Exceptions log | Link to recorded exceptions to the policies | Are exceptions dated and expiring? |

```yaml
strategy:
  title: ""
  version: ""                # for example 0.1 draft
  author: ""
  contributors: []
  scope: ""
  horizon: ""                # for example "quarters 2 to 5"
  status: draft              # draft / agreed / superseded
  agreed_by: ""
  agreed_on: ""
diagnosis:
  - id: D1
    finding: ""
    evidence: []             # numbers with their source
    consequence: ""          # why it matters to customers or money
guiding_policies:
  - id: P1
    policy: ""
    answers: [D1]
    cost: ""                 # the freedom or option it removes
    owner: ""                # decides exceptions
    test_decision: ""        # a past decision it would have settled
coherent_actions:
  - {id: A1, kind: enforcement, action: "", policy: P1, owner: "", due: ""}
  - {id: A2, kind: escalation, action: "", policy: P1, owner: "", due: ""}
  - {id: A3, kind: transition, action: "", policy: P1, owner: "", due: ""}
will_not_do:
  - {option: "", reason: ""}
review_triggers:
  - {condition: "", observed_in: "", check: ""}
next_review: ""
```

## Example: Northstar, week 14 draft

**Fictional.** The three policies, the diagnosis, and the register items come from
[Chapter 30](../parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md) and
the [first quarter](../case-studies/northstar/first-quarter.md) page. The scope line, the
"will not do" list, the review triggers, and the policy owners are illustrative additions for this
template. Dates are weeks from the director's first day.

```yaml
strategy:
  title: Northstar technical strategy
  version: 0.1 draft
  author: Engineering Director
  contributors: [Ines Carvalho, Kwame Mensah, Li Na Zhou]
  scope: All 24 components in components.csv and the four build systems
  horizon: quarters 2 to 5 (weeks 14 to 65)
  status: draft
  agreed_by: ""              # Victor Lindqvist, not yet
  agreed_on: ""
diagnosis:
  - id: D1
    finding: Change is unsafe
    evidence:
      - 19 of 30 baseline Sev1 and Sev2 incidents (63 percent) triggered by Northstar's own changes
      - changes ship through four different build systems
    consequence: Availability of 99.62 percent against a 99.9 percent contract; $410,000 credits
  - id: D2
    finding: The estate ages unwatched
    evidence:
      - oldest critical vulnerability disclosed 19 months earlier
      - nobody owned runtime and framework versions; Core framework past free community support
    consequence: Security questionnaires from renewal customers cannot be answered with evidence
  - id: D3
    finding: Knowledge is concentrated
    evidence:
      - shell-script deploys for four services understood by one engineer
      - one Jenkins controller with one de facto first responder
      - ledger currency and rounding changed safely by one person
    consequence: One departure turns a routine change into an incident
guiding_policies:
  - id: P1
    policy: Converge before adding. No new runtime, datastore, or build system for a tier 1
      component without a retirement plan for one already in use
    answers: [D1, D3]
    cost: Teams lose the freedom to pick tools
    owner: Kwame Mensah
    test_decision: CI consolidation target (DL-10)
  - id: P2
    policy: Own the order-to-cash logic; buy what changes for reasons outside Northstar
    answers: [D3]
    cost: Vendor spend and dependence for tax rates and partner formats
    owner: Ines Carvalho
    test_decision: tax-svc build, buy, or hybrid (TR-09, DL-09)
  - id: P3
    policy: Every tier 1 component runs on supported versions and has two people who can change it
    answers: [D2, D3]
    cost: Upgrade and pairing work taken from feature capacity
    owner: Li Na Zhou
    test_decision: Core framework migration (TR-01)
coherent_actions:
  - {id: A1, kind: enforcement, action: "Technology risk register TR-01 to TR-09, reviewed monthly by the director and staff engineers", policy: P3, owner: Engineering Director, due: week 16}
  - {id: A2, kind: escalation, action: "Exceptions to P1 decided by the director within 10 working days and recorded", policy: P1, owner: Engineering Director, due: week 14}
  - {id: A3, kind: transition, action: "Supported-version plan for Core (TR-01, TR-03)", policy: P3, owner: Ines Carvalho, due: week 26}
  - {id: A4, kind: transition, action: "Second responder for each one-person system (TR-02, TR-06, TR-07)", policy: P3, owner: Tom Becker and Marcus Oyelaran, due: week 26}
will_not_do:
  - {option: "Rewrite Core", reason: "Constraint 3; the diagnosis points at change safety, not at the codebase"}
  - {option: "Fund the core/customer redesign (about three engineer-years) in quarter 2", reason: "Only the permissions extraction is funded; slice the rest once that seam holds"}
  - {option: "Add a fifth build system for new services", reason: "P1"}
review_triggers:
  - {condition: "Change-induced share of Sev1 and Sev2 still above half for two quarters", observed_in: incident tracker, check: quarterly}
  - {condition: "Any TR item reaches score 9 with no funded response", observed_in: risk register, check: monthly}
  - {condition: "Constraint 3 or the flat-headcount constraint is lifted", observed_in: CTO, check: on change}
next_review: week 26
```

What to notice: each policy has a decision already waiting for it in the decision log, so the first
quarter of the strategy's life is a live test of whether it decides anything. Policy 2 points toward
buying tax-rate content but does not choose between the vendor engine and the hybrid; that remains a
selection decision with its own costs ([Chapter 30](../parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md)).
The first "will not do" line restates a constraint the CTO set; the second disappoints Ines Carvalho,
which is why it is written down.

## Common mistakes

- **Goals as strategy.** "Become cloud-native" or "modernize the stack" with no diagnosis. A goal
  says where you want to be; a strategy says why it is hard and what you will do about it.
- **Policies that cost nothing.** "Use the right tool for the job" rules nothing out and decides
  nothing. If no team would object to a policy, it is not doing work.
- **Actions without enforcement.** A policy with only transitions is a project list; a policy with
  no escalation path is ignored the first time a deadline presses.
- **An empty "will not do".** If nothing is ruled out, the strategy has not chosen.
- **Writing alone.** A strategy drafted without the staff engineers is unenforceable; one written by
  committee has no diagnosis.
- **No review trigger.** The diagnosis goes stale while the policies keep being cited.

## Review questions

1. Which decision from last quarter would each policy have settled, and would it have settled it
   differently from how it was actually decided?
2. Which finding has the weakest evidence, and what would you measure to strengthen or drop it?
3. Who loses something under this strategy, and have they read it?
4. Which review trigger is most likely to fire first, and who will notice?
