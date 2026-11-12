# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-12 10:13
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `7d986cea-7271-4bf9-94bd-066fd34e2f4a` | unsure | 0.628 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `092454b5-5334-421b-b084-21cbe5aa94f9` | unsure | 0.544 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `4c3800b2-d9ab-469f-bc4a-2131f4dc9adb` | unsure | 0.620 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `14875b31-cf40-4b4e-9c30-f67ce0a90c46` | unsure | 0.601 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `9011ceff-0f92-4121-909f-344a4c98e296` | human | 0.664 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `53db3909-148b-4ab0-88bc-2bb5782976fa` | unsure | 0.539 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `5fb1bc85-e5b2-4ffd-a06d-8275cabe9eae` | unsure | 0.523 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `ca07d9e1-77ff-4729-b750-d04e9e329f4c` | human | 0.694 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `1dbbe148-4fb2-4201-81f8-7d1c8e5e837b` | unsure | 0.646 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `93ce1dfb-972e-4df0-ae26-d8b6e01de321` | ai | 0.951 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `731561ad-7088-4786-a411-60d7f2fd6fb5` | unsure | 0.616 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `38190297-1f2e-4f1a-9698-9b39f9be97f6` | ai | 0.732 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `01482dc7-0d65-471a-8bc3-a44543141540` | ai | 0.780 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `bedc156a-0907-4e7b-b1bb-55cc211e7d7c` | ai | 0.779 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `2cca2c95-d8d8-4ee3-b280-13f05086da3c` | ai | 0.793 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `0cd4c09c-32d9-4bd6-a24d-b184b7ed7074` | ai | 0.818 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `4f8b2cc6-f4d4-4909-a33a-a1f5ade108d3` | ai | 0.833 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `0f6476e0-3a30-4d79-affa-5e28652cde2f` | unsure | 0.612 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `7f0cfbd1-f958-4b06-bbe9-704ef13df2b4` | unsure | 0.552 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `f7ca3f28-4b66-4f8b-9e6d-a8028f725228` | human | 0.772 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `10c70d76-570c-4e98-9ce6-3362e8385280` | unsure | 0.568 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4b8a0511-7a3f-4844-b289-3400f30e0928` | unsure | 0.513 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `6db76140-e9ee-4e03-9183-c9153a7294fe` | unsure | 0.520 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `3a7f8f19-401f-43f9-b03e-0e54b911c8ba` | unsure | 0.565 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `3b63129a-154f-4b4d-b863-57e7a2a571b0` | human | 0.683 |  |
| MF04 | malformed | text is only punctuation | 200 | `3528c5ac-abc1-4fbf-a231-b03418a861c7` | human | 0.696 |  |
| MF05 | malformed | text is a very long single word | 200 | `7f189155-ffa9-4d8b-b263-b6896eb70c57` | ai | 0.931 |  |
| MF06 | malformed | text is emoji only | 200 | `d44b056f-cac1-4049-bdb5-e983a25e857f` | ai | 0.699 |  |
| MF07 | malformed | text is right-to-left script | 200 | `7631dce6-436f-4601-8ab5-fc7f99414a93` | ai | 0.663 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c9b2d9d2-f9e6-40c8-84a8-ead9c9509e1b` | human | 0.672 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e49df9ea-873e-4705-ae94-8f800bb8d255` | human | 0.672 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `66719594-6840-47bb-8a00-5f4babae4424` | human | 0.672 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `81528048-63a8-4850-94a9-75ab6a63c7ec` | human | 0.672 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e9d9e925-d76f-4d4e-8778-04290cc5eb1e` | human | 0.672 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f3242597-aee5-4d01-acda-4941b94e29d5` | human | 0.672 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f0fe3093-f477-4551-9554-2d3f89db103a` | human | 0.672 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0abd3422-6023-49cb-a76d-16d93320f0ae` | human | 0.672 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `64fd4738-2158-445d-8db0-6cf58d6bb692` | human | 0.672 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `43afeeef-13ca-4df5-97f7-f3c8709ceeac` | human | 0.672 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "7d986cea-7271-4bf9-94bd-066fd34e2f4a",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.6281,
  "model_score": 0.1635,
  "style_score": 0.5654,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "092454b5-5334-421b-b084-21cbe5aa94f9",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5438,
  "model_score": 0.5943,
  "style_score": 0.3416,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "4c3800b2-d9ab-469f-bc4a-2131f4dc9adb",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.6203,
  "model_score": 0.6662,
  "style_score": 0.4366,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "14875b31-cf40-4b4e-9c30-f67ce0a90c46",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.601,
  "model_score": 0.6114,
  "style_score": 0.5593,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "9011ceff-0f92-4121-909f-344a4c98e296",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.6644,
  "model_score": 0.3212,
  "style_score": 0.3934,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "53db3909-148b-4ab0-88bc-2bb5782976fa",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.539,
  "model_score": 0.5727,
  "style_score": 0.404,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "5fb1bc85-e5b2-4ffd-a06d-8275cabe9eae",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5234,
  "model_score": 0.5862,
  "style_score": 0.2723,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "ca07d9e1-77ff-4729-b750-d04e9e329f4c",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.6941,
  "model_score": 0.2452,
  "style_score": 0.5488,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "1dbbe148-4fb2-4201-81f8-7d1c8e5e837b",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6461,
  "model_score": 0.7042,
  "style_score": 0.4135,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "93ce1dfb-972e-4df0-ae26-d8b6e01de321",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9505,
  "model_score": 0.9792,
  "style_score": 0.8359,
  "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "731561ad-7088-4786-a411-60d7f2fd6fb5",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6161,
  "model_score": 0.6175,
  "style_score": 0.6103,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "38190297-1f2e-4f1a-9698-9b39f9be97f6",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7315,
  "model_score": 0.7387,
  "style_score": 0.7025,
  "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "01482dc7-0d65-471a-8bc3-a44543141540",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7796,
  "model_score": 0.8051,
  "style_score": 0.6775,
  "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "bedc156a-0907-4e7b-b1bb-55cc211e7d7c",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7794,
  "model_score": 0.8329,
  "style_score": 0.5654,
  "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "2cca2c95-d8d8-4ee3-b280-13f05086da3c",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7935,
  "model_score": 0.8005,
  "style_score": 0.7656,
  "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "0cd4c09c-32d9-4bd6-a24d-b184b7ed7074",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.8176,
  "model_score": 0.8814,
  "style_score": 0.5623,
  "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "4f8b2cc6-f4d4-4909-a33a-a1f5ade108d3",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.8331,
  "model_score": 0.8816,
  "style_score": 0.639,
  "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "0f6476e0-3a30-4d79-affa-5e28652cde2f",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.6116,
  "model_score": 0.3223,
  "style_score": 0.6529,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "7f0cfbd1-f958-4b06-bbe9-704ef13df2b4",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5519,
  "model_score": 0.4625,
  "style_score": 0.3906,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "f7ca3f28-4b66-4f8b-9e6d-a8028f725228",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.7723,
  "model_score": 0.2044,
  "style_score": 0.321,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "10c70d76-570c-4e98-9ce6-3362e8385280",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5681,
  "model_score": 0.5943,
  "style_score": 0.4631,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "4b8a0511-7a3f-4844-b289-3400f30e0928",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5133,
  "model_score": 0.4998,
  "style_score": 0.4344,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "6db76140-e9ee-4e03-9183-c9153a7294fe",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5197,
  "model_score": 0.6401,
  "style_score": 0.1369,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "3a7f8f19-401f-43f9-b03e-0e54b911c8ba",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5653,
  "model_score": 0.5583,
  "style_score": 0.5932,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "3b63129a-154f-4b4d-b863-57e7a2a571b0",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.6833,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "3528c5ac-abc1-4fbf-a231-b03418a861c7",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.6955,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "7f189155-ffa9-4d8b-b263-b6896eb70c57",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.9314,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "d44b056f-cac1-4049-bdb5-e983a25e857f",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.6988,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "7631dce6-436f-4601-8ab5-fc7f99414a93",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.6626,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c9b2d9d2-f9e6-40c8-84a8-ead9c9509e1b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6719,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "e49df9ea-873e-4705-ae94-8f800bb8d255",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6719,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "66719594-6840-47bb-8a00-5f4babae4424",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6719,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "81528048-63a8-4850-94a9-75ab6a63c7ec",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6719,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "e9d9e925-d76f-4d4e-8778-04290cc5eb1e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6719,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "f3242597-aee5-4d01-acda-4941b94e29d5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6719,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "f0fe3093-f477-4551-9554-2d3f89db103a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6719,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "0abd3422-6023-49cb-a76d-16d93320f0ae",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6719,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "64fd4738-2158-445d-8db0-6cf58d6bb692",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6719,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "43afeeef-13ca-4df5-97f7-f3c8709ceeac",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.6719,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
