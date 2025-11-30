from flask import Flask, render_template, request, jsonify
from chatbot.model import CollegeChatbot
from chatbot.small_talk import handle_small_talk
from deep_translator import GoogleTranslator  # translation
from difflib import SequenceMatcher          # NEW: fuzzy matching
import re                                    # NEW: for splitting words

app = Flask(__name__)

FAQ_FILE = "data/faq_data.json"
bot = CollegeChatbot(FAQ_FILE)

# ------------ COURSES: SCHOOLS + ANSWERS ------------

COURSE_SCHOOL_OPTIONS = [
    {"number": 1, "question": "School of Engineering"},
    {"number": 2, "question": "School of Computer Applications"},
    {"number": 3, "question": "School of Commerce & Management"},
    {"number": 4, "question": "School of Basic & Applied Sciences"},
    {"number": 5, "question": "School of Health Sciences"},
    {"number": 6, "question": "School of Arts, Design & Humanities"},
    {"number": 7, "question": "School of Design & Digital Transmedia"},
    {"number": 8, "question": "School of Law"},
    {"number": 9, "question": "Online Degree Programs"},
    {"number": 10, "question": "Medical College (CDSIMER)"}
]

COURSE_SCHOOL_ANSWERS = {
    1: (
        "School of Engineering – Courses:\n\n"
        "• B.Tech Computer Science & Engineering (CSE)\n"
        "• B.Tech CSE (AI & Machine Learning)\n"
        "• B.Tech CSE (Data Science)\n"
        "• B.Tech CSE (Cyber Security)\n"
        "• B.Tech AI & Robotics\n"
        "• B.Tech Computer Science & Technology\n"
        "• B.Tech Electronics & Communication Engineering (ECE)\n"
        "• B.Tech Mechanical Engineering\n"
        "• B.Tech Aerospace Engineering\n"
        "• M.Tech specialisations (CSE and allied fields)"
    ),
    2: (
        "School of Computer Applications – Courses:\n\n"
        "• BCA\n"
        "• BCA (AI & ML)\n"
        "• BCA (Data Science)\n"
        "• BCA (Cloud & Cyber Security)\n"
        "• MCA (Master of Computer Applications)"
    ),
    3: (
        "School of Commerce & Management – Courses:\n\n"
        "• BBA\n"
        "• B.Com (general / professional / honours options)\n"
        "• MBA\n"
        "• Ph.D programmes in Management / Commerce"
    ),
    4: (
        "School of Basic & Applied Sciences – Courses:\n\n"
        "• B.Sc Biotechnology\n"
        "• B.Sc Genetics\n"
        "• B.Sc Microbiology\n"
        "• B.Sc Biochemistry\n"
        "• B.Sc Chemistry\n"
        "• B.Sc Physics\n"
        "• B.Sc Mathematics\n"
        "• M.Sc programmes in selected science disciplines"
    ),
    5: (
        "School of Health Sciences – Courses:\n\n"
        "• B.Sc Imaging Technology\n"
        "• B.Sc Medical Lab Technology (MLT)\n"
        "• B.Sc Operation Theatre Technology\n"
        "• B.Sc Anaesthesia Technology\n"
        "• B.Sc Cardiac Care Technology\n"
        "• B.Sc Emergency & Trauma Care\n"
        "• Physiotherapy programmes\n"
        "• Nursing programmes\n"
        "• Pharmacy programmes (B.Pharm / M.Pharm via College of Pharmaceutical Sciences)"
    ),
    6: (
        "School of Arts, Design & Humanities – Courses:\n\n"
        "• BA Journalism & Mass Communication\n"
        "• BA in related arts / media / humanities areas (as notified by DSU)"
    ),
    7: (
        "School of Design & Digital Transmedia – Courses:\n\n"
        "• Animation\n"
        "• VFX\n"
        "• Game Design\n"
        "• Digital Design\n"
        "• Graphic Design"
    ),
    8: (
        "School of Law – Courses:\n\n"
        "• BA LL.B (Hons)\n"
        "• BBA LL.B (Hons)\n"
        "• LL.B\n"
        "• Other law and legal studies programmes as per university offerings"
    ),
    9: (
        "Online Degree Programs – Courses:\n\n"
        "• Online BBA\n"
        "• Online BCA\n"
        "• Online B.Com\n"
        "• Online B.Sc (selected specialisations)\n"
        "• Online MBA\n"
        "• Online MCA\n"
        "• Other online learning programmes (as listed on DSU online portal)"
    ),
    10: (
        "Medical College (CDSIMER) – Courses:\n\n"
        "• MBBS\n"
        "• Allied Health Science programmes\n"
        "• Nursing\n"
        "• Physiotherapy\n"
        "• Postgraduate medical specialisations (based on approvals and availability)"
    ),
}

# ---------- FUZZY WORD HELPER (for typos like "corses") ----------

