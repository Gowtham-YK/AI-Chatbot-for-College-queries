import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher   # <-- added for spelling mistake detection


class CollegeChatbot:
    """
    Semantic chatbot using SentenceTransformer embeddings.

    - Understands grammar mistakes & different wording
    - Now handles spelling mistakes (added fuzzy correction)
    - Detects ambiguity between multiple FAQs
    """

    def __init__(self, faq_path: str, threshold: float = 0.55, ambiguity_margin=0.10,
                 fuzzy_threshold: float = 0.75):
        """
        faq_path: path to data/faq_data.json
        threshold: minimum embedding similarity to accept answer
        ambiguity_margin: how close #2 match must be to #1 to trigger clarification
        fuzzy_threshold: minimum fuzzy ratio to trigger spelling correction
        """
        self.threshold = threshold
        self.ambiguity_margin = ambiguity_margin
        self.fuzzy_threshold = fuzzy_threshold

        # Load FAQ data
        with open(faq_path, "r", encoding="utf-8") as f:
            self.faq_data = json.load(f)

        self.questions = [item["question"] for item in self.faq_data]
        self.answers = [item["answer"] for item in self.faq_data]

        # Lowercase copy for fuzzy matching
        self.questions_lower = [q.lower() for q in self.questions]

        # Load SentenceTransformer embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Pre-compute question embeddings
        self.question_embeddings = self.model.encode(
            self.questions,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

    # ================================================================
    #                     SPELLING MISTAKE FIXER
    # ================================================================
    def _fuzzy_spell_fix(self, user_query: str):
        """
        If user types spelling mistakes or broken grammar,
        find the closest FAQ question using difflib.

        Returns:
            index (int) if found, else None
        """
        text = user_query.lower().strip()
        if not text:
            return None

        best_ratio = 0.0
        best_index = None

        for idx, q in enumerate(self.questions_lower):
            ratio = SequenceMatcher(None, text, q).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_index = idx

        if best_ratio >= self.fuzzy_threshold:
            return best_index

        return None

    # ================================================================
    #                   SEMANTIC MATCHING (MAIN ENGINE)
    # ================================================================
    def _get_top_matches(self, user_query: str, top_k: int = 3):
        if not user_query or not user_query.strip():
            return []

        query_embedding = self.model.encode(
            [user_query],
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        scores = cosine_similarity(query_embedding, self.question_embeddings)[0]
        sorted_indices = np.argsort(scores)[::-1][:top_k]

        matches = []
        for idx in sorted_indices:
            matches.append(
                {
                    "index": int(idx),
                    "score": float(scores[idx]),
                    "question": self.questions[idx],
                    "answer": self.answers[idx],
                }
            )
        return matches

    # ================================================================
    #                       MAIN CHATBOT LOGIC
    # ================================================================
    def get_reply(self, user_query: str):
        # 1) Try semantic matching first
        matches = self._get_top_matches(user_query, top_k=3)

        if not matches:
            return {
                "type": "answer",
                "text": "I didn't catch that. Could you please type your question again?"
            }

        best = matches[0]
        best_score = best["score"]

        # 2) Not confident → try spelling-correction fallback
        if best_score < self.threshold:
            fuzzy_idx = self._fuzzy_spell_fix(user_query)
            if fuzzy_idx is not None:
                return {
                    "type": "answer",
                    "text": self.answers[fuzzy_idx]
                }

            # Still not sure
            return {
                "type": "answer",
                "text": (
                    "I'm not completely sure about that. "
                    "Try rephrasing your question or ask something related to "
                    "courses, fees, hostel or admissions."
                )
            }

        # 3) Check ambiguity → offer clarification options
        ambiguous = [best]
        for candidate in matches[1:]:
            if candidate["score"] >= best_score - self.ambiguity_margin:
                ambiguous.append(candidate)

        if len(ambiguous) > 1:
            return {
                "type": "clarify",
                "options": ambiguous
            }

        # 4) Confident single answer
        return {
            "type": "answer",
            "text": best["answer"]
        }

    # Compatibility for old calls
    def get_answer(self, user_query: str) -> str:
        result = self.get_reply(user_query)
        if result["type"] == "answer":
            return result["text"]

        lines = ["I found multiple possible matches:"]
        for i, opt in enumerate(result["options"], start=1):
            lines.append(f"{i}. {opt['question']}")
        lines.append("Please reply with the option number.")

        return "\n".join(lines)
