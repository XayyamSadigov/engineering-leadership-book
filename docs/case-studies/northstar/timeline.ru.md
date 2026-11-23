# Хронология { #timeline }

!!! warning "Вымысел"
    Всё на этой странице придумано для книги. См. примечание в
    [обзоре Northstar](index.md).

Эта страница показывает первый год директора по разработке в Northstar целиком: что произошло на каждой
неделе, где лежит полная запись и какая глава об этом рассказывает. Вторая таблица даёт главные результаты
по кварталам. Недели отсчитываются от первого дня директора. Каждый квартал длится 13 недель: квартал 1 —
недели 1–13, квартал 2 — недели 14–26, квартал 3 — недели 27–39, квартал 4 — недели 40–52. Люди
перечислены на странице [«Действующие лица»](cast.md). Тот же год, рассказанный как история, — на
странице [«Год вкратце»](year-in-brief.md).

## По неделям { #week-by-week }

Столбец «Запись» ведёт к разделу [хроники года 1](first-quarter.md) или другой
страницы, где хранятся подробности.

### Квартал 1: владение, серьёзность и релизный поезд { #quarter-1-ownership-severity-and-the-release-train }

| Неделя | Событие | Запись | Глава |
|---|---|---|---|
| До недели 1 | Базовый квартал: 30 инцидентов Sev1 и Sev2, доступность 99.62%, $410,000 сервисных кредитов, 34% незапланированной работы | [исходные данные](baseline-data.md) | [19](../../parts/05-engineering-quality/19-defining-measuring-and-owning-quality.md), [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md) |
| 1 | Вы приходите директором по разработке. Мандат CTO: за двенадцать месяцев вдвое сократить инциденты Sev1 и Sev2 и выйти на 99.9%, без роста численности и с выполнением обоих обязательств по продлению | [обзор](index.md#the-situation-when-you-arrive) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md) |
| 2 | Классификация инцидентов вместе с Kwame Mensah; разовое сканирование безопасности всех 24 компонентов; Priya Raman ограничивает свою практическую работу 8 часами в неделю и делегирует | [квартал 1](first-quarter.md#timeline-of-quarter-1) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md), [26](../../parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md), [2](../../parts/01-foundations/02-from-individual-contributor-to-leader.md) |
| 3 | Опубликованы определения серьёзности; пересмотрена страница стандартов (39 из 52 правил ненаблюдаемы); приходит опросник по безопасности от клиента с продлением | [квартал 1](first-quarter.md#timeline-of-quarter-1) | [25](../../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md), [20](../../parts/05-engineering-quality/20-engineering-standards-and-their-governance.md), [26](../../parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md) |
| 4 | Модель ресурсов согласована с Victor Lindqvist и Amara Okafor; первые 40 нестабильных тестов отправлены в карантин; у core/customer и core/scheduler появляются владельцы | [квартал 1](first-quarter.md#timeline-of-quarter-1), [решения](first-quarter.md#decisions-that-hold-for-the-rest-of-the-book) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md), [23](../../parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md), [21](../../parts/05-engineering-quality/21-technical-debt.md) |
| 4–5 | Обучены 12 координаторов инцидентов | [решения](first-quarter.md#decisions-that-hold-for-the-rest-of-the-book) | [25](../../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md) |
| 5 | Первый еженедельный релиз Core | [квартал 1](first-quarter.md#timeline-of-quarter-1) | [23](../../parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md) |
| 6 | Изменения флагов payments-gateway переходят на проверенные и валидируемые merge request'ы | [квартал 1](first-quarter.md#timeline-of-quarter-1) | [23](../../parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md) |
| 7 | Двухчасовая задержка платежей, оценённая как Sev3, переоценена; аудит серьёзности включён в еженедельный разбор. Подходит срок обещанной проверки миграций, и она срывается | [квартал 1](first-quarter.md#timeline-of-quarter-1), [решения](first-quarter.md#decisions-that-hold-for-the-rest-of-the-book) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md), [25](../../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md) |
| 8 | Контрактный тест ловит изменение округления в payments-gateway; выясняется, что 2 из 7 закрытий уязвимостей с пометкой «не затронуто» не анализировались | [квартал 1](first-quarter.md#timeline-of-quarter-1) | [22](../../parts/05-engineering-quality/22-testing-strategy-and-test-architecture.md), [26](../../parts/05-engineering-quality/26-security-and-software-supply-chain-quality.md) |
| 9 | Sev1 в Billing: кредит-ноты применены дважды, откат не срабатывает; временное правило для миграций ledger | [квартал 1](first-quarter.md#timeline-of-quarter-1) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md), [23](../../parts/05-engineering-quality/23-code-review-ci-cd-and-release-engineering.md), [25](../../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md) |
| 10 | Объявлен переход QA: семь QA-инженеров переходят в продуктовые команды инженерами по качеству; репетиция миграций обязательна для данных tier 1 | [квартал 1](first-quarter.md#timeline-of-quarter-1), [решения](first-quarter.md#decisions-that-hold-for-the-rest-of-the-book) | [19](../../parts/05-engineering-quality/19-defining-measuring-and-owning-quality.md), [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md), [22](../../parts/05-engineering-quality/22-testing-strategy-and-test-architecture.md) |
| 11 | В пайплайне появляется проверка незавершённых миграций | [квартал 1](first-quarter.md#timeline-of-quarter-1) | [25](../../parts/05-engineering-quality/25-incidents-postmortems-and-change-failure-analysis.md) |
| 13 | День 90: Sev1 и Sev2 — с 30 до 21; оба обязательства по продлению идут по плану | [день 90](first-quarter.md#day-90) | [27](../../parts/05-engineering-quality/27-quality-transformation-at-enterprise-scale.md) |

### Квартал 2: продления и операционная система { #quarter-2-the-renewals-and-the-operating-system }

| Неделя | Событие | Запись | Глава |
|---|---|---|---|
| 14 | Li Na Zhou открывает ADR-0001 (как интеграции читают данные ledger); заведён журнал решений организации; интервью об удержании с Ines Carvalho; начинается еженедельная синхронизация Billing и Orders | [отправные точки](first-quarter.md#starting-points-for-quarter-2), [квартал 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2) | [28](../../parts/06-technical-leadership/28-architecture-decision-making-and-governance.md), [39](../../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md), [10](../../parts/02-people-management/10-motivation-retention-and-senior-engineers.md), [37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md) |
| 14–15 | Интервью об удержании с тремя инженерами ledger; время, которое директор проводит с информацией из первых рук, измерено: 4.7% | [отправные точки](first-quarter.md#starting-points-for-quarter-2), [квартал 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2) | [10](../../parts/02-people-management/10-motivation-retention-and-senior-engineers.md), [40](../../parts/09-engineering-directorship/40-the-directors-job.md) |
| 14–19 | Разбор встреч один на один Daniel Cho (проведено 84 из 90, 55 в основном о статусе) | [отправные точки](first-quarter.md#starting-points-for-quarter-2) | [5](../../parts/02-people-management/05-one-on-ones-coaching-and-mentorship.md) |
| 15 | Опубликован путь эскалации | [квартал 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2) | [39](../../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md) |
| 16 | Первые индивидуальные встречи через уровень; проверка здоровья команды Customer Experience; практическая работа Priya Raman — 8 часов | [квартал 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2), [отправные точки](first-quarter.md#starting-points-for-quarter-2) | [37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md), [14](../../parts/03-high-performing-teams/14-distributed-teams-team-health-and-dysfunction.md), [41](../../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md) |
| 17 | Mateo Arango Ríos говорит директору, что больше года выполняет работу лида | [отправные точки](first-quarter.md#starting-points-for-quarter-2) | [5](../../parts/02-people-management/05-one-on-ones-coaching-and-mentorship.md), [14](../../parts/03-high-performing-teams/14-distributed-teams-team-health-and-dysfunction.md) |
| 18 | Повторный замер потока: ожидание окружений сокращается примерно с 6 дней до 2 | [отправные точки](first-quarter.md#starting-points-for-quarter-2) | [16](../../parts/04-execution/16-flow-lead-time-dependencies-and-unplanned-work.md) |
| 19 | Интеграция с бухгалтерской системой запущена для клиента с продлением | [квартал 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2) | [39](../../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md) |
| 20 | Tomasz Wierzbicki сообщает о внешнем предложении на 20% выше базового оклада; первая контрольная точка плана коучинга Ines Carvalho; Priya — 10 часов | [отправные точки](first-quarter.md#starting-points-for-quarter-2), [квартал 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2) | [10](../../parts/02-people-management/10-motivation-retention-and-senior-engineers.md), [29](../../parts/06-technical-leadership/29-staff-and-principal-engineers.md), [41](../../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md) |
| 22 | Ожидания к руководителям, записанные на одной странице; набросан новый календарь встреч | [квартал 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2), [инвентаризация правил](first-quarter.md#rules-and-processes-inventory) | [41](../../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md), [37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md) |
| 24 | Черновые оценки шести руководителей; новый календарь пересмотрен; Priya — 12 часов | [квартал 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2), [инвентаризация правил](first-quarter.md#rules-and-processes-inventory) | [41](../../parts/09-engineering-directorship/41-managing-and-developing-engineering-managers.md), [37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md) |
| 26 | Массовый заказ готов, выпуск прогнозируется к концу недели; первый письменный отчёт Victor после дня 90; вторая контрольная точка коучинга Ines | [квартал 2](first-quarter.md#the-renewals-and-the-operating-system-in-quarter-2), [отправные точки](first-quarter.md#starting-points-for-quarter-2) | [39](../../parts/08-management-operating-system/39-reviews-decision-logs-escalation-and-executive-reporting.md), [29](../../parts/06-technical-leadership/29-staff-and-principal-engineers.md) |

### Квартал 3: ресурсы, портфель и первый квартал на целевом уровне { #quarter-3-capacity-portfolio-and-the-first-quarter-at-target }

| Неделя | Событие | Запись | Глава |
|---|---|---|---|
| 27 (начало квартала 3) | Первый калиброванный цикл повышений (9 номинированы, 5 повышены); предложена перестройка операционной системы; запущен Engineering Excellence Day; резерв на поддержку массового заказа на недели 27–30 | [отправные точки](first-quarter.md#starting-points-for-quarter-2), [план квартала 3](first-quarter.md#the-quarter-3-plan) | [8](../../parts/02-people-management/08-career-development-promotion-and-compensation.md), [37](../../parts/08-management-operating-system/37-cadences-and-leadership-meetings.md), [43](../../parts/09-engineering-directorship/43-leading-change-and-director-failure-patterns.md), [38](../../parts/08-management-operating-system/38-scorecards-quarterly-planning-and-capacity-allocation.md) |
| 28, 32, 36 | Engineering Excellence Days, участвуют 64, 41 и 23 инженера | [план квартала 3](first-quarter.md#the-quarter-3-plan) | [43](../../parts/09-engineering-directorship/43-leading-change-and-director-failure-patterns.md) |
| 31 | Greg Tanaka просит третью функцию для сделки — правила согласования закупок | [план квартала 3](first-quarter.md#the-quarter-3-plan) | [42](../../parts/09-engineering-directorship/42-cross-functional-dependencies-portfolio-and-influence.md) |
| Около 33 | Должна начаться автоматическая выдача выписок по сервисным кредитам | [план квартала 3](first-quarter.md#the-quarter-3-plan) | [42](../../parts/09-engineering-directorship/42-cross-functional-dependencies-portfolio-and-influence.md) |
| 34 | Портфельный форум по третьей функции для сделки (итог не записан) | [план квартала 3](first-quarter.md#the-quarter-3-plan) | [42](../../parts/09-engineering-directorship/42-cross-functional-dependencies-portfolio-and-influence.md) |
| 37 | Engineering Excellence Day прекращён | [план квартала 3](first-quarter.md#the-quarter-3-plan) | [43](../../parts/09-engineering-directorship/43-leading-change-and-director-failure-patterns.md) |
| 39 | Истекает исключение для core/permissions; Orders оценивает даты вступления прайс-листов в силу в 14 инженеро-недель, после чего Greg Tanaka называет клиенту неделю 46 | [итоги квартала 3](first-quarter.md#quarter-3-results), [квартал 4](first-quarter.md#calendar-of-quarter-4) | [13](../../parts/03-high-performing-teams/13-decision-making-in-teams.md), [44](../../parts/10-business-leadership/44-working-with-product.md) |

### Квартал 4: черновики, позиции и открытые решения { #quarter-4-drafts-positions-and-open-decisions }

У событий четвёртого квартала нет записанных итогов. См. [брифинг по итогам четвёртого
квартала](quarter-4-briefing.md).

| Неделя | Событие | Запись | Глава |
|---|---|---|---|
| 40 | Состав по уровням: 39 Engineer, 38 Senior, 3 Staff; дистрибьютор из топ-40 жалуется на исправление заказов | [итоги квартала 3](first-quarter.md#quarter-3-results), [квартал 4](first-quarter.md#calendar-of-quarter-4) | [48](../../parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md), [44](../../parts/10-business-leadership/44-working-with-product.md) |
| 40–41 | Выборка из 400 исправленных заказов находит 340 ошибок | [квартал 4](first-quarter.md#calendar-of-quarter-4) | [44](../../parts/10-business-leadership/44-working-with-product.md) |
| 41 | Victor просит страницу о разработке для плана совету директоров; Rajiv Menon просит план по персоналу; рабочий договор отправлен Amara; инвентаризация хранилища данных у Farah Haddad; клиент спрашивает об ИИ | [квартал 4](first-quarter.md#calendar-of-quarter-4), [данные и ИИ](first-quarter.md#data-and-ai-chapter-54) | [46](../../parts/10-business-leadership/46-stakeholder-management-and-negotiation.md), [48](../../parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md), [44](../../parts/10-business-leadership/44-working-with-product.md), [54](../../parts/12-cto-leadership/54-data-and-ai-strategy.md) |
| 42 | Три условия Amara; встречное предложение директора по странице для совета; опрос об использовании ИИ; потенциальный клиент требует SOC 2 | [квартал 4](first-quarter.md#calendar-of-quarter-4), [данные и ИИ](first-quarter.md#data-and-ai-chapter-54), [риски](first-quarter.md#risk-security-and-compliance-chapter-53) | [44](../../parts/10-business-leadership/44-working-with-product.md), [46](../../parts/10-business-leadership/46-stakeholder-management-and-negotiation.md), [54](../../parts/12-cto-leadership/54-data-and-ai-strategy.md), [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md) |
| 43 | Margaret Lin просит сессию по технологическим рискам; Victor просит корпоративный реестр технологических рисков | [риски](first-quarter.md#risk-security-and-compliance-chapter-53) | [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md) |
| 43–45 | Четыре руководителя просят ИИ-функции или ответы | [данные и ИИ](first-quarter.md#data-and-ai-chapter-54) | [54](../../parts/12-cto-leadership/54-data-and-ai-strategy.md) |
| 44 | Предложение по организации второго года; срез состояния безопасности; подсчитаны 34 опросника по безопасности | [предложение на второй год](first-quarter.md#the-year-2-organization-proposal-week-44), [риски](first-quarter.md#risk-security-and-compliance-chapter-53) | [35](../../parts/07-organization-design/35-designing-organizations-at-four-scales.md), [36](../../parts/07-organization-design/36-reorganizations-evolution-and-succession.md), [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md) |
| 44–46 | Замерена неделя Victor (48 часов, из них 2 на стратегию); 11 неформальных технических запросов | [работа CTO](first-quarter.md#the-ctos-job-chapter-50) | [50](../../parts/12-cto-leadership/50-what-a-cto-actually-does.md) |
| 45 | Поднят вопрос о VP of Engineering; подготовлен черновик продолжения программы качества; срок страницы о разработке для совета | [квартал 4](first-quarter.md#calendar-of-quarter-4) | [47](../../parts/11-vp-engineering/47-the-vp-of-engineering.md), [49](../../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md), [46](../../parts/10-business-leadership/46-stakeholder-management-and-negotiation.md) |
| 46 | Срок решения по организации второго года; бизнес-варианты Victor для Helena Marsh; оценка FY1 от финансов | [предложение на второй год](first-quarter.md#the-year-2-organization-proposal-week-44), [стратегия](first-quarter.md#three-year-technology-strategy-chapter-51), [финансы](first-quarter.md#finances-chapter-52) | [35](../../parts/07-organization-design/35-designing-organizations-at-four-scales.md), [51](../../parts/12-cto-leadership/51-enterprise-technology-strategy.md), [52](../../parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md) |
| 46–47 | Встречи один на один с руководителями и их позиции по продолжению | [квартал 4](first-quarter.md#calendar-of-quarter-4) | [49](../../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md) |
| 46–48 | Черновик бюджета разработки на FY2; Victor собирает опасения членов совета директоров | [финансы](first-quarter.md#finances-chapter-52), [совет директоров](first-quarter.md#board-preparation-chapter-55) | [52](../../parts/12-cto-leadership/52-technology-investment-budgeting-and-financial-literacy.md), [55](../../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md) |
| 47 | Черновик стратегии Victor и его черновик «оставить, отдать, прекратить»; реестр рисков директора, варианты по SOC 2 и позиция по ИИ; частное предложение Greg Tanaka, отклонённое | [стратегия](first-quarter.md#three-year-technology-strategy-chapter-51), [работа CTO](first-quarter.md#the-ctos-job-chapter-50), [риски](first-quarter.md#risk-security-and-compliance-chapter-53), [данные и ИИ](first-quarter.md#data-and-ai-chapter-54), [квартал 4](first-quarter.md#calendar-of-quarter-4) | [51](../../parts/12-cto-leadership/51-enterprise-technology-strategy.md), [50](../../parts/12-cto-leadership/50-what-a-cto-actually-does.md), [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md), [54](../../parts/12-cto-leadership/54-data-and-ai-strategy.md), [49](../../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md) |
| 48 | Срок рекомендации по VP; премортем стратегии; Victor пересматривает реестр рисков; черновик страницы для совета несёт два главных тезиса | [квартал 4](first-quarter.md#calendar-of-quarter-4), [стратегия](first-quarter.md#three-year-technology-strategy-chapter-51), [риски](first-quarter.md#risk-security-and-compliance-chapter-53), [совет директоров](first-quarter.md#board-preparation-chapter-55) | [47](../../parts/11-vp-engineering/47-the-vp-of-engineering.md), [51](../../parts/12-cto-leadership/51-enterprise-technology-strategy.md), [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md), [55](../../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md) |
| 49 | Встреча команды руководителей; черновик плана по персоналу; пакет для совета директоров отправлен | [квартал 4](first-quarter.md#calendar-of-quarter-4), [стратегия](first-quarter.md#three-year-technology-strategy-chapter-51), [совет директоров](first-quarter.md#board-preparation-chapter-55) | [49](../../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md), [48](../../parts/11-vp-engineering/48-capacity-strategy-workforce-planning-and-governance.md), [51](../../parts/12-cto-leadership/51-enterprise-technology-strategy.md), [55](../../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md) |
| 50 | Заседание совета директоров и сессия комитета по аудиту по технологическим рискам (итоги не записаны) | [квартал 4](first-quarter.md#calendar-of-quarter-4), [совет директоров](first-quarter.md#board-preparation-chapter-55) | [55](../../parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.md), [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md) |
| 50–51 | Подготовлен черновик инвентаризации правил и процессов | [инвентаризация правил](first-quarter.md#rules-and-processes-inventory) | [59](../../parts/13-advanced-problems/59-transformation-under-constraint-and-scaling-without-bureaucracy.md) |
| 51 | Запрошены решения по продолжению; запланировано объявление организации второго года | [квартал 4](first-quarter.md#calendar-of-quarter-4), [предложение на второй год](first-quarter.md#the-year-2-organization-proposal-week-44) | [49](../../parts/11-vp-engineering/49-multi-year-transformation-communication-and-politics.md), [36](../../parts/07-organization-design/36-reorganizations-evolution-and-succession.md) |
| 52 | Срок исключения по безопасности для auth-svc | [риски](first-quarter.md#risk-security-and-compliance-chapter-53) | [53](../../parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.md) |

## Результаты по кварталам { #results-by-quarter }

Базовый квартал — это 90-дневный квартал до прихода директора; кварталы директора длятся по 13 недель.
Квартал 3 — последний измеренный квартал: итоги четвёртого квартала не записаны, поэтому главы, действие
которых происходит в неделях 40–52, используют цифры третьего квартала. «n.r.» означает «не записано»
(not recorded).

| Показатель | Базовый | Квартал 1 | Квартал 2 | Квартал 3 |
|---|---|---|---|---|
| Инциденты Sev1 и Sev2 (мандат: 15 или меньше) | 30 | 21 | 17 | 14 |
| из них Sev1 | 7 (9 по определениям недели 3) | n.r. | 3 | 2 |
| из них через релизы Core | 9 | 4 | 2 | n.r. |
| Повторные инциденты | 11 из 30 | 5 из 21 | 3 из 17 | n.r. |
| Доля обнаруженных клиентами | 47% | 29% | 29% | n.r. |
| Доступность, договорные пути (обязательство 99.9%) | 99.62% | n.r. | 99.86% | 99.89% |
| Сервисные кредиты | $410,000 | n.r. | $95,000 | $60,000 |
| Незапланированная работа | 34% | 31% | 28% | 25% |
| Tier 1, выполняющие четыре операционных минимума | 3 из 15 | 8 из 15 | 11 из 15 | 13 из 15 |
| Релизы Core | 2 в месяц | 11 | 13 | n.r. |
| Доля неудачных изменений Core | 31% | 22% | 23% | n.r. |
| Закрытие корректирующих действий | 32% | 70% | 78% | n.r. |

Источники: [день 90](first-quarter.md#day-90), [итоги квартала 2](first-quarter.md#quarter-2-results),
[итоги квартала 3](first-quarter.md#quarter-3-results) и [исходные данные](baseline-data.md).

## Второй год и далее { #year-2-and-later }

- Год 1 — недели 1–52. В терминах финансов это финансовый год 1 (FY1); FY0 — год до прихода директора.
- Год 2 — недели 53–104 (кварталы 5–8, FY2), год 3 — недели 105–156, год 4 — недели 157–208.
- Предложение по организации второго года вступает в силу в начале квартала 5 (неделя 53); все передачи
  дел завершаются к неделе 57, пересмотр — на неделе 64.
- У продолжения программы качества контрольные точки на неделях 56, 78 и 104.
