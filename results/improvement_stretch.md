# Stretch — second improvement: AI_THRESHOLD 0.65 → 0.80

Weights stay 0.8 model / 0.2 style. All numbers are computed by script from `results/attack_marks_before.md`, `attack_marks_after.md`, `attack_marks_after2.md`, the run logs and the appeal-check files.

## a. Per attack: before / after / after2

| id | family | before mark | after mark | after2 mark | before combined | after combined | after2 combined | after → after2 |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | broke | broke | broke | 0.4322 | 0.3719 | 0.3719 |  |
| EV02 | evasion | broke | broke | broke | 0.468 | 0.5438 | 0.5438 |  |
| EV03 | evasion | broke | broke | broke | 0.5514 | 0.6203 | 0.6203 |  |
| EV04 | evasion | broke | broke | broke | 0.5854 | 0.601 | 0.601 |  |
| EV05 | evasion | broke | broke | broke | 0.3573 | 0.3356 | 0.3356 |  |
| EV06 | evasion | broke | broke | broke | 0.4884 | 0.539 | 0.539 |  |
| EV07 | evasion | broke | broke | broke | 0.4293 | 0.5234 | 0.5234 |  |
| EV08 | evasion | broke | broke | broke | 0.397 | 0.3059 | 0.3059 |  |
| EV09 | evasion | broke | broke | broke | 0.5589 | 0.6461 | 0.6461 |  |
| EV10 | evasion | held | held | held | 0.9075 | 0.9505 | 0.9505 |  |
| FP01 | false_positive | held | held | held | 0.6139 | 0.6161 | 0.6161 |  |
| **FP02** | **false_positive** | **broke** | **broke** | **held** | **0.7206** | **0.7315** | **0.7315** | **FIXED** |
| **FP03** | **false_positive** | **broke** | **broke** | **held** | **0.7413** | **0.7796** | **0.7796** | **FIXED** |
| **FP04** | **false_positive** | **broke** | **broke** | **held** | **0.6991** | **0.7794** | **0.7794** | **FIXED** |
| **FP05** | **false_positive** | **broke** | **broke** | **held** | **0.7831** | **0.7935** | **0.7935** | **FIXED** |
| FP06 | false_positive | broke | broke | broke | 0.7218 | 0.8176 | 0.8176 |  |
| FP07 | false_positive | broke | broke | broke | 0.7603 | 0.8331 | 0.8331 |  |
| FP08 | false_positive | held | held | held | 0.4876 | 0.3884 | 0.3884 |  |
| PI01 | prompt_injection | held | broke | broke | 0.4265 | 0.4481 | 0.4481 |  |
| PI02 | prompt_injection | broke | broke | broke | 0.2627 | 0.2277 | 0.2277 |  |
| PI03 | prompt_injection | broke | broke | broke | 0.5287 | 0.5681 | 0.5681 |  |
| PI04 | prompt_injection | held | held | held | 0.4671 | 0.4867 | 0.4867 |  |
| PI05 | prompt_injection | held | held | held | 0.4443 | 0.5197 | 0.5197 |  |
| PI06 | prompt_injection | held | held | held | 0.5757 | 0.5653 | 0.5653 |  |
| MF01 | malformed | held | held | held | — | — | — |  |
| MF02 | malformed | held | held | held | — | — | — |  |
| MF03 | malformed | held | held | held | 0.4167 | 0.3167 | 0.3167 |  |
| MF04 | malformed | held | held | held | 0.3778 | 0.3045 | 0.3045 |  |
| MF05 | malformed | broke | broke | broke | 0.8321 | 0.9314 | 0.9314 |  |
| **MF06** | **malformed** | **held** | **broke** | **held** | **0.6242** | **0.6988** | **0.6988** | **FIXED** |
| **MF07** | **malformed** | **held** | **broke** | **held** | **0.6016** | **0.6626** | **0.6626** | **FIXED** |
| MF08 | malformed | held | held | held | — | — | — |  |
| RQ01 | malformed | held | held | held | — | — | — |  |
| RQ02 | malformed | held | held | held | — | — | — |  |
| RQ03 | malformed | held | held | held | — | — | — |  |
| RQ04 | malformed | held | held | held | — | — | — |  |
| RQ05 | malformed | held | held | held | — | — | — |  |
| RQ06 | malformed | held | held | held | — | — | — |  |
| RQ07 | malformed | held | held | held | — | — | — |  |
| RQ08 | malformed | held | held | held | — | — | — |  |
| RQ09 | malformed | held | held | held | — | — | — |  |
| RQ10 | malformed | held | held | held | — | — | — |  |
| RQ11 | malformed | held | held | held | — | — | — |  |
| RQ12 | malformed | held | held | held | — | — | — |  |
| FL01_01 | flood_same_creator | held | held | held | 0.4238 | 0.3281 | 0.3281 |  |
| FL01_02 | flood_same_creator | held | held | held | 0.4238 | 0.3281 | 0.3281 |  |
| FL01_03 | flood_same_creator | held | held | held | 0.4238 | 0.3281 | 0.3281 |  |
| FL01_04 | flood_same_creator | held | held | held | 0.4238 | 0.3281 | 0.3281 |  |
| FL01_05 | flood_same_creator | held | held | held | 0.4238 | 0.3281 | 0.3281 |  |
| FL01_06 | flood_same_creator | held | held | held | 0.4238 | 0.3281 | 0.3281 |  |
| FL01_07 | flood_same_creator | held | held | held | 0.4238 | 0.3281 | 0.3281 |  |
| FL01_08 | flood_same_creator | held | held | held | 0.4238 | 0.3281 | 0.3281 |  |
| FL01_09 | flood_same_creator | held | held | held | 0.4238 | 0.3281 | 0.3281 |  |
| FL01_10 | flood_same_creator | held | held | held | 0.4238 | 0.3281 | 0.3281 |  |
| FL01_11 | flood_same_creator | held | held | held | — | — | — |  |
| FL01_12 | flood_same_creator | held | held | held | — | — | — |  |

