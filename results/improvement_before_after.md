# Before vs after — weights 0.5/0.5 → 0.8 model / 0.2 style

The only change is `WEIGHT_MODEL_SIGNAL = 0.8`, `WEIGHT_STYLE_SIGNAL = 0.2` in `config.py`. Thresholds, disagreement gap and pull, signals, routes and scenarios are unchanged. Every number below is computed by script from `results/attack_marks_before.md`, `results/attack_marks_after.md`, `results/run_*_before.md`, `results/run_*_after.md` and the appeal-check files.

## a. Per attack

| id | family | before mark | after mark | before combined | after combined | before guess | after guess | change |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | broke | broke | 0.4322 | 0.3719 | unsure | unsure |  |
| EV02 | evasion | broke | broke | 0.468 | 0.5438 | unsure | unsure |  |
| EV03 | evasion | broke | broke | 0.5514 | 0.6203 | unsure | unsure |  |
| EV04 | evasion | broke | broke | 0.5854 | 0.601 | unsure | unsure |  |
| EV05 | evasion | broke | broke | 0.3573 | 0.3356 | unsure | human |  |
| EV06 | evasion | broke | broke | 0.4884 | 0.539 | unsure | unsure |  |
| EV07 | evasion | broke | broke | 0.4293 | 0.5234 | unsure | unsure |  |
| EV08 | evasion | broke | broke | 0.397 | 0.3059 | unsure | human |  |
| EV09 | evasion | broke | broke | 0.5589 | 0.6461 | unsure | unsure |  |
| EV10 | evasion | held | held | 0.9075 | 0.9505 | ai | ai |  |
| FP01 | false_positive | held | held | 0.6139 | 0.6161 | unsure | unsure |  |
| FP02 | false_positive | broke | broke | 0.7206 | 0.7315 | ai | ai |  |
| FP03 | false_positive | broke | broke | 0.7413 | 0.7796 | ai | ai |  |
| FP04 | false_positive | broke | broke | 0.6991 | 0.7794 | ai | ai |  |
| FP05 | false_positive | broke | broke | 0.7831 | 0.7935 | ai | ai |  |
| FP06 | false_positive | broke | broke | 0.7218 | 0.8176 | ai | ai |  |
| FP07 | false_positive | broke | broke | 0.7603 | 0.8331 | ai | ai |  |
| FP08 | false_positive | held | held | 0.4876 | 0.3884 | unsure | unsure |  |
| PI01 | prompt_injection | held | broke | 0.4265 | 0.4481 | unsure | unsure | **NEWLY BROKEN** |
| PI02 | prompt_injection | broke | broke | 0.2627 | 0.2277 | human | human |  |
| PI03 | prompt_injection | broke | broke | 0.5287 | 0.5681 | unsure | unsure |  |
| PI04 | prompt_injection | held | held | 0.4671 | 0.4867 | unsure | unsure |  |
| PI05 | prompt_injection | held | held | 0.4443 | 0.5197 | unsure | unsure |  |
| PI06 | prompt_injection | held | held | 0.5757 | 0.5653 | unsure | unsure |  |
| MF01 | malformed | held | held | — | — | bad_input | bad_input |  |
| MF02 | malformed | held | held | — | — | bad_input | bad_input |  |
| MF03 | malformed | held | held | 0.4167 | 0.3167 | unsure | human |  |
| MF04 | malformed | held | held | 0.3778 | 0.3045 | unsure | human |  |
| MF05 | malformed | broke | broke | 0.8321 | 0.9314 | ai | ai |  |
| MF06 | malformed | held | broke | 0.6242 | 0.6988 | unsure | ai | **NEWLY BROKEN** |
| MF07 | malformed | held | broke | 0.6016 | 0.6626 | unsure | ai | **NEWLY BROKEN** |
| MF08 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ01 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ02 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ03 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ04 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ05 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ06 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ07 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ08 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ09 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ10 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ11 | malformed | held | held | — | — | bad_input | bad_input |  |
| RQ12 | malformed | held | held | — | — | bad_input | bad_input |  |
| FL01_01 | flood_same_creator | held | held | 0.4238 | 0.3281 | unsure | human |  |
| FL01_02 | flood_same_creator | held | held | 0.4238 | 0.3281 | unsure | human |  |
| FL01_03 | flood_same_creator | held | held | 0.4238 | 0.3281 | unsure | human |  |
| FL01_04 | flood_same_creator | held | held | 0.4238 | 0.3281 | unsure | human |  |
| FL01_05 | flood_same_creator | held | held | 0.4238 | 0.3281 | unsure | human |  |
| FL01_06 | flood_same_creator | held | held | 0.4238 | 0.3281 | unsure | human |  |
| FL01_07 | flood_same_creator | held | held | 0.4238 | 0.3281 | unsure | human |  |
| FL01_08 | flood_same_creator | held | held | 0.4238 | 0.3281 | unsure | human |  |
| FL01_09 | flood_same_creator | held | held | 0.4238 | 0.3281 | unsure | human |  |
| FL01_10 | flood_same_creator | held | held | 0.4238 | 0.3281 | unsure | human |  |
| FL01_11 | flood_same_creator | held | held | — | — | rate_limited | rate_limited |  |
| FL01_12 | flood_same_creator | held | held | — | — | rate_limited | rate_limited |  |

Rows where the mark changed: PI01 (newly broken), MF06 (newly broken), MF07 (newly broken).

