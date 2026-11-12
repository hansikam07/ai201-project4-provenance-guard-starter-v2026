# Diagnosis evidence — before

Read-only evidence for the diagnosis. Nothing here called /submit or changed the audit log. Sources: `results/run_2026-11-12_1007_before.md` (my own eval), `results/attack_marks_before.md` and `logs/audit.jsonl` lines 42–97 (attack run). Combined scores for the eval texts are recomputed with `scoring.combine_signals` from the recorded model and style scores. The eval scores were identical in all three trials, so trial 1 is used.

## 1. What the code does

### `scoring.py::combine_signals`

It takes the weighted average of the two scores, then softens it if they disagree.

```python
total = config.WEIGHT_MODEL_SIGNAL + config.WEIGHT_STYLE_SIGNAL
avg = (config.WEIGHT_MODEL_SIGNAL * model_score + config.WEIGHT_STYLE_SIGNAL * style_score) / total

if abs(model_score - style_score) > config.DISAGREEMENT_GAP:
    avg = 0.5 + (avg - 0.5) * (1 - config.DISAGREEMENT_PULL)

return round(min(max(avg, 0.0), 1.0), 4)
```

- **Weights:** 0.5 for the model signal and 0.5 for the style signal, so it is a plain average.
- **Disagreement rule:** if the two scores are more than 0.4 apart, the average is pulled halfway back toward 0.5 (pull = 0.5). It is symmetric, so it softens a likely-AI and a likely-human reading equally.
- **Score to label (`score_to_label`):** `score >= 0.65` gives "ai", `score <= 0.35` gives "human", and anything between is "unsure". Because the combined score is an average of two numbers, it can only land between them. Reaching "human" needs both signals low; reaching "ai" needs both high.

### `stylometry.py::style_signal`

It never reads the words for meaning. It takes three shape measures, each scaled to 0..1 where **high means more human**, flips each (`1 - x`), and averages them with equal weight. Higher final score means more AI-like.

```python
parts = [1.0 - sentence_length_spread(text), 1.0 - type_token_ratio(text), 1.0 - punctuation_density(text)]
return round(_clamp01(sum(parts) / len(parts)), 4)
```

| measure | how it is computed | scaling |
|---|---|---|
| `sentence_length_spread` | stdev / mean of sentence lengths in words; fewer than 2 sentences returns 0.5 | `cv / 0.8`, clamped to 0..1 (`SPREAD_FULL = 0.8`) |
| `type_token_ratio` | unique words / words, first 100 words only; under 10 words returns 0.5 | `(ratio - 0.5) / (0.9 - 0.5)`, clamped |
| `punctuation_density` | count of `, ; : (` `! ?` dashes per word (full stops and apostrophes not counted); no words returns 0.5 | `marks_per_word / 0.2`, clamped (`PUNCT_FULL = 0.2`) |

The scaling constants are rough guesses tuned by eye, not fitted to data (comment at `stylometry.py:48-53`).

## 2. Min / mean / max by group

| group | n | model min / mean / max | style min / mean / max | combined min / mean / max |
|---|---|---|---|---|
| (a) my 9 human texts | 9 | 0.3268 / 0.4511 / 0.632 | 0.3428 / 0.5654 / 0.7298 | 0.4165 / 0.5067 / 0.63 |
| (b) my 5 AI texts | 5 | 0.705 / 0.8298 / 0.9151 | 0.4423 / 0.4993 / 0.552 | 0.5894 / 0.6467 / 0.7223 |
| (c) 8 FP attacks | 8 | 0.3223 / 0.735 / 0.8816 | 0.5623 / 0.6469 / 0.7656 | 0.4876 / 0.691 / 0.7831 |
| (d) 10 EV attacks | 10 | 0.1635 / 0.5444 / 0.9792 | 0.2723 / 0.4771 / 0.8359 | 0.3573 / 0.5175 / 0.9075 |
| (e) 6 PI attacks | 6 | 0.2044 / 0.4932 / 0.6401 | 0.1369 / 0.3899 / 0.5932 | 0.2627 / 0.4508 / 0.5757 |

