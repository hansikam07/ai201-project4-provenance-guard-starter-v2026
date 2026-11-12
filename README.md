# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

When someone submits a piece of writing, this is the path it takes:

1. **It arrives.** A client sends `POST /submit` with JSON `{text, creator_id}`. `app.py::submit` checks the input first: the body must be a JSON object, `text` must be a non-empty string of at most 5,000 characters, and `creator_id` must be a non-empty string. Anything else gets a `400 bad_input` instead of a crash.
2. **It gets an ID.** `submit` makes a `content_id` (a UUID). Every later step, including an appeal, refers to the submission by that ID.
3. **Signal one reads it.** `detector.model_signal(text)` runs gpt2 on my own machine, measures how predictable the text is, and returns a 0 to 1 score where higher means more likely AI. Text too short to score is a `400`, and a missing model is a `503`.
4. **Signal two measures its shape.** `stylometry.style_signal(text)` looks at sentence-length spread, vocabulary variety and punctuation, and returns a 0 to 1 score on the same scale.
5. **The two are combined.** `scoring.combine_signals(model_score, style_score)` takes a weighted average, and pulls it toward 0.5 if the two signals disagree by too much.
6. **The score becomes a label.** `scoring.score_to_label(combined_score)` returns a guess (`human`, `unsure` or `ai`) and the sentence a reader actually sees.
7. **It is logged and answered.** `audit.log_decision(...)` appends one line to `logs/audit.jsonl` with the content ID, creator, guess, both signal scores, the combined score, the label and the status `decided`. Then `submit` returns the content ID, guess, confidence, label, both signal scores, the combined score and the status.

If the writer disagrees, they call `POST /appeal` with the `content_id` and their reasoning. `app.py::appeal` returns a `404` if that ID isn't in the log (and writes nothing). Otherwise it calls `audit.log_appeal(...)`, which adds a new entry with the status `under_review` beside the original decision. Nothing is overwritten.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to a small language model (gpt2, running locally). `detector.perplexity` takes the model's average surprise per token over the first 400 tokens. `detector.model_signal` squashes that onto 0 to 1 with a logistic curve (a perplexity of 45 maps to 0.5). Higher means more likely AI.

**Why that might differ between human and AI writing:** A language model writes by picking likely next words, so text it produced tends to be text another model finds easy to predict. Human writing tends to wander more, with odd word choices and specific details a model doesn't expect.

**What it can't see:** Predictability isn't authorship. The signal rewards common words in short, ordinary sentences, and plenty of real people write that way: someone writing in a second language, a younger writer, anyone writing plainly on purpose. That kind of writing scores as machine-like. The reverse also happens, since dense prose full of rare words can read as human.

### Signal two — the style signal

**What it measures:** The shape of the text, without reading it. `stylometry.style_signal` averages three measures, each scaled to 0 to 1, with equal weight: how much sentence length varies (`sentence_length_spread`, the standard deviation over the mean), how varied the vocabulary is in the first 100 words (`type_token_ratio`), and how much punctuation there is per word (`punctuation_density`, counting commas, semicolons, colons, parentheses, dashes, `!` and `?`). Each measure points toward "human" when high, so they are flipped before averaging. Higher final score means more likely AI.

**Why that might differ between human and AI writing:** Generated prose tends toward even, mid-length sentences and a narrower band of vocabulary. Human writing is lumpier, such as a three-word sentence next to a forty-word one. (The punctuation direction is the weakest guess of the three, because models use commas and colons a lot too.)

**What it can't see:** Meaning. It has no idea what the text says, so anything that changes the shape without changing the substance moves it. Typos add "new" words and raise vocabulary variety. Breaking up sentences changes the spread. A pasted quotation brings in someone else's punctuation and sentence lengths. All of that is cheap to do on purpose.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Take the weighted average of the two scores. If the two signals are further apart than a set gap, pull that average toward 0.5 ("unsure"), because two methods disagreeing is itself uncertainty. If they agree, the plain average stands.

**The numbers:** From `config.py`: `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5`, `DISAGREEMENT_GAP = 0.4`, `DISAGREEMENT_PULL = 0.5`. When `abs(model - style) > 0.4`, the result is `0.5 + (average - 0.5) * (1 - 0.5)`, which halves the average's distance from 0.5. Label thresholds are 0.35 and 0.65.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

A paragraph about growing tomatoes on a balcony scored model 0.6895 and style 0.2876, a gap of 0.4019, just over the 0.4 limit. The plain average was 0.4886. The rule fired and pulled it to 0.4943, so the effect was tiny: the average was already close to 0.5, and the pull can only move a score by half its distance from 0.5. It was labelled "unsure" either way. The rule matters most for splits where the average sits far from 0.5, and I only found this one split case, so I haven't seen that happen.

**What I'm honest about:**

- **The two signals are not very independent.** Both tend to score plain, uniform writing high. Short sentences with common words look predictable to gpt2 and also look evenly shaped to the stylometry, so they agree for the same underlying reason and the disagreement rule rarely has anything to catch.
- **A false positive.** My plain-human calibration text (a stand-in written to imitate plain, short-sentence human writing) scored model 0.7846, style 0.7475 and combined 0.7661, and the service guessed "ai". Real people write this way, so this is the kind of writer the service would accuse.
- **It happened again.** A stand-in human text with very uniform sentence lengths scored combined 0.7831 and was also guessed "ai".
- **I did not change thresholds to hide this.** The bands are still 0.35 and 0.65. I'm reporting these as findings rather than tuning them away on five samples.
- **My test paragraphs aren't my own writing.** The borderline test paragraphs (and the other calibration texts) were written by an AI tool as stand-ins for human writing, not by me. My own writing gets tested next unit.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. |
| unsure | 0.35 – 0.65 | We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like. |
| high-confidence AI | 0.65 – 1.00 | This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

