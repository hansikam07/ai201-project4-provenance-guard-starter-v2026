# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives

Of 10 paragraphs I wrote myself, at most 1 is labeled high-confidence AI, in each of 3 trials.

**Why this target:** I don't want to wrongly accuse a real writer, but I also don't want AI text to go unflagged, so I allow only 1 in 10. A wrongly accused writer loses trust in the site, while a missed AI post costs the site much less.

---

## 2. Score spread

The combined score of my clearly-AI sample is at least 0.35 higher than the combined score of my clearly-human sample.

**Why this target:** My "unsure" band is 0.30 wide (0.35 to 0.65). A gap of 0.35 means a clearly-AI and a clearly-human sample can land in different labels. A smaller gap would let both end up "unsure", and the score wouldn't tell anyone anything.

---

## 3. Label coverage

Across 5 or more test texts (clearly AI, clearly human, borderline, plain writing, formal writing), my service returns each of the three labels at least once, in each of 3 trials. `scoring.label_ranges()` shows no gap between the bands.

**Why this target:** If a label can never appear, the system is broken without anyone noticing. My style signal may barely vary, which would make one label unreachable.

---

## 4. Appeal path

For 5 of 5 appeals on real content_ids, `GET /log` shows an appeal entry with status `under_review` next to the original decision. An appeal on a content_id that doesn't exist returns a 404 and writes nothing to the log.

**Why this target:** Wrong flags can happen, so the appeal is the only thing a wrongly accused writer can do. If even one appeal isn't recorded, that writer has no recourse.

---

## 5. Bad input

A request with missing, null, empty or whitespace-only `text`, or with `text` over 5,000 characters, returns HTTP 400 with a JSON error saying bad input. None of them return a 500 or crash the service.

**Why this target:** A request with no text gives the detector nothing to test, and the detector raises an error on very short text. The detector only reads about 400 tokens, so I don't accept far more than it can use.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
