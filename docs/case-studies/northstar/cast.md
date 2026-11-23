# Cast

!!! warning "Fictional"
    Every person on this page is invented for the book. See the note on the
    [Northstar overview](index.md).

This page lists every named person in the two fictional companies, grouped by where they sit. The
chapters column gives the chapters where the person matters most. Many people appear in more
chapters than are listed. For what happened when, see the [timeline](timeline.md).

You, the reader, are Northstar's Engineering Director. You report to Victor Lindqvist (CTO). Weeks
are counted from your first day.

!!! tip "The people who drive the story"
    - **Victor Lindqvist**, CTO and your manager; he decides the year-2 questions.
    - **Amara Okafor** (CPO), **Rajiv Menon** (CFO), and **Greg Tanaka** (VP Sales), the executives
      whose demands compete for engineering time.
    - **The six engineering managers**, who report to you: Priya Raman (Orders), Marcus Oyelaran
      (Billing), Elena Sokolova (Payments and Integrations), Daniel Cho (Customer Experience), Farah
      Haddad (Data and Analytics), and Tom Becker (Platform Operations).
    - **The three staff engineers**, who also report to you: Ines Carvalho (Core domain), Kwame Mensah
      (infrastructure and reliability), and Li Na Zhou (data and integration).

    Everyone else on this page matters in only a few chapters. Look them up when you meet them; you
    do not need to remember them in advance.

## Northstar Technologies