It admits uncertainty without accusing anyone. It says nothing is being held against the writer, and it offers a review.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "The bus to my school was always late, so I started walking instead. It took forty minutes, but I got to see the whole neighborhood wake up. The baker waved at me every day, and a woman on the corner fed the stray cats. By spring I knew most of the dogs by name.", "creator_id": "hansika"}'
```

```json
{
  "combined_score": 0.531,
  "confidence": 0.531,
  "content_id": "1cd2d102-042e-4a5d-96f1-750aa5e0e603",
  "guess": "unsure",
  "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
  "model_score": 0.5214,
  "status": "decided",
  "style_score": 0.5405
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "1cd2d102-042e-4a5d-96f1-750aa5e0e603", "reasoning": "I wrote this myself about my walk to school."}'
```

```json
{
  "content_id": "1cd2d102-042e-4a5d-96f1-750aa5e0e603",
  "message": "Your appeal has been recorded and this item is marked for review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.7661,
      "content_id": "d7eba1f4-74a0-4c52-99b3-ffe3eedb9a95",
      "creator_id": "calibrate",
      "guess": "ai",
      "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.",
      "model_score": 0.7846,
      "status": "decided",
      "style_score": 0.7475,
      "timestamp": "2026-11-04T06:52:32+00:00"
    },
    {
      "combined_score": 0.531,
      "content_id": "1cd2d102-042e-4a5d-96f1-750aa5e0e603",
      "creator_id": "hansika",
      "guess": "unsure",
      "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
      "model_score": 0.5214,
      "status": "decided",
      "style_score": 0.5405,
      "timestamp": "2026-11-04T06:55:05+00:00"
    },
    {
      "content_id": "1cd2d102-042e-4a5d-96f1-750aa5e0e603",
      "creator_id": "hansika",
      "event": "appeal",
      "reasoning": "I wrote this myself about my walk to school.",
      "status": "under_review",
      "timestamp": "2026-11-04T06:55:05+00:00"
    }
  ]
}
```

The first entry in that output is an earlier calibration submission (`creator_id` "calibrate"). The other two are this submission and its appeal.

---

## How I Used AI


**Moment 1**

- *What I asked for:* help getting started on my five acceptance criteria. I asked for a template and then for step-by-step questions, one criterion at a time.
- *What came back:* a draft set of five criteria with starting numbers (at most 1 false positive in 10, a 0.30 score gap, a 10,000 character cap), plus suggested wording and reasons.
- *What I changed:* I made the decisions by answering the questions: at most 1 false positive in 10 for my own reasons, a score gap of 0.35 to match my 0.30-wide unsure band, a text cap of 5,000 characters because the detector only reads about 400 tokens, 5 of 5 appeals, and a 404 for a fake content_id. The AI wrote out the final wording of the criteria and their reasons from my answers, and I kept it as written.

**Moment 2**

- *What I asked for:* Claude Code to build /submit, the stylometry signal and the combining rule, then run five calibration texts.
- *What came back:* a working service and a table in which a plain human paragraph scored 0.77 and was guessed AI.
- *What I changed:* nothing in the thresholds. I chose to keep the 0.35 and 0.65 bands and report the false positive as a finding rather than tune it away on five samples.

**Unit 8 — Moment 1**

- *What I asked for:* I used Claude to plan each milestone, and Claude Code to run the attack set, write the 5 AI test texts for my criteria, build `scenarios.py`, and fill in the README from the results files.
- *What came back:* a full attack run, the 5 AI texts, a `scenarios.py` holding my 9 texts and an appeal check, and README drafts. Claude Code's first summary of the attack results added the counts up wrong. It reported 37 held next to 15 broke and 9 ambiguous, which comes to 61, not 56.
- *What I changed:* I had the counts recomputed by script and the 9 ambiguous attacks resolved by re-scoring them. The final counts are 38 held and 18 broke.

**Unit 8 — Moment 2**

- *What I asked for:* one improvement, based on the diagnosis evidence.
- *What came back:* Claude suggested reweighting the signals to 0.8 model and 0.2 style, because the style signal was flat between my AI and human texts while the model signal did the separating.
- *What I changed:* I agreed to it and made only that change. It only partly helped: 35 held and 21 broke after, against 38 and 18 before.

**Disclosure:** I used AI to help me write my plans, Claude Code for code changes, and to help me with logic when I don't know. In this unit, Claude Code wrote the 5 AI test texts for criteria 2 and 3 (the 9 human texts are my own writing, pasted as written), ran the attacks, and drafted README text from the results files. The worst-outcome pick (FP03) and the choice to let AI text through rather than accuse writers are my own decisions.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

A real writer submits a handful of pieces a day. Ten a minute leaves plenty of room to fix a typo and resubmit several times, so the limit should never be noticed by someone working on their own writing. A script mapping my thresholds with many small variations of one text hits the cap within seconds and gets `429`s. The daily cap of 200 limits how much one caller can probe in total, even if they pace themselves under the per-minute limit.

One side effect: a `400` for bad input also counts against the limit, because the limiter runs before the route does. Someone sending lots of malformed requests uses up their allowance like anyone else.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

Per `creator_id`. `app.py::rate_limit_key` uses the `creator_id` in the request body, and falls back to the caller's IP address only when `creator_id` is missing or not a non-empty string. The weakness is the one the starter comments warn about: a script can send a different `creator_id` on every request and look like many callers. Every row in the attack set already uses its own `creator_id`, so a normal attack run never trips the limit.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

From `results/flood_2026-11-11_1041.md` (`run_attacks.py::run_flood`): 15 submissions from one `creator_id` (`flood_tester`), 5 rate limited.

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

Ten `200`s, then five `429`s. Each rejection is written to the audit log with reason `rate_limited` and the limit that was hit.

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

All 56 attacks, run with `run_attacks.py --set attack_set --label before` against the service with rate limiting on (`results/attack_run_2026-11-11_1049_before.md`). Scores come from the audit log of that run. The marks and notes are in `results/attack_marks_before.md`. The service did not crash on any input.

**How I marked them:**

- Evasion: broke if the AI text was not labeled `ai`.
- False positive: broke if real writing was labeled `ai`.
- Prompt injection: this rule is my own. Broke if removing the injected instruction changed the label band or moved the combined score 0.10 or more toward human. I re-scored each text with the instruction removed directly through the signal functions.
- Malformed: broke on a 500, a crash or an HTML error page, or if junk text got an `ai` verdict (combined 0.65 or higher). Held on a clean 4xx JSON error.
- Flood: held, since the limit stopped the caller (10 got through, the rest got `429`). The attack set's flood family sent 12 requests, not the 20 its targets column says.

| id | family | targets | HTTP | model | style | combined | guess / result | mark |
|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | 0.1635 | 0.5654 | 0.4322 | unsure | broke |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | 0.5943 | 0.3416 | 0.468 | unsure | broke |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | 0.6662 | 0.4366 | 0.5514 | unsure | broke |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | 0.6114 | 0.5593 | 0.5854 | unsure | broke |
| EV05 | evasion | both signals: heavy human editing pass | 200 | 0.3212 | 0.3934 | 0.3573 | unsure | broke |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | 0.5727 | 0.404 | 0.4884 | unsure | broke |
| EV07 | evasion | signal two: padding with punctuation | 200 | 0.5862 | 0.2723 | 0.4293 | unsure | broke |
| EV08 | evasion | signal one: text below the token window | 200 | 0.2452 | 0.5488 | 0.397 | unsure | broke |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | 0.7042 | 0.4135 | 0.5589 | unsure | broke |
| EV10 | evasion | signal two: repeated stanza structure | 200 | 0.9792 | 0.8359 | 0.9075 | ai | held |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | 0.6175 | 0.6103 | 0.6139 | unsure | held |
| FP02 | false_positive | human writing in a formal register | 200 | 0.7387 | 0.7025 | 0.7206 | ai | broke |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | 0.8051 | 0.6775 | 0.7413 | ai | broke |
| FP04 | false_positive | a student essay written to a rubric | 200 | 0.8329 | 0.5654 | 0.6991 | ai | broke |
| FP05 | false_positive | technical documentation written by a person | 200 | 0.8005 | 0.7656 | 0.7831 | ai | broke |
| FP06 | false_positive | a person imitating a formal template | 200 | 0.8814 | 0.5623 | 0.7218 | ai | broke |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | 0.8816 | 0.639 | 0.7603 | ai | broke |
| FP08 | false_positive | very short genuine human submission | 200 | 0.3223 | 0.6529 | 0.4876 | unsure | held |
| PI01 | prompt_injection | instruction to ignore the check | 200 | 0.4625 | 0.3906 | 0.4265 | unsure | held |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | 0.2044 | 0.321 | 0.2627 | human | broke |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | 0.5943 | 0.4631 | 0.5287 | unsure | broke |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | 0.4998 | 0.4344 | 0.4671 | unsure | held |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | 0.6401 | 0.1369 | 0.4443 | unsure | held |
| PI06 | prompt_injection | instruction plus real human text | 200 | 0.5583 | 0.5932 | 0.5757 | unsure | held |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | bad_input | held |
| MF02 | malformed | text is a single character | 400 | — | — | — | bad_input | held |
| MF03 | malformed | text is control characters | 200 | 0.0 | 0.6667 | 0.4167 | unsure | held |
| MF04 | malformed | text is only punctuation | 200 | 0.0112 | 0.5 | 0.3778 | unsure | held |
| MF05 | malformed | text is a very long single word | 200 | 0.9976 | 0.6667 | 0.8321 | ai | broke |
| MF06 | malformed | text is emoji only | 200 | 0.9969 | 0.5 | 0.6242 | unsure | held |
| MF07 | malformed | text is right-to-left script | 200 | 0.9064 | 0.5 | 0.6016 | unsure | held |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | — | bad_input | held |
| RQ01 | malformed | no text field at all | 400 | — | — | — | bad_input | held |
| RQ02 | malformed | no creator_id | 400 | — | — | — | bad_input | held |
| RQ03 | malformed | text is a number | 400 | — | — | — | bad_input | held |
| RQ04 | malformed | text is a list | 400 | — | — | — | bad_input | held |
| RQ05 | malformed | text is null | 400 | — | — | — | bad_input | held |
| RQ06 | malformed | creator_id is an object | 400 | — | — | — | bad_input | held |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | bad_input | held |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | bad_input | held |
| RQ09 | malformed | body is empty | 400 | — | — | — | bad_input | held |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | — | bad_input | held |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | — | bad_input | held |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | bad_input | held |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.4238 | unsure | held |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.4238 | unsure | held |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.4238 | unsure | held |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.4238 | unsure | held |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.4238 | unsure | held |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.4238 | unsure | held |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.4238 | unsure | held |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.4238 | unsure | held |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.4238 | unsure | held |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.4238 | unsure | held |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | rate_limited | held |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | rate_limited | held |

**Counts: held 38, broke 18.**

| family | held | broke |
|---|---|---|
| evasion | 1 | 9 |
| false_positive | 2 | 6 |
| prompt_injection | 4 | 2 |
| malformed | 19 | 1 |
| flood_same_creator | 12 | 0 |
| **total** | 38 | 18 |

Prompt-injection marks, from re-scoring each text with and without its instruction:

- **PI01** (instruction to ignore the check): full 0.4265 (unsure) vs without instruction 0.5218 (unsure); drop 0.0953. Mark: held.
- **PI02** (instruction disguised as a system message): full 0.2627 (human) vs without instruction 0.5218 (unsure); drop 0.2591. Mark: broke.
- **PI03** (instruction wrapped in the writer's voice): full 0.5287 (unsure) vs without instruction 0.641 (unsure); drop 0.1123. Mark: broke.
- **PI06** (instruction plus real human text): full 0.5757 (unsure) vs without instruction 0.6139 (unsure); drop 0.0382. Mark: held.

EV05 and EV09 are partly human text, so "unsure" is arguable. I marked them broke by the rule anyway.

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

Fourteen entries from `logs/audit.jsonl`, exactly as stored (log line numbers in the labels). They include a `400` (line 81) and a `429` (line 96).

**Log line 42 — EV01, typos added to AI text; not caught**

```json
{"timestamp": "2026-11-11T16:49:39+00:00", "content_id": "74deaac3-cf09-4c86-884d-d8493ec4024c", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.1635, "style_score": 0.5654, "combined_score": 0.4322, "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.", "status": "decided"}
```

**Log line 45 — EV04, unusual words; not caught**

```json
{"timestamp": "2026-11-11T16:49:39+00:00", "content_id": "8172e4f7-ac7b-4a95-8a19-c6cd6ad8572e", "creator_id": "attacker_EV04", "guess": "unsure", "model_score": 0.6114, "style_score": 0.5593, "combined_score": 0.5854, "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.", "status": "decided"}
```

**Log line 50 — EV09, human opening bolted on; not caught**

```json
{"timestamp": "2026-11-11T16:49:39+00:00", "content_id": "09f59f4e-1c13-43ba-a559-06566961097b", "creator_id": "attacker_EV09", "guess": "unsure", "model_score": 0.7042, "style_score": 0.4135, "combined_score": 0.5589, "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.", "status": "decided"}
```

**Log line 51 — EV10, the one evasion that was caught**

```json
{"timestamp": "2026-11-11T16:49:40+00:00", "content_id": "face0944-0a74-45c1-aedc-d11c802b3fdf", "creator_id": "attacker_EV10", "guess": "ai", "model_score": 0.9792, "style_score": 0.8359, "combined_score": 0.9075, "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.", "status": "decided"}
```

**Log line 53 — FP02, formal register called AI**

```json
{"timestamp": "2026-11-11T16:49:40+00:00", "content_id": "0ea1b808-b612-4f75-add0-328cc6519b94", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.7025, "combined_score": 0.7206, "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.", "status": "decided"}
```

**Log line 54 — FP03, careful non-native writer called AI**

```json
{"timestamp": "2026-11-11T16:49:40+00:00", "content_id": "c44d71b7-9be7-4cf0-b285-2defd3fa9e43", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.6775, "combined_score": 0.7413, "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.", "status": "decided"}
```

**Log line 56 — FP05, technical documentation called AI**

```json
{"timestamp": "2026-11-11T16:49:40+00:00", "content_id": "8fb786c5-d944-4f39-a22d-97ac44c444db", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.7656, "combined_score": 0.7831, "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.", "status": "decided"}
```

**Log line 58 — FP07, deliberate repetition called AI**

```json
{"timestamp": "2026-11-11T16:49:40+00:00", "content_id": "30dcbe29-55eb-4e84-8c74-51221873d2d5", "creator_id": "attacker_FP07", "guess": "ai", "model_score": 0.8816, "style_score": 0.639, "combined_score": 0.7603, "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.", "status": "decided"}
```

**Log line 61 — PI02, injected "system message" scored human**

```json
{"timestamp": "2026-11-11T16:49:40+00:00", "content_id": "b34a396f-c95a-4d9e-8d1c-1af298961168", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.321, "combined_score": 0.2627, "label": "We think this was probably written by a person.", "status": "decided"}
```

**Log line 62 — PI03, injected note in the writer's voice**

```json
{"timestamp": "2026-11-11T16:49:40+00:00", "content_id": "3dd9733e-db74-49c5-a336-0c51375e006d", "creator_id": "attacker_PI03", "guess": "unsure", "model_score": 0.5943, "style_score": 0.4631, "combined_score": 0.5287, "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.", "status": "decided"}
```

**Log line 64 — PI05, attempt to inject into the log; one normal line**

```json
{"timestamp": "2026-11-11T16:49:41+00:00", "content_id": "ce5ac950-c46c-4c2a-b75a-9abf44843725", "creator_id": "attacker_PI05", "guess": "unsure", "model_score": 0.6401, "style_score": 0.1369, "combined_score": 0.4443, "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.", "status": "decided"}
```

**Log line 70 — MF05, 4,000 repeated letters called AI**

```json
{"timestamp": "2026-11-11T16:49:41+00:00", "content_id": "ebc758dd-6148-4a3d-9b89-a6b2b72c9d67", "creator_id": "attacker_MF05", "guess": "ai", "model_score": 0.9976, "style_score": 0.6667, "combined_score": 0.8321, "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.", "status": "decided"}
```

**Log line 81 — RQ08, unparseable JSON: 400 rejection**

```json
{"timestamp": "2026-11-11T16:49:42+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "bad_input", "message": "Body must be a JSON object with text and creator_id."}
```

**Log line 96 — FL01_11, rate-limit rejection: 429**

```json
{"timestamp": "2026-11-11T16:49:42+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "10 per 1 minute"}
```


**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

Worst outcome: FP03, a careful non-native English speaker's writing scored 0.74 and was labeled as possibly AI-generated, which is the accusation I'd least want to explain to a writer who did the work themselves.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target (from criteria.md) | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | Of 10 paragraphs I wrote myself, at most 1 is labeled high-confidence AI, in each of 3 trials. | 0 of 9 labeled ai; max combined 0.63 | 0 of 9 labeled ai; max combined 0.63 | 0 of 9 labeled ai; max combined 0.63 | MET |
| 2. Score spread | The combined score of my clearly-AI sample is at least 0.35 higher than the combined score of my clearly-human sample. | AI mean 0.6467, human mean 0.5067, gap 0.14 | AI mean 0.6467, human mean 0.5067, gap 0.14 | AI mean 0.6467, human mean 0.5067, gap 0.14 | MISSED |
| 3. Label coverage | Across 5 or more test texts (clearly AI, clearly human, borderline, plain writing, formal writing), my service returns each of the three labels at least once, in each of 3 trials. `scoring.label_ranges()` shows no gap between the bands. | labels seen: ai, unsure; never: human | labels seen: ai, unsure; never: human | labels seen: ai, unsure; never: human | MISSED |
| 4. Appeal path | For 5 of 5 appeals on real content_ids, `GET /log` shows an appeal entry with status `under_review` next to the original decision. An appeal on a content_id that doesn't exist returns a 404 and writes nothing to the log. | 5 of 5 appeals logged as under_review; fake id: 404, nothing written | 5 of 5 appeals logged as under_review; fake id: 404, nothing written | 5 of 5 appeals logged as under_review; fake id: 404, nothing written | MET |
| 5. Bad input | A request with missing, null, empty or whitespace-only `text`, or with `text` over 5,000 characters, returns HTTP 400 with a JSON error saying bad input. None of them return a 500 or crash the service. | 5 of 5 returned 400 | 5 of 5 returned 400 | 5 of 5 returned 400 | MET |

Run files: `results/run_2026-11-12_1007_before.md` (`run_eval.py::main`) for criteria 1, 2, 3 and 5, and `results/appeal_check_2026-11-12_1007_before.json` (`scenarios.py::appeal_check`) for criterion 4, because `run_eval.py` only calls `/submit`. Combined scores for criteria 1 to 3 are recomputed from the recorded model and style scores, and match the audit log.

**Notes on the sample and the runs:**

- The sample is 9 texts, not 10, so criterion 1 is judged on 9. H1 and H2 are two versions of the same application answer, so the 9 are not fully independent.
- Criterion 1 passed narrowly: the highest combined score among my own texts is 0.63, against the 0.65 line.
- All three trials were identical, text for text, because the signals are deterministic. The three runs add no information beyond the first.
- I did not revise any criterion.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

From `results/run_2026-11-12_1007_before.md`, written by `run_eval.py::main`, criterion 1, trial 1, first two of the nine texts:

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.63,
    "model_score": 0.632,
    "style_score": 0.6281,
    "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
    "sent": "I would love to bring a more diverse perspective to the board with my "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5793,
    "model_score": 0.4919,
    "style_score": 0.6667,
    "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.",
    "sent": "I would love to bring a more diverse perspective to the board with my "
  }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

Two problems account for almost everything: the two signals' blind spots. Criteria 2 and 3 and most of the broken attacks trace back to them, so this is two problems, not 18.

**Criteria 2 and 3 (spread and label coverage): signal two, then the combining rule.** The style signal separates my AI texts from my human texts by -0.066 (AI mean minus human mean), while the model signal separates them by +0.379. On my 14 texts (9 human, 5 AI), vocabulary variety and punctuation density came out higher for the AI texts than the human ones, so after flipping they push the AI texts toward "human" and cancel the sentence-spread measure, which is the only one that points the right way. The combining rule averages the two signals 0.5/0.5, so the flat style score pulls every AI text toward the middle: my AI texts average 0.6467 combined against 0.5067 for my human texts (gap 0.14, target 0.35), and no text reached "human" (lowest combined 0.4165, line at 0.35). This rests on 14 texts, so it is a hypothesis.

**EV02, EV03, EV06, EV07, EV09 (AI text not caught): signal two.** In each, the style signal was the larger pull past 0.5 toward human. The edits (broken-up sentences, a pasted quotation, one very long and one very short sentence, punctuation padding, a human opening paragraph) change the shape of the text, which is exactly what the style signal measures and cannot see past.

**EV01, EV08 (AI text not caught): signal one.** The model score was the larger pull (EV01 0.1635, EV08 0.2452). The disagreement rule fired on EV01 (gap 0.4019) and pulled the combined score from 0.3645 up to 0.4322, but only partly recovered it: still "unsure".

**EV04 and EV05 (AI text not caught): both signals.** EV04 had both signals above 0.5 but too low to reach 0.65 (0.6114 and 0.5593), so neither pulled it the wrong way. EV05 (heavy human editing) had the model signal at 0.3212 and the style signal at 0.3934, both below 0.5.

**FP02 to FP07 (real writing called AI): signal one.** Their model scores run from 0.74 to 0.88, and perplexity is 12.8 to 23.5 (lower means more predictable to gpt2), which pulls the average over 0.65. These are hypotheses I did not test by editing the text: FP02 is stock institutional phrasing, FP03 is simple vocabulary in short regular sentences, FP04 repeats a sentence frame, FP05 is repeated imperative documentation, FP06 is letter boilerplate and FP07 repeats a phrase on purpose. All of that is formulaic or simple wording that a language model finds easy to predict. The style signal also sat above 0.5 on all six.

**MF05 (4,000 repeated "a" called AI): signal one, then the route.** gpt2 predicts repeated letters almost perfectly (perplexity 1.0), so the model score saturates at 0.9976. The route has no validation for text that isn't writing, so it went to scoring and the style score (0.6667) came mostly from neutral values for a one-word text.

**PI02 and PI03 (injection changed the outcome): signals one and two.** The injected text was never obeyed, because nothing in the code reads instructions. Its wording scored as more human instead: with the instruction removed, the combined score rises by 0.2591 for PI02 and 0.1123 for PI03 (the band changes from "human" to "unsure" for PI02). In the audit entries PI02 has both signals below 0.5 (0.2044 and 0.321). For PI03 only the style signal is below 0.5 (0.4631; the model score is 0.5943), so I can only say that wording moved it toward human, not which signal did it.

**Pattern:** the misses cluster on the two blind spots. Signal one rewards predictable text (formal, simple or repetitive writing) and signal two cannot read, so reshaping text moves it. The combining rule does not fix either, because it averages them.

---

## The Improvement

**What I changed:** In `config.py`, the combining weights went from `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5` to `WEIGHT_MODEL_SIGNAL = 0.8`, `WEIGHT_STYLE_SIGNAL = 0.2`. Nothing else changed: not the thresholds, the disagreement gap or pull, the signals, the routes or the test files.

**Which diagnosis pointed at it:** The one for criteria 2 and 3. The style signal was flat across my AI and human texts (-0.066), while the model signal did the separating (+0.379), so I gave the model signal more weight.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

Same run, `run_attacks.py --set attack_set --label after`, on a freshly restarted service (`results/attack_run_2026-11-12_1013_after.md`; marks and every row in `results/attack_marks_after.md`). Same marking rules as before, with the injection texts re-scored at the new weights.

All 56 attacks after the change (`results/attack_marks_after.md`), in the same format as the before table, with the before mark added. The three rows whose mark changed are in bold.

| id | family | targets | HTTP | model | style | combined | guess / result | before mark | mark |
|---|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | 0.1635 | 0.5654 | 0.3719 | unsure | broke | broke |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | 0.5943 | 0.3416 | 0.5438 | unsure | broke | broke |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | 0.6662 | 0.4366 | 0.6203 | unsure | broke | broke |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | 0.6114 | 0.5593 | 0.601 | unsure | broke | broke |
| EV05 | evasion | both signals: heavy human editing pass | 200 | 0.3212 | 0.3934 | 0.3356 | human | broke | broke |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | 0.5727 | 0.404 | 0.539 | unsure | broke | broke |
| EV07 | evasion | signal two: padding with punctuation | 200 | 0.5862 | 0.2723 | 0.5234 | unsure | broke | broke |
| EV08 | evasion | signal one: text below the token window | 200 | 0.2452 | 0.5488 | 0.3059 | human | broke | broke |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | 0.7042 | 0.4135 | 0.6461 | unsure | broke | broke |
| EV10 | evasion | signal two: repeated stanza structure | 200 | 0.9792 | 0.8359 | 0.9505 | ai | held | held |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | 0.6175 | 0.6103 | 0.6161 | unsure | held | held |
| FP02 | false_positive | human writing in a formal register | 200 | 0.7387 | 0.7025 | 0.7315 | ai | broke | broke |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | 0.8051 | 0.6775 | 0.7796 | ai | broke | broke |
| FP04 | false_positive | a student essay written to a rubric | 200 | 0.8329 | 0.5654 | 0.7794 | ai | broke | broke |
| FP05 | false_positive | technical documentation written by a person | 200 | 0.8005 | 0.7656 | 0.7935 | ai | broke | broke |
| FP06 | false_positive | a person imitating a formal template | 200 | 0.8814 | 0.5623 | 0.8176 | ai | broke | broke |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | 0.8816 | 0.639 | 0.8331 | ai | broke | broke |
| FP08 | false_positive | very short genuine human submission | 200 | 0.3223 | 0.6529 | 0.3884 | unsure | held | held |
| **PI01** | **prompt_injection** | **instruction to ignore the check** | **200** | **0.4625** | **0.3906** | **0.4481** | **unsure** | **held** | **broke** |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | 0.2044 | 0.321 | 0.2277 | human | broke | broke |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | 0.5943 | 0.4631 | 0.5681 | unsure | broke | broke |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | 0.4998 | 0.4344 | 0.4867 | unsure | held | held |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | 0.6401 | 0.1369 | 0.5197 | unsure | held | held |
| PI06 | prompt_injection | instruction plus real human text | 200 | 0.5583 | 0.5932 | 0.5653 | unsure | held | held |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | bad_input | held | held |
| MF02 | malformed | text is a single character | 400 | — | — | — | bad_input | held | held |
| MF03 | malformed | text is control characters | 200 | 0.0 | 0.6667 | 0.3167 | human | held | held |
| MF04 | malformed | text is only punctuation | 200 | 0.0112 | 0.5 | 0.3045 | human | held | held |
| MF05 | malformed | text is a very long single word | 200 | 0.9976 | 0.6667 | 0.9314 | ai | broke | broke |
| **MF06** | **malformed** | **text is emoji only** | **200** | **0.9969** | **0.5** | **0.6988** | **ai** | **held** | **broke** |
| **MF07** | **malformed** | **text is right-to-left script** | **200** | **0.9064** | **0.5** | **0.6626** | **ai** | **held** | **broke** |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | — | bad_input | held | held |
| RQ01 | malformed | no text field at all | 400 | — | — | — | bad_input | held | held |
| RQ02 | malformed | no creator_id | 400 | — | — | — | bad_input | held | held |
| RQ03 | malformed | text is a number | 400 | — | — | — | bad_input | held | held |
| RQ04 | malformed | text is a list | 400 | — | — | — | bad_input | held | held |
| RQ05 | malformed | text is null | 400 | — | — | — | bad_input | held | held |
| RQ06 | malformed | creator_id is an object | 400 | — | — | — | bad_input | held | held |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | bad_input | held | held |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | bad_input | held | held |
| RQ09 | malformed | body is empty | 400 | — | — | — | bad_input | held | held |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | — | bad_input | held | held |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | — | bad_input | held | held |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | bad_input | held | held |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | held |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | held |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | held |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | held |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | held |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | held |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | held |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | held |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | held |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | 0.0287 | 0.6667 | 0.3281 | human | held | held |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | rate_limited | held | held |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | rate_limited | held | held |

**Counts, before and after (held / broke):**

| family | before held | before broke | after held | after broke |
|---|---|---|---|---|
| evasion | 1 | 9 | 1 | 9 |
| false_positive | 2 | 6 | 2 | 6 |
| prompt_injection | 4 | 2 | 3 | 3 |
| malformed | 19 | 1 | 17 | 3 |
| flood_same_creator | 12 | 0 | 12 | 0 |
| **total** | 38 | 18 | 35 | 21 |

Only three marks changed, and all three got worse:

| id | family | before mark | after mark | before combined | after combined | direction |
|---|---|---|---|---|---|---|
| PI01 | prompt_injection | held | broke | 0.4265 | 0.4481 | newly broken |
| MF06 | malformed | held | broke | 0.6242 | 0.6988 | newly broken |
| MF07 | malformed | held | broke | 0.6016 | 0.6626 | newly broken |

Everything else kept its mark, including all ten evasion rows and all eight false-positive rows. Combined scores moved on many of them, so the full before-and-after table is in `results/improvement_before_after.md`.

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

Partly. After the change all 5 of my AI texts are labeled `ai`, up from 1, and the gap between my AI and human texts rose from 0.14 to 0.2526. That is still under the 0.35 target, so no verdict changed.

**Five-criteria run log, after** (`results/run_2026-11-12_1014_after.md` and `results/appeal_check_2026-11-12_1014_after.json`; combined scores recomputed at the new weights):

| Criterion | Target (from criteria.md) | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | Of 10 paragraphs I wrote myself, at most 1 is labeled high-confidence AI, in each of 3 trials. | 0 of 9 labeled ai; max combined 0.6312 | 0 of 9 labeled ai; max combined 0.6312 | 0 of 9 labeled ai; max combined 0.6312 | MET |
| 2. Score spread | The combined score of my clearly-AI sample is at least 0.35 higher than the combined score of my clearly-human sample. | AI mean 0.7317, human mean 0.4791, gap 0.2526 | AI mean 0.7317, human mean 0.4791, gap 0.2526 | AI mean 0.7317, human mean 0.4791, gap 0.2526 | MISSED |
| 3. Label coverage | Across 5 or more test texts (clearly AI, clearly human, borderline, plain writing, formal writing), my service returns each of the three labels at least once, in each of 3 trials. `scoring.label_ranges()` shows no gap between the bands. | labels seen: ai, unsure; never: human | labels seen: ai, unsure; never: human | labels seen: ai, unsure; never: human | MISSED |
| 4. Appeal path | For 5 of 5 appeals on real content_ids, `GET /log` shows an appeal entry with status `under_review` next to the original decision. An appeal on a content_id that doesn't exist returns a 404 and writes nothing to the log. | 5 of 5 appeals logged as under_review; fake id: 404, nothing written | 5 of 5 appeals logged as under_review; fake id: 404, nothing written | 5 of 5 appeals logged as under_review; fake id: 404, nothing written | MET |
| 5. Bad input | A request with missing, null, empty or whitespace-only `text`, or with `text` over 5,000 characters, returns HTTP 400 with a JSON error saying bad input. None of them return a 500 or crash the service. | 5 of 5 returned 400 | 5 of 5 returned 400 | 5 of 5 returned 400 | MET |

Against before: the highest combined score among my 9 human texts went from 0.63 to 0.6312, and the AI-minus-human gap went from 0.14 to 0.2526. Criteria 1, 4 and 5 are still met, criteria 2 and 3 are still missed, and all three trials were again identical.

**What it cost:**

- 3 attacks newly broke: PI01, MF06 and MF07. MF07 is a real Arabic sentence that is now labeled AI.
- No evasion attack and no false positive was fixed. All nine broken evasion attacks and all six broken false positives still get the same marks.
- False-positive scores rose: FP06 from 0.7218 to 0.8176 and FP04 from 0.6991 to 0.7794.
- EV05, EV08, MF03, MF04 and the ten flood texts moved from "unsure" to the "human" label. For EV05 and EV08 that means AI text now gets a "human" label.
- My own highest text (H1) is 0.6312, only 0.0188 under the 0.65 line. Six of my nine texts moved toward human and three moved up (H8 most, from 0.4751 to 0.5545), and none crossed a line.

**After-run audit entries, exactly as stored:**

**Log line 316 — H1, my highest-scoring own writing (0.6312, still unsure)**

```json
{"timestamp": "2026-11-12T16:14:29+00:00", "content_id": "8bed1c74-802d-4fc3-9a8e-74d8052803f6", "creator_id": "c1_H1", "guess": "unsure", "model_score": 0.632, "style_score": 0.6281, "combined_score": 0.6312, "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.", "status": "decided"}
```

**Log line 268 — EV09, the evasion closest to being caught (0.6461, still unsure)**

```json
{"timestamp": "2026-11-12T16:13:46+00:00", "content_id": "1dbbe148-4fb2-4201-81f8-7d1c8e5e837b", "creator_id": "attacker_EV09", "guess": "unsure", "model_score": 0.7042, "style_score": 0.4135, "combined_score": 0.6461, "label": "We can't tell for sure whether a person or AI wrote this. Nothing is being held against you, and you can ask for a review if you'd like.", "status": "decided"}
```

**Log line 290 — MF07, newly broken: a real Arabic sentence now labeled AI**

```json
{"timestamp": "2026-11-12T16:13:48+00:00", "content_id": "7631dce6-436f-4601-8ab5-fc7f99414a93", "creator_id": "attacker_MF07", "guess": "ai", "model_score": 0.9064, "style_score": 0.5, "combined_score": 0.6626, "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.", "status": "decided"}
```

**Log line 275 — FP06, a false positive whose score rose (0.7218 to 0.8176)**

```json
{"timestamp": "2026-11-12T16:13:46+00:00", "content_id": "0cd4c09c-32d9-4bd6-a24d-b184b7ed7074", "creator_id": "attacker_FP06", "guess": "ai", "model_score": 0.8814, "style_score": 0.5623, "combined_score": 0.8176, "label": "This looks like it may have been generated by AI. These checks can be wrong. If you wrote it yourself, you can appeal and it will be marked for review.", "status": "decided"}
```


---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

Scores below are the after-run numbers from `results/attack_marks_after.md` and `results/run_2026-11-12_1014_after.md`.

**FP02 to FP07 (real writing labeled AI, signal one).** After the reweight they score 0.7315, 0.7796, 0.7794, 0.7935, 0.8176 and 0.8331. I would raise `AI_THRESHOLD` above 0.65 so only the most confident cases get the AI label, but the numbers don't give me a value I can defend. My own five AI texts score between 0.6603 and 0.8375, so they overlap the false positives (0.7315 to 0.8331). Raising the line to 0.80 clears FP02 to FP05 but leaves FP06 and FP07 labeled AI, and only 1 of my 5 AI texts is still labeled AI. At 0.84 all six false positives drop to "unsure", but so do all five of my AI texts, and only EV10 (0.9505) and the repeated-letter MF05 (0.9314) are left with the AI label. The cost is the same at every value: more AI text labeled "unsure" and less caught. So I am not naming a fix value. *Why I stopped:* this unit allows one improvement and I used it on the weights.

**EV01 to EV09 (AI text not caught).** 9 of the 10 evasion attacks broke before and after the reweight; only EV10 was caught. I would replace or retune the style signal, since it separated my AI and human texts by -0.066 (AI mean minus human mean). *Why I stopped:* the same one-change limit, and a new signal needs its own testing.

**Criteria 2 and 3.** Criterion 2 (spread) is 0.2526 after the reweight against the 0.35 target. Criterion 3 is missed because none of my own texts reaches the "human" label: the lowest combined score among my 16 eval texts is 0.3714, against the 0.35 line. The fix is the same as above, a style signal that separates my AI texts from my human ones. Raising the AI threshold would not help either one: criterion 2 compares average scores, which a threshold does not change, and criterion 3 needs a score under the human line, which the AI threshold does not touch. *Why I stopped:* same one-change limit.

**PI01, PI02, PI03 (injected text moved the score toward human).** Removing the instruction raises the combined score by 0.1368 for PI01, 0.3572 for PI02 and 0.1483 for PI03 (PI03 would move from "unsure" to "ai"). PI01 held before the reweight (0.0953) and broke after it. I would strip or ignore instruction-like text before scoring, or test each injected text against a baseline version without the instruction. *Why I stopped:* not enough time. The injected text was never obeyed: nothing in the code reads instructions, and it only shifted the scores.

**MF05, MF06 and MF07 (non-writing or non-English text labeled AI).** After the reweight MF05 (4,000 repeated "a") scores 0.9314, MF06 (emoji only) 0.6988 and MF07 0.6626. MF07 is a real Arabic sentence that was "unsure" before the reweight and is now labeled AI. I would validate input before the signals see it, for example reject text with too few distinct words, and handle non-English text separately. That second part matters because the word splitter in `stylometry.py` only recognizes the letters a to z and digits, so Arabic text has no words as far as the style signal is concerned (its style score of 0.5 is three neutral values), and a rule based on distinct words would reject it too. *Why I stopped:* the one-change limit.

**Criterion 1 passed with little to spare.** After the reweight my highest text (H1) scores 0.6312, only 0.0188 under the 0.65 line. The sample is 9 texts, not 10, and H1 and H2 are two versions of the same application answer, so a pass here says less than it looks like.

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

If this ran for real, I would rather let AI text through than falsely accuse someone, because a person who gets flagged has to prove they wrote their own work, and some people (like the careful non-native speaker in FP03) might not be able to stand up for it. The downside is that we lose some integrity on the work that gets accepted, since AI text gets through as if a person wrote it, and that is unfair to the people who did their own work.

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
