# Engineering Manager performance rubric

**Used in:** [Chapter 4](../parts/01-foundations/04-the-leadership-ladder.md) (measuring managerial
effectiveness), [Chapter 41](../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md)
(managing and developing engineering managers).
**Owner:** the manager's manager (usually the director); the manager writes a self-assessment
against the same rubric first.
**Cadence:** a two-quarter evidence window. Recheck the development plan quarterly; re-rate every
two quarters, [calibrated](../glossary.md#calibration) across all managers who report to the same leader.

An engineering manager's output is a team that delivers and keeps improving without them. This
rubric assesses that, on six dimensions, using evidence a third person could check. It replaces
the common default of reviewing managers on their team's roadmap delivery alone, which rewards
renegotiated commitments and personal heroics and ignores whether the team is getting stronger.

## How to fill it in

1. Fix the window: the last two quarters, with start and end weeks.
2. Collect evidence before rating: incident and review records, the scorecard, promotion packets,
   one-on-one notes the manager chooses to share, skip-level conversations, upward feedback, and
   what neighboring teams say. Date every item.
3. For each dimension, record the strongest dated evidence and the strongest contrary evidence.
   Every rating cites at least one dated, observable item with its source: an artifact, a metric
   read in context, a skip-level theme, a peer manager, a staff engineer, or the self-assessment.
4. Rate **Not yet**, **Solid**, or **Strong** against the level descriptions. Rate **No evidence**
   when the window holds none; never fill the gap with impression. Two "No evidence" ratings are a
   finding about the director's own signal sources. Rate **Not yet** only against an expectation
   the manager knew before the behavior rated; facts from before the window are context.
5. Read outcomes in context: what the team controls, what it inherited, and what a shared system
   (a release train, another team) decided for it.
6. Agree at most two development goals, each with an observable change and a check date.
7. Calibrate with the other managers' assessments before sharing ratings. Do not add the ratings
   into a composite score or rank managers against each other.

## Template

The rubric:

| Dimension | Not yet | Solid | Strong |
|---|---|---|---|
| **1. Outcomes in context** | Misses are explained by others; commitments renegotiated silently | Team meets most commitments or misses them visibly and early; results read against what the team controls | Team improves its own outcome measures quarter on quarter, including ones the manager inherited |
| **2. Operational ownership** | Incidents recur; actions stay open; the manager or one expert is the fallback | Owned components meet the operational minimums; actions closed; recurrence falling | The team finds its own blind spots (near misses, risky configuration) before an incident does |
| **3. People growth** | No written expectations; growth happens by accident or departure | Each engineer has expectations and a development goal; feedback cites evidence | People take on scope they could not two quarters ago; promotions hold up in calibration; a successor exists |
| **4. Team health** | Knowledge and on-call load concentrated in a few people; regretted attrition unexplained | Load and knowledge spread is measured and improving; one-on-ones held and about more than status | People raise bad news early; the team sustains pace without after-hours rescue |
| **5. Cross-team leverage** | Dependencies escalated to the director; friction with neighbors persists | Agrees interfaces and contracts with neighboring teams; resolves disputes at peer level | Practices or capabilities from this team are adopted by others |
| **6. Running the role** | Writes the hard code; routes tickets; reports only good news upward | Time budget fits the role; technical direction delegated; escalates early with options | Upward reports are trusted because they include bad news first; the team runs well when the manager is away |

One record per manager per window:

```yaml
assessment:
  manager: ""
  team: ""
  window: {start_week: 0, end_week: 0}
  assessor: ""
  self_assessment_received: false
  dimensions:
    - name: outcomes_in_context        # and the other five
      rating: ""                       # not_yet, solid, strong, no_evidence
      evidence:
        - {week: 0, item: "", source: ""}
      contrary_evidence:
        - {week: 0, item: ""}
  development_goals:
    - {dimension: "", observable_change: "", check_week: 0}
  calibrated_with: []
```

## Example: Northstar, Elena Sokolova, Payments and Integrations

!!! info "Northstar so far"
    Weeks 1 to 26 of the Engineering Director's first year at Northstar Technologies, a fictional company.
    Elena Sokolova manages Payments and Integrations and has the organization's best operational
    discipline. The director drafts this assessment in week 24 and finalizes it in week 27. See the
    [timeline](../case-studies/northstar/timeline.md) and the [cast](../case-studies/northstar/cast.md).

Window: weeks 1 to 26 (quarters 1 and 2). Baseline-quarter facts from the
[baseline data](../case-studies/northstar/baseline-data.md) are context, not window evidence.

| Dimension | Rating | Dated evidence | Contrary evidence |
|---|---|---|---|
| 1. Outcomes in context | Strong | Week 19: accounting integration live for the renewal customer with daily reconciliation (director's report); week 6: payments-gateway flag changes move to reviewed, validated merge requests (pipeline record) | The ledger read path is unnamed and ADR-0001, the decision on how integrations read ledger data, is open |
| 2. Operational ownership | Strong | Weekly 30-minute operations review, two years old at baseline and still running at the start of quarter 2 (meeting notes); week 8: a contract test catches a payments-gateway rounding change (pipeline record) | Blind spot: payments-gateway configuration edits never reached the near-miss log (17 entries at baseline), though that file produced two incidents; webhooks arrived in week 4 with signing keys never rotated |
| 3. People growth | Solid | Rotating facilitator in the operations review gives each engineer practice leading it (meeting notes); a senior engineer acts as tech lead (self-assessment) | The acting tech lead holds no title; no promotion case yet |
| 4. Team health | Strong | In the operations review the engineer coming off on-call presents and Elena speaks last, so bad news surfaces from the team (meeting notes); one departure in the 12 months before the window (HR record, context) | No upward feedback collected for her team in the window |
| 5. Cross-team leverage | Strong | Week 16: facilitates Customer Experience's team health check (peer manager); start of quarter 2: Priya Raman (Orders manager) asks to adopt the operations review and near-miss log in Orders (peer manager) | |
| 6. Running the role | Solid | Time split 35 people, 35 delivery, 15 technical (calendar reconstruction, baseline); technical direction delegated to a senior engineer; quarter 2: lowers WIP limits for the integration (team board) | Week 14 onward: Victor Lindqvist (CTO) told her in passing to "read the tables now" on ADR-0001; whether she escalated the conflict is not recorded. Ask |

There is no composite score: the six
ratings are read separately and are not used to rank Elena against the other managers.

**Development goals:**

1. *People growth:* make the acting tech lead's scope explicit and written, and bring a promotion
   case with evidence to the quarter 3 calibration if it holds. Check: week 30.
2. *Operational ownership:* extend the near-miss log to configuration and to webhooks, and report
   the first entries in the operations review. Check: week 32.

## Common mistakes

- **Rating the team's luck.** Payments' dependency incidents (a partner bank outage) say little about
  the manager; what the team did afterwards says a lot.
- **Filling "No evidence" with impression.** It is a legitimate rating and a prompt to look.
- **Rewarding heroics.** A manager who fixes the weekend failure personally scores lower on
  dimension 6, not higher on dimension 2.
- **Skipping contrary evidence.** Strong teams have blind spots; Payments' near-miss log missed the
  file that produced two incidents.
- **Assessing without calibration.** Without it, ratings measure the assessor.

## Review questions

1. Which ratings rest on practices rather than on results, and when will results be visible?
2. What would a skip-level engineer on this team dispute?
3. What would the neighboring teams say about dimension 5?
4. Which "No evidence" ratings reveal a gap in the director's own information?
5. What should this manager stop doing to make room for the two goals?

## Evidence and references

The method is [Chapter 41](../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md).

- [Scullen, Mount, and Goff, 2000](../references/bibliography.md#scullen2000latent): the abstract
  reports that the rater's own tendencies accounted for over half of the variance in managers'
  ratings (**research finding**). That is why every rating cites dated evidence and is calibrated.
- [Hoffman and Tadelis, 2021](../references/bibliography.md#hoffman2021people): at one large high-tech
  firm, the abstract reports that survey-measured people-management skills had a strong negative
  relation to employee turnover (**research finding**), support for rating team health and people
  growth alongside delivery.
- [Google re:Work](../references/bibliography.md#rework-great-managers): Project Oxygen, Google's
  multi-year look at whether managers matter (**industry research**).

The six dimensions, the evidence rules, and the two-goal limit are **this book's recommendation**.
