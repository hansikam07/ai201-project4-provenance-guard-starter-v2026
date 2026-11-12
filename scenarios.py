"""
What my test runs. ← UNIT 8, MILESTONE 3

Each of my five criteria (see criteria.md) has something run against it.
`run_eval.py` runs everything in SCENARIOS three times. It only calls /submit,
so criterion 4 (appeals) lives in `appeal_check()` at the bottom of this file
and is run separately:

    .venv/bin/python scenarios.py appeals before

Every scenario here uses "bodies" so each submission has its own creator_id
(c1_H1, c2_AI3, ...) and the rate limit is never tripped. Each body is sent
three times in total, once per trial.

The human texts H1..H9 are my own writing, verbatim, typos included.
The AI texts and the mixed texts were written once and not tuned.
"""

# ── My own writing (verbatim, typos and all) ─────────────────────────────────

H1 = """I would love to bring a more diverse perspective to the board with my interests and background. I will be a helpful, collaborative member that helps bring this club forward, and what better honor than doing so alongside a board full of other smart women! As a leader of this organization, I would also love to serve as a mentor to upcoming students and guide them through all the doubts I once experienced. A position with WiCS will help me build experience and expand my network, especially as a first-gen college student this opportunity will be very significant for me. I would also be grateful for the community, friends, and mentors I could gain from this position."""

H2 = """I would love to bring a more diverse perspective to the board with my interests and background.   I will be a helpful, collaborative member that brings this club forward and what better honor than doing with a board full of other smart women! and as leader of this organization I would like to serve as a mentor to upcoming students and guide them through all the doubts I once experienced. A position with WiCS will help me build more experience as well as a better network, especially as someone that came in without much tech experience or exposure this is an opportunity that will help me learn more. I would also be grateful for the community and friends and mentors that I could gain from this position."""

H3 = """A dimension of the story that can be explored using the framework of deontology is the relationships and the duties within the story. Deontology is about the innate duties that belong to relationships, here we have mother-son, mil-dil, grandma-grandchild, also caretaker-patient relationship with the android. In this story particularly we can explore the relationship between the different characters to see how the duty of the relationship is being fulfilled or not, also whether the relationship between them is still the same or maybe one could interpret it as a change in relationship due to Mildred’s cognitive decline(is it the same relationship even if she doesn’t remember?) Particularly the scenes where android notes how Paul would constantly care for Mildred now hasn’t been to visit in months. Susan rarely visited and somehow towards teh end when the rets of teh characters visits declined Susan made an appearance. And then for Anna there can also be an exploration of conflicting duties, her duty as a grandchild to grandmother but also her duties to her current obligation as a busy young adult. This can help us better understand the relationships between the characters, initially help us first understand what the relationships could be with a deontological view and later can build a more complex understanding of the relationships by adding the other frameworks."""

H4 = """A dimension of the story to further explore with the framework of virtue ethics is the scene when the fire started in Mildred home and the android was actually unsure to a level of what to do. It didn't have the time to comfort Mildred like it usually did. This puzzled me very much because I thought that the android only had the emulations of the different members of Mildred’s family and it’s empathy net that was programmed in, therefore I didn’t see how habituation could be possible when u work by emulating others. However here there was no time for the android to make its usually calculated move and more so worked off its habituation to protect Mildred? While actions are not continuous however the empathy net was. (Is this going into whether the android is conscious or not?) This will help shed more light on the values of the robot and Paul, for Paul it will add another way to approach understanding his character, for the android it will help deliver a better understanding of how the android functioned within this family, understanding how the android virtues were will."""

H5 = """At first it felt really hard to see the framework of communitarianism in this story however there are elements that can be. However there are a few instances in which we could see how more of a communitarian framework could lead the characters to make different choices. A few instances can be when Paul reaches out to his dad Henry being emulated by the android]. Throughout this story we see a lot more of Paul playing the role of caretaker for his mom (dad also passed away) but when he was also hit with his mother’s passing he too needed some comfort thus he reached out to the emulation of Henry. Up until then he had never actually interacted with the android or its emulation in the manner of receiving emotional comfort. Since he was very cognizant of the fact that this isn;t his father and is an emulation him still reaching out shows a major emotional toll on him that is causing him to seek comfort however he can. With more communitarianism value within these characters they wouldn’t have outsourced the emotional labor which would have now better emotionally equipped him for the passing of his mother. This framework and this moment in the story will help understand the effect of the use of the robot not just in relation to Mildred and whether it was an ethical choice but also how the use of the android has effect Paul, Susan and Anna emotionally and changed how they react to Mildred passing due to not approaching the end of life care by themselves."""

