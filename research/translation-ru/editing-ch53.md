# Literary editing notes: chapter 53

File: `docs/parts/12-cto-leadership/53-risk-governance-regulation-and-security-strategy.ru.md`. Edited from
the Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit
copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the sorted list of numeric tokens is identical before and after (357
tokens, NBSP normalised); link targets, citation link texts, `{ #anchors }`, heading lines, exercise labels,
admonition lines, every table line and all three Mermaid blocks are byte-identical. No wrapped line starts
with a number and a period. About 60 sentence-level edits. NBSP 83 → 88: label numbers now attach to the
word before them («главе⍽30», «неделе⍽44», «глава⍽52»). Failure-mode fields were already «Как заметить:» /
«Что делать:»; audit "control" is «механизм контроля» throughout.

The translation was accurate and clean. Section 2a patterns appeared as expected (English word order,
missing connectives, «который» chains). Only new patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 «стоит» as "costs", again (see editing-ch25, 1.1)

In Russian «стоит X» with a genitive reads as "is worth X". Use «обходится в», «обойдётся в».

- «Второй банковский маршрут (пробел TR-08) стоит работы по интеграции и второго договора.» → «…обойдётся в
  работу по интеграции и второй договор.»
- «Альтернатива стоит около 0,26 FTE в год плюс неизвестные трения в сделках.» → «Альтернатива обходится
  примерно в 0,26 FTE в год плюс трения в сделках, размер которых неизвестен.»

### 1.2 A person with a relative clause as the subject of an abstract result

English "A CTO who can name X gives the board something to govern" came through as a noun phrase with
«который». Russian wants a condition.

- «CTO, который может назвать десять важных технологических рисков, их владельцев и то, что компания
  принимает, даёт совету директоров предмет для управления.» → «Если CTO может назвать десять важных
  технологических рисков, их владельцев и то, какие риски компания принимает, у совета директоров есть чем
  управлять.»

### 1.3 «он / она / его» that can point to a person or to a unit

Chapters with org charts (a service that reports to a person who reports to another) make every pronoun
ambiguous. Name the referent.

- «…службу безопасности из двух человек, которая подчиняется Marta, а та — Rajiv. В его квартальном отчёте…»
  (Rajiv's or Joon's?) → «В квартальном отчёте Joon…»
- «безопасность должна быть в ИТ именно потому, что она проверяет разработку» (Marta or the service?) →
  «…потому что служба проверяет разработку»

### 1.4 "Results belong to teams": possession calqued as «принадлежат»

- «Результаты в области безопасности принадлежат командам, которые владеют системами.» → «Результатами в
  области безопасности владеют команды — владельцы систем.»

## 2. Two showcase paragraphs

### 2.1 Risk appetite

**Before.** Риск-аппетит делает эти решения последовательными: он говорит, какие виды и объёмы риска
компания готова нести ради своих целей. […] Рабочая формулировка написана в единицах индикаторов. […]
Активно эксплуатируемая уязвимость — это уязвимость из публичного списка тех, которые злоумышленники уже
используют. Компенсирующая мера — это замещающая защита, например блокировка доступа на балансировщике
нагрузки, которая снижает риск, пока настоящее исправление ждёт своей очереди.

**After.** Риск-аппетит делает эти решения последовательными: он определяет, какие виды риска и в каком
объёме компания готова нести ради своих целей. […] Рабочую формулировку пишут в единицах индикаторов. […]
Активно эксплуатируемая уязвимость — это уязвимость из публичного списка тех, что злоумышленники уже
используют. Компенсирующая мера — замещающая защита, которая снижает риск, пока настоящее исправление ждёт
своей очереди; например, блокировка доступа на балансировщике нагрузки.

### 2.2 The auth-svc exception in the case

**Before.** Строка 2 сразу выводит ER-03 за пределы аппетита. Директор записал исключение для auth-svc в
квартале 1 как действующее «до миграции» (глава 26). Joon Park вписал в запись дату — неделю 52 — на неделе
44, без новой подписи. […] Директор вписывает оба факта в черновик, а не смягчает строки.

**After.** Строка 2 сразу выводит ER-03 за пределы аппетита. Директор записал исключение для auth-svc в
квартале 1 как действующее «до миграции» (глава 26). На неделе 44 Joon Park вписал в запись дату, неделю
52, но новой подписи не было. […] Директор не смягчает строки, а вписывает оба факта в черновик.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| уязвимость системы (exposure), метрики уязвимости системы | «подверженность атакам», «метрики подверженности» | in a security chapter it collides with «уязвимость» (vulnerability) in the same sentence: «Докладывайте об уязвимости системы… критические уязвимости…»; kept for consistency with notes-t7 |
| уровень обзора (altitude) | «уровень обобщения» | "altitude" of register items means how aggregated they are; «обзор» suggests a view |
| принимающий риск / принимающий | keep | clear once introduced |
| подъём рисков наверх | keep | reads naturally |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«Поэтому не запрещайте матрицы, а реже останавливайтесь на них»** rendered «но и не останавливайтесь на
   них». Assumes the English means "don't stop at the matrix" (use it for triage, then go further). If it
   says "rely on them less", restore «реже».
2. **«Добавьте к ним проверку того, кто классифицирует находки (глава 18)».** Elsewhere the chapter speaks
   of checking *how* teams classify findings («аудит классификации»). If the English says "an audit of how
   findings are classified", «кто» is a slip. Not changed.
3. **Trade-offs: «Ни одно из двух мест не решает проблему ёмкости службы из двух человек»** rendered «Но
   при любом подчинении в службе остаются два человека, и проблема ёмкости не решается.» Check that the
   English says neither placement fixes the two-person capacity.
4. **«просит провести на заседании комитета на неделе 50 сессию»** rendered «просит посвятить сессию на
   заседании комитета на неделе 50 технологическим рискам»: wording only.