Rows that changed from after to after2: FP02 (fixed), FP03 (fixed), FP04 (fixed), FP05 (fixed), MF06 (fixed), MF07 (fixed).
Attack texts whose label changed from after to after2: FP02: ai→unsure, FP03: ai→unsure, FP04: ai→unsure, FP05: ai→unsure, MF06: ai→unsure, MF07: ai→unsure.

## b. Counts (held / broke)

| family | before held | before broke | after held | after broke | after2 held | after2 broke |
|---|---|---|---|---|---|---|
| evasion | 1 | 9 | 1 | 9 | 1 | 9 |
| false_positive | 2 | 6 | 2 | 6 | 6 | 2 |
| prompt_injection | 4 | 2 | 3 | 3 | 3 | 3 |
| malformed | 19 | 1 | 17 | 3 | 19 | 1 |
| flood_same_creator | 12 | 0 | 12 | 0 | 12 | 0 |
| **total** | 38 | 18 | 35 | 21 | 41 | 15 |

## c. Five-criteria run log — after2

Files: `results/run_2026-11-12_1031_after2.md` and `results/appeal_check_2026-11-12_1031_after2.json`. All three trials identical.

| Criterion | Target (from criteria.md) | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | Of 10 paragraphs I wrote myself, at most 1 is labeled high-confidence AI, in each of 3 trials. | 0 of 9 labeled ai; max combined 0.6312 | 0 of 9 labeled ai; max combined 0.6312 | 0 of 9 labeled ai; max combined 0.6312 | MET |
| 2. Score spread | The combined score of my clearly-AI sample is at least 0.35 higher than the combined score of my clearly-human sample. | AI mean 0.7317, human mean 0.4791, gap 0.2526 | AI mean 0.7317, human mean 0.4791, gap 0.2526 | AI mean 0.7317, human mean 0.4791, gap 0.2526 | MISSED |
| 3. Label coverage | Across 5 or more test texts (clearly AI, clearly human, borderline, plain writing, formal writing), my service returns each of the three labels at least once, in each of 3 trials. `scoring.label_ranges()` shows no gap between the bands. | labels seen: ai, unsure; never: human | labels seen: ai, unsure; never: human | labels seen: ai, unsure; never: human | MISSED |
| 4. Appeal path | For 5 of 5 appeals on real content_ids, `GET /log` shows an appeal entry with status `under_review` next to the original decision. An appeal on a content_id that doesn't exist returns a 404 and writes nothing to the log. | 5 of 5 appeals logged as under_review; fake id: 404, nothing written | 5 of 5 appeals logged as under_review; fake id: 404, nothing written | 5 of 5 appeals logged as under_review; fake id: 404, nothing written | MET |
| 5. Bad input | A request with missing, null, empty or whitespace-only `text`, or with `text` over 5,000 characters, returns HTTP 400 with a JSON error saying bad input. None of them return a 500 or crash the service. | 5 of 5 returned 400 | 5 of 5 returned 400 | 5 of 5 returned 400 | MET |

| | before | after | after2 |
|---|---|---|---|
| highest combined among my 9 human texts | 0.63 | 0.6312 | 0.6312 |
| AI mean − human mean | 0.14 | 0.2526 | 0.2526 |
| lowest combined of my 16 eval texts | 0.4165 | 0.3714 | 0.3714 |
| verdicts (1–5) | MET MISSED MISSED MET MET | MET MISSED MISSED MET MET | MET MISSED MISSED MET MET |

## d. Own texts: scores and labels

| text | after combined | after2 combined | before label | after label | after2 label | change after → after2 |
|---|---|---|---|---|---|---|
| H1 | 0.6312 | 0.6312 | unsure | unsure | unsure |  |
| H2 | 0.5269 | 0.5269 | unsure | unsure | unsure |  |
| H3 | 0.4094 | 0.4094 | unsure | unsure | unsure |  |
| H4 | 0.3714 | 0.3714 | unsure | unsure | unsure |  |
| H5 | 0.4728 | 0.4728 | unsure | unsure | unsure |  |
| H6 | 0.4537 | 0.4537 | unsure | unsure | unsure |  |
| H7 | 0.4201 | 0.4201 | unsure | unsure | unsure |  |
| H8 | 0.5545 | 0.5545 | unsure | unsure | unsure |  |
| H9 | 0.4718 | 0.4718 | unsure | unsure | unsure |  |
| AI1 | 0.7369 | 0.7369 | unsure | ai | unsure | ai→unsure |
| AI2 | 0.7493 | 0.7493 | unsure | ai | unsure | ai→unsure |
| AI3 | 0.8375 | 0.8375 | ai | ai | ai |  |
| AI4 | 0.6603 | 0.6603 | unsure | ai | unsure | ai→unsure |
| AI5 | 0.6744 | 0.6744 | unsure | ai | unsure | ai→unsure |
| MIX1 | 0.4363 | 0.4363 | unsure | unsure | unsure |  |
| MIX2 | 0.4891 | 0.4891 | unsure | unsure | unsure |  |

Own texts whose label changed from after to after2: AI1 (ai→unsure), AI2 (ai→unsure), AI4 (ai→unsure), AI5 (ai→unsure).
Own texts whose label changed from before to after2: none.
