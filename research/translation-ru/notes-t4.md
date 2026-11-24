# Translation notes, lane t4 (Chapters 19–20)

Source: English working tree (`b84a765` text). Files:
`docs/parts/05-engineering-quality/19-defining-measuring-and-owning-quality.ru.md`,
`docs/parts/05-engineering-quality/20-engineering-standards-and-their-governance.ru.md`.

Structural check for both: heading anchors, link targets, exercise labels, Mermaid count, admonition
types and table digits identical to the English (ch20 differs only in punctuation inside two cells, «Q3»
without the English final period); `tools/validate_book.py` passes. Words (wc -w): ch19 5 494, ch20 5 551.
Failure Modes fields: «Как заметить:» (Signal) / «Что делать:» (Countermeasure).

## New terms

| English | Русский | Rule | Where |
|---|---|---|---|
| external / internal / delivery quality | внешнее / внутреннее качество / качество поставки | T | ch19 |
| quality profile | профиль качества | T | ch19, ch20 |
| central QA | централизованный QA | T | ch19 |
| embedded quality engineers | встроенные инженеры по качеству | T | ch19 |
| team-owned quality | качество во владении команды; владение команды (short, tables) | T | ch19 |
| platform-enabled quality | качество с опорой на платформу | T | ch19 |
| conformance (to specification) | соответствие спецификации; тестирование на соответствие | T | ch19 |
| Garvin's approaches: transcendent, product-, user-, manufacturing-, value-based | трансцендентный, продуктовый, пользовательский, производственный, ценностный | T | ch19 |
| Garvin's dimensions: performance, serviceability | эксплуатационные характеристики, удобство обслуживания | T | ch19 |
| critical user path | критический пользовательский путь | T | ch19 |
| measure set / ownership map | набор показателей / карта владения | T | ch19 |
| path correctness rate | доля корректных результатов на пути | T | ch19 |
| unit-level (logic, defects) | модульный уровень, логика модульного уровня | T | ch19 |
| end-to-end flow | сквозной сценарий | T | ch19 |
| exploratory testing | исследовательское тестирование | T | ch19 |
| sign-off | утверждение релиза | T | ch19 |
| fix rate | доля исправленных дефектов | T | ch19 |
| line coverage | покрытие строк | T | ch19, ch20 |
| triage (support) | сортировка обращений; сортировка | T | ch19 |
| exposure (defect counts) | открытость клиентам | T | ch19 |
| accessibility (testing) | доступность интерфейса (accessibility) | B | ch19; avoids clash with доступность = availability |
| safety case | обоснование безопасности (safety case) | B | ch19 |
| compliance theater | театр соответствия | T | ch20 (intro, heading, section) |
| enforcement ladder | лестница контроля (enforcement ladder) | B | ch20 |
| ladder rungs: default, automated check, human review, audit, exhortation | по умолчанию (умолчание), автоматическая проверка, ревью человеком, аудит, призывы | T | ch20 |
| enforcement (mechanism) | обеспечение (соблюдения); механизм обеспечения | T | ch20 |
| intent / scope / level / owner / verification / exemption path / review date | назначение / область действия / уровень / владелец / проверка (способ проверки) / порядок исключений / дата пересмотра | T | ch20; the seven parts |
| must / should / may (RFC 2119) | «must» («обязательно») / «should» («следует») / «may» («можно») | B | ch20 |
| rules / guidance | правила / рекомендации | T | ch20 |
| retire (a standard) | отменить; отмена | T | ch20 |
| effective false positive | фактически ложное срабатывание (effective false positive) | B | ch20 |
| fix-it week | неделя исправлений (fix-it week) | B | ch20 |
| "Not useful" button / not-useful rate | кнопка «Бесполезно» (Not useful) / доля «бесполезно» | B | ch20 |
| build gate; gate (verb) | блокировка сборки; блокировать сборку | T | ch20; term base "stage gate" (контрольная точка) is a different sense |
| review-time warning | предупреждение на ревью | T | ch20 |
| baseline (existing violations) | зафиксировать как исходный уровень | T | ch20 |
| bypass flag | флаг обхода | T | ch20 |
| fitness function | фитнес-функция (fitness function) | B | ch20 |
| tier deflation | занижение уровня критичности (tier deflation) | B | ch20 |
| guild / council / named owner | гильдия / совет / назначенный владелец | T | ch20 |
| decoupling (Meyer and Rowan) | отделение (decouple) формы от практики | B | ch20 |
| attestation | подтверждение (attestations) | B | ch20 |
| system evidence | системные свидетельства | T | ch20 |
| rubber stamp(ing) | утверждение не глядя | T | ch20 |
| standards register / exemption register | реестр стандартов / реестр исключений | T | ch20 |
| enterprise standard / list | общекорпоративный стандарт / список | T | ch20 |
| audit trail; auditable pipeline | журнал аудита; пайплайн с журналом аудита | T | ch20 |
| warning wallpaper / exemption sprawl / checkbox compliance / the wiki of musts | обои из предупреждений / разрастание исключений / соблюдение для галочки / вики обязательных правил | T | ch20, failure-mode names |
| incident lead | руководитель по инциденту | T | ch20 |

Reused from earlier lanes: компенсирующая мера, исключение, уровень сервиса для решений (decision
service level), мерж-реквест, команда содействия (enabling), операционные минимумы, tier 1.

## Doubts and notes on the English

- Ch19 Part V overview: "Chapter 21: pricing technical debt" rendered «как оценить технический долг в
  деньгах»; "the path from merge to customer" → «путь от слияния кода до клиента».
- Ch19 Failure Modes: two entries ("The platform that owns nothing", "Ranking by exposure") have no
  Signal field in the English; kept as is (only «Что делать:»). Same in ch20 ("Warning wallpaper",
  "Standards instead of ownership" has neither).
- Ch20 F2 keeps Latin item letters (a)–(e) so the solutions page can refer to them.
- Ch20 Decision Framework diagram: "Ever wrong?" rendered «Ошибается?» to stay short.
- Ch20 "compliance theater": glossary has «соответствие требованиям (compliance)»; «театр соответствия»
  chosen by analogy with the established «театр безопасности». The maintainer may prefer
  «показное соблюдение».