H6 = """One dimension to further explore can be how the android decision making process, when it contemplates what to say based on how Mildred might respond, has underlying utilitarian structure. It is seen evaluation acting like the emulation and sticking to the correct characteristic responses versus drawing on it’s empathy net to see what Mildred might actually want and weigh which response might actually result in less harm. The android is seen actually considering percentages and math when evaluating. More so than sticking to the emulation the android determines its action based on the outcome which is Mildred response and comfort. Compared to this Paul and the other family members just make decisions and action regarding Mildred without any of this consideration. This can help us explore the "benefits" of using eth android for the carework versus just having the family or other humans do it. Humans rarely evaluate each and every thing they say with an actual utilitarian framework and more of whatever decision feels like it will yield the best outcome instead of actually checking. This can be important to see the android as more than just a tool for the family and consider how the android actually functions in regards to Mildred and the family. This can also raise questions about the android itself, whether it has its own thoughts or it is just a complication of all the family members it tries to emulate and the empathy net that's built in."""

H7 = """From identifying professionals, to reaching out, following up, prompt replies and setting up times I have a lot of experiences reaching out to professionals since I co-hosted a podcast for a club. I have worked with government officials so I know the importance of follow ups and prompt replies. And over my CS career I have become involved in various organizations that focus on professional development and opportunities so I have the exposure to pose new event ideas and collaborations for WiCS."""

H8 = """I have been a part of the WiCS Dev Project in the past, so I am familiar with how the Dev Project works, and I have experience with web development both through personal projects, hackathons, and the WiCyS Web Dev committee. I have built with Java, Python, JavaScript, HTML, CSS, TypeScript, and C#. I also have backend experience and have worked with APIs, and have used Vercel, MongoDB, Supabase, Postman, and Figma. Additionally, I really enjoy helping others understand concepts and gain new skills, so I would love to help people with their questions and issues."""

H9 = """Many, many WiCS events later, my answer remains the Scavenger Hunt! It was a great way to make friends and hang out with them when I was a new and unfamiliar student. Becoming familiar with the faculty was also really helpful, and after doing it again this year and seeing how much I had progressed (I answered like one the first time and did five this year), getting to do it again with my professor and friends was a top experience that I hope future members can also enjoy."""

HUMAN = [H1, H2, H3, H4, H5, H6, H7, H8, H9]

# ── Clearly-AI texts (written once, not tuned) ───────────────────────────────

AI1 = """Effective time management is an essential skill for students and professionals alike. First, it is important to prioritize tasks based on urgency and importance. Second, breaking large projects into smaller, manageable steps can reduce stress and improve productivity. Additionally, minimizing distractions allows individuals to maintain focus and achieve better results. In conclusion, adopting consistent time management strategies can lead to greater success and a healthier work-life balance."""

AI2 = """Artificial intelligence is transforming the way organizations operate in the modern world. It offers numerous benefits, including increased efficiency, improved decision-making, and enhanced customer experiences. However, it is important to consider the ethical implications of deploying these technologies responsibly. Organizations should establish clear guidelines for data privacy, transparency, and accountability. By embracing innovation while maintaining ethical standards, businesses can unlock the full potential of AI."""

AI3 = """Regular physical exercise provides a wide range of benefits for both the body and the mind. Key advantages include improved cardiovascular health, stronger muscles, and better sleep quality. Furthermore, exercise has been shown to reduce symptoms of anxiety and depression. It is recommended that adults engage in at least 150 minutes of moderate activity each week. Ultimately, incorporating movement into daily routines is one of the most effective ways to enhance overall well-being."""

AI4 = """Climate change represents one of the most significant challenges facing humanity today. Rising global temperatures contribute to more frequent extreme weather events, sea level rise, and loss of biodiversity. To address this issue, governments, businesses, and individuals must work together to reduce greenhouse gas emissions. Key solutions include transitioning to renewable energy, improving energy efficiency, and protecting natural ecosystems. Through collective action and sustained commitment, a more sustainable future is within reach."""

AI5 = """Building strong communication skills is crucial for success in any professional environment. To begin with, active listening ensures that team members feel heard and valued. Moreover, clear and concise writing helps prevent misunderstandings and saves valuable time. It is also beneficial to seek feedback regularly and adapt one's approach accordingly. Overall, investing in communication skills fosters collaboration, trust, and long-term career growth."""

AI = [AI1, AI2, AI3, AI4, AI5]

# ── Mixed human-plus-AI texts (written once, not tuned) ──────────────────────

MIX1 = H7 + " " + (
    "Furthermore, building strong professional relationships is essential for fostering "
    "collaboration and driving organizational success. By leveraging effective "
    "communication strategies, student leaders can create meaningful opportunities for "
    "growth and engagement across the community."
)

MIX2 = (
    "Student organizations play a vital role in fostering community and supporting "
    "personal growth. They provide valuable opportunities for networking, skill "
    "development, and leadership. "
) + H9

MIXED = [MIX1, MIX2]


def _bodies(prefix: str, groups: list[tuple[str, list[str]]]) -> list[dict]:
    """One body per text, each with its own creator_id like c2_AI3."""
    return [
        {"text": text, "creator_id": f"{prefix}_{tag}{i}"}
        for tag, texts in groups
        for i, text in enumerate(texts, 1)
    ]


