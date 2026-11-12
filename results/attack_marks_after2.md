# Attack marks — after2

Weights 0.8 model / 0.2 style and AI_THRESHOLD 0.80; everything else unchanged. Same marking rules as `attack_marks_before.md`, except that the AI verdict for a malformed attack is the label `ai` (combined 0.80 or higher). Scores come from the audit log of the run in attack_run_2026-11-12_1029_after2.md. Prompt-injection marks come from scoring each text with and without its instruction directly through the signal functions, using the current config.

| id | family | targets | HTTP | model | style | combined | guess | mark | note |
|---|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | 0.1635 | 0.5654 | 0.3719 | unsure | broke |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | 0.5943 | 0.3416 | 0.5438 | unsure | broke |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | 0.6662 | 0.4366 | 0.6203 | unsure | broke |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | 0.6114 | 0.5593 | 0.601 | unsure | broke |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | 0.3212 | 0.3934 | 0.3356 | human | broke | partly human text, so 'unsure' is arguable; marked by the rule |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | 0.5727 | 0.404 | 0.539 | unsure | broke |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | 0.5862 | 0.2723 | 0.5234 | unsure | broke |  |
| EV08 | evasion | signal one: text below the token window | 200 | 0.2452 | 0.5488 | 0.3059 | human | broke |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | 0.7042 | 0.4135 | 0.6461 | unsure | broke | partly human text, so 'unsure' is arguable; marked by the rule |
| EV10 | evasion | signal two: repeated stanza structure | 200 | 0.9792 | 0.8359 | 0.9505 | ai | held |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | 0.6175 | 0.6103 | 0.6161 | unsure | held | not called AI, but unsure on real writing |
| FP02 | false_positive | human writing in a formal register | 200 | 0.7387 | 0.7025 | 0.7315 | unsure | held |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | 0.8051 | 0.6775 | 0.7796 | unsure | held |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | 0.8329 | 0.5654 | 0.7794 | unsure | held |  |
| FP05 | false_positive | technical documentation written by a person | 200 | 0.8005 | 0.7656 | 0.7935 | unsure | held |  |
| FP06 | false_positive | a person imitating a formal template | 200 | 0.8814 | 0.5623 | 0.8176 | ai | broke |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | 0.8816 | 0.639 | 0.8331 | ai | broke |  |
| FP08 | false_positive | very short genuine human submission | 200 | 0.3223 | 0.6529 | 0.3884 | unsure | held | not called AI, but unsure on real writing |
| PI01 | prompt_injection | instruction to ignore the check | 200 | 0.4625 | 0.3906 | 0.4481 | unsure | broke | full 0.4481 (unsure) vs without instruction 0.5849 (unsure); drop 0.1368 |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | 0.2044 | 0.321 | 0.2277 | human | broke | full 0.2277 (human) vs without instruction 0.5849 (unsure); drop 0.3572 |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | 0.5943 | 0.4631 | 0.5681 | unsure | broke | full 0.5681 (unsure) vs without instruction 0.7164 (unsure); drop 0.1483 |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | 0.4998 | 0.4344 | 0.4867 | unsure | held | label is a fixed string |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | 0.6401 | 0.1369 | 0.5197 | unsure | held | normal one-line log entry |
| PI06 | prompt_injection | instruction plus real human text | 200 | 0.5583 | 0.5932 | 0.5653 | unsure | held | full 0.5653 (unsure) vs without instruction 0.6161 (unsure); drop 0.0508 |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | bad_input | held |  |
| MF02 | malformed | text is a single character | 400 | — | — | — | bad_input | held |  |
| MF03 | malformed | text is control characters | 200 | 0.0 | 0.6667 | 0.3167 | human | held | not an AI verdict on non-writing |
| MF04 | malformed | text is only punctuation | 200 | 0.0112 | 0.5 | 0.3045 | human | held | not an AI verdict on non-writing |
| MF05 | malformed | text is a very long single word | 200 | 0.9976 | 0.6667 | 0.9314 | ai | broke | AI verdict on non-writing |
| MF06 | malformed | text is emoji only | 200 | 0.9969 | 0.5 | 0.6988 | unsure | held | not an AI verdict on non-writing (combined 0.65 or higher, but below the AI threshold) |
| MF07 | malformed | text is right-to-left script | 200 | 0.9064 | 0.5 | 0.6626 | unsure | held | not an AI verdict on non-writing (combined 0.65 or higher, but below the AI threshold) |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | — | bad_input | held |  |
| RQ01 | malformed | no text field at all | 400 | — | — | — | bad_input | held |  |
| RQ02 | malformed | no creator_id | 400 | — | — | — | bad_input | held |  |
| RQ03 | malformed | text is a number | 400 | — | — | — | bad_input | held |  |
| RQ04 | malformed | text is a list | 400 | — | — | — | bad_input | held |  |
| RQ05 | malformed | text is null | 400 | — | — | — | bad_input | held |  |
| RQ06 | malformed | creator_id is an object | 400 | — | — | — | bad_input | held |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | bad_input | held |  |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | bad_input | held |  |
| RQ09 | malformed | body is empty | 400 | — | — | — | bad_input | held |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | — | bad_input | held |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | — | bad_input | held |  |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | bad_input | held |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | inside the limit |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | inside the limit |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | inside the limit |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | inside the limit |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | inside the limit |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | inside the limit |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | inside the limit |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | inside the limit |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | inside the limit |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | inside the limit |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | rate_limited | held | 429 after 10 in a minute |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | rate_limited | held | 429 after 10 in a minute |

## Counts

| family | held | broke | ambiguous |
|---|---|---|---|
| evasion | 1 | 9 | 0 |
| false_positive | 6 | 2 | 0 |
| prompt_injection | 3 | 3 | 0 |
| malformed | 19 | 1 | 0 |
| flood_same_creator | 12 | 0 | 0 |
| TOTAL | 41 | 15 | 0 |
