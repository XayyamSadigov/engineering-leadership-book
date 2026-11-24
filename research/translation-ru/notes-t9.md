# Translation notes, lane t9 (Chapters 29–30)

Source: English working tree. Files:
`docs/parts/06-technical-leadership/29-staff-and-principal-engineers.ru.md`,
`docs/parts/06-technical-leadership/30-technical-strategy-and-technology-selection.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order, link targets, exercise labels, admonition types, Mermaid count, table rows and
table numbers identical; the multiset of numbers in the whole page matches except the H1 anchor and one
word-form number (ch30 F2 "from year 3" → «с третьего года»). Failure Modes use «Как заметить:» /
«Что делать:» where the English has Signal/Countermeasure fields (ch30); ch29's failure modes are
prose ("Detect…") and stay prose. Words (wc -w; no-break spaces glue some tokens): ch29 5 232, ch30 5 355.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| scope (of a staff role); a one-page scope; rescoping | область ответственности; одностраничное описание области ответственности; пересмотр области ответственности | T | ch29; follows ch04.ru («область ответственности») |
| owned decisions | собственные решения; решения, которые принадлежат ему | T | ch29; ch28.ru «решения ей не принадлежали» |
| sponsor; sponsor of last resort | спонсор; спонсор последней инстанции | T | ch29; follows ch04.ru |
| roaming critic / overloaded hero | блуждающий критик / перегруженный герой | T | ch29 |
| critic pattern | паттерн критика | T | ch29 |
| stop list | стоп-лист (glossed in the five-part list as «что прекращается») | T | ch29 |
| unscheduled questions / incident pulls | внеплановые вопросы / выдёргивание на инциденты | T | ch29 |
| mandated program work; program mandate; standards domain | работа по программе в рамках мандата; мандат на программу; область стандартов | T | ch29 |
| shared leadership | распределённое лидерство (shared leadership) | B | ch29 |
| force multiplier | множитель силы (force multiplier) | B | ch29 |
| big-picture thinking / project execution / leveling up others (Reilly) | мышление на уровне общей картины / исполнение проектов / рост других | T | ch29 |
| snacking / preening / chasing ghosts (Larson) | «перекусы» (snacking) / «самолюбование» (preening) / «погоня за призраками» (chasing ghosts) | B | ch29 |
| appeal (disagreement rule) | апелляция; обжаловать | T | ch29 |
| disagreement rule | правило разногласий | T | ch29 |
| shadow manager / title as retention / the scope that is a project / invisible staff engineer | теневой руководитель / должность ради удержания / область ответственности, которая на деле проект / невидимый staff-инженер | T | ch29 failure modes |
| "What it looks like / Why it happens / What changes it" | «Как это выглядит / Почему так происходит / Что помогает» | T | ch29 |
| principal architect (Northstar's former one; X1) | ведущий архитектор (principal architect) | T | ch29; follows baseline-data.ru |
| Staff band midpoint; Senior Engineers (level) | середина вилки уровня Staff; инженеры уровня Senior | T | ch29; notes-t2 level names |
| distinguished engineer | distinguished-инженер | E | ch29, by analogy with principal-инженер |
| kernel (Rumelt) | «ядро» стратегии (kernel) | B | ch30 |
| diagnosis / guiding policy / coherent actions | диагноз / направляющая политика (guiding policy) / согласованные действия (coherent actions) | B | ch30 |
| enforcements / escalations / transitions (Larson) | механизмы соблюдения / эскалации / переходы | T | ch30 |
| total cost of ownership (TCO) | совокупная стоимость владения (total cost of ownership, TCO) | B | ch30; then TCO |
| exit, exit cost, exit path | уход, стоимость ухода, путь ухода | T | ch30; "Replace (exit)" → «Заменить (уход)» |
| differentiation; differentiating / commodity capability | дифференциация; дифференцирующая / типовая возможность | T | ch30 |
| adopt (open source) | взять open source; брать (проект) | T | ch30; «внедрять» kept for adopting technologies |
| lock-in | привязка к вендору | T | ch30 |
| security advisories | рекомендации по безопасности | T | ch30 |
| innovation tokens | «жетоны на инновации» (innovation tokens) | B | ch30 |
| technology radar; rings Adopt / Trial / Assess / Caution | технологический радар; кольца kept English | E for rings | ch30; follows notes-t8 |
| quality / architecture characteristics | характеристики качества / архитектурные характеристики | T | ch30 |
| pillars (Well-Architected) | опоры (pillars) | B | ch30 |
| proof of concept; happy path | проверка концепции (proof of concept); успешный сценарий | B / T | ch30 |
| end-of-life (EOL) | окончание поддержки (end-of-life, EOL) | B | ch30; EOL in tables |
| concentration / skills (risk kinds) | концентрация / навыки | T | ch30 |
| exposure (to events) | подверженность (событиям) | T | ch30; ch26's «уязвимость системы» did not fit here |
| technology risk register | реестр технологических рисков | T | ch30; follows glossary.ru register IDs |
| responses mitigate / transfer / accept / exit | снизить / передать / принять / уйти | T | ch30; term base risk treatment verbs plus «уйти» |
| second responder | второй ответственный | T | ch30 |
| standby (instance) | резервный экземпляр | T | ch30 |
| extended support | расширенная поддержка | T | ch30 |
| Finance's day rate | дневная ставка финансов | T | ch30; follows first-quarter.ru |
| upfront / annual (cost table) | разовые затраты / ежегодные затраты | T | ch30 |
| rate content | данные о ставках; содержимое ставок | T | ch30 |
| vision document / goals as strategy / resume-driven selection / build bias / buy and forget / the scoring game / the orphaned register | документ о видении / цели вместо стратегии / выбор ради резюме / перекос в сторону разработки / купить и забыть / игра в оценки / бесхозный реестр | T | ch30 failure modes |
| converge before adding (policy 1) | «Сначала сократить, потом добавлять» | T | ch30 |
| quotes (vendor) | коммерческие предложения | T | ch30 |

Reused from earlier lanes: решатель (solver), правая рука (right hand), связующая работа (glue work),
динамика заложника, часы консультаций, ранбук (runbook), координатор инцидента (incident commander),
выделение permissions, свободный бюджет на инструменты, компенсирующая мера, спайк (spike), срезанные
углы, выделение на профилактику, полная стоимость сотрудника.

## Doubts and notes on the English (English not changed)

- ch29: "truck factor" is the English term; per the term base ("bus factor" kept) rendered
  «truck factor (он же bus factor)» on first use in each chapter, then "truck factor" as in the source.
- ch29: the long evidence paragraph (Wang; Gren and Ralph; Avelino) split into two in Russian, one topic
  each; no content change.
- ch29 references: "mostly free at staffeng.com" is an access-like note in reader text; translated
  faithfully (same pattern flagged in notes-t1 for Ch 4).
- ch29 example: "a floor for staff engineers" read as "the average cost understates staff cost";
  rendered «Для staff-инженеров это нижняя граница».
- ch29 case: Rafael Duarte "shares core/order-capture review ownership" rendered «вместе с ней отвечает
  за ревью core/order-capture»; if "shares" means shares it with other Orders engineers (not with Ines),
  «отвечает за ревью core/order-capture вместе с другими» would be more exact.
- ch30: "**standard**, vendor guidance" for AWS Well-Architected kept as «**стандарт**, рекомендации
  вендора»; the label looks generous for vendor guidance, but it is the English label.
- ch30: "Opara-Martins … as the abstract reports it" is an access note in prose; translated faithfully
  («в изложении аннотации»).
- ch30 example: "Per day it is higher than the book's planning rate of $3,558 per engineer-week" is
  arithmetic-heavy prose; translated faithfully.
- ch30 F2: "from year 3" rendered «с третьего года» (word form), so the page number check shows one
  missing "3"; not a content change.
