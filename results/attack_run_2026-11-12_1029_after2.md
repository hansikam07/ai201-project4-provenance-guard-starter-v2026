# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-12 10:29
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `4524553a-6fe3-4162-b7cd-c66a4b3b1dbe` | unsure | 0.628 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `7a6ef4a1-4e3b-4b21-8e10-5b3f80b6cc5e` | unsure | 0.544 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `a67d9920-5d66-40c1-a474-6c37899a0164` | unsure | 0.620 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `866c21d4-f203-4c93-9fc7-04ae1d3f0d16` | unsure | 0.601 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `8478ce7a-d49a-444a-913e-eb550b44f733` | human | 0.664 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0e47ce55-6f8a-4473-a852-7623b90d75c2` | unsure | 0.539 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `bb92c065-9e54-4393-9790-56af0c687a02` | unsure | 0.523 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `de2a37a8-ee65-4aca-866f-a68075d54afb` | human | 0.694 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `d27dddf0-8348-4224-894a-e58f72b85035` | unsure | 0.646 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c42e33aa-b928-44dc-a192-d6a53bd86a58` | ai | 0.951 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9dda46b2-b69c-498a-a1e2-2504856eb859` | unsure | 0.616 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `0430afea-97d8-43af-a2d9-98860ea0113c` | unsure | 0.732 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `29cafe94-3175-4ef7-92a4-bcd07f9395e3` | unsure | 0.780 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `91121d35-f162-4cab-9b3f-39484df75b64` | unsure | 0.779 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `dce37a1d-6c77-4daa-b64e-4deab3ca73ce` | unsure | 0.793 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `1e9e5582-2828-4190-8c4e-b3455f7fd184` | ai | 0.818 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `2e89e41a-87d4-45b0-bcc4-270b7cab644a` | ai | 0.833 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `bb767d12-8b50-4525-895f-faaee0efcd63` | unsure | 0.612 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `aa948e4c-b046-4efb-9581-5b3a0360cc1b` | unsure | 0.552 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `58e32e75-7cd1-49cc-a927-e79523750b44` | human | 0.772 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `7e80a676-b4c8-41d1-a3da-27523c695fa6` | unsure | 0.568 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `2c5c6751-609d-4999-98fd-44cb710da3ee` | unsure | 0.513 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `cd646062-059a-4651-a9f3-d9efe76de13c` | unsure | 0.520 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `24be2ae8-cecc-4808-bf02-f7fe918ba10d` | unsure | 0.565 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `46388230-98f2-4f3f-b969-3da44bac1fd2` | human | 0.683 |  |
| MF04 | malformed | text is only punctuation | 200 | `ffc95cf8-f0d8-41c9-b9ac-9f4a7faf7130` | human | 0.696 |  |
| MF05 | malformed | text is a very long single word | 200 | `c20d648a-80ba-4049-85cf-2ddd2afcdaf3` | ai | 0.931 |  |
| MF06 | malformed | text is emoji only | 200 | `b00ec973-195d-4836-a5ca-77e66792e4f1` | unsure | 0.699 |  |
| MF07 | malformed | text is right-to-left script | 200 | `91d934d9-0454-4c01-a698-2c8e0cb8f85d` | unsure | 0.663 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `816a1c38-ade2-43e7-9e62-1611f7db12bc` | human | 0.672 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6320b4f2-c170-49f4-af98-b305bfaa5969` | human | 0.672 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `02a76834-a0b5-4294-a9af-4d375b230e97` | human | 0.672 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1ab0c710-7bff-4bea-9441-102fca933da2` | human | 0.672 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `038c0f73-4f92-4cfb-8dc8-ef65c88ef21a` | human | 0.672 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6b848d0e-82a7-4eca-91ac-b2f2a6a8b6b7` | human | 0.672 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5fe2f3d9-05ff-4ca1-a47a-56e77b5a374e` | human | 0.672 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b2f9359e-12f9-414a-92c4-aeb53533452e` | human | 0.672 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4b4b36b9-d873-4306-9e49-84dc4c969da8` | human | 0.672 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f86fc5b2-f093-4f39-b877-bc7482155ff3` | human | 0.672 |  |
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
  "content_id": "4524553a-6fe3-4162-b7cd-c66a4b3b1dbe",
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
  "content_id": "7a6ef4a1-4e3b-4b21-8e10-5b3f80b6cc5e",
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
  "content_id": "a67d9920-5d66-40c1-a474-6c37899a0164",
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
  "content_id": "866c21d4-f203-4c93-9fc7-04ae1d3f0d16",
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
  "content_id": "8478ce7a-d49a-444a-913e-eb550b44f733",
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
  "content_id": "0e47ce55-6f8a-4473-a852-7623b90d75c2",
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
  "content_id": "bb92c065-9e54-4393-9790-56af0c687a02",
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
  "content_id": "de2a37a8-ee65-4aca-866f-a68075d54afb",
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
  "content_id": "d27dddf0-8348-4224-894a-e58f72b85035",
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
  "content_id": "c42e33aa-b928-44dc-a192-d6a53bd86a58",
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
  "content_id": "9dda46b2-b69c-498a-a1e2-2504856eb859",
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
  "content_id": "0430afea-97d8-43af-a2d9-98860ea0113c",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7315,
  "model_score": 0.7387,
  "style_score": 0.7025,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "29cafe94-3175-4ef7-92a4-bcd07f9395e3",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7796,
  "model_score": 0.8051,
  "style_score": 0.6775,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "91121d35-f162-4cab-9b3f-39484df75b64",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7794,
  "model_score": 0.8329,
  "style_score": 0.5654,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "dce37a1d-6c77-4daa-b64e-4deab3ca73ce",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7935,
  "model_score": 0.8005,
  "style_score": 0.7656,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "1e9e5582-2828-4190-8c4e-b3455f7fd184",
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
  "content_id": "2e89e41a-87d4-45b0-bcc4-270b7cab644a",
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
  "content_id": "bb767d12-8b50-4525-895f-faaee0efcd63",
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
  "content_id": "aa948e4c-b046-4efb-9581-5b3a0360cc1b",
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
  "content_id": "58e32e75-7cd1-49cc-a927-e79523750b44",
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
  "content_id": "7e80a676-b4c8-41d1-a3da-27523c695fa6",
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
  "content_id": "2c5c6751-609d-4999-98fd-44cb710da3ee",
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
  "content_id": "cd646062-059a-4651-a9f3-d9efe76de13c",
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
  "content_id": "24be2ae8-cecc-4808-bf02-f7fe918ba10d",
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
  "content_id": "46388230-98f2-4f3f-b969-3da44bac1fd2",
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
  "content_id": "ffc95cf8-f0d8-41c9-b9ac-9f4a7faf7130",
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
  "content_id": "c20d648a-80ba-4049-85cf-2ddd2afcdaf3",
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
  "content_id": "b00ec973-195d-4836-a5ca-77e66792e4f1",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.6988,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "91d934d9-0454-4c01-a698-2c8e0cb8f85d",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.6626,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "816a1c38-ade2-43e7-9e62-1611f7db12bc",
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
  "content_id": "6320b4f2-c170-49f4-af98-b305bfaa5969",
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
  "content_id": "02a76834-a0b5-4294-a9af-4d375b230e97",
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
  "content_id": "1ab0c710-7bff-4bea-9441-102fca933da2",
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
  "content_id": "038c0f73-4f92-4cfb-8dc8-ef65c88ef21a",
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
  "content_id": "6b848d0e-82a7-4eca-91ac-b2f2a6a8b6b7",
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
  "content_id": "5fe2f3d9-05ff-4ca1-a47a-56e77b5a374e",
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
  "content_id": "b2f9359e-12f9-414a-92c4-aeb53533452e",
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
  "content_id": "4b4b36b9-d873-4306-9e49-84dc4c969da8",
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
  "content_id": "f86fc5b2-f093-4f39-b877-bc7482155ff3",
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
