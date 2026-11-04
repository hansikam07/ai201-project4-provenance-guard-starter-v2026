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
- **A false positive.** My plain-human calibration text scored model 0.7846, style 0.7475 and combined 0.7661, and the service guessed "ai". A person wrote that style of text; the service accused it.
- **It happened again.** A human text with very uniform sentence lengths scored combined 0.7831 and was also guessed "ai".
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

- *What I asked for:* a draft of five acceptance criteria to start from.
- *What came back:* five criteria with defaults (at most 2 false positives in 10, a 0.30 score gap, a 10,000 character cap).
- *What I changed:* I made the false-positive target tighter, at most 1 in 10, and wrote my own reasons. I raised the score gap to 0.35 so it matched my 0.30-wide unsure band, and I cut the text cap to 5,000 characters because the detector only reads about 400 tokens.

**Moment 2**

- *What I asked for:* Claude Code to build /submit, the stylometry signal and the combining rule, then run five calibration texts.
- *What came back:* a working service and a table in which a plain human paragraph scored 0.77 and was guessed AI.
- *What I changed:* nothing in the thresholds. I chose to keep the 0.35 and 0.65 bands and report the false positive as a finding rather than tune it away on five samples.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



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
