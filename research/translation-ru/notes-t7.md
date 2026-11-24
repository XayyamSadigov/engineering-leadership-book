# Translation notes, lane t7 (Chapters 25–26)

Source: English working tree. Files:
`docs/parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.ru.md`,
`26-security-and-software-supply-chain-quality.ru.md`. Both pass `tools/validate_book.py` (no build run).
Structural check per chapter against the English: heading anchors in order, link targets, exercise labels,
admonition types, Mermaid count, table rows, table numbers and INC ids identical. Failure Modes use
«Как заметить:» / «Что делать:». Words (wc -w): ch25 5 700, ch26 5 958.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| failure mode (incident sense) | вид отказа | T | ch25; follows glossary.ru «Повторный инцидент» |
| operations (role) / operations lead | операции (operations) / руководитель операций | B | ch25; follows glossary.ru «Координатор инцидента» |
| communications (role) / communications lead | коммуникация / ответственный за коммуникацию | T | ch25 |
| planning role; scribe | роль планирования; секретарь (scribe) | B | ch25 |
| declare (an incident); declaration criteria | объявить инцидент; критерии объявления | T | ch25 |
| mitigate | смягчить последствия | T | ch25 |
| fail over | переключиться на резерв | T | ch25 |
| responders | те, кто чинит | T | ch25 |
| customer-facing staff | сотрудники клиентских служб; сотрудники, работающие с клиентами | T | ch25 |
| review triggers | условия обязательного разбора | T | ch25 |
| trigger (of an incident) | триггер; изменение-триггер | T | ch25; matches notes-t5 |
| latent faults | скрытые дефекты | T | ch25 |
| hindsight bias | ретроспективное искажение (hindsight bias) | B | ch25 |
| second story | «вторая история» | T | ch25 |
| follow-through | доведение действий до конца; доведение | T | ch25 |
| interim control | временная мера | T | ch25; first-quarter.ru has «временное правило» for the specific rule |
| action triage / action backlog | разбор накопившихся действий | T | ch25 |
| "won't do" (closure) | «не будем делать» | T | ch25 |
| restoration time | время восстановления | T | ch25 |
| customer-detected (column) | обнаружено клиентами | T | ch25 |
| high-potential near miss | почти-инцидент (near miss) с высоким потенциалом ущерба | B | ch25; near miss from notes-t2 |
| neutral facilitator | нейтральный ведущий | T | ch25; facilitator = ведущий (notes-t2) |
| commander rotation | график координаторов | T | ch25 |
| on-call leads | старшие по дежурствам | T | ch25 |
| mean time to repair (MTTR) | среднее время восстановления (mean time to repair, MTTR) | B | ch25 |
| Orthogonal Defect Classification | ортогональная классификация дефектов (Orthogonal Defect Classification) | B | ch25 |
| configuration guards / migration safety / contract checks | защита конфигурации / безопасность миграций / проверки контрактов | T | ch25 table |
| severity drift / hero response / ceremonial review / blame by other means / root cause tunnel vision / action-item inflation | дрейф серьёзности / ставка на героев / ритуальный разбор / обвинение другими средствами / туннельное зрение на первопричине / инфляция действий | T | ch25 failure modes |
| disclosure question (CTO) | вопрос раскрытия информации | T | ch25 |
| quality attribute | атрибут качества | T | ch26 |
| exposure (security) | уязвимость системы; «насколько угрожает» | T | ch26; «уязвимость системы» where a noun is needed, to keep it apart from a single vulnerability |
| earmark (capacity) | целевая доля ресурса; выделить целевым образом | T | ch26 |
| provenance | происхождение (provenance); сведения о происхождении | B | ch26 |
| gap analysis; Current / Target Profile | анализ разрывов; текущий профиль (Current Profile) / целевой профиль (Target Profile) | B | ch26; follows glossary.ru |
| CSF functions (Govern, Identify…) | kept in English with a Russian gloss once; English in the table | E | ch26; follows glossary.ru |
| SSDF practice groups | English with Russian gloss once in prose; Russian in the table | B | ch26; Russian wording from glossary.ru |
| checklist theater | театр чек-листов | T | ch26; by analogy with «театр соответствия» (notes-t4) |
| hosted build platform; hardened platform | размещённая сборочная платформа; защищённая платформа | T | ch26 |
| two-party review | изменение проверяют два человека | T | ch26 |
| base score (CVSS) | базовая оценка | T | ch26 |
| reachability; reachable | достижимость; достижимый | T | ch26 |
| findings | находки | T | ch26 |
| disclosure (of a vulnerability); disclosure program | раскрытие; программа раскрытия уязвимостей | T | ch26 |
| bug bounty | bug bounty | E | ch26 |
| penetration test | пентест | T | ch26; follows baseline-data.ru |
| secrets manager; rotation; rotate | менеджер секретов; ротация; ротировать | T | ch26 |
| credentials | учётные данные | T | ch26; follows baseline-data.ru |
| trust boundary | граница доверия | T | ch26 |
| threat modeling | моделирование угроз | T | ch26; follows baseline-data.ru |
| security control | механизм защиты; мера защиты | T | ch26 |
| security champions | чемпионы по безопасности (security champions) | B | ch26 |
| application security (AppSec) | безопасность приложений (AppSec) | B | ch26 |
| security function / central team | служба безопасности / центральная команда | T | ch26 |
| residual risk | остаточный риск | T | ch26 |
| questionnaire (customer security) | опросник | T | ch26 |
| assurance | гарантии | T | ch26 |
| "not affected" (decision) | «не затронуты» | T | ch26; one reflection question reads «нас не затрагивает» for syntax |
| checklist theater / scanner graveyard / severity laundering / champions without time / orphaned control / heroic upgrade | театр чек-листов / кладбище находок сканера / отмывание серьёзности / чемпионы без времени / бесхозный механизм защиты / героическое обновление | T | ch26 failure modes |
| vanity counts | показатели напоказ | T | ch26; matches «SLO напоказ» (notes-t6) |
| discretionary tooling budget | свободный бюджет на инструменты | T | ch26 |

Reused from earlier lanes: компенсирующая мера, исключение, кредит-ноты, исправление вперёд, раскатка,
тенант, пачка, справедливая культура (just culture), почти-инцидент, ведущий, подтверждения (attestations).

## Doubts and notes on the English (English not changed)

- Ch 25, Severity section: "four consecutive incidents were rated Sev3 … until the director re-rated it"
  — "it" is singular after four incidents. Rendered «пока директор не переоценил их».
- Ch 25, Failure Modes: "Severity drift" has no "Signal:" field, only "Countermeasure:"; the Russian
  follows the English.
- Ch 25, "contested" is not bold in the English ("and the evidence is contested"); rendered «и вопрос
  спорный», not bold.
- Ch 25, the table row "Sev1, or wrong financial data…" makes the number checker flag `1,` vs `1`; a false
  positive (comma after "Sev1").
- Ch 26, References: "the statement that the Core is not a checklist". "Core" here is the CSF Core, which
  a reader of this book will take for Northstar's monolith. Added the gloss «(ядро CSF)»; the English may
  want "the CSF Core".
- Ch 26, Case: "with time to migrate it off scripts" — "it" refers to webhooks; rendered «их».
- Ch 26, A1: "The Billing team of Marcus Oyelaran (Billing manager)" repeats "Billing"; rendered
  «Команде Billing, которой руководит Marcus Oyelaran».
- Ch 26 tables: "8 of 24" style cells rendered «8 из 24» (numbers verbatim, word translated, as earlier
  lanes did with words in number cells). "1.8 FTE" kept with a decimal point inside the table.
