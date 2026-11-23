# Глоссарий { #glossary }

На этой странице простыми словами определены термины, которые книга использует чаще всего, — для
читателя с инженерным бэкграундом и без подготовки в менеджменте, финансах или психологии. Термины
сгруппированы по темам; чтобы найти нужный, воспользуйтесь поиском в браузере. В каждой статье указано
значение, в котором термин используется в книге, единица измерения, если она есть, и ссылка на раздел
главы, где тема разобрана полностью. Если две главы употребляют слово в разных смыслах, статья приводит
оба и говорит, какая глава использует какой. Статьи о Northstar и Halvard описывают вымышленные компании
книги, а не реальные. В заголовках статей рядом с русским термином приведён английский, чтобы его было
проще найти в английских главах.

## Деньги и бизнес { #money-and-business }

### ARR { #arr }

Annual recurring revenue, годовая регулярная выручка: годовая стоимость подписочных контрактов,
действующих в данный момент. Это темп (run rate), а не выручка, полученная за период, поэтому она
расходится со строкой выручки всякий раз, когда бизнес растёт или сокращается. Отток (churn) — это ARR,
потерянный, когда клиенты не продлевают контракт или покупают меньше; в подписочном бизнесе надёжность
сказывается при продлении, а не в момент поставки. Единица: доллары в год. Подробно:
[глава 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#reading-a-business-model)
и [глава 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#the-three-statements-read-by-a-technology-leader).

### Валовая маржа (gross margin) { #gross-margin }

Доля выручки, остающаяся после затрат на предоставление сервиса (хостинг, поддержка, платёжные комиссии,
сервисные кредиты). Затраты на облако и нагрузка от инцидентов уменьшают её напрямую. Единица: процент от
выручки. Подробно:
[глава 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#reading-a-business-model).

### Сервисные кредиты (service credits) { #service-credits }

Деньги, которые поставщик возвращает клиенту или вычитает из счёта, когда нарушает договорное
обязательство, например по доступности. Кредиты вычитаются из выручки, поэтому каждый не выплаченный
кредитом доллар стоит полного доллара. Единица: доллары. Подробно:
[глава 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#reading-a-business-model).

### Операционные расходы (operating expense) { #operating-expense }

Текущие расходы бизнеса, которые отражаются в отчёте о прибылях и убытках в том периоде, когда возникли:
исследования и разработка (большая часть зарплат инженеров), продажи и маркетинг, общие и
административные расходы. Когда CFO просит «операционные расходы без роста», речь идёт об этой строке.
Единица: доллары в год. Подробно:
[глава 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#the-three-statements-read-by-a-technology-leader).

### Капитализация ПО и списание на расходы (capitalized versus expensed software) { #capitalized-versus-expensed-software }

Списание на расходы отражает затраты в отчёте о прибылях и убытках в момент их возникновения.
Капитализация учитывает подходящие работы над ПО как актив и распределяет их стоимость на срок полезного
использования в виде амортизации — ежегодного неденежного начисления. Какие работы подходят, определяют
стандарты бухгалтерского учёта (ASC 350-40 для ПО для внутреннего использования и облачного ПО в США,
IAS 38 по МСФО), а решение принимают финансы; капитализация меняет отчётную прибыль, но не денежные
средства и не ресурсы команды. Подробно:
[глава 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#capitalized-versus-expensed-software).

### EBITDA { #ebitda }

Прибыль до вычета процентов, налогов и амортизации. Поскольку амортизация в ней прибавляется обратно,
капитализация большего объёма ПО увеличивает EBITDA на всю капитализированную сумму, и поэтому
капитализация становится темой для совета директоров везде, где компанию оценивают по EBITDA. Единица:
доллары. Подробно:
[глава 52](parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md#the-three-statements-read-by-a-technology-leader).

### Полная стоимость сотрудника (fully loaded cost) { #fully-loaded-cost }

Полная годовая стоимость найма одного человека: зарплата плюс льготы, налоги на фонд оплаты труда и
прочие расходы, которые сопровождают рабочее место. В Northstar она в среднем составляет $185 000 на
инженера в год — по этой ставке книга переводит ресурсы в деньги. Единица: доллары на инженеро-год.
Вводится в [обзоре Northstar](case-studies/northstar/index.md#the-company) и используется в
[главе 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#opportunity-cost-and-sunk-cost).

### Стоимость задержки (cost of delay) { #cost-of-delay }

Ценность, теряемая за единицу времени, пока работа не сделана: незаработанная выручка, несэкономленные
затраты, неснятый риск. Важна её форма: одни задачи каждую неделю теряют постоянную сумму, другие ничего не
теряют до дедлайна, а потом очень много. Единица: доллары в неделю. Подробно:
[глава 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#cost-of-delay-definition-shape-and-origin)
и [глава 15](parts/04-execution/15-planning-prioritization-and-delivery-methods.md#prioritization-as-economics).

### CD3 и WSJF { #cd3-and-wsjf }

Два способа ранжировать работу по стоимости задержки. CD3 (стоимость задержки, делённая на длительность)
использует оценки в деньгах и времени; WSJF (Weighted Shortest Job First, из фреймворка SAFe) использует
для того же отношения относительные баллы. Задачи с фиксированной датой так не ранжируют: их планируют в
обратном порядке от даты. Подробно:
[глава 15](parts/04-execution/15-planning-prioritization-and-delivery-methods.md#prioritization-as-economics).

### Альтернативные издержки и невозвратные затраты (opportunity cost and sunk cost) { #opportunity-cost-and-sunk-cost }

Альтернативные издержки — ценность лучшей альтернативы, от которой отказываются при выборе. При
фиксированной численности альтернативные издержки проекта — это ценность работы, которую эти инженеры
сделали бы иначе, обычно стоимость задержки вытесненной задачи, а не их зарплата. Невозвратные затраты —
уже потраченные деньги или усилия, которые нельзя вернуть; они не должны влиять на то, что делать дальше.
Подробно:
[глава 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#opportunity-cost-and-sunk-cost).

### Чистая приведённая стоимость (NPV) { #net-present-value-npv }

Сегодняшняя стоимость будущих денежных поступлений проекта минус сегодняшняя стоимость его выплат после
дисконтирования более поздних денег (см. следующую статью). Положительное значение означает, что проект
зарабатывает больше требуемой компанией доходности. Более простой срок окупаемости (время, за которое
возвращаются первоначальные затраты) игнорирует стоимость денег во времени и всё, что происходит после
даты окупаемости. Единица: доллары. Подробно:
[глава 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#a-common-frame-payback-net-present-value-and-options).

### Ставка дисконтирования и барьерная ставка (discount rate and hurdle rate) { #discount-rate-and-hurdle-rate }

Годовая ставка, по которой будущие деньги приводятся к сегодняшней стоимости, потому что доллар потом
стоит меньше, чем доллар сейчас. Теоретически это стоимость капитала компании; на практике используйте
ставку, которую задают финансы, — барьерную ставку (в Northstar это 10 процентов). Единица: процентов в
год. Подробно:
[глава 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#a-common-frame-payback-net-present-value-and-options).

## Ресурсы и планирование { #capacity-and-planning }

### FTE { #fte }

Full-time equivalent, эквивалент полной ставки: полное рабочее время одного человека; используется для
подсчёта ресурсов независимо от того, как оно распределено между людьми (два человека на полставки — это
1 FTE). Большинство таблиц ресурсов в книге даны в FTE, усреднённых за квартал. Единица: FTE. Подробно:
[глава 27](parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md#funding-the-work).

### FTE-квартал (FTE-quarter) { #fte-quarter }

Один FTE на один квартал из 13 недель, то есть 1 FTE-квартал равен 13 инженеро-неделям (в главе 38
62 FTE-квартала — это 806 инженеро-недель). Он измеряет объём работы, тогда как FTE измеряет темп
ресурса. Единица: FTE-кварталы. Подробно:
[глава 38](parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#engineering-organization-example).

### Инженеро-неделя, инженеро-день, инженеро-год (engineer-week, engineer-day, engineer-year) { #engineer-week-engineer-day-engineer-year }

Рабочая неделя, день или год одного инженера; используются для оценки объёма работы. Книга оценивает
инженеро-год в $185 000, а инженеро-неделю примерно в $3558 ($185 000, делённые на 52 недели).
Некоторые главы (21, 30, 52) оценивают инженеро-день примерно в $800 ($185 000, делённые на 230 рабочих
дней), поэтому в этих главах пять инженеро-дней стоят больше одной инженеро-недели; сравнивайте
сопоставимое. Подробно:
[глава 45](parts/10-business-leadership/45-business-models-and-engineering-economics.md#opportunity-cost-and-sunk-cost).

### Плановый и осторожный сценарии (planned case and cautious case) { #planned-case-and-cautious-case }

Два сценария ресурсов, которые задаёт квартальный план. Плановый сценарий предполагает, что
незапланированная работа останется на измеренном уровне; осторожный — что её будет больше (22 и
28 процентов ресурса в плане Northstar на третий квартал). Организация берёт обязательства только в
объёме, который выдерживает осторожный сценарий, а остальное помечает как цели. Подробно:
[глава 38](parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#quarterly-planning-at-organization-level).

### Список непрофинансированного (unfunded list) { #unfunded-list }

Письменный список запрошенных задач, которые квартальный план не финансирует. Он превращает «разработка
медленная» в явный, общий выбор одних задач вместо других. Подробно:
[глава 38](parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#quarterly-planning-at-organization-level).

### Незапланированная работа (unplanned work) { #unplanned-work }

Работа, которая попадает в очередь команды после того, как та решила, чем заниматься, и вытесняет
что-то запланированное. Книга делит её на четыре источника: восстановление после сбоев, запросы других
команд, поломки инструментов и окружений и срочные бизнес-запросы. Команда, которая получает много
запросов и сбоев других команд, — это «приёмник прерываний» (interrupt sink). Единица: процент ресурса или
FTE. Подробно:
[глава 16](parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md#unplanned-work-visible-and-classified).

### Выделение на профилактику (prevention allocation) { #prevention-allocation }

Ресурс, явно и по каждой команде зарезервированный под работу, которая устраняет источники инцидентов и
незапланированной работы, а не финансируемый из того, что осталось. В Northstar это было 12 FTE в первом
и втором кварталах и 8 FTE в третьем. Единица: FTE. Подробно:
[глава 27](parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md#funding-the-work).

### Незавершённая работа (WIP) и лимит WIP { #work-in-progress-wip-and-wip-limit }

Незавершённая работа — всё начатое и не законченное, включая задачи, которые заблокированы или ждут
ревью. Лимит WIP ограничивает число задач, которые могут одновременно находиться на каждом этапе доски.
Единица: задачи. Подробно:
[глава 16](parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md#littles-law-and-work-in-progress).

### Закон Литтла (Little's law) { #littles-law }

Для стабильной системы среднее время выполнения равно среднему объёму незавершённой работы, делённому на
среднюю пропускную способность. Это теорема о средних: меньше незавершённой работы означает меньше
ожидания, только если пропускная способность сохраняется. Подробно:
[глава 16](parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md#littles-law-and-work-in-progress).

### Прогноз, цель и обязательство (forecast, target, and commitment) { #forecast-target-and-commitment }

Прогноз — вероятностное утверждение о том, когда работа будет закончена; им владеет команда. Цель —
результат, которого хочет руководство. Обязательство — обещание определённого объёма к определённой дате
тому, кто будет на него опираться; его дают по осторожному краю прогноза (85-й или 95-й процентиль).
Подробно:
[глава 17](parts/04-execution/17-predictability-and-managing-uncertainty.md#forecasts-targets-and-commitments).

### Процентильный прогноз и моделирование Монте-Карло (percentile forecast and Monte Carlo simulation) { #percentile-forecast-and-monte-carlo-simulation }

Пропускная способность — число задач, которые команда завершает за неделю. Моделирование Монте-Карло
многократно повторяет случайный эксперимент, здесь — выбирает прошлые недели пропускной способности,
чтобы получить диапазон возможных дат завершения. Процентильный прогноз читает этот диапазон:
«85-й процентиль, неделя 30» означает, что 85 процентов смоделированных прогонов завершились к неделе 30.
Подробно:
[глава 17](parts/04-execution/17-predictability-and-managing-uncertainty.md#forecasting-from-throughput).

## Поставка и качество { #delivery-and-quality }

### Lead time { #lead-time }

Книга использует два значения, и каждая глава говорит, какое. **Время внесения изменений** (change lead
time, в терминах DORA — lead time for changes) — время от коммита до работы в продакшене; в этом значении
термин используют таблица команд Northstar и главы 14, 15 и 18 (медиана Core в базовом квартале —
19 дней). **Lead time** в главе 16 — время от момента, когда организация берёт на себя работу, до момента,
когда клиенты могут ею пользоваться; оно длиннее и включает ожидание до того, как написана первая строка
кода. Единица: дни. Подробно:
[глава 18](parts/04-execution/18-measuring-engineering-productivity.md#what-the-dora-metrics-measure)
и [глава 16](parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md#where-lead-time-accumulates).

### Метрики DORA (DORA metrics) { #dora-metrics }

Метрики поставки, публикуемые DORA (DevOps Research and Assessment, ныне часть Google Cloud). Многие
дашборды показывают «четыре ключевые метрики»; актуальное руководство перечисляет пять: время внесения
изменений, частоту развёртываний (развёртываний за период), время восстановления после неудачного
развёртывания, долю неудачных изменений и долю развёртываний-переделок. Они описывают одну систему
поставки за раз и ничего не говорят о том, то ли было построено. Подробно:
[глава 18](parts/04-execution/18-measuring-engineering-productivity.md#what-the-dora-metrics-measure).

### Доля неудачных изменений (change failure rate) { #change-failure-rate }

Доля развёртываний или релизов, которые заканчиваются неудачей. DORA считает развёртывания, потребовавшие
немедленного вмешательства, например отката или хотфикса. Northstar считает релиз неудачным, если в
течение 72 часов за ним последовали хотфикс, откат или связанный инцидент; это другое, локальное
определение. Единица: проценты. Подробно:
[глава 23](parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md#change-approval-and-pipeline-outcomes)
и [глава 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#classifying-change-failures-to-find-the-prevention-point).

### SPACE { #space }

Фреймворк, который рассматривает продуктивность разработчиков как несколько измерений: удовлетворённость
и благополучие, результативность, активность, коммуникация и сотрудничество, эффективность и поток. Книга
использует его как чек-лист, чтобы набор метрик не покрывал только одно измерение. Подробно:
[глава 18](parts/04-execution/18-measuring-engineering-productivity.md#space-a-checklist-of-dimensions).

### Опыт разработчиков (DevEx) { #developer-experience-devex }

То, как разработчики переживают свою ежедневную работу и её трение; обычно измеряется по циклам обратной
связи, когнитивной нагрузке и состоянию потока с сочетанием опросов и системных данных. Указывает на
причины, которые руководитель может изменить. Подробно:
[глава 18](parts/04-execution/18-measuring-engineering-productivity.md#developer-experience-devex).

### Пропущенный дефект (escaped defect) { #escaped-defect }

Дефект, который после релиза нашёл клиент, а не какая-либо проверка до релиза. Northstar считает
обращения клиентов об ошибках, подтверждённые как дефекты (212 в базовом квартале, 38 процентов из них —
регрессии поведения, которое раньше работало), и классифицирует каждый по точке обнаружения: самому
раннему шагу, на котором разумная проверка поймала бы дефект. Единица: штук за квартал. Подробно:
[глава 19](parts/05-engineering-quality/19-defining-measuring-and-owning-quality.md#detection-points-tell-you-who-should-own-a-check).

### Технический долг: основной долг и проценты (technical debt) { #technical-debt-principal-and-interest }

Накопленная стоимость дизайна и кода, которые больше не соответствуют работе. Основной долг — стоимость
его устранения; проценты — регулярная стоимость жизни с ним, в инженерном времени и в рисках, например
инцидентах. Правило книги: метафору используйте для коммуникации, а экономику — для решений. Единица:
проценты в часах за период. Подробно:
[глава 21](parts/05-engineering-quality/21-technical-debt.md#measuring-interest-instead-of-ugliness).

### «Асфальтированная дорога» (paved road) { #paved-road }

Поддерживаемый способ по умолчанию собирать и запускать сервис: шаблон с health-check'ами, логированием и
алертами и общий пайплайн, который выполняет согласованные проверки. Команды, которые идут по ней,
соблюдают большинство стандартов, не задумываясь. Подробно:
[глава 20](parts/05-engineering-quality/20-engineering-standards-and-their-governance.md#paved-roads-before-review-boards).

### Контрактный тест (contract test) { #contract-test }

Тест на границе между сервисами. В контрактах, задаваемых потребителем (consumer-driven contracts), каждый
потребитель описывает части интерфейса поставщика, на которые он опирается, в виде исполняемых ожиданий,
а поставщик запускает их в своей сборке, так что ломающее изменение падает там же, с указанием
потребителя. Подробно:
[глава 22](parts/05-engineering-quality/22-testing-strategy-and-test-architecture.md#contracts-at-boundaries).

### Фича-флаг (feature flag) { #feature-flag }

Переключатель между ветками кода во время выполнения. Он отделяет развёртывание (перенос кода в
продакшен) от релиза (открытия поведения пользователям), и каждый флаг — источник риска, которым нужно
управлять и который потом нужно удалить. Флаги делают возможной прогрессивную поставку, например
канареечный релиз, который сначала направляет на новую версию небольшую долю трафика. Подробно:
[глава 23](parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md#flags-separating-deploy-from-release).

### Релизный поезд (release train) { #release-train }

Релиз, который уходит по фиксированному расписанию и везёт все готовые изменения. Core в Northstar
выпускался двухнедельным поездом, перед каждым из которых шёл трёхдневный ручной регрессионный прогон
примерно из 1900 тест-кейсов; с недели 5 первого квартала поезд стал еженедельным. Подробно:
[глава 23](parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md#practical-playbook).

## Надёжность и инциденты { #reliability-and-incidents }

### Серьёзность (Sev1, Sev2, Sev3) { #severity-sev1-sev2-sev3 }

Оценка, которая задаёт реакцию на инцидент, а затем становится метрикой. Правила книги: определять уровни
по наблюдаемому влиянию на клиентов, включить класс для неверных данных, разрешить повышать серьёзность
любому, а понижать — только координатору инцидента с записанной причиной. Письменное определение Sev1 в
Northstar (неделя 3): «путь заказа или оплаты недоступен хотя бы для одного клиента, или клиентам видна
хотя бы одна неверная финансовая запись»; Sev2 и Sev3 последовательно уже, а главный показатель — сумма
Sev1 и Sev2. Якорь для ссылок: `#severity-sev1-sev2-sev3`. Подробно:
[глава 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#severity-definitions-that-resist-reclassification).

### Tier 1 { #tier-1 }

Высший из трёх уровней критичности, которые назначают каждому компоненту обязательства по влиянию на
бизнес. В Northstar компонент относится к tier 1, если он находится на пути заказа или оплаты, и решение
об этом принимается вне команды-владельца (15 компонентов в первый год). Tier 2 и tier 3 несут более
лёгкие обязательства, например дежурство только в рабочие часы и более простые алерты. Подробно:
[глава 20](parts/05-engineering-quality/20-engineering-standards-and-their-governance.md#tiering)
и [глава 24](parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#operational-readiness).

### Операционные минимумы tier 1 (tier 1 operational minimums) { #tier-1-operational-minimums }

Четыре условия, которым в Northstar должен соответствовать каждый компонент tier 1: названная
команда-владелец, полный набор алертов о проблемах, видимых пользователям, ранбук для известных отказов и
график дежурств. Пятое требование — развёртывание через аудируемый пайплайн с автоматическим откатом —
отслеживается отдельно как стандарт пайплайна. В базовом квартале все четыре условия выполняли 3 из 15
компонентов tier 1. Они составляют ядро операционной готовности: могут ли люди, которые не строили сервис,
безопасно его эксплуатировать. Подробно:
[глава 24](parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#operational-readiness).

### SLI, SLO и SLA { #sli-slo-and-sla }

Индикатор уровня сервиса (service level indicator, SLI) — точно определённая мера какого-то аспекта
сервиса, например доля успешных попыток оплаты. Целевой уровень сервиса (service level objective, SLO) —
цель для SLI, которой владеют разработка и продукт. Соглашение об уровне сервиса (service level
agreement, SLA) — договор, который привязывает к невыполнению обязательства последствия, например
сервисные кредиты. SLA Northstar обещает доступность 99,9% за квартал на путях заказа и оплаты — это
около 2,2 часа допустимого простоя за 90 дней. Подробно:
[глава 24](parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#sli-slo-sla).

### Бюджет ошибок и скорость его расходования (error budget and burn rate) { #error-budget-and-burn-rate }

Бюджет ошибок (error budget) — ненадёжность, которую SLO допускает за своё окно (100 процентов минус
цель). Политика бюджета ошибок, согласованная заранее, говорит, что происходит, когда бюджет исчерпан,
например приостанавливаются релизы новой функциональности. Скорость расходования (burn rate) показывает,
как быстро тратится бюджет; при скорости 1 бюджет расходуется ровно за окно. Подробно:
[глава 24](parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#error-budgets-as-a-decision-mechanism)
и [глава 24](parts/05-engineering-quality/24-reliability-slos-and-operational-readiness.md#alerting-on-the-budget).

### Координатор инцидента (incident commander) { #incident-commander }

Человек, который координирует инцидент: держит общую картину, распределяет работу и принимает решения,
но не занимается отладкой. Другие роли отвечают за операции (изменения в системе), коммуникацию и
планирование. Подробно:
[глава 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#roles-separate-coordinating-from-fixing).

### Безобвинительный разбор (blameless review) { #blameless-review }

Разбор после инцидента (его также называют постмортемом), который ищет сопутствующие факторы, не обвиняя
человека или команду, чтобы люди и дальше рассказывали, что произошло на самом деле. Книга предпочитает
несколько сопутствующих факторов одной «первопричине», на которой поиск останавливается на последнем шаге
перед сбоем. Подробно:
[глава 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#blameless-review-and-its-critics).

### Повторный инцидент (recurrence) { #recurrence }

Инцидент с видом отказа, который уже встречался раньше. В базовом квартале у Northstar было
11 повторных среди 30 инцидентов Sev1 и Sev2, а закрыто было 32 процента корректирующих действий
(задач по итогам разборов). Смотрите на закрытие вместе с повторяемостью, потому что тривиальные действия
раздувают долю закрытых. Подробно:
[глава 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#follow-up-actions-and-recurrence).

### Точка предотвращения (prevention point) { #prevention-point }

Самый ранний шаг, на котором разумный и доступный по цене контроль остановил бы неудачное изменение или
ограничил бы его последствия: доведение до конца ранее принятого решения по разбору, тест или контракт,
контроль выкатки либо обнаружение и восстановление. Такая классификация сбоев показывает, куда вкладывать.
Подробно:
[глава 25](parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md#classifying-change-failures-to-find-the-prevention-point).

### Доля инцидентов, обнаруженных клиентами (customer-detected share) { #customer-detected-share }

Доля инцидентов, о которых первым сообщил клиент, а не мониторинг. Главы считают её по инцидентам Sev1 и
Sev2 (47 процентов в базовом квартале, 14 из 30); [шаблон карты показателей качества](templates/engineering-quality-scorecard.md)
считает её по Sev1–Sev3. Всегда уточняйте, по каким. Единица: проценты. Подробно:
[глава 19](parts/05-engineering-quality/19-defining-measuring-and-owning-quality.md#choosing-measures-and-how-each-misleads).

## Безопасность, риски и соответствие требованиям { #security-risk-and-compliance }

### NIST CSF { #nist-csf }

NIST Cybersecurity Framework 2.0, который организует результаты в области безопасности по шести функциям:
Govern, Identify, Protect, Detect, Respond и Recover (управлять, выявлять, защищать, обнаруживать,
реагировать, восстанавливать). Используйте его для анализа разрывов, отталкиваясь от собственных систем, а
не как чек-лист, на который отвечают строка за строкой. Подробно:
[глава 26](parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#frameworks-as-maps-not-checklists).

### SSDF { #ssdf }

Secure Software Development Framework (NIST SP 800-218): практики безопасной разработки в четырёх
группах (подготовить организацию, защитить ПО, производить хорошо защищённое ПО, реагировать на
уязвимости), которые встраиваются в существующий жизненный цикл. Подробно:
[глава 26](parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#frameworks-as-maps-not-checklists).

### SLSA { #slsa }

Supply-chain Levels for Software Artifacts: стандарт с уровнями на двух треках, Build и Source, которые
описывают, насколько вы можете доказать, какой проверенный исходный код и какая сборка породили
работающий артефакт. Подробно:
[глава 26](parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#supply-chain-integrity-with-slsa).

### SBOM { #sbom }

Software bill of materials, перечень компонентов ПО: машиночитаемый список компонентов продукта, их
версий и связей между ними. Сгенерированный при сборке, он за минуты отвечает на вопрос «затрагивает ли
нас эта уязвимость?». Подробно:
[глава 26](parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#software-bills-of-materials).

### Активно эксплуатируемая уязвимость (KEV) { #known-exploited-vulnerability-kev }

Уязвимость, о которой известно, что её используют злоумышленники, — из каталога Known Exploited
Vulnerabilities агентства CISA. Предлагаемый книгой срок устранения таких уязвимостей — 7 дней, и он
важнее одних лишь оценок серьёзности. Подробно:
[глава 26](parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md#dependencies-and-remediation).

### Реестр рисков (risk register) { #risk-register }

Список рисков, каждый из которых сформулирован как причина, событие и последствие, с владельцем, тем, кто
принимает риск, оценкой, способом обработки, ранним индикатором и датой пересмотра. Инженерный реестр
охватывает то, что может исправить одна организация; корпоративный реестр формулирует риски как
последствия для бизнеса и питает реестр компании. Подробно:
[глава 30](parts/06-technical-leadership/30-technical-strategy-and-technology-selection.md#the-technology-risk-register)
и [глава 53](parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md#what-an-enterprise-technology-risk-register-is).

### Риск-аппетит (risk appetite) { #risk-appetite }

Формулировка того, какие виды и объёмы риска компания готова нести ради своих целей. Риск можно снизить,
передать, избежать или принять; принятие должно быть явным, сделанным тем, у кого есть полномочия, и на
оговорённый срок. Подробно:
[глава 53](parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md#treatment-decisions-and-who-may-make-them).

### SOC 2 { #soc-2 }

Проверка независимым лицензированным аудитором тех контролей компании, которые относятся к безопасности,
доступности, целостности обработки, конфиденциальности или приватности. Крупные клиенты часто требуют
такой отчёт в контрактах. Подробно:
[глава 53](parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md#regulation-and-contracts-through-engineering-controls).

### Комитет по аудиту (audit committee) { #audit-committee }

Комитет совета директоров, который надзирает за финансовой отчётностью и рисками, включая
технологические риски и риски безопасности там, где нет технологического комитета. Подробно:
[глава 53](parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md#what-an-enterprise-technology-risk-register-is)
и [глава 55](parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md#what-a-board-does-with-technology).

## Люди и карьера { #people-and-careers }

### Встреча через уровень (skip-level) { #skip-level }

Разговор руководителя руководителя с людьми на два уровня ниже. Правило книги: темы возвращаются к
непосредственному руководителю, цитаты — никогда, так что встреча через уровень проверяет систему, не
превращаясь в обходной канал. Подробно:
[глава 40](parts/09-engineering-directorship/40-the-directors-job.md#building-your-own-signal-sources).

### Структурированное интервью (structured interview) { #structured-interview }

Интервью, в котором каждый кандидат получает вопросы, относящиеся к работе, а каждый ответ оценивается по
письменным критериям до любого обсуждения. Рабочее задание (work sample), в котором кандидат под
наблюдением выполняет часть настоящей работы, — частый элемент структурированного цикла интервью.
Подробно:
[глава 7](parts/02-people-management/07-hiring-and-structured-interviews.md#what-structure-means).

### Карьерная лестница (career ladder) { #career-ladder }

Документ (его также называют матрицей грейдов, leveling guide), который для каждого уровня описывает
ожидаемые масштаб и влияние и поведение, которое к ним ведёт. Он нужен инженеру, руководителю, который
даёт обратную связь, комитету по повышениям и тому, кто задаёт вилки оплаты. Подробно:
[глава 8](parts/02-people-management/08-career-development-promotion-and-compensation.md#what-a-ladder-is-for).

### Калибровка (calibration) { #calibration }

Два значения. В карьере — встреча, на которой руководители вместе рассматривают заявки на повышение по
одним и тем же критериям, чтобы уровень означал одно и то же в каждой команде (глава 8). В
прогнозировании — свойство, при котором команда, говорящая «уверены на 85 процентов», оказывается права
примерно в 85 процентах случаев (глава 17). Подробно:
[глава 8](parts/02-people-management/08-career-development-promotion-and-compensation.md#calibration-what-it-fixes-and-what-it-breaks).

### «Пока нет» (not yet) { #not-yet }

Термин книги для отклонённой заявки на повышение, поданной как план: сначала решение, затем разрыв,
привязанный к карьерной лестнице, и то, что изменило бы ответ. Подробно:
[глава 8](parts/02-people-management/08-career-development-promotion-and-compensation.md#a-not-yet-that-can-be-used).

### План улучшения результативности (PIP) { #performance-improvement-plan-pip }

Формальный, ограниченный по времени процесс с письменными ожиданиями и поддержкой для человека, который не
соответствует планке. Многие организации воспринимают его как первый шаг к увольнению, что сводит на нет
его смысл. Подробно:
[глава 9](parts/02-people-management/09-performance-management-and-underperformance.md#the-improvement-process).

### Интервью об удержании (stay interview) { #stay-interview }

Структурированный разговор с человеком, которого вы хотите удержать: что держит вас здесь, что заставило
бы уйти и что одно вы бы изменили. Подробно:
[глава 10](parts/02-people-management/10-motivation-retention-and-senior-engineers.md#exit-data-stay-data-and-system-data).

### Психологическая безопасность (psychological safety) { #psychological-safety }

То, как люди воспринимают последствия межличностного риска на работе, например признания ошибки или
слов о том, что дата нереальна. Это не отсутствие стандартов: высокоэффективные команды сочетают её с
высокой подотчётностью. Подробно:
[глава 11](parts/03-high-performing-teams/11-high-performance-trust-safety-and-accountability.md#what-psychological-safety-is).

### Staff-plus-инженер (staff-plus engineer) { #staff-plus-engineer }

Старший индивидуальный исполнитель (staff, principal или выше), чья работа — техническое лидерство за
пределами собственных задач. Распространённые архетипы — техлид, архитектор, решатель проблем (solver) и
правая рука, у каждого свой масштаб и свой типичный провал. Подробно:
[глава 29](parts/06-technical-leadership/29-staff-and-principal-engineers.md#archetypes)
и [глава 1](parts/01-foundations/01-what-engineering-management-is.md#where-staff-plus-engineers-sit).

### Единая точка отказа по знаниям (single point of knowledge failure) { #single-point-of-knowledge-failure }

Область работы команды, которую безопасно может выполнять только один человек. Bus factor (или truck
factor) — наименьшее число людей, внезапное отсутствие которых поставит проект в серьёзное положение.
Подробно:
[глава 12](parts/03-high-performing-teams/12-team-charters-working-agreements-and-knowledge-sharing.md#single-points-of-knowledge-failure).

### Покрытие преемниками (succession coverage) { #succession-coverage }

Есть ли у каждой критической роли человек, который мог бы её принять. Готовность бывает такой: готов
сейчас, готов после развития, только временно или никто; покрытие достаточно, если у роли есть человек,
готовый сейчас, или временная замена плюс кто-то в развитии, и при этом замещающий не занимает другую
критическую роль. Подробно:
[глава 36](parts/07-organization-design/36-reorganizations-evolution-and-succession.md#succession-coverage).

## Организационный дизайн { #organization-design }

### Охват управления (span of control) { #span-of-control }

Число людей, которые подчиняются одному руководителю напрямую. Универсально правильного числа нет: оно
зависит от того, сколько каждому подчинённому нужно от руководителя. Подробно:
[глава 34](parts/07-organization-design/34-spans-layers-and-dependency-mapping.md#why-there-is-no-universal-span).

### Уровень управления (layer) { #layer }

Уровень управления между инженером и человеком, который может принимать решения за всю организацию.
Каждый добавленный уровень стоит задержки решений и потери информации по пути наверх. Подробно:
[глава 34](parts/07-organization-design/34-spans-layers-and-dependency-mapping.md#what-a-layer-costs).

### Закон Конвея и обратный манёвр Конвея (Conway's law and the reverse Conway maneuver) { #conways-law-and-the-reverse-conway-maneuver }

Закон Конвея: организации производят архитектуры систем, копирующие их коммуникационные структуры.
Обратный манёвр Конвея проектирует ту организацию, которую должна скопировать желаемая система; его логика
здрава, доказательства слабы. Подробно:
[глава 33](parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md#what-conway-argued-and-the-evidence-since)
и [глава 33](parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md#the-reverse-conway-maneuver-and-its-evidence-gap).

### Типы команд и режимы взаимодействия (team types and interaction modes) { #team-types-and-interaction-modes }

Словарь *Team Topologies*: потоковые (stream-aligned), платформенные, команды содействия (enabling) и
команды сложной подсистемы (complicated-subsystem), взаимодействующие через сотрудничество (на
определённый срок), «X как сервис» или фасилитацию. Это таксономия, а не проверенная модель. Подробно:
[глава 33](parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md#team-types-and-interaction-modes-as-vocabulary).

### Когнитивная нагрузка (cognitive load) { #cognitive-load }

Умственное усилие, которого требует задача. Применительно к командам: обязанности команды должны
соответствовать нагрузке, которую она способна нести. Подробно:
[глава 33](parts/07-organization-design/33-conways-law-team-topologies-and-cognitive-load.md#cognitive-load-origin-and-transfer).

### Хартия команды и рабочее соглашение (team charter and working agreement) { #team-charter-and-working-agreement }

Хартия команды описывает её назначение, границы, интерфейсы и права на решения. Рабочее соглашение — набор
правил, которые команда сама себе устанавливает и соблюдает, например сроки ревью или обмен дежурствами.
Подробно:
[глава 12](parts/03-high-performing-teams/12-team-charters-working-agreements-and-knowledge-sharing.md#what-a-team-charter-is-and-what-the-evidence-says).

### Права на решения (decision rights) { #decision-rights }

Кто может принимать какие решения, каким методом и с какой записью. Книга называет четыре метода: решить
единолично, посоветоваться, согласие и делегировать; ролевые модели вроде RACI (Responsible, Accountable,
Consulted, Informed — исполняет, отвечает, консультирует, информируется) распределяют их по каждому
решению. Подробно:
[глава 13](parts/03-high-performing-teams/13-decision-making-in-teams.md#four-methods-defined)
и [глава 13](parts/03-high-performing-teams/13-decision-making-in-teams.md#decision-rights-made-explicit).

### Стоимость перехода (transition cost) { #transition-cost }

Ресурс, теряемый, пока люди после реорганизации заново выстраивают контекст, отношения, графики дежурств
и ритм планирования. Оцените её до принятия решения. Единица: инженеро-недели. Подробно:
[глава 36](parts/07-organization-design/36-reorganizations-evolution-and-succession.md#pricing-the-transition).

## Стратегия и управление { #strategy-and-governance }

### Запись архитектурного решения (ADR) { #architecture-decision-record-adr }

Короткий документ, фиксирующий одно значимое техническое решение: его контекст, варианты, выбор и
причины, чтобы преемники не принимали и не отменяли его вслепую. Подробно:
[глава 28](parts/06-technical-leadership/28-architecture-decision-making-and-governance.md#architecture-decision-records).

### Журнал решений (decision log) { #decision-log }

Запись решений организации, которые не принадлежат ни одному репозиторию кода (владение, распределение
ресурсов, определения серьёзности), — каждое с тем, кто решает, вариантами, статусом, датой «нужно к» и
условием пересмотра. Записи Northstar нумеруются начиная с DL-01. Подробно:
[глава 39](parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md#the-decision-log).

### Путь эскалации (escalation path) { #escalation-path }

Маршрут, по которому разногласие передаётся тому, у кого есть полномочия над обеими сторонами. Чистая
эскалация совместна (одно письменное обоснование от обеих сторон), идёт к ближайшему общему руководителю,
ограничена по времени и заканчивается в журнале решений. Вызов более опытного специалиста по инцидентам —
другой механизм. Подробно:
[глава 39](parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md#escalation-paths).

### Операционный разбор и операционное ревью (operational review and operating review) { #operational-review-and-operating-review }

Две разные встречи. Операционный разбор (operational review) — еженедельная встреча директора об
инцидентах, задачах по итогам разборов, бюджетах ошибок и прогнозах с датами (главы 37 и 39).
Операционное ревью (operating review) — ежемесячная встреча VP с каждым директором о карте показателей
его направления, профинансированных ставках и укомплектованности (глава 47). Подробно:
[глава 37](parts/08-management-operating-system/37-cadences-and-leadership-meetings.md#what-the-system-is-made-of)
и [глава 47](parts/11-vp-engineering/47-the-vp-of-engineering.md#the-operating-review).

### Карта показателей (scorecard) { #scorecard }

Короткий набор показателей, который пересматривается в фиксированном ритме и охватывает несколько
областей (результаты, качество, поставка, обязательства и инвестиции, люди), потому что одна из них может
улучшаться, пока организация становится хуже. Каждый показатель стоит в паре с другим, который выявляет
подгонку. Подробно:
[глава 38](parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#the-organization-scorecard).

### OKR { #okr }

Objectives and key results, цели и ключевые результаты: качественная цель в паре с несколькими
измеримыми результатами, которые показали бы, что она достигнута. Подробно:
[глава 38](parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md#what-the-research-says-about-goals-and-about-okrs).

### Горизонты (horizons) { #horizons }

Три вида ставок: горизонт 1 улучшает существующий бизнес, горизонт 2 расширяет его на новых клиентов или
рынки, горизонт 3 создаёт опционы на будущее. Книга рассматривает их как виды ставок, а не как окна
поставки. Подробно:
[глава 51](parts/12-cto-leadership/51-enterprise-technology-strategy.md#horizons-as-kinds-of-bet-not-as-years).

### Ограничение (constraint) { #constraint }

Единственный шаг, который ограничивает выход системы; улучшение чего-либо другого выход не повышает.
Находите его по данным об инцидентах, пропущенных дефектах и пайплайне, а не по мнениям. Подробно:
[глава 3](parts/01-foundations/03-managerial-leverage-and-systems-thinking.md#constraints)
и [глава 27](parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md#finding-the-constraint).

### Ловушка возможностей (capability trap) { #capability-trap }

Петля, в которой давление заставляет людей урезать время на улучшения, возможности деградируют,
результаты падают, а давление растёт ещё сильнее. Подробно:
[глава 3](parts/01-foundations/03-managerial-leverage-and-systems-thinking.md#the-capability-trap).

## Доказательства и исследования { #evidence-and-research }

### Метки доказательности (evidence labels) { #evidence-labels }

Слова, которыми книга говорит, насколько сильна опора утверждения: научный результат, отраслевое
исследование, стандарт, задокументированная практика, консенсус практиков, мнение эксперта, рекомендация
книги и иллюстрация. Большинство отраслевых исследований корреляционные: они показывают, что две вещи
меняются вместе, но не что одна вызывает другую. Объяснено на странице
[«Метки доказательности»](references/evidence-labels.md).

### Метаанализ (meta-analysis) { #meta-analysis }

Исследование, которое объединяет результаты многих исследований по одному вопросу, обычно с поправкой на
известные искажения, чтобы оценить средний эффект. Оно хорошо ровно настолько, насколько хороши
объединённые исследования и охваченные ими условия. Подробно:
[глава 7](parts/02-people-management/07-hiring-and-structured-interviews.md#what-selection-research-measures).

### Размер эффекта (d, g) (effect size) { #effect-size-d-g }

Число, показывающее, насколько велика разница, измеренная в единицах разброса результата, а не в исходных
единицах, — так можно сравнивать исследования с разными шкалами. d Коэна и g Хеджеса — две
распространённые формы; глава 6 приводит средний эффект обратной связи как d = 0,41 и называет его
умеренным. Подробно:
[глава 6](parts/02-people-management/06-feedback-conflict-and-difficult-conversations.md#what-the-feedback-research-shows).

### Коэффициент валидности (validity coefficient) { #validity-coefficient }

В исследованиях найма — корреляция между оценками по методу отбора и последующей результативностью в
работе: 0 означает отсутствие предсказательной силы, 1 — идеальное предсказание. Это среднее по
исследованиям, а не валидность вашего собственного цикла интервью. Подробно:
[глава 7](parts/02-people-management/07-hiring-and-structured-interviews.md#what-selection-research-measures).

### Подгонка метрик: закон Кэмпбелла, закон Гудхарта (metric gaming) { #metric-gaming-campbells-law-goodharts-law }

Чем больше показатель используется для решений о людях, тем сильнее давление искажает и само число, и
деятельность, которую оно должно было отслеживать; популярную версию, «когда мера становится целью»,
называют законом Гудхарта. Книга сопровождает каждую метрику описанием того, как её подгоняют, и вторым
показателем, который это выявляет. Подробно:
[глава 18](parts/04-execution/18-measuring-engineering-productivity.md#how-each-metric-is-gamed-and-its-pair).

## Сокращения Northstar { #northstar-shorthand }

### Northstar Technologies { #northstar-technologies }

Сквозной вымышленный кейс книги: софтверная компания в сфере order-to-cash примерно из 620 человек,
80 инженеров в шести командах, $140 млн ARR и договор о доступности 99,9%. Описана в
[обзоре Northstar](case-studies/northstar/index.md).

### Halvard Systems { #halvard-systems }

Вторая вымышленная компания книги, примерно с 500 инженерами и несколькими вице-президентами; появляется
там, где Northstar слишком мала, чтобы показать проблему. Описана на
[странице Halvard](case-studies/northstar/halvard.md).

### Мандат (the mandate) { #the-mandate }

Задание CTO новому директору в одном предложении: за двенадцать месяцев вдвое сократить число инцидентов
Sev1 и Sev2 и выполнить обязательство 99,9%, без чистого роста численности и не сорвав два обязательства
по продлению. Описан в
[обзоре Northstar](case-studies/northstar/index.md#the-situation-when-you-arrive).

### Пять ограничений (the five constraints) { #the-five-constraints }

Правила, которые действуют на протяжении всего кейса: (1) численность остаётся на уровне 80 инженеров;
(2) два обязательства по продлению сохраняют свои даты; (3) никакого профинансированного переписывания
Core; (4) $250 000 на инструменты по своему усмотрению без бизнес-кейса; (5) любой план, меняющий работу
QA-инженеров, говорит, чем они займутся дальше. «Ограничение 3» означает третье. Описаны в
[обзоре Northstar](case-studies/northstar/index.md#constraints-that-hold-throughout-the-book).

### Обязательства по продлению (renewal commitments) { #renewal-commitments }

Два обязательства перед клиентами, от которых зависят крупнейшие продления: функция массового заказа и
интеграция с бухгалтерской системой; обе нужно выполнить в первые два квартала (недели 19 и 26). Описаны в
[обзоре Northstar](case-studies/northstar/index.md#constraints-that-hold-throughout-the-book).

### Core { #core }

Java-монолит Northstar: около 1,4 млн строк в восьми крупных модулях, три из которых (customer,
permissions, scheduler) в базовом квартале меняли четыре команды и не владела ни одна. Он выпускается
релизным поездом; остальные четырнадцать сервисов развёртываются независимо. Описан в
[обзоре Northstar](case-studies/northstar/index.md#the-system).

### Недели, кварталы и годы (weeks, quarters, and years) { #weeks-quarters-and-years }

Неделя 1 — первая неделя директора. Квартал 1 («квартал трансформации») — недели 1–13, квартал 2 —
недели 14–26, квартал 3 — недели 27–39, квартал 4 — недели 40–52. «Базовый квартал» — квартал до прихода
директора. Год 2 — недели 53–104 (кварталы 5–8); финансовый год 1 (FY1) совпадает с неделями 1–52.
Квартал 3 — последний измеренный квартал; решения четвёртого квартала открыты. Описано на
[странице о первом годе](case-studies/northstar/first-quarter.md).

### Номера INC (INC numbers) { #inc-numbers }

Идентификаторы инцидентов Northstar. INC-401 – INC-430 — это 30 инцидентов Sev1 и Sev2 базового квартала,
перечисленные в [файле инцидентов](case-studies/northstar/data/incidents-last-quarter.csv); главы
называют каждый несколькими словами о том, что произошло.

### ADR-0001 { #adr-0001 }

Первая запись архитектурного решения в Northstar, открытая Li Na Zhou (staff-инженер, данные и интеграции)
в неделю 14: как интеграциям читать проведённые данные главной книги — напрямую из таблиц, через
версионированный контракт экспорта или из событий проводок. К неделе 26 вопрос всё ещё был открыт.
Описано на [странице о первом годе](case-studies/northstar/first-quarter.md); формат ADR разобран в
[главе 28](parts/06-technical-leadership/28-architecture-decision-making-and-governance.md#architecture-decision-records).

### Продолжение (the continuation) { #the-continuation }

Двухлетнее предложение директора, подготовленное в неделю 45, о продолжении программы качества после
первого года: этап 2 «Удержание» (Hold; кварталы 5 и 6, 6 FTE на профилактику, $150 000 на инструменты,
контрольная точка в неделю 78) и этап 3 «Сближение» (Converge; кварталы 7 и 8, 5 FTE, $100 000 на инструменты,
только если выбрана цель для CI, контрольная точка в неделю 104) — после контрольной точки этапа 1 в
неделю 56, без запроса на рост численности. Каждый этап заканчивается контрольной точкой, где письменные
критерии выхода решают, финансируется ли следующий. Подробно:
[глава 49](parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md#stages-gates-and-exit-criteria).