All executives, the director, the six engineering managers, and the three staff engineers work at
headquarters in Minneapolis. Engineers work in Minneapolis, in Bogotá, or remotely in the US (see
[locations](baseline-data.md#locations-and-working-arrangements)).

### Executives

| Name | Role | What they want, and what they do in the story | Chapters |
|---|---|---|---|
| Helena Marsh | Chief Executive Officer (CEO); board member | Renewals from the two largest customers; an end to outage calls. Presents the year-2 operating plan to the board in week 50 | 18, 46, 49, 51, 55 |
| Victor Lindqvist | Chief Technology Officer (CTO); the director's manager | A reliable platform without asking the board for headcount. One direct report, the director. Decides the year-2 organization and the other quarter 4 questions | 39, 46, 47, 50–55, 60; appears throughout |
| Amara Okafor | Chief Product Officer (CPO) | The roadmap she committed to customers, on the dates she gave. Leads three product managers | 15, 17, 38, 42, 44, 46, 49 |
| Rajiv Menon | Chief Financial Officer (CFO) | Flat operating expense; service credits to stop. Corporate IT reports to him | 18, 45, 48, 49, 52, 53 |
| Sofia Alvarez | VP Customer Success | Fewer escalations; honest status during incidents. Helped write the severity definitions | 25, 42, 44, 49, 54 |
| Greg Tanaka | VP Sales | Two features promised in open deals; later a third deal feature | 15, 17, 42, 44, 48, 49, 51 |

### Product management

| Name | Role | Team | Chapters |
|---|---|---|---|
| Keiko Ashworth | Product manager for the ordering area (Orders and Customer Experience's ordering screens); Minneapolis | Amara Okafor's group | 44 |

Amara Okafor's other two product managers, who cover billing and payments and data and customer
reporting, are not named.

### Engineering managers

Each reports to the director.

| Name | Team | Notes | Chapters |
|---|---|---|---|
| Priya Raman | Orders (14 engineers; 16 reports from week 10) | Seven years at Northstar; promoted from inside Orders eight months before the director arrived; still writes code | 2, 11, 13, 21, 33, 41 |
| Marcus Oyelaran | Billing (13 engineers) | Highest incident count; three people carry most on-call pages | 3, 6, 10, 25, 41 |
| Elena Sokolova | Payments and Integrations (12 engineers) | Best operational discipline in the organization; the team holds a weekly operations review | 11, 14, 16, 41 |
| Daniel Cho | Customer Experience (15 engineers; 17 reports from week 10) | Nine web and six mobile engineers under one manager. Leads the proposed Web team in the year-2 proposal | 5, 14, 35, 36, 41 |
| Farah Haddad | Data and Analytics (11 engineers) | Acts as the team's data architect; runs the warehouse inventory in week 41 | 8, 12, 41, 54 |
| Tom Becker | Platform Operations (12: five infrastructure and seven QA engineers) | Leads the proposed Developer Platform in the year-2 proposal | 9, 32, 41 |

### Staff engineers

Each reports to the director. None owned a component at baseline.

| Name | Area | Notes | Chapters |
|---|---|---|---|
| Ines Carvalho | Core domain | Eleven years at Northstar. Owns the Core code standard; leads the permissions extraction | 3, 10, 21, 29, 31 |
| Kwame Mensah | Infrastructure and reliability | Owns the operational minimums and pipelines standards; leads the release working group | 20, 23, 24, 25, 32 |
| Li Na Zhou | Data and integration | Owns the data, migration, and configuration standards; opened ADR-0001 in week 14 | 16, 20, 25, 28, 29 |

### Engineers

| Name | Role | Team, location | Notes | Chapters |
|---|---|---|---|---|
| Aisha Bello | Senior Engineer | Orders | Leads bulk-ordering implementation from week 2 | 2, 11, 41 |
| Rafael Duarte | Senior Engineer | Orders | Applied for the Orders manager role and lost to Priya Raman; asks about management or the staff track | 2, 4, 31 |
| Hannah Lindgren | Informal web lead (no title) | Customer Experience, Minneapolis | | 5, 14, 36 |
| Mateo Arango Ríos | Informal mobile lead (no title) | Customer Experience, Bogotá | Lead work for over a year without recognition; proposed manager of Mobile in the year-2 proposal | 5, 14, 35, 36, 40 |
| Teodora Vasquez-Lund | Senior Engineer, ledger expert | Billing | | 6, 36, 41 |
| Tomasz Wierzbicki | Engineer, ledger expert | Billing | Reports an outside offer 20 percent above base in week 20 | 10, 48 |
| Tamsin Achterberg | The ledger backfill | Billing | Joined about 24 weeks before the director; can respond alone only on credit notes | 7, 48 |
| Sunil Varghese | Senior Engineer | Data and Analytics, US | Designed the warehouse pipelines | 8, 36 |
| Yusuf Demir | Engineer | Data and Analytics, Minneapolis | | 8, 48 |
| Bram Verhoeven | Senior infrastructure engineer | Platform Operations | Six years at Northstar; built Core's Jenkins pipeline | 9, 32 |

People who matter but are not named:

- the third Billing ledger engineer (Engineer level);
- the ledger engineer who left before the director arrived;
- Payments and Integrations' informal tech lead;
- a senior data engineer hired from outside five months before arrival;
- the Platform Operations infrastructure engineer who understands the shell-script deploys;
- the seven QA engineers, who become quality engineers in product teams from week 10.

### Corporate IT and security

| Name | Role | Chapters |
|---|---|---|
| Marta Kowalczyk | Head of IT: corporate IT and internal business systems, 14 people; reports to Rajiv Menon (CFO) | 50, 53 |
| Joon Park | IT security lead; his two-person security function sits inside IT, outside engineering. Northstar has no CISO | 26, 50, 53, 54 |

### Board of directors

| Name | Seat | Chapters |
|---|---|---|
| Anders Holm | Co-founder, non-executive chair | 55, 60 |
| Helena Marsh | CEO | 55 |
| Natalie Brooks | Calder Ridge Partners (growth-equity minority investor) | 55, 60 |
| Samuel Osei | Calder Ridge Partners | 55, 60 |
| Margaret Lin | Independent; former CFO; chairs the audit committee | 53, 55, 60 |
| David Ferrante | Independent; former technology executive at a payments company | 55, 60 |

## Halvard Systems

Halvard's CTO is not named. See [Halvard Systems](halvard.md) for the company.

!!! note "Similar names"
    Two names echo Northstar's: Owen Achterberg (Halvard) is not Tamsin Achterberg (Northstar), and
    Mateo Rinaldi (Halvard) is not Mateo Arango Ríos (Northstar).

### Commerce

| Name | Role | Chapters |
|---|---|---|
| Nadia Brennan | VP, Commerce (130 engineers) | 47, 57 |
| Owen Achterberg | Director, Checkout | 47 |
| Selin Kaya | Director, Catalog and Search | 47 |
| Joaquín Ferreyra | Director, Merchant Tools | 47 |
| Ingrid Solberg | Staff engineer in Checkout; incident commander during the outage | 57 |

### Payroll

| Name | Role | Chapters |
|---|---|---|
| Ngozi Adeyemi | VP, Payroll; hired from outside | 56 |
| Hiroshi Takeda | Principal engineer, Payroll | 56 |
| Rhys Gallagher | Director, Pay Calculation | 56 |
| Beatriz Quintero | Director, Time and Attendance | 56 |

### Field Operations

| Name | Role | Chapters |
|---|---|---|
| Imani Okonkwo | VP, Field Operations | 58 |
| Leah Marchetti | HR business partner, Field Operations | 58 |
| Mateo Rinaldi | Director, Dispatch | 58 |
| Ruth Halloran | Director, Mobile Workforce | 58 |
| Tobias Engel | Director, Classic Scheduler | 58 |

### Insights

| Name | Role | Chapters |
|---|---|---|
| Henrik Sørlie | VP, Insights | 58 |
| Esther Castellanos | Director, Reporting | 58 |
| Kenji Iwasaki | Director, Forecasting | 58 |
| Dalia Ferraz | Founder and CTO of Corvane (acquired); then director of Streaming, Insights' third unit | 58 |

### Platform organization

| Name | Role | Chapters |
|---|---|---|
| Gwen Abernathy | VP of Platform | 59 |
| Arjun Mehta | Principal engineer; owns the tier 1 minimums and auditable pipeline policies | 59 |

### Company-wide

| Name | Role | Chapters |
|---|---|---|
| Mireille Dubois | Head of communications | 57 |