def has_approx_word(text: str, targets, threshold: float = 0.8) -> bool:
    """
    Returns True if any word in `text` is approximately equal
    to any word in `targets` (tolerates spelling mistakes).
    """
    words = re.findall(r"[a-z]+", text.lower())
    for w in words:
        for tgt in targets:
            if SequenceMatcher(None, w, tgt).ratio() >= threshold:
                return True
    return False


def is_courses_query(text: str) -> bool:
    """
    Detect queries asking about courses/branches/schools,
    even with spelling mistakes like 'corses', 'coruses', etc.
    """
    t = text.lower()

    # direct phrase checks
    keywords = [
        "list of courses",
        "courses",
        "course list",
        "what courses does",
        "programmes",
        "programs",
        "schools in dsu",
        "schools at dsu",
        "list schools",
        "streams",
        "branches"
    ]
    if any(k in t for k in keywords):
        return True

    # fuzzy spelling for course-related words
    if has_approx_word(t, ["course", "courses", "corse", "corses", "coursee"]):
        return True

    # fuzzy for school / branch / program / stream words
    if has_approx_word(
        t,
        [
            "school", "schools",
            "program", "programs", "programme", "programmes",
            "branch", "branches",
            "stream", "streams"
        ]
    ):
        return True

    return False


# ---------- FEE OPTIONS ----------

FEE_OPTIONS = [
    {"number": 1, "question": "College tuition fee structure"},
    {"number": 2, "question": "Hostel fee structure"},
]

FEE_ANSWERS = {
    1: (
        "College tuition fee structure (summary):\n\n"
        "• Academic fees depend on the programme (B.Tech, BBA, B.Com, MBA, Nursing, etc.) "
        "and also on the admission quota (CET / COMEDK / DSAT / Management).\n"
        "• For example, for B.Tech 2nd year (AY 2024-25, 2023-24 batch), the official DSU notification "
        "mentions Tuition & Academic fees per year approximately in this range:\n"
        "  - CET quota: around ₹1.27 lakh\n"
        "  - COMEDK quota: around ₹2.97 lakh\n"
        "  - DSAT and Other quotas: around ₹2.47–3.72 lakh depending on branch.\n\n"
        "For the exact, up-to-date fee of your programme and batch, please refer to the latest DSU fee "
        "notification or ask a specific question like:\n"
        "\"What is the B.Tech 2nd year tuition and academic fee at DSU for the 2024-25 academic year?\""
    ),
    2: (
        "Hostel fee structure (summary for 2024-25):\n\n"
        "• Girls – S Residences / DSU Girls Hostel:\n"
        "  - 2 sharing (S Residences): about ₹2.26 lakh per year (hostel + mess + deposit)\n"
        "  - 3 sharing: about ₹2.21 lakh per year\n"
        "  - 4 sharing: about ₹1.91 lakh per year\n\n"
        "• Nursing Girls Hostel:\n"
        "  - 4 sharing: about ₹1.51 lakh per year\n"
        "  - 6 sharing: about ₹1.36 lakh per year\n\n"
        "• Boys – S Residences:\n"
        "  - 3 sharing: about ₹2.21 lakh per year\n"
        "  - 4 sharing: about ₹1.91 lakh per year\n\n"
        "For detailed breakup and MBBS-specific hostels, you can ask:\n"
        "\"What are the hostel fees for girls at DSU Harohalli Campus?\" or\n"
        "\"What is the hostel fee structure for MBBS students at DSU?\""
    ),
}

def detect_fee_ambiguity(text: str):
    """
    Detects when the user is asking something fee-related,
    including spelling mistakes like 'fee strcture', 'fess', etc.
    """
    t = text.lower()

    # direct phrase
    if "fee structure" in t or "fees structure" in t:
        return FEE_OPTIONS

    # fuzzy detection of fee-related words
    if has_approx_word(t, ["fee", "fees", "fess", "feee", "feez"]):
        return FEE_OPTIONS

    return None


# ----------------- TRANSLATION HELPERS ----------------- #

def translate_to_english(text: str) -> str:
    """Translate any input text to English (for internal processing)."""
    try:
        return GoogleTranslator(source="auto", target="en").translate(text)
    except Exception:
        return text


def maybe_translate_from_english(text: str, target_lang: str) -> str:
    """
    Translate English output text into the user's chosen language.
    If target_lang is empty or translation fails, return English text.
    """
    target_lang = (target_lang or "").strip().lower()
    if not target_lang:
        return text
    try:
        return GoogleTranslator(source="en", target=target_lang).translate(text)
    except Exception:
        return text


