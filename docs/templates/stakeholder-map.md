# Stakeholder map

!!! warning "Awaiting human review"
    This template has passed the book's automated validation and an editorial self-review, but not yet
    the human review in which each cited claim is checked against its source. Treat it as a reviewed
    draft. Corrections are welcome; see the repository's CONTRIBUTING file.

**Used in:** Chapter 42 (cross-functional dependencies, portfolio, and influence), Chapter 46
(stakeholder management and negotiation).
**Owner:** the leader driving the decision; it is a private working document, not a circulated one.
**Cadence:** one map per contested decision, built before the proposal is final; every stance is
re-checked before the decision meeting, and any entry older than a quarter is treated as unknown.

A stakeholder map is drawn for one decision, not for a person. The same CFO is a player on a budget
question and a context setter on a severity definition, so a map that tries to describe people in
general describes nobody usefully. For each person whose support or resistance changes the outcome,
it records their power and interest in this decision, what they want and what they want to avoid,
where they stand and on what evidence, what they will do if there is no agreement, and how you will
engage them.

The two-by-two of power against interest, with its four groups (players, subjects, context setters,
and crowd), follows Eden and Ackermann, who also warn that what a team writes about stakeholders is
a set of informed guesses, not facts ([Eden and Ackermann, 2021](../references/bibliography.md#eden2021modelling)).
Working on interests rather than stated demands is the advice principled negotiation is known for
([Fisher and Ury, 1981](../references/bibliography.md#fisher1981getting)). Both are **expert
opinion**. How to influence each person once mapped is Chapter 42's subject.

Keep the map private. "Skeptic" next to a colleague's name is preparation; circulated, it becomes a
grievance. What you share is the decision document the map helped you write.

## How to fill it in

1. **Write the decision in one sentence, with its date and decider.** If you cannot, you are not
   ready to map. Start a new map when the decision changes.
2. **List everyone who can decide, approve, block, or is materially affected,** including people
   with no formal role who could block in practice. Leave everyone else off.
3. **Place each person on power and interest for this decision.** High power, high interest:
   *players*, consulted one-to-one before the proposal is final. High interest, low power: *subjects*,
   involved in shaping options; they may form coalitions. High power, low interest: *context setters*,
   given a short briefing on the one point that touches them and asked what would make them object.
   Low on both: *crowd*, informed through normal channels.
4. **Write the interest, including what they want to avoid.** Avoidance goals (no surprise slip, no
   hidden headcount, no loss of standing) often decide a stance more than goals do. Mark each as a
   guess until you have checked it in conversation.
5. **Record stance with evidence and a date.** Champion, supporter, neutral, skeptic, opponent, or
   unknown, followed by what they said or did and when you last checked. A stance without evidence is
   a presumption; write "unknown".
6. **Write their alternative if there is no agreement.** What they will do if your proposal fails:
   escalate, wait, build their own. It tells you how much they need you.
7. **Record what they need from you and the stance you need by the decision date,** which is often
   neutral rather than champion.
8. **Plan engagement:** channel, cadence, and who owns the relationship. Nobody affected should hear
   the proposal first in a group.
9. **After the decision, record which guesses were wrong.**

## Template

**Decision this map is for (one sentence):** ________________________________

| Field | Meaning |
|---|---|
| Stakeholder | Name |
| Role | Job, and role in this decision (decides / approves / consulted / affected / can block) |
| Position for this decision | Player / subject / context setter / crowd, from power and interest |
| Power | High / medium / low, over this outcome |
| Interest | What they want from this decision, and what they want to avoid (a guess until checked) |
| Stance, evidence, last checked | Champion / supporter / neutral / skeptic / opponent / unknown; what they said or did; date |
| Alternative if no agreement | What they will do if this fails |
| What they need from us | Within our authority, serving their interest |
| Stance needed by decision date | Usually the least support that lets the decision hold |
| Engagement plan | Channel, cadence, relationship owner |

```yaml
map:
  decision: ""               # one sentence
  decision_date: ""
  decider: ""
  owner: ""
  last_revised: ""
stakeholders:
  - name: ""
    role: ""
    role_in_decision: ""     # decides / approves / consulted / affected / can block
    position: ""             # player / subject / context setter / crowd
    power: ""                # high / medium / low
    interest:
      wants: ""
      avoids: ""
      checked: false
    stance:
      value: ""              # champion / supporter / neutral / skeptic / opponent / unknown
      evidence: ""
      last_checked: ""
    alternative_if_no_agreement: ""
    needs_from_us: ""
    stance_needed: ""
    engagement: {channel: "", cadence: "", owner: ""}
after_decision:
  wrong_guesses: []
  what_worked: []
```

## Example: Northstar, year-2 organization proposal (quarter 4)

**Fictional.** The decision, its dates, the proposal's contents, and each executive's stated wants
come from the [Northstar overview](../case-studies/northstar/index.md) and the
[first quarter](../case-studies/northstar/first-quarter.md) page. Every placement, interest, stance,
alternative, and engagement plan is an illustrative assessment written for this template, not canon;
the canon leaves the CTO's decision open.

**Decision this map is for:** whether Victor Lindqvist approves, in week 46, the year-2 organization
proposal drafted in week 44 (Customer Experience split into Web and Mobile with Mateo Arango Ríos as
Mobile's manager, his seat not backfilled; core/permissions to Orders; search-svc to Data and
Analytics; Platform Operations renamed Developer Platform; about 21 engineer-weeks of transition
cost), for announcement in week 51 and effect in week 53.

| Stakeholder | Position | Interest: wants / avoids | Stance, evidence, checked | Alternative if no agreement | Stance needed | Engagement |
|---|---|---|---|---|---|---|
| Victor Lindqvist, CTO (decides) | Player | A structure he can defend / asking the board for headcount | Unknown; no comment on the draft yet; week 44 | Chooses option B (keep Customer Experience whole) | Supporter | One-to-one with the four priced options; director |
| Daniel Cho, Customer Experience | Subject | A coherent team and standing / losing face over the split | Unknown; not yet told; week 44 | Opposes in the leadership meeting, or quietly disengages | Neutral | Private briefing before week 46; director |
| Mateo Arango Ríos, mobile lead | Subject | Recognition for lead work done over a year / a title without support | Supporter; raised it himself in week 17; week 44 | Waits, or leaves for a lead role elsewhere | Supporter | One-to-one plus a development plan; director |
| Priya Raman, Orders | Subject | core/permissions on her terms / overload after bulk ordering | Supporter; set "after week 26" as her condition; week 44 | Accepts under protest | Supporter | Handoff date in writing; director |
| Farah Haddad, Data and Analytics | Subject | A settled search-svc question / new load without capacity | Unknown; week 44 | Asks to defer the handoff | Neutral | Handoff plan with on-call readiness; director |
| Amara Okafor, CPO | Context setter | Committed dates kept / surprise slips from transition work | Unknown; week 44 | Asks Victor to delay the change | Neutral | Short briefing on the 21 engineer-weeks in the quarter 5 plan; director |
| Rajiv Menon, CFO | Context setter | Flat operating expense / hidden headcount growth | Unknown; week 44 | Questions the manager count in budget review | Neutral | One-page totals: 79 engineers, 7 managers, the director; director |
| Sofia Alvarez, VP Customer Success | Crowd | Fewer escalations / mobile incidents with no owner | Unknown; week 44 | None | Informed | Announcement plus Mobile's on-call rotation; Daniel Cho |

What to notice: the people most affected (Daniel Cho, Mateo Arango Ríos) are subjects with little
power, and the two context setters can still stop the change late if their one concern is not met
early. Every stance but two is "unknown" in week 44; the map's first job is to show where the
director has not yet talked to anyone. Contacts are ordered by who would be hurt most by hearing it
last, not by rank.

## Common mistakes

- **A map per person instead of per decision.** Power and interest change with the issue; a general
  map misplaces people on most decisions.
- **The stale map.** Stances from two quarters ago, still treated as current. Date every stance.
- **A misplaced context setter.** Someone high in power and low in interest is left as crowd, then
  appears late with a veto. Ask them early what would make them object.
- **Presumptions treated as facts.** Interests and stances are informed guesses until checked.
- **Stance needed set to "champion" for everyone.** Most decisions need a few supporters and no
  active opponent.
- **Circulating the map.** It damages the relationships it was meant to manage.

## Review questions

1. Who could block this decision without any formal role in it, and where are they on the map?
2. Which stance has no evidence, or evidence older than a quarter?
3. For each player, what do they want to avoid, and does the proposal trigger it?
4. Who will hear about this proposal first from someone other than you?
