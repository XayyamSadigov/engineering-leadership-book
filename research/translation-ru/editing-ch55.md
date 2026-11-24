# Literary editing notes: chapter 55

File: `docs/parts/12-cto-leadership/55-boards-due-diligence-and-executive-decision-making.ru.md`. Edited from
the Russian text only; the English chapter was not opened. The file was not yet committed, so the pre-edit
copy was kept in the session scratchpad.

Checks: `validate_book.py` passes; the multiset of numeric tokens is identical before and after (347 tokens,
NBSP normalised); link targets, citation link texts, `{ #anchors }`, heading lines, exercise labels,
admonition lines, every table line and all three Mermaid blocks are byte-identical. No wrapped line starts
with a number and a period (19 numbered-list lines before and after). About 75 sentence-level edits. NBSP
76 → 77. Failure-mode fields are «Как заметить:» only (no other field in this chapter).

The translation was accurate and clean. Section 2a patterns appeared as expected; the ch53 patterns «стоит»
as "costs" (→ «обходится в») and "a person who… does X" (→ condition) recurred several times. Only new
patterns follow.

## 1. Patterns new beyond section 2a

### 1.1 Two «по» in one clause from "a record by which… judged by how…"

- «Оставляйте запись, по которой решение можно оценить по тому, как его принимали» → «Оставляйте запись,
  чтобы решение потом оценивали по тому, как его принимали»

### 1.2 A compound term with a dash colliding with ellipsis dashes

The term «член совета — эксперт» already contains a dash; in a list of "with X — when" pairs the reader
cannot tell which dash is which.

- «с председателем — за неделю, с членом совета — экспертом — по существу, с председателем комитета по
  аудиту — по рискам» → «встреча с председателем за неделю до заседания, разговор по существу с членом
  совета — экспертом, разговор о рисках с председателем комитета по аудиту»

### 1.3 Loose paraphrase of arithmetic

- «вероятность для одного квартала, умноженная сама на себя четыре раза (0,59 × 0,59 × 0,59 × 0,59)» (four
  factors are three multiplications) → «вероятность для одного квартала возводят в четвёртую степень»

### 1.4 An abstract subject with a sensory verb ("the board sees X inside the envelope")

- «Совет видит $150 000 внутри утверждаемых им рамок, а 6 FTE — выбор, который менеджмент делает внутри
  этих рамок» → «$150 000 совет видит внутри утверждаемых им рамок, а 6 FTE — это выбор менеджмента в
  пределах этих рамок» (theme first, and the second half gets its own predicate)

## 2. Two showcase paragraphs

### 2.1 Exposure as the currency of a board report

**Before.** […] Нужны и пороги, при превышении которых совет получает информацию между заседаниями (…).
«Доля неудачных изменений 23%» — это не подверженность риску. Подверженность риску звучит так: «около
$7,0 млн годовой регулярной выручки продлевается в ближайшие четыре квартала у шести наших крупнейших
клиентов, на продукте, надёжность которого прописана в их контрактах, а до уровня контракта нам не хватает
13 минут в квартал».

**After.** […] Нужны и пороги: если их превысили, совет узнаёт об этом между заседаниями (…). «Доля
неудачных изменений 23%» — это не подверженность риску. Подверженность риску звучит иначе: «в ближайшие
четыре квартала шесть наших крупнейших клиентов продлевают контракты на продукт, надёжность которого
прописана в этих контрактах; это около $7,0 млн годовой регулярной выручки, а до уровня контракта нам не
хватает 13 минут в квартал».

### 2.2 Being ready for due diligence

**Before.** Компания, которая поддерживает доказательства в актуальном состоянии (SBOM, перечень лицензий,
реестр рисков, история инцидентов, карта знаний), отвечает за дни. Компания, которая собирает их в
последний момент, отвечает за недели и выглядит хуже, чем есть.

**After.** Если доказательства (SBOM, перечень лицензий, реестр рисков, история инцидентов, карта знаний)
поддерживают в актуальном состоянии, компания отвечает за дни. Если их собирают в последний момент, ответ
занимает недели, и компания выглядит хуже, чем она есть.

## 3. Term proposals

| Current | Proposal | Reason |
|---|---|---|
| член совета — эксперт | allow «эксперт в совете» in running prose | the inner dash collides with other dashes (1.2); kept everywhere for consistency |
| подверженность риску (exposure) | keep; in prose prefer «чем рискует компания» where it fits (notes-t22 allows it) | eight uses in a few pages make the text heavy |
| ошибка оценки по исходу (outcome bias) | keep | clear |

## 4. Meaning doubts (not changed in meaning; please check against the English)

1. **«Лучшая публичная иллюстрация второй и третьей веток — взлом»** rendered «…иллюстрирует публичная
   история взлома Yahoo». Assumes the English refers to Yahoo's breach (the next sentences describe it).
2. **«надёжность, проданная клиентам»** rendered «обещанная клиентам надёжность». Check that "sold" means
   the contractual promise.
3. **«для решений, которые связывают больше квартала ресурса»** (Enterprise Application) not changed: it is
   ambiguous between "more than a quarter's worth of capacity" and "capacity for longer than a quarter".
4. **de Wit: «разногласия по поводу задачи сильнее положительно связаны с результативностью»**: «сильнее»
   has no comparator (stronger than in other teams?). Not changed.
5. **«Если он окажется ложным»** (warranty) rendered «Если факт окажется ложным»: wording only.
