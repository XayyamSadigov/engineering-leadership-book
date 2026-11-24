# Translation notes, lane t11 (Chapters 33–34)

Source: English working tree. Files:
`docs/parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.ru.md`,
`docs/parts/07-organization-design/34-spans-layers-and-dependency-mapping.ru.md`.
Both pass `tools/validate_book.py` (no build run). Structural check per chapter against the English:
heading anchors in order, link targets, exercise labels, admonition types, Mermaid count, table rows and
every number in tables identical. Failure Modes in both chapters have only a "Detect it:" field, rendered
«Как заметить:». Words (wc -w; no-break spaces glue some tokens): ch33 5 658, ch34 5 297.

## New terms (not in the term base; used consistently)

| English | Русский | Rule | Where |
|---|---|---|---|
| mirroring hypothesis; mirroring | гипотеза зеркального отражения (mirroring hypothesis); зеркальное отражение | B | ch33 |
| partial mirroring; break the mirror | частичное отражение; «разбить зеркало» | T | ch33 |
| socio-technical congruence; congruence gap | социотехническая согласованность; разрыв согласованности | T | ch33 |
| coordination requirements / needs | потребности в координации | T | ch33 |
| modification requests | запросы на изменение (тикеты на изменения) | T | ch33 |
| logical dependencies | логические зависимости | T | ch33 |
| intrinsic / extraneous / germane load | внутренняя (intrinsic) / внешняя (extraneous) / учебная (germane) нагрузка | B | ch33; «учебная» chosen over «релевантная» because the English glosses germane as "spent on learning"; maintainer may prefer the Russian psychology term «релевантная» |
| schemas (Sweller) | схемы знаний | T | ch33 |
| proxies (of load) | косвенные признаки | T | ch33 |
| knowledge map / knowledge count | карта знаний (follows ch12.ru) / число знающих | T | ch33 |
| team-and-component map | карта команд и компонентов | T | ch33 |
| component file (components.csv) | файл компонентов | T | ch33 |
| reporting group | группа подчинения | T | ch33 |
| seam (split along a seam) | шов (разделить по шву) | T | ch33, ch34 |
| enabling engagement | работа команды содействия; работа считается содействием | T | ch33 |
| exit criterion / exit (of an engagement) | критерий выхода / выход | T | ch33 |
| interrupt rotation | ротация на прерываниях | T | follows notes-t3 |
| bulk ordering | массовый заказ | T | follows cast.ru |
| value streams | потоки создания ценности | T | ch33; follows notes-t3 «карта потока создания ценности» |
| org chart | оргструктура; схема | T | ch33, ch34 |
| org chart redraw / reverse Conway fantasy / load laundering / interrupt-sink platform / permanent collaboration / gamed load survey | перерисованная оргструктура / фантазия об обратном манёвре Конвея / отмывание нагрузки / платформа — «приёмник прерываний» / вечное сотрудничество / подогнанный опрос о нагрузке | T | ch33 failure modes; «отмывание» follows ch26 «отмывание серьёзности» |
| span (short for span of control) | охват; охват управления | T | ch34; term base gives the long form |
| layer (in ch34 title and prose) | уровень управления; уровень иерархии (nav title) | T | ch34 |
| decision hop; hop | переход (решения на уровень вверх); переход | T | ch34 |
| lowest common manager | ближайший общий руководитель | T | ch34 |
| staff meeting | совещание с подчинёнными | T | ch34 |
| control loss (Williamson) | «потеря контроля» (control loss) | B | ch34 |
| engagement (Gallup) | вовлечённость | T | ch34 |
| individual work / hands-on work (manager's) | собственная исполнительская работа; исполнительская работа | T | ch34 |
| triage (manager with sixteen does triage) | сортировка срочного | T | ch34 |
| requesting / providing team | запрашивающая / предоставляющая команда | T | ch34 |
| recount (the matrix) | пересчитать; пересчёт | T | ch34 |
| candidate move | возможный шаг | T | ch34 |
| order-to-invoice mapping / contract | сопоставление заказов и счетов; контракт сопоставления заказов и счетов | T | ch34 |
| order-entry screens; web shell | экраны оформления заказа; общая веб-оболочка | T | ch34 |
| order capture (domain, team) | приём заказов | T | ch33, ch34 |
| option set | набор вариантов | T | ch34 |
| dotted lines | пунктирные линии подчинения | T | ch34 |
| flattening | сокращение уровней (иерархии); плоская структура | T | ch34 |
| span table | таблица охвата | T | ch34 |
| span-only reorg / messenger layer / silent overload / dumping-ground team | реорганизация только ради охвата / уровень-передатчик / тихая перегрузка / команда-свалка | T | ch34 failure modes |
| senior manager (layer) | старший руководитель | T | follows notes-t1 |

Table headers in the ch34 dependency matrix keep the English short team names (`Payments`,
`Customer Exp.`, `Data`, `Platform`), as names stay in Latin script.

## Doubts and notes on the English (English not changed)

- ch33 Why This Matters: "A CTO who reorganizes for reporting convenience" is ambiguous (convenience of
  reporting lines vs of status reporting). Rendered «ради удобства схемы подчинения» (reporting lines).
- ch33 Example: "Bulk ordering … occupies 5 Orders engineers" and later "5 Orders engineers" keep the
  digit as in English; Russian prose has «5 инженеров», which is fine but a word form would read better.
- ch33 Trade-offs: "*Team Topologies* emphasizes keeping teams together" rendered «настаивает на том,
  чтобы команды не разбивали» (stable, long-lived teams).
- ch33 Learning objective "say which kind of load each action would remove" kept as an objective with
  «говорить», since the English uses "say".
- ch34 Case option table: M3 shows "−4 links", while the Example table gives M3 as 6 removed and 2
  created; the case figure is the net. M1 "−4" is gross (0 counted created). Consistent, but a reader may
  stumble; the English might write "net −4" for M3.
- ch34 Deep explanation: "Graicunas, writing in the 1930s" with a 1937 citation; rendered «в 1930-х
  годах».
- ch34 F1: "(first year as manager, sites, informal leads, hands-on work, recent changes)" lists the
  table's facts, not the five factors; translated as is.
- ch34 X1: "Rajiv Menon (CFO)" glossed «CFO, финансовый директор» on first use on the page.