Attack texts whose label (guess) changed: EV05: unsure→human, EV08: unsure→human, MF03: unsure→human, MF04: unsure→human, MF06: unsure→ai, MF07: unsure→ai, FL01_01: unsure→human, FL01_02: unsure→human, FL01_03: unsure→human, FL01_04: unsure→human, FL01_05: unsure→human, FL01_06: unsure→human, FL01_07: unsure→human, FL01_08: unsure→human, FL01_09: unsure→human, FL01_10: unsure→human.

## b. Counts per family

| family | before held | before broke | after held | after broke |
|---|---|---|---|---|
| evasion | 1 | 9 | 1 | 9 |
| false_positive | 2 | 6 | 2 | 6 |
| prompt_injection | 4 | 2 | 3 | 3 |
| malformed | 19 | 1 | 17 | 3 |
| flood_same_creator | 12 | 0 | 12 | 0 |
| TOTAL | 38 | 18 | 35 | 21 |

## c. Five-criteria run log — after

Files: `results/run_2026-11-12_1014_after.md` and `results/appeal_check_2026-11-12_1014_after.json`. Combined scores recomputed with `scoring.combine_signals` at the new weights.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | ≤1 of my 9 texts labeled AI, every trial | 0 of 9 flagged; max combined 0.6312 (pass) | 0 of 9 flagged; max combined 0.6312 (pass) | 0 of 9 flagged; max combined 0.6312 (pass) | MET |
| 2. Score spread | AI mean − human mean ≥ 0.35, every trial | AI mean 0.7317 − human mean 0.4791 = 0.2526 (FAIL) | AI mean 0.7317 − human mean 0.4791 = 0.2526 (FAIL) | AI mean 0.7317 − human mean 0.4791 = 0.2526 (FAIL) | MISSED |
| 3. Label coverage | human, unsure, ai all appear, every trial | labels: ai, unsure (FAIL) | labels: ai, unsure (FAIL) | labels: ai, unsure (FAIL) | MISSED |
| 4. Appeal path | 5/5 appeals under_review; fake id 404, nothing written | 5/5 appeals ok; fake id ok: True (pass) | 5/5 appeals ok; fake id ok: True (pass) | 5/5 appeals ok; fake id ok: True (pass) | MET |
| 5. Bad input | all 5 → HTTP 400 JSON, no 500, every trial | statuses [400, 400, 400, 400, 400] (pass) | statuses [400, 400, 400, 400, 400] (pass) | statuses [400, 400, 400, 400, 400] (pass) | MET |

### Comparison with before

| Criterion | before verdict | after verdict | before (run 1) | after (run 1) |
|---|---|---|---|---|
| 1. False positives | MET | MET | 0 of 9 flagged; max combined 0.63 | 0 of 9 flagged; max combined 0.6312 |
| 2. Score spread | MISSED | MISSED | AI mean 0.6467 − human mean 0.5067 = 0.14 | AI mean 0.7317 − human mean 0.4791 = 0.2526 |
| 3. Label coverage | MISSED | MISSED | labels: ai, unsure | labels: ai, unsure |
| 4. Appeal path | MET | MET | 5/5 appeals ok; fake id ok: True | 5/5 appeals ok; fake id ok: True |
| 5. Bad input | MET | MET | statuses [400, 400, 400, 400, 400] | statuses [400, 400, 400, 400, 400] |

Texts whose scores or guess differ between trials in the after run: 0.

## Own-text movement (label coverage scenario, trial 1)

| text | model | style | before combined | after combined | before guess | after guess | change |
|---|---|---|---|---|---|---|---|
| H1 | 0.632 | 0.6281 | 0.63 | 0.6312 | unsure | unsure |  |
| H2 | 0.4919 | 0.6667 | 0.5793 | 0.5269 | unsure | unsure |  |
| H3 | 0.3738 | 0.5518 | 0.4628 | 0.4094 | unsure | unsure |  |
| H4 | 0.3414 | 0.4916 | 0.4165 | 0.3714 | unsure | unsure |  |
| H5 | 0.4303 | 0.6428 | 0.5366 | 0.4728 | unsure | unsure |  |
| H6 | 0.3268 | 0.7298 | 0.5141 | 0.4537 | unsure | unsure |  |
| H7 | 0.3639 | 0.645 | 0.5045 | 0.4201 | unsure | unsure |  |
| H8 | 0.6074 | 0.3428 | 0.4751 | 0.5545 | unsure | unsure |  |
| H9 | 0.4922 | 0.3904 | 0.4413 | 0.4718 | unsure | unsure |  |
| AI1 | 0.7953 | 0.5034 | 0.6493 | 0.7369 | unsure | ai | unsure→ai |
| AI2 | 0.8195 | 0.4683 | 0.6439 | 0.7493 | unsure | ai | unsure→ai |
| AI3 | 0.9143 | 0.5303 | 0.7223 | 0.8375 | ai | ai |  |
| AI4 | 0.9151 | 0.4423 | 0.5894 | 0.6603 | unsure | ai | unsure→ai |
| AI5 | 0.705 | 0.552 | 0.6285 | 0.6744 | unsure | ai | unsure→ai |
| MIX1 | 0.3991 | 0.585 | 0.492 | 0.4363 | unsure | unsure |  |
| MIX2 | 0.5224 | 0.356 | 0.4392 | 0.4891 | unsure | unsure |  |

Own texts whose label changed: AI1 (unsure→ai), AI2 (unsure→ai), AI4 (unsure→ai), AI5 (unsure→ai).
Highest combined among my 9 human texts: before 0.63, after 0.6312. Distance to the 0.65 line: before 0.02, after 0.0188.
