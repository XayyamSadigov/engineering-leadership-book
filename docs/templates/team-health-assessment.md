# Team health assessment

**Used in:** Chapter 14 (distributed teams, team health, and diagnosing dysfunction), Chapter 11 (trust,
psychological safety, and accountability), Chapter 41 (facilitating a health check as a trial
assignment for a future manager).
**Owner:** the team owns the results; a facilitator from outside the team's reporting line runs the
session; the manager convenes it and owns the response to the team's requests.
**Cadence:** once a quarter, about two hours, with each team's trend read against its own previous
sessions; more often only while a team is in the middle of a structural change.

A team health assessment is a structured way for a team to say how its working life is going, and to
agree what to do about it. Its value is the discussion more than the ratings, and its candor depends on
what happens to the answers. Used to help the team, it stays honest; used to judge or rank teams, it
drifts toward green
([Chapter 14](../parts/03-high-performing-teams/14-distributed-teams-team-health-and-dysfunction.md)).

This template is a facilitated workshop of the kind Spotify's squad health check describes: the team
rates about ten areas green, yellow, or red with a trend, and discusses why. Its authors warn that the
model works only where trust is high, because self-reported data is easy to game; that teams should not
be compared; and that it is a support tool, not a judgment tool
([Kniberg and Lindwall, 2014](../references/bibliography.md#kniberg2014squad)). That is **documented
practice** at one company, with no outcome data. Survey scores tied to performance reviews lose their
value, as Orosz and Beck describe at one large company
([Orosz and Beck, 2023](../references/bibliography.md#orosz2023measuring)), **expert opinion**. Where a
validated instrument is needed, for research or for a formal diagnosis of how a team is structured,
supported, and led, the Team Diagnostic Survey was developed and tested for that
([Wageman, Hackman, and Lehman, 2005](../references/bibliography.md#wageman2005team)). The access rule,
the pairing with system signals, and the two-action limit are **this book's recommendation**.

This is not the developer-experience survey of
[Chapter 18](../parts/04-execution/18-measuring-engineering-productivity.md), which measures friction
across the organization anonymously. It is a conversation inside one team.

## How to fill it in

1. **Write the access rule before the first session** and read it out at the start: the team owns the
   results and decides what leaves the room; by default only patterns and requests do. Ratings leave the
   room only by the team's explicit agreement, for a stated purpose, once.
2. **Choose a facilitator outside the reporting line,** often a manager of another team or a staff
   engineer. The manager does not attend the rating discussion unless the team asks.
3. **Split the session if one subgroup is quieter,** for example by site or specialty. Two honest
   sessions beat one session where half the room is on video and silent.
4. **Rate each area green, yellow, or red, with a trend** (better, same, worse) against the last
   session. A first session has no trend; say so instead of guessing.
5. **For each yellow or red, write why, in the team's words.** The reason is the data; the color is an
   index to it.
6. **Pair each red or yellow area with a system signal** the team or facilitator can check: release
   pain with deployment data, support with incident load, process with retrospective actions. Where the
   signal disagrees with the rating, discuss the disagreement.
7. **End with at most two actions the team owns,** each with an owner and a date, and at most one
   request for help from the manager or director. An assessment without follow-up teaches silence.
8. **Send upward only what the access rule allows:** patterns ("release pain"), requests, and actions.
   No scores, no league tables, and nothing in anyone's objectives or performance review.
9. **Open the next session with last time's actions and request:** done, not done, and why.
10. **Read results by layer** if a pattern points to dysfunction: structure first, then leadership,
    relationships, and individuals, as Chapter 14 sets out.

## Template

**Areas (adapt to your teams; keep about ten).** Each area is written as the healthy statement the team
rates itself against. The list follows the squad health check's well-known areas; the wording here is
this book's.

| Area | Healthy statement |
|---|---|
| Easy to release | We release when we choose, with little risk or ceremony |
| Suitable process | Our way of working fits our work |
| Technical quality | Our code and systems are in a state we are glad to work in |
| Value | We deliver things that matter to customers or the business |
| Speed | We get things done quickly, without long waits on others |
| Mission | We know why we are here and agree with it |
| Fun | We enjoy working together |
| Learning | We learn something new most weeks |
| Support | We get help when we ask for it |
| Pawns or players | We decide what to build and how; decisions are made where we can hear them |

**The session record.**

| Field | Meaning |
|---|---|
| Team, session, date | Which team; which subgroup if split; date |
| Facilitator | Name and role; confirm outside the reporting line |
| Access rule | As written before the session, and any exception the team agreed |
| Ratings | Per area: green / yellow / red; trend better / same / worse / first session |
| Why (team's words) | For every yellow and red |
| Paired system signal | The measure or record checked against each yellow and red |
| Actions (at most two) | Owned by the team: owner and date |
| Request for help (at most one) | To the manager or director, in the team's words |
| What leaves the room | Exactly what is sent upward |
| Last session's follow-up | Each action and request: done, not done, why |

```yaml
session:
  team: ""
  subgroup: ""            # blank if the whole team
  date: ""
  facilitator: {name: "", role: "", outside_reporting_line: true}
  access_rule: "The team owns the results; only patterns, requests, and actions leave the room."
  exception_agreed: ""    # blank, or what the team agreed to share, with whom, and why
areas:
  - name: easy_to_release   # and the other nine
    rating: ""              # green / yellow / red
    trend: ""               # better / same / worse / first_session
    why: ""
    paired_signal: ""
actions:                    # at most two
  - {item: "", owner: "", due: ""}
request_for_help: {to: "", request: ""}
leaves_the_room: []
previous_followup:
  - {item: "", result: "", why: ""}
```

## Example: Northstar, Customer Experience mobile session (week 16)

**Fictional.** The session, its ratings, the request, and the system signals come from the
[baseline data](../case-studies/northstar/baseline-data.md), the
[first quarter](../case-studies/northstar/first-quarter.md) page, and Chapter 14's case study. The
layout and the pairing of each area with a signal are illustrative and written for this template. The
director's response is left open, as in Chapter 14.

**Context.** Customer Experience has 15 engineers under Daniel Cho: nine web (seven in Minneapolis, two
remote) and six mobile, all in Bogotá, plus two quality engineers in Minneapolis since the week 10
announcement. One board and one two-week sprint cover web and mobile. In week 16 the director asked
Elena Sokolova, whose team also spans both sites, to facilitate. She ran two sessions: web with the
quality engineers, and mobile. Normally only patterns and requests leave the room; because a structural
decision depended on the results, both groups agreed to show their ratings to Daniel and the director
this once. No earlier session is recorded, so there is no trend.

| Field | Mobile session |
|---|---|
| Facilitator | Elena Sokolova, manager of Payments and Integrations; outside the reporting line |
| Access rule and exception | Patterns and requests only, by default; ratings shared once with Daniel Cho and the director, agreed by the group, because a structural decision depended on them |
| Green | Learning, fun |
| Yellow | Four areas; the record does not itemize them |
| Red | Easy to release, suitable process, support, pawns or players |
| Trend | First session |
| Request for help | "Our own board, and decisions that happen where we can hear them" (Mateo Arango Ríos, for the group) |
| Web session, for comparison within the team | 5 green, 4 yellow, 1 red (speed, which web tied to waiting on Orders) |

**Paired system signals for mobile's red areas.**

| Red area | System signal on record | Agrees? |
|---|---|---|
| Easy to release | Mobile releases pass app-store review, yet share web's two-week sprint; INC-426's fix waited for that review and restoration took 1,310 minutes | Yes |
| Suitable process | One board and one sprint for two products with different release mechanics; 6 of the last 8 retrospective actions concerned web work | Yes |
| Support | About half of Daniel's video one-on-ones with mobile engineers were rescheduled in the baseline quarter | Yes |
| Pawns or players | Retrospectives run with Minneapolis in one room and Bogotá on video; Mateo Arango Ríos had done lead work for over a year without recognition | Yes |

What to notice: on delivery measures the team looked healthy (26 deploys a month, the most of any team;
28 percent unplanned work against an organization average of 34), and the health check found what those
measures could not. Splitting the session by subgroup is what surfaced it: in one joint session the
web majority's mostly green picture would have averaged mobile away. Every red has a system signal that
agrees with it, which is why Chapter 14's diagnosis starts at the structure layer (two products, one
board, and a site boundary on top of a specialty boundary) rather than at Daniel or the mobile
engineers. The one-time disclosure was a deliberate exception with a stated purpose. Repeated as a
habit, it would turn the next session into a performance.

## Common mistakes

- **The league table.** Results compiled across teams as traffic lights in a monthly review. Within two
  quarters everyone reports green. Report patterns and requests, never scores.
- **The manager in the room.** People rate the boss's presence, not their working life. Use a
  facilitator outside the reporting line.
- **One session for a split team.** The quieter subgroup's view averages away; split by site or
  specialty when one group is quieter.
- **Ratings without reasons.** A red with no "why" cannot be acted on.
- **Ten actions.** Two owned actions and one request are a commitment; ten are a wish list.
- **No follow-up.** If last quarter's request is not answered at the start of the next session, the
  team learns to stop asking.
- **Coaching a structural problem.** When reds cluster on release, process, and decisions for one
  subgroup, check the team's design before its relationships.

## Review questions

1. What happened, visibly, to the last request this team made in a health check?
2. Which red or yellow area has no system signal checked against it?
3. Is there a subgroup that was quieter in the session than it is in one-on-ones?
4. Who outside the team has seen these ratings, and did the team agree to that for a stated purpose?
5. If the paired signal disagrees with the rating, which one are you inclined to believe, and why?