def handle_translate_command(text: str):
    """
    Direct translation command for the user.

    Pattern:
      translate to <language>: some text

    Ex:
      translate to kannada: Hello how are you?
    """
    raw = text.strip()
    lower = raw.lower()

    if lower.startswith("translate to ") and ":" in raw:
        before, after = raw.split(":", 1)
        lang_part = before[len("translate to "):].strip()
        content = after.strip()

        if not content:
            return "Please provide some text to translate after the colon (:)."

        try:
            translated = GoogleTranslator(
                source="auto",
                target=lang_part
            ).translate(content)
            return translated
        except Exception:
            return (
                f"Sorry, I couldn't translate to '{lang_part}'. "
                "Please check the language name (e.g., 'kannada', 'hindi', 'french')."
            )

    return None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_msg = (data.get("message") or "").strip()
    topic = (data.get("topic") or "").strip().lower()
    lang = (data.get("lang") or "").strip().lower()  # user-selected language

    if not user_msg:
        return jsonify({
            "reply": "Please type something so I can help you.",
            "clarify": False,
            "options": []
        })

    # 0) Direct translate command (bypass DSU logic)
    direct_translation = handle_translate_command(user_msg)
    if direct_translation is not None:
        return jsonify({
            "reply": direct_translation,
            "clarify": False,
            "options": []
        })

    # 1) Translate user message to English for understanding
    processed_msg = translate_to_english(user_msg)

    # 2) Small talk
    small = handle_small_talk(processed_msg)
    if small:
        reply_text = maybe_translate_from_english(small, lang)
        return jsonify({"reply": reply_text, "clarify": False, "options": []})

    # 3) Number reply for COURSES
    if topic == "courses" and user_msg.isdigit():
        n = int(user_msg)
        if n in COURSE_SCHOOL_ANSWERS:
            base = COURSE_SCHOOL_ANSWERS[n]
            reply_text = maybe_translate_from_english(base, lang)
            return jsonify({
                "reply": reply_text,
                "clarify": False,
                "options": []
            })

    # 4) Number reply for FEE OPTIONS
    if topic == "fee" and user_msg.isdigit():
        n = int(user_msg)
        if n in FEE_ANSWERS:
            base = FEE_ANSWERS[n]
            reply_text = maybe_translate_from_english(base, lang)
            return jsonify({
                "reply": reply_text,
                "clarify": False,
                "options": []
            })

    # 5) Number reply for ambiguous FAQ options (NEW)
    if topic == "faq" and user_msg.isdigit():
        idx = int(user_msg)
        if 0 <= idx < len(bot.answers):
            base = bot.answers[idx]
            reply_text = maybe_translate_from_english(base, lang)
            return jsonify({
                "reply": reply_text,
                "clarify": False,
                "options": []
            })

    # 6) Courses query → show schools options
    if is_courses_query(processed_msg):
        lines = ["Here are the schools at DSU. Please choose one option:\n"]
        for opt in COURSE_SCHOOL_OPTIONS:
            lines.append(f"{opt['number']}. {opt['question']}")
        reply_text = "\n".join(lines)
        reply_text = maybe_translate_from_english(reply_text, lang)

        translated_options = [
            {
                "number": opt["number"],
                "question": maybe_translate_from_english(opt["question"], lang)
            }
            for opt in COURSE_SCHOOL_OPTIONS
        ]

        return jsonify({
            "reply": reply_text,
            "clarify": True,
            "options": translated_options,
            "clarify_topic": "courses"
        })

    # 7) Fee ambiguity → show fee options
    fee_opts = detect_fee_ambiguity(processed_msg)
    if fee_opts:
        base_lines = ["I found more than one thing related to that. Please choose one option:"]
        for opt in fee_opts:
            base_lines.append(f"{opt['number']}. {opt['question']}")
        reply = "\n".join(base_lines)
        reply = maybe_translate_from_english(reply, lang)

        translated_options = [
            {
                "number": opt["number"],
                "question": maybe_translate_from_english(opt["question"], lang)
            }
            for opt in fee_opts
        ]

        return jsonify({
            "reply": reply,
            "clarify": True,
            "options": translated_options,
            "clarify_topic": "fee"
        })

    # 8) Default FAQ-based answer *with ambiguity options* (NEW)
    result = bot.get_reply(processed_msg)

    # a) Simple answer
    if result["type"] == "answer":
        answer_en = result["text"]
        answer_final = maybe_translate_from_english(answer_en, lang)
        return jsonify({
            "reply": answer_final,
            "clarify": False,
            "options": []
        })

    # b) Ambiguous → send FAQ options for user to choose
    if result["type"] == "clarify":
        # result["options"] is a list of dicts: {index, score, question, answer}
        options = result["options"]

        base_lines = ["I found multiple similar questions. Please choose one:"]
        for opt in options:
            base_lines.append(f"{opt['index']}. {opt['question']}")
        reply_text = "\n".join(base_lines)
        reply_text = maybe_translate_from_english(reply_text, lang)

        # Build options array for frontend (number = global FAQ index)
        api_options = [
            {
                "number": opt["index"],
                "question": maybe_translate_from_english(opt["question"], lang)
            }
            for opt in options
        ]

        return jsonify({
            "reply": reply_text,
            "clarify": True,
            "options": api_options,
            "clarify_topic": "faq"
        })

    # safety fallback (shouldn't normally reach here)
    return jsonify({
        "reply": "I'm not completely sure about that. Please try rephrasing.",
        "clarify": False,
        "options": []
    })


if __name__ == "__main__":
    app.run(debug=True)
