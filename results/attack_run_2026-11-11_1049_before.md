# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 10:49
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `74deaac3-cf09-4c86-884d-d8493ec4024c` | unsure | 0.568 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `ee59f19b-33fe-42b8-9399-879d86c819c5` | unsure | 0.532 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `a05c77b6-5b9e-4336-b8a3-454ca70edca9` | unsure | 0.551 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `8172e4f7-ac7b-4a95-8a19-c6cd6ad8572e` | unsure | 0.585 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `a2215b41-5872-4c92-9b79-5c13aabe8f6e` | unsure | 0.643 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `4559cdb3-03c4-40fc-9984-d8e00953a4d3` | unsure | 0.512 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `b6d8ba94-f0a5-40b8-9c4e-d7001e8e1c53` | unsure | 0.571 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `a1568f30-9dd9-4f3a-8818-b981e7395d35` | unsure | 0.603 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `09f59f4e-1c13-43ba-a559-06566961097b` | unsure | 0.559 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `face0944-0a74-45c1-aedc-d11c802b3fdf` | ai | 0.907 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `cd8665d6-3401-43f2-a40c-90d8b1ecf439` | unsure | 0.614 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `0ea1b808-b612-4f75-add0-328cc6519b94` | ai | 0.721 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c44d71b7-9be7-4cf0-b285-2defd3fa9e43` | ai | 0.741 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `f82825a5-1122-4b65-a6cd-bf3e632be572` | ai | 0.699 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `8fb786c5-d944-4f39-a22d-97ac44c444db` | ai | 0.783 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `468783b4-f3fd-4265-a7a9-200a5e3894f1` | ai | 0.722 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `30dcbe29-55eb-4e84-8c74-51221873d2d5` | ai | 0.760 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `946897dd-bfcd-446b-909b-d5ce6a880fa1` | unsure | 0.512 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `8cb1e3d5-df8b-4991-89f7-8684e570390d` | unsure | 0.574 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `b34a396f-c95a-4d9e-8d1c-1af298961168` | human | 0.737 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `3dd9733e-db74-49c5-a336-0c51375e006d` | unsure | 0.529 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `6cbfb7d1-c57b-4970-b041-09988f85b615` | unsure | 0.533 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `ce5ac950-c46c-4c2a-b75a-9abf44843725` | unsure | 0.556 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `afcde4b8-97de-4e86-9cda-3c966eceb57d` | unsure | 0.576 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `5ea3b901-a0ef-46f6-8c78-a8654a795e55` | unsure | 0.583 |  |
| MF04 | malformed | text is only punctuation | 200 | `44eab557-87a3-4d6d-9440-a6c0cda7c988` | unsure | 0.622 |  |
| MF05 | malformed | text is a very long single word | 200 | `ebc758dd-6148-4a3d-9b89-a6b2b72c9d67` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `8b47fb95-c45f-4e20-8690-de15c6672dcc` | unsure | 0.624 |  |
| MF07 | malformed | text is right-to-left script | 200 | `0dd4d01a-4ffe-4828-a2b7-f8a8c88946d3` | unsure | 0.602 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e67ec4f2-7955-4408-81cb-383cea1d3143` | unsure | 0.576 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `62fc86c7-dd81-405e-8be7-0c7fafb845f2` | unsure | 0.576 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `869ad46d-8c69-4fe6-8de2-13ac2a5af1ab` | unsure | 0.576 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d9caf2b5-4388-4c4a-8bff-db1ae89429d5` | unsure | 0.576 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7513c274-0eed-4b8e-98fd-726b3dde8d80` | unsure | 0.576 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `665b2000-ea25-4491-8694-028bda1e4a66` | unsure | 0.576 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `92dc40e1-6397-44ed-9798-8270e4427442` | unsure | 0.576 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e117abc6-3877-4a03-9891-585b0406a324` | unsure | 0.576 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `06dae869-4ff3-4669-a756-a6aebb97a04a` | unsure | 0.576 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b42e8582-16dd-4885-8737-289bd71189f9` | unsure | 0.576 |  |
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
  "content_id": "74deaac3-cf09-4c86-884d-d8493ec4024c",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5678,
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
  "content_id": "ee59f19b-33fe-42b8-9399-879d86c819c5",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.532,
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
  "content_id": "a05c77b6-5b9e-4336-b8a3-454ca70edca9",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5514,
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
  "content_id": "8172e4f7-ac7b-4a95-8a19-c6cd6ad8572e",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5854,
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
  "content_id": "a2215b41-5872-4c92-9b79-5c13aabe8f6e",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.6427,
  "model_score": 0.3212,
  "style_score": 0.3934,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "4559cdb3-03c4-40fc-9984-d8e00953a4d3",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5116,
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
  "content_id": "b6d8ba94-f0a5-40b8-9c4e-d7001e8e1c53",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5707,
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
  "content_id": "a1568f30-9dd9-4f3a-8818-b981e7395d35",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.603,
  "model_score": 0.2452,
  "style_score": 0.5488,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "09f59f4e-1c13-43ba-a559-06566961097b",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5589,
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
  "content_id": "face0944-0a74-45c1-aedc-d11c802b3fdf",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9075,
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
  "content_id": "cd8665d6-3401-43f2-a40c-90d8b1ecf439",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6139,
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
  "content_id": "0ea1b808-b612-4f75-add0-328cc6519b94",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7206,
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
  "content_id": "c44d71b7-9be7-4cf0-b285-2defd3fa9e43",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7413,
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
  "content_id": "f82825a5-1122-4b65-a6cd-bf3e632be572",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6991,
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
  "content_id": "8fb786c5-d944-4f39-a22d-97ac44c444db",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7831,
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
  "content_id": "468783b4-f3fd-4265-a7a9-200a5e3894f1",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7218,
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
  "content_id": "30dcbe29-55eb-4e84-8c74-51221873d2d5",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7603,
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
  "content_id": "946897dd-bfcd-446b-909b-d5ce6a880fa1",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.5124,
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
  "content_id": "8cb1e3d5-df8b-4991-89f7-8684e570390d",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.5735,
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
  "content_id": "b34a396f-c95a-4d9e-8d1c-1af298961168",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.7373,
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
  "content_id": "3dd9733e-db74-49c5-a336-0c51375e006d",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5287,
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
  "content_id": "6cbfb7d1-c57b-4970-b041-09988f85b615",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5329,
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
  "content_id": "ce5ac950-c46c-4c2a-b75a-9abf44843725",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5557,
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
  "content_id": "afcde4b8-97de-4e86-9cda-3c966eceb57d",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5757,
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
  "content_id": "5ea3b901-a0ef-46f6-8c78-a8654a795e55",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.5833,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "44eab557-87a3-4d6d-9440-a6c0cda7c988",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.6222,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "ebc758dd-6148-4a3d-9b89-a6b2b72c9d67",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8321,
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
  "content_id": "8b47fb95-c45f-4e20-8690-de15c6672dcc",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.6242,
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
  "content_id": "0dd4d01a-4ffe-4828-a2b7-f8a8c88946d3",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.6016,
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
  "content_id": "e67ec4f2-7955-4408-81cb-383cea1d3143",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5762,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "62fc86c7-dd81-405e-8be7-0c7fafb845f2",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5762,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "869ad46d-8c69-4fe6-8de2-13ac2a5af1ab",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5762,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "d9caf2b5-4388-4c4a-8bff-db1ae89429d5",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5762,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "7513c274-0eed-4b8e-98fd-726b3dde8d80",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5762,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "665b2000-ea25-4491-8694-028bda1e4a66",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5762,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "92dc40e1-6397-44ed-9798-8270e4427442",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5762,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "e117abc6-3877-4a03-9891-585b0406a324",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5762,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "06dae869-4ff3-4669-a756-a6aebb97a04a",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5762,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
  "content_id": "b42e8582-16dd-4885-8737-289bd71189f9",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.5762,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
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
