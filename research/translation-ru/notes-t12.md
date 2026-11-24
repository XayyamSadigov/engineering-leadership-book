# Translation notes, lane t12 (Chapters 35–36)

Source: English working tree. Files:
`docs/parts/07-organization-design/35-designing-organizations-at-four-scales.ru.md`,
`docs/parts/07-organization-design/36-reorganizations-evolution-and-succession.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order, link targets, exercise labels, admonition types, Mermaid count, table rows and
every number in tables identical. Prose number differences are only word forms ("year 2" → «второй год»,
four times per chapter), «1:1» for "one-on-one", and the thousands separator. Words (wc -w; no-break
spaces glue some tokens): ch35 5 809, ch36 5 820.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| organization design (the artifact); design | проект организации; проект | T | ch35, ch36; «организационный дизайн» kept for the discipline (term base) |
| breakage | поломка | T | ch35 |
| coordination load / cost | координационная нагрузка / стоимость координации | T | ch35 |
| band (20, 50, 100, 500) | диапазон; отметка (in "passes 20 engineers") | T | ch35 |
| structural answer | структурный ответ | T | ch35 |
| group lead | руководитель группы | T | ch35 |
| route / router (leaders route work) | маршрутизировать / маршрутизатор | T | ch35 |
| fiefdoms | удельные княжества | T | ch35 |
| technical direction function | функция технического направления | T | ch35; "technical direction" per notes-t1 |
| portfolio planning | планирование портфеля | T | ch35 |
| intake (platform) | единый вход для запросов | T | ch35; follows notes-t10 «единый вход» |
| product statement (platform) | описание продукта | T | ch35 |
| adoption measure | показатель принятия | T | ch35; «принятие» follows notes-t10 |
| grow / hold / harvest (portfolio direction) | рост / удержание / сбор отдачи (harvest) | B | ch35; maintainer may prefer «доение» (business slang) — avoided as too colloquial |
| release mechanics | механика релизов | T | ch35 |
| sites (locations) | площадки | T | ch35, ch36 |
| dual career path | двойной карьерный путь | T | ch35 |
| layer test / span, link, and layer tests (Ch 34) | проверка уровня / тесты охвата, связей и уровней | T | ch35; Ch 34.ru does not name these tests |
| headcount formula / premature layer / platform dumping ground / title without a mandate / functional silos / copying a famous company's model | формула численности / преждевременный уровень / платформа-свалка / должность без мандата / функциональные колодцы / копирование модели известной компании | T | ch35 failure modes |
| "Signal:" / "Detection:" (ch35 failure-mode fields) | «Признак:» / «Как заметить:» | T | ch35; the English uses Signal + Detection, not Signal + Countermeasure, so «Как заметить:» goes to Detection and Signal gets «Признак:»; ch36 has Detection only |
| engineer-turned-manager | бывший инженер (ставший руководителем) | T | ch35 |
| quality engineers | инженеры по качеству | T | term base 3.x |
| ramp-up | вхождение в работу | T | ch36; follows notes-t3 |
| handoff (of ownership, rotation) | передача дел; передача | T | ch36 |
| payback | окупаемость | T | ch36; term base "payback period" = срок окупаемости |
| increment (over the smaller option) | прирост | T | ch36 |
| transition dip / misfit | просадка перехода / несоответствие | T | ch36; «просадка» follows notes-t8 |
| adjust / partial reversal / full reversal | корректировка / частичный откат / полный откат | T | ch36 |
| procedural justice; job control; job insecurity | процедурная справедливость; контроль над собственной работой; неуверенность в сохранении работы | T | ch36 |
| intervening variables / factors | промежуточные факторы | T | ch36 |
| longitudinal; observational | лонгитюдный; наблюдательный | T | ch36 |
| consult on the problem, decide the names privately | советуйтесь о проблеме, имена решайте без огласки | T | ch36 |
| announcement day; all-engineering call | день объявления; общий звонок для всей разработки | T | ch36 |
| critical role | критическая роль | T | ch36; follows glossary.ru |
| readiness: ready now / ready with development / interim only / none | готов сейчас / готов после развития / только временно / никого | T | ch36; follows glossary.ru «Покрытие преемниками» |
| cover (succession) | замена; покрытие | T | ch36 |
| heir apparent | назначенный наследник | T | ch36 |
| perpetual / leaked / boxes-only reorganization; succession theater | вечная / утёкшая реорганизация; реорганизация квадратиков; театр преемственности | T | ch36 failure modes; «фабрика бесхозных компонентов» reused from notes-t10 |
| shadow (incidents, on-call) | участвовать в инцидентах как наблюдатель | T | ch36 |
| user-facing alerts | алерты по пользовательским симптомам | T | ch36; follows notes-t6 symptom alerts |
| human resources | HR | T | ch36 |

Reused from earlier lanes: связь зависимости, ротация на прерываниях, инвентаризация владения,
ранбук (runbook), неформальный лид, найм на замену, место, исключение, tier 1, truck factor (он же bus
factor), мерж-реквест, приём заказов, контракт сопоставления заказов и счетов, «Год вкратце», хроника
года 1, список действующих лиц.

## Doubts and notes on the English (English not changed)

- ch35 Failure Modes use "Signal:" and "Detection:" (not Signal/Countermeasure). See the table above for
  the rendering; the maintainer may prefer one label set for the whole book.
- ch35 Brackenridge table: the arithmetic cell is English words around numbers; translated
  («50 инженеров = 5 команд по 8–9 (43) + платформа 5 + 2 staff-инженера»), numbers unchanged
  ("8 to 9" → «8–9»).
- ch35 Case table: "her stated condition, after week 26, is met" is ambiguous (stated after week 26, or
  met after week 26). Rendered «её условие, поставленное после недели 26, выполнено».
- ch35 "A team health check in week 16 rated mobile red on 4 of 10 indicators" rendered with
  «проверка здоровья команды», following first-quarter.ru.
- ch35 "Larson's *The Engineering Executive's Primer* … the engineering executive's core
  responsibilities": "engineering executive" rendered «руководитель разработки высшего уровня» (notes-t1).
- ch36 Case: "two Sev2 incidents sat at the mobile-bff and mobile boundary" — "mobile" read as the mobile
  app (mobile-app); rendered «на границу между mobile-bff и мобильным приложением».
- ch36 Case transition plan: "Orders engineers shadow incidents" rendered «участвуют в инцидентах как
  наблюдатели».
- ch36 Succession table: "Payments then falls to its tech lead" rendered «Тогда Payments переходит к
  техлиду команды» to avoid an ambiguous «её».
- ch36 Enterprise application: "nobody attends the announcement as the remote audience of a room"
  rendered «никто не слушает объявление как удалённый зритель чужой переговорной».
- ch36 "the evidence on failure rates is thin": rendered «данные о доле провалов слабые».
- Both chapters: "year 2" in prose rendered as word forms («второго года»), so the page number check
  shows four missing "2" per chapter; not a content change.
