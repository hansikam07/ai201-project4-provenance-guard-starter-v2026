"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures ───────────────────────────────────────────────────────
# Each measure returns a float from 0 to 1 where HIGHER MEANS MORE HUMAN-LIKE.
# style_signal flips all three, so the final score runs the same way as signal
# one: higher means more likely AI. The *_RANGE constants are where a raw value
# maps to the ends of 0..1; they are rough guesses, tuned by eye on a handful of
# texts, not fitted to data.

SPREAD_FULL = 0.8              # sentence-length CV at or above this scores 1.0
TTR_LOW, TTR_HIGH = 0.5, 0.9   # first-100-word type-token ratio, mapped to 0..1
PUNCT_FULL = 0.2               # marks per word at or above this scores 1.0
TTR_WINDOW = 100               # words used for type-token ratio

# Commas, semicolons, colons, "(" (one per pair), ! and ?, em/en dashes, "--",
# and a hyphen standing alone between spaces (a typed dash). Hyphens inside
# words like "well-known" are not counted.
_PUNCT = re.compile(r"[,;:(!?]|—|–|--|(?<=\s)-(?=\s)")


def _clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies.

    Scale: 0..1. Computed as stdev / mean of sentence lengths in words (so a
    long text and a short one compare), divided by SPREAD_FULL and clamped.
    Direction: HIGH = uneven sentences = more human. LOW = marching in step.
    A text with fewer than two sentences has no spread, so it returns a neutral
    0.5 instead of raising.

    Cannot see: why the lengths vary. Splitting an AI paragraph into a few
    fragments, or gluing sentences together, moves it without changing who
    wrote it. It also trusts the rough splitter: abbreviations ("Dr. Smith")
    and unpunctuated text produce wrong sentence counts.
    """
    lengths = [len(words(sent)) for sent in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.5
    mean = statistics.mean(lengths)
    cv = statistics.stdev(lengths) / mean
    return _clamp01(cv / SPREAD_FULL)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words, on the first 100 words only.

    Scale: 0..1. The raw ratio is measured on a fixed 100-word window so long
    texts aren't penalised for repeating common words, then stretched from
    0.5-0.9 to 0..1 and clamped. Under 10 words is too little to judge and
    returns a neutral 0.5.
    Direction: HIGH = varied vocabulary = more human. LOW = repetitive = AI-ish.

    Cannot see: which words. Typos and invented spellings count as new unique
    words, so adding mistakes to AI text raises this. It also ignores everything
    past word 100, and a short text on a narrow topic repeats words naturally.
    """
    toks = words(text)[:TTR_WINDOW]
    if len(toks) < 10:
        return 0.5
    ratio = len(set(toks)) / len(toks)
    return _clamp01((ratio - TTR_LOW) / (TTR_HIGH - TTR_LOW))


def punctuation_density(text: str) -> float:
    """
    How much punctuation per word, counting commas, semicolons, colons,
    parentheses, dashes, ! and ? (not full stops or apostrophes).

    Scale: 0..1. Marks per word divided by PUNCT_FULL, clamped.
    Direction: HIGH = more and more varied punctuation = more human. LOW =
    plain, sparse punctuation = AI-ish. This is the weakest of the three
    directional assumptions: models also use commas and colons heavily, and
    some careful humans barely use any.

    Cannot see: whether the punctuation is right or meaningful. Sprinkling in
    commas or dashes raises it, and it says nothing about the words. It counts
    marks, not variety, so twenty commas score the same as a mix.
    """
    n_words = len(words(text))
    if n_words == 0:
        return 0.5
    marks = len(_PUNCT.findall(text))
    return _clamp01((marks / n_words) / PUNCT_FULL)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0-1 score. **Higher means more likely AI.**

    The three measures already sit on 0..1 and all point toward "human" when
    high, so each is flipped (1 - x) and the three are averaged with equal
    weight. Equal weights are a choice, not a finding.

    Cannot see: meaning, facts, or intent. It only reads shape, so anything that
    reshapes the text moves it.
    """
    parts = [
        1.0 - sentence_length_spread(text),
        1.0 - type_token_ratio(text),
        1.0 - punctuation_density(text),
    ]
    return round(_clamp01(sum(parts) / len(parts)), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
