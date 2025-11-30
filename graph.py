"""
graph.py  –  DSU-CHATBOT (NLM Project) Graphs

This script generates graphs for your project report / PPT.

You can change the numbers in the lists (like accuracy values)
to match your real experiment results.
"""

import matplotlib.pyplot as plt
import numpy as np

# ==============================
# 1. MODEL / MODULE COMPARISON
# ==============================

# These are the main NLP / NLM components you used
model_names = [
    "SentenceTransformer\n(all-MiniLM-L6-v2)",
    "Custom Semantic Engine\n(CollegeChatbot)",
    "cosine_similarity\n(sklearn)",
    "GoogleTranslator\n(deep_translator)"
]

# Example "effectiveness scores"
effectiveness_scores = [95, 93, 90, 88]

plt.figure(figsize=(10, 6))
bars = plt.bar(model_names, effectiveness_scores)

plt.title("Module-wise Contribution in DSU-CHATBOT (NLM Project)")
plt.ylabel("Effectiveness / Contribution Score (%)")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.3)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1,
             f"{height:.0f}%", ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig("nlm_module_contribution.png")
plt.show()

# ==========================================
# 2. BEFORE vs AFTER USING NLM (MiniLM)
# ==========================================

labels = ["Before NLM\n(rule/keyword based)", "After NLM\n(all-MiniLM-L6-v2)"]
semantic_accuracy = [60, 91]

plt.figure(figsize=(7, 5))
bars = plt.bar(labels, semantic_accuracy, color=["#f97373", "#22c55e"])

plt.title("Impact of Natural Language Model on Semantic Understanding")
plt.ylabel("Semantic Match Accuracy (%)")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.3)

# value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1,
             f"{height:.0f}%", ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig("before_after_nlm_accuracy.png")
plt.show()

# =======================================================
# 3. AMBIGUITY & SPELLING HANDLING PERFORMANCE (NLM)
# =======================================================

metrics = ["Handles spelling mistakes", "Handles grammar errors", "Ambiguity detection (questions)"]
scores = [90, 88, 86]

x = np.arange(len(metrics))
width = 0.6

plt.figure(figsize=(9, 5))
bars = plt.bar(x, scores, width, color="#3b82f6")

plt.xticks(x, metrics, rotation=10, ha="right")
plt.ylabel("Success Rate (%)")
plt.title("NLM Behaviour Evaluation – DSU-CHATBOT")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.3)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1,
             f"{height:.0f}%", ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig("nlm_spelling_ambiguity_performance.png")
plt.show()

# ==========================================
# 4. RESPONSE TIME PER QUERY (SIMULATED)
# ==========================================

queries = list(range(1, 21))
response_times = [
    280, 260, 300, 250, 270,
    290, 260, 255, 275, 265,
    280, 295, 270, 260, 250,
    255, 265, 275, 285, 270
]

plt.figure(figsize=(9, 4))
plt.plot(queries, response_times, marker='o', linestyle='-', color="#22c55e")
plt.title("DSU-CHATBOT Response Time per Query")
plt.xlabel("Query Number")
plt.ylabel("Response Time (ms)")
plt.grid(True, linestyle="--", alpha=0.4)
plt.xticks(queries)
plt.tight_layout()
plt.savefig("chatbot_response_time.png")
plt.show()

# ===================================================
# 5. LANGUAGE USAGE DISTRIBUTION (TRANSLATOR USAGE)
# ===================================================

languages = ["English", "Kannada", "Hindi", "Tamil", "Telugu", "Others"]
counts = [70, 10, 8, 5, 4, 3]

plt.figure(figsize=(7, 7))
plt.pie(counts, labels=languages, autopct="%1.1f%%",
        startangle=140, wedgeprops={'edgecolor': 'white'})
plt.title("Language-wise Usage of DSU-CHATBOT")
plt.tight_layout()
plt.savefig("language_usage_pie.png")
plt.show()

print(" - nlm_module_contribution.png")
print(" - before_after_nlm_accuracy.png")
print(" - nlm_spelling_ambiguity_performance.png")
print(" - chatbot_response_time.png")
print(" - language_usage_pie.png")


# ====================================================
# 6. DEEP LEARNING vs NON-DEEP LEARNING COMPARISON
# ====================================================

plt.figure(figsize=(10, 6))

methods = [
    "Rule-based\n(No ML)",
    "Traditional ML\n(TF-IDF + Cosine)",
    "Deep Learning\n(SentenceTransformer)",
    "Full DSU-CHATBOT\n(NLM + Engine)"
]

accuracy = [45, 72, 91, 94]   # Example values (edit if needed)

bars = plt.bar(methods, accuracy, color=["#ef4444", "#f59e0b", "#3b82f6", "#22c55e"])

plt.title("Deep Learning Performance Comparison – DSU-CHATBOT")
plt.ylabel("Accuracy (%)")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.3)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        f"{height:.0f}%",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()
plt.savefig("deep_learning_comparison.png")
plt.show()

print(" - deep_learning_comparison.png")
print("✅ All graphs generated successfully!")
