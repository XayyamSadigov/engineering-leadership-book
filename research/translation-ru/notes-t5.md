# Translation notes, lane t5 (Chapters 21–22)

Source: English working tree. Files: `docs/parts/05-engineering-quality/21-technical-debt.ru.md`,
`22-testing-strategy-and-test-architecture.ru.md`. Both pass `tools/validate_book.py` (no build run).
Structural check per chapter: heading anchors in order, link targets, exercise labels, Mermaid count,
admonition types and every number in tables identical to the English page. Failure Modes use
«Как заметить:» / «Что делать:».

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| time interest / risk interest | проценты временем / проценты риском | T | ch21 |
| option cost | цена упущенной возможности (option cost) | B | ch21 |
| register entry | запись (реестра); пункт | T | ch21 |
| ratio (interest over principal) | отношение (годовых процентов к основному долгу) | T | ch21 |
| trigger (debt) | триггер | T | ch21 |
| remove / reduce / contain / accept | устранить / сократить / локализовать / принять | T | ch21 |
| dormant debt | спящий долг | T | ch21 |
| shortcut (taken) | срезанный угол; срезать угол | T | ch21 |
| default; retire / retirement | дефолт; вывести из эксплуатации / вывод из эксплуатации | T | ch21 |
| reckless / prudent, deliberate / inadvertent (Fowler) | безрассудный / благоразумный, намеренный / непреднамеренный | T | ch21 |
| experience report (OOPSLA) | отчёт об опыте | T | ch21 |
| systematic mapping | систематическое картирование (systematic mapping) | B | ch21 |
| standing share / standing capacity | постоянная доля / постоянный ресурс | T | ch21 |
| borrowing (from the share), payback date | заём из доли, дата возврата | T | ch21 |
| spurious failures | ложные падения | T | ch21, ch22 |
| the debt wiki / principal-first ranking / the rewrite pitch / allocation leakage / debt as a blame word / interest inflation | вики долга / ранжирование по основному долгу / предложение всё переписать / утечка доли / долг как обвинение / инфляция процентов | T | ch21 failure-mode names |
| slice (of a large entry) | срез | T | ch21 |
| test portfolio | портфель тестов | T | ch22 |
| escape profile | профиль пропусков | T | ch22 |
| test size / scope | размер / охват (scope) | B for scope | ch22 |
| hermetic / hermeticity | герметичный / герметичность | T | ch22 |
| testing trophy / testing honeycomb | кубок тестирования (testing trophy) / соты тестирования (testing honeycomb) | B | ch22 |
| ice cream cone / hourglass | «рожок мороженого» / «песочные часы» | T | ch22 |
| consumer-driven contracts | контракты, задаваемые потребителем (consumer-driven contracts) | B | ch22, per term base note |
| expectations (contract) | ожидания | T | ch22 |
| gate; merge gate; release path | контрольная точка; проверка перед слиянием; путь релиза | T | ch22 |
| quarantine; fix-or-delete deadline | карантин; срок «исправить или удалить» | T | ch21, ch22; follows `first-quarter.ru.md` |
| retries; retried pass | перезапуски; прохождение после перезапуска | T | ch22 |
| non-change failure | падение, не связанное с изменением | T | ch21, ch22 |
| flakiness budget; new-test admission check | бюджет нестабильности; проверка допуска новых тестов | T | ch22 |
| line coverage; mutation testing; surviving mutant; mutation score | покрытие строк; мутационное тестирование; выживший мутант; показатель мутационного тестирования | T | ch22 |
| exploratory testing; exploration charter | исследовательское тестирование; исследовательский сценарий (charter) | B for charter | ch22; «исследовательские сценарии» follows `first-quarter.ru.md` |
| migration rehearsal; ordering checks | репетиция миграции; проверки порядка | T | ch21, ch22 |
| expand-and-contract | расширение и сужение (expand-and-contract) | B | ch22; follows ch23.ru |
| configuration as code | конфигурация как код | T | ch22 |
| per-change budgets / scheduled load tests | бюджеты на каждое изменение / плановые нагрузочные тесты | T | ch22 |
| shared-environment tar pit / quarantine graveyard | трясина общего окружения / кладбище карантина | T | ch22 |

## Doubts and notes on the English (English not changed)

- ch21 Kruchten reference: "read at abstract level only" is an access note in reader text (CLAUDE.md §7
  asks to fold it into the evidence label). Translated faithfully. The same chapter's prose also says
  "the abstract of an IEEE Software special issue's introduction says…", rendered «как сказано в аннотации…».
- ch21 "This is **research** about the literature": "research" is not in the evidence-label list;
  rendered «**исследование** литературы». "research finding with a narrow base" → «научный результат с
  узкой базой».
- ch22 "**expert opinion and documented practice**" rendered as a combined label «мнением экспертов и
  задокументированной практикой» (plural «экспертов», since several authors are meant).
- ch22 Petrović is cited as 2022 in the link text but the bibliography id is `petrovic2021mutation`;
  link text kept as in English.
- ch22 Example info box says Core "ships on a two-week train"; rendered «двухнедельным релизным поездом».
- ch22: "ledger" (lowercase, as a system area) kept in Latin («запись в ledger»), matching
  `cast.ru.md` («эксперт по ledger»).
- Tables keep English number format (`1,900`, `1.5 инженера`); words in number cells translated.