SCENARIOS = [
    # 1. At most 1 of my own texts labelled high-confidence AI, every trial.
    {
        "name": "false positives",
        "criterion": 1,
        "bodies": _bodies("c1", [("H", HUMAN)]),
    },
    # 2. Mean combined(AI sample) - mean combined(human sample) >= 0.35.
    #    Order matters: the first 9 bodies are human, the last 5 are AI.
    {
        "name": "score spread",
        "criterion": 2,
        "bodies": _bodies("c2", [("H", HUMAN), ("AI", AI)]),
    },
    # 3. All three labels appear across the set, every trial.
    {
        "name": "label coverage",
        "criterion": 3,
        "bodies": _bodies("c3", [("H", HUMAN), ("AI", AI), ("MIX", MIXED)]),
    },
    # 5. Bad input answers 400 with a JSON error, never a 500.
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "c5_missing"},                          # no text field
            {"text": None, "creator_id": "c5_null"},
            {"text": "", "creator_id": "c5_empty"},
            {"text": "   \n\t  ", "creator_id": "c5_whitespace"},
            {"text": "word " * 1001, "creator_id": "c5_toolong"},  # 5,005 characters
        ],
    },
]


# ── Criterion 4: appeals (run_eval.py can only call /submit, so this is separate)

def appeal_check(url: str = "http://127.0.0.1:5000", trials: int = 3, label: str = "") -> dict:
    """
    5 appeals on fresh submissions, each checked against GET /log, plus one
    appeal on a content_id that doesn't exist. Repeated for `trials` trials.

    A real appeal counts as OK when /appeal answers 200 with status
    "under_review", AND the log holds an appeal entry with status
    "under_review" that comes after the original "decided" entry.
    The fake id counts as OK when /appeal answers 404 {"error": "not_found"}
    AND the log did not grow.

    Writes results/appeal_check_<date>[_label].json and returns the same data.
    """
    import datetime as dt
    import json

    import requests

    import config

    def log_entries():
        return requests.get(f"{url}/log", timeout=30).json()["entries"]

    appeal_texts = [H7, H8, H9, H1, H2]
    all_trials = []

    for trial in range(1, trials + 1):
        appeals = []
        for i, text in enumerate(appeal_texts, 1):
            creator = f"c4_t{trial}_{i}"
            sub = requests.post(f"{url}/submit", json={"text": text, "creator_id": creator}, timeout=90)
            sub_json = sub.json()
            content_id = sub_json.get("content_id")
            reasoning = f"I wrote this myself (appeal check, trial {trial}, appeal {i})."
            resp = requests.post(f"{url}/appeal", json={"content_id": content_id, "reasoning": reasoning}, timeout=30)
            entries = [e for e in log_entries() if e.get("content_id") == content_id]
            decision_idx = next((k for k, e in enumerate(entries) if e.get("status") == "decided" and "event" not in e), None)
            appeal_idx = next((k for k, e in enumerate(entries) if e.get("event") == "appeal"), None)
            ok = (
                sub.status_code == 200
                and resp.status_code == 200
                and resp.json().get("status") == "under_review"
                and decision_idx is not None
                and appeal_idx is not None
                and appeal_idx > decision_idx
                and entries[appeal_idx].get("status") == "under_review"
            )
            appeals.append({
                "creator_id": creator,
                "submit_status": sub.status_code,
                "content_id": content_id,
                "appeal_status": resp.status_code,
                "appeal_response": resp.json(),
                "log_entries_for_id": entries,
                "ok": ok,
            })

        before = len(log_entries())
        fake = requests.post(f"{url}/appeal", json={"content_id": "no-such-content-id", "reasoning": "checking"}, timeout=30)
        after = len(log_entries())
        fake_result = {
            "status": fake.status_code,
            "response": fake.json(),
            "log_entries_before": before,
            "log_entries_after": after,
            "ok": fake.status_code == 404 and fake.json() == {"error": "not_found"} and before == after,
        }
        all_trials.append({"trial": trial, "appeals": appeals, "fake_id": fake_result})

    config.RESULTS_DIR.mkdir(exist_ok=True)
    suffix = f"_{label}" if label else ""
    path = config.RESULTS_DIR / f"appeal_check_{dt.datetime.now().strftime('%Y-%m-%d_%H%M')}{suffix}.json"
    path.write_text(json.dumps(all_trials, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {path.relative_to(config.ROOT)}")
    for t in all_trials:
        ok = sum(a["ok"] for a in t["appeals"])
        print(f"trial {t['trial']}: {ok}/5 appeals ok, fake id ok: {t['fake_id']['ok']}")
    return {"trials": all_trials, "file": str(path)}


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "appeals":
        appeal_check(label=sys.argv[2] if len(sys.argv) > 2 else "")
    else:
        print("Usage: python scenarios.py appeals [label]")