## 3. Which signal separates my human texts from my AI texts better

| signal | human mean | AI mean | AI − human |
|---|---|---|---|
| model_score | 0.4511 | 0.8298 | +0.3788 |
| style_score | 0.5654 | 0.4993 | -0.0662 |
| combined_score | 0.5067 | 0.6467 | +0.1400 |

The **model signal** separates them better (difference +0.3788) than the style signal (-0.0662). Style is nearly flat between my human and AI texts.

Standard deviation of `style_score` across decisions in the before runs (population stdev; the style signal's possible range is 0 to 1):

| set | decisions | style_score stdev |
|---|---|---|
| attack run decisions (log lines 42–97) | 39 | 0.1457 |
| my eval run, all trials (results file, 3 criteria scenarios × 3 trials) | 117 | 0.1136 |
| my 16 unique eval texts (trial 1 of label coverage) | 16 | 0.1108 |
| every decision in the log from line 42 on (attack + eval + appeal check; repeats counted) | 171 | 0.1241 |

## 4. The 18 attacks that broke

Neutral is 0.5. For each broke attack I measured how far each signal sits on the wrong side of 0.5. 'Wrong' means: for evasion (AI text that should score high), a score *below* 0.5 pulled it toward human; for false positives and MF05 (non-AI that should score low), a score *above* 0.5 pulled it toward AI; for PI02 and PI03 (broke because the injected instruction moved the score toward human), a score below 0.5. Pull = distance past 0.5 in the wrong direction; blank means that signal was on the right side or neutral.

| id | family | model | style | combined | model pull | style pull | main culprit | gap | rule fired? |
|---|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | 0.1635 | 0.5654 | 0.4322 | +0.3365 |  | model | 0.4019 | yes |
| EV02 | evasion | 0.5943 | 0.3416 | 0.468 |  | +0.1584 | style | 0.2527 | no |
| EV03 | evasion | 0.6662 | 0.4366 | 0.5514 |  | +0.0634 | style | 0.2296 | no |
| EV04 | evasion | 0.6114 | 0.5593 | 0.5854 |  |  | neither | 0.0521 | no |
| EV05 | evasion | 0.3212 | 0.3934 | 0.3573 | +0.1788 | +0.1066 | model | 0.0722 | no |
| EV06 | evasion | 0.5727 | 0.404 | 0.4884 |  | +0.0960 | style | 0.1687 | no |
| EV07 | evasion | 0.5862 | 0.2723 | 0.4293 |  | +0.2277 | style | 0.3139 | no |
| EV08 | evasion | 0.2452 | 0.5488 | 0.397 | +0.2548 |  | model | 0.3036 | no |
| EV09 | evasion | 0.7042 | 0.4135 | 0.5589 |  | +0.0865 | style | 0.2907 | no |
| FP02 | false_positive | 0.7387 | 0.7025 | 0.7206 | +0.2387 | +0.2025 | model | 0.0362 | no |
| FP03 | false_positive | 0.8051 | 0.6775 | 0.7413 | +0.3051 | +0.1775 | model | 0.1276 | no |
| FP04 | false_positive | 0.8329 | 0.5654 | 0.6991 | +0.3329 | +0.0654 | model | 0.2675 | no |
| FP05 | false_positive | 0.8005 | 0.7656 | 0.7831 | +0.3005 | +0.2656 | model | 0.0349 | no |
| FP06 | false_positive | 0.8814 | 0.5623 | 0.7218 | +0.3814 | +0.0623 | model | 0.3191 | no |
| FP07 | false_positive | 0.8816 | 0.639 | 0.7603 | +0.3816 | +0.1390 | model | 0.2426 | no |
| PI02 | prompt_injection | 0.2044 | 0.321 | 0.2627 | +0.2956 | +0.1790 | model | 0.1166 | no |
| PI03 | prompt_injection | 0.5943 | 0.4631 | 0.5287 |  | +0.0369 | style | 0.1312 | no |
| MF05 | malformed | 0.9976 | 0.6667 | 0.8321 | +0.4976 | +0.1667 | model | 0.3309 | no |

The disagreement rule fired on **1 of the 18** broke attacks.
Across all 39 attack decisions it would fire on: EV01 (gap 0.4019), PI05 (gap 0.5032), MF03 (gap 0.6667), MF04 (gap 0.4888), MF06 (gap 0.4969), MF07 (gap 0.4064), FL01_01 (gap 0.638), FL01_02 (gap 0.638), FL01_03 (gap 0.638), FL01_04 (gap 0.638), FL01_05 (gap 0.638), FL01_06 (gap 0.638), FL01_07 (gap 0.638), FL01_08 (gap 0.638), FL01_09 (gap 0.638), FL01_10 (gap 0.638).

## 5. Which decisions got the "human" label

Decisions in the before runs (log line 42 to the end: attack run, eval run, appeal check): **171**. Labeled "human": **1**.

- log line 61: `attacker_PI02`, model 0.2044, style 0.321, combined 0.2627

The attack run's PI02 is the only decision any text got the human label. None of my 9 human texts, 5 AI texts or 2 mixed texts reached it in any of the 3 trials (lowest combined 0.4165).

For context, 15 earlier test decisions (lines 1–41: calibration and my own spot checks, not part of the before runs) were labeled human.

## 6. What may be driving the high model scores (hypotheses, not facts)

I scored each text directly (no /submit) and measured the raw perplexity and the three style measures, so each hypothesis sits next to a number. Lower perplexity means gpt2 found the text more predictable, which `model_signal` turns into a higher score.

| text | model | style | perplexity | spread | ttr | punct |
|---|---|---|---|---|---|---|
| my H1 | 0.632 | 0.6281 | 32.1 | 0.32 | 0.50 | 0.30 |
| my H2 | 0.4919 | 0.6667 | 45.9 | 0.41 | 0.47 | 0.12 |
| my H3 | 0.3738 | 0.5518 | 62.1 | 0.80 | 0.35 | 0.20 |
| my H4 | 0.3414 | 0.4916 | 67.9 | 0.79 | 0.55 | 0.18 |
| my H5 | 0.4303 | 0.6428 | 53.6 | 0.62 | 0.40 | 0.06 |
| my H6 | 0.3268 | 0.7298 | 70.7 | 0.40 | 0.35 | 0.06 |
| my H7 | 0.3639 | 0.645 | 63.8 | 0.42 | 0.47 | 0.18 |
| my H8 | 0.6074 | 0.3428 | 34.3 | 0.64 | 0.44 | 0.89 |
| my H9 | 0.4922 | 0.3904 | 45.9 | 1.00 | 0.49 | 0.34 |
| my AI1 | 0.7953 | 0.5034 | 19.3 | 0.24 | 0.88 | 0.37 |
| my AI2 | 0.8195 | 0.4683 | 17.5 | 0.16 | 0.91 | 0.53 |
| my AI3 | 0.9143 | 0.5303 | 10.2 | 0.23 | 0.91 | 0.27 |
| my AI4 | 0.9151 | 0.4423 | 10.2 | 0.18 | 0.94 | 0.56 |
| my AI5 | 0.705 | 0.552 | 26.1 | 0.05 | 0.89 | 0.40 |
| FP01 | 0.6175 | 0.6103 | 33.4 | 0.57 | 0.50 | 0.10 |
| FP02 | 0.7387 | 0.7025 | 23.5 | 0.30 | 0.53 | 0.07 |
| FP03 | 0.8051 | 0.6775 | 18.5 | 0.41 | 0.56 | 0.00 |
| FP04 | 0.8329 | 0.5654 | 16.5 | 0.46 | 0.77 | 0.07 |
| FP05 | 0.8005 | 0.7656 | 18.9 | 0.35 | 0.21 | 0.14 |
| FP06 | 0.8814 | 0.5623 | 12.8 | 0.65 | 0.59 | 0.08 |
| FP07 | 0.8816 | 0.639 | 12.8 | 0.91 | 0.00 | 0.17 |
| FP08 | 0.3223 | 0.6529 | 71.6 | 0.54 | 0.50 | 0.00 |
| MF05 | 0.9976 | 0.6667 | 1.0 | 0.50 | 0.50 | 0.00 |

### What the measures show on my own texts

Mean of each style measure (0..1, high = more human-like by the code's assumption). The code expects AI text to score *lower* than human text on all three.

| measure | my 9 human | my 5 AI | 8 FP attacks | does AI score lower than human, as the code assumes? |
|---|---|---|---|---|
| sentence_length_spread | 0.599 | 0.171 | 0.524 | yes |
| type_token_ratio | 0.447 | 0.907 | 0.457 | NO — opposite |
| punctuation_density | 0.257 | 0.424 | 0.078 | NO — opposite |

Observation: on my own texts only the sentence-length spread points the way the code assumes. Type-token ratio and punctuation density come out *higher* for my AI texts than my human ones, so after flipping they push the AI texts toward "human" and cancel the spread signal. That is why the style score is nearly flat (human 0.5654, AI 0.4993). This is 14 texts, so treat it as a pointer, not a conclusion.

### Hypotheses for the high model scores (not facts)

Each line is a guess from reading the text and the perplexity above. I have not tested any of them by editing the text.

- **FP01 (model 0.6175, perplexity 33.4):** *Hypothesis:* Short, plain narrative sentences made of everyday words ("We got to the campsite about four."). Common words in ordinary order are easy for gpt2 to predict. It stayed "unsure" rather than "ai", so the effect is milder here.
- **FP02 (0.7387, 23.5):** *Hypothesis:* Stock institutional phrasing: "This report sets out the findings", "its remit was to review", "the group recommends that the committee adopt". Boilerplate like this appears constantly in training text, so it is predictable.
- **FP03 (0.8051, 18.5):** *Hypothesis:* A careful non-native writer sticking to simple, high-frequency vocabulary in short, regular sentences with no punctuation other than full stops. This matches the blind spot the starter describes for signal one.
- **FP04 (0.8329, 16.5):** *Hypothesis:* A repeated sentence frame: "The first cause is economic… The second cause is political… The third cause is social." followed by "In conclusion…". Each repeat of the frame is easy to predict.
- **FP05 (0.8005, 18.9):** *Hypothesis:* Documentation style: repeated imperative frames ("Set the host value… Set the port value…") and heavy reuse of "the service" (vocabulary variety 0.21). Conventional technical phrasing is highly predictable.
- **FP06 (0.8814, 12.8):** *Hypothesis:* Letter boilerplate: "Dear Sir or Madam, I am writing to enquire about the position… I look forward to hearing from you." Templates like this are common enough that gpt2 can almost finish them.
- **FP07 (0.8816, 12.8):** *Hypothesis:* Deliberate repetition: "It rained on Monday. It rained on Tuesday." plus a days-of-the-week sequence. Once the pattern is established, each repeat costs the model almost nothing. Type-token ratio is 0.00 here, which the style signal also reads as AI-like.
- **FP08 (0.3223, 71.6):** *Hypothesis:* Not a false positive. At about nine words and fragment sentences, it is surprising enough to gpt2 to score low. It stayed "unsure" only because the style signal gave it 0.6529, mostly from having no punctuation to count.
- **MF05 (0.9976, perplexity 1.0):** *Hypothesis:* 4,000 repeated letters "a". After a few repeats gpt2 predicts the next token almost perfectly, so perplexity falls to about 1 and the model score saturates near 1. The style score of 0.6667 comes from neutral and zero values: one "sentence" gives spread 0.5, under 10 words gives vocabulary variety 0.5, and no punctuation gives 0, and (0.5 + 0.5 + 1.0) / 3 = 0.6667.

Common thread (also a hypothesis): the model signal rewards text that is formulaic, repetitive or made of common words, and several kinds of real writing (formal, template, rubric, plain, repeated) are exactly that. In my own eval the model signal does separate my writing from my AI texts (+0.38), but my writing sits at 0.33 to 0.63 and the AI texts at 0.71 to 0.92, and the attack FP texts land in the AI range.
