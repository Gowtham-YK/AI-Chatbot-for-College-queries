# AI-Chatbot-for-College-queries
CHATBOT is an NLP + NLM powered college assistant that answers DSU queries, handles spelling/grammar mistakes, supports multiple languages, detects ambiguous questions, and provides course/fee/hostel info instantly with a smart ChatGPT-style UI and Android app support.
Here is a **perfect, professional GitHub project description** for your **DSU-CHATBOT (NLM + NLP Based College Assistant)**.
You can **copy–paste** this directly into your GitHub **README.md**.

---

# Intelligent College Query Assistant (NLP + NLM Project)

A smart AI chatbot built with **Natural Language Processing (NLP)** and **Natural Language Models (NLM)** helps students and parents get quick answers about Dayananda Sagar University (DSU). The chatbot understands **spelling mistakes, grammar errors, multiple languages, and similar questions**, and it can **ask for clarification when questions are unclear**.

---

# Project Overview

DSU-CHATBOT is a fully intelligent assistant designed to handle frequently asked questions (FAQ) related to DSU, such as courses, fees, hostels, admissions, facilities, placements, and more.

It uses:

✅ **SentenceTransformer (all-MiniLM-L6-v2)** for understanding meaning  
✅ **Cosine Similarity** for matching meanings  
✅ **Custom Semantic Engine (CollegeChatbot)** for reasoning  
✅ **Deep Translator (GoogleTranslator API)** for translating output  
✅ **Flask Web App + Web UI** for interactive chatting  
✅ **Android App (WebView)** for access on mobile  
✅ **Graph-based analysis** using Matplotlib (performance, accuracy, NLM impact)  

The entire system mimics real chat interactions with features like typing indicators, message bubbles, clarification cards, voice input, settings panel, and dynamic language responses.

---

# Key Features

### ✔️ 1. Natural Language Understanding (NLM-powered)

* Understands *meaning*, not just keywords  
* Handles spelling mistakes (e.g., "hotell" → "hostel")  
* Handles grammar mistakes (e.g., “what fee DSU hostel have?”)  
* Detects unclear questions and shows options  

### ✔️ 2. Multilingual Support (Translation Engine)

Users can choose the output language:  
**Kannada, Hindi, Tamil, Telugu, Malayalam, Marathi, Bengali**, or English.  

### ✔️ 3. Smart Clarification Handling

If a question matches multiple answers (e.g., “fees”), the chatbot shows **options** and asks the user to choose.  

### ✔️ 4. Detailed Course & Fee Queries

Includes structured information for:  

* All DSU Schools & Departments  
* Course Lists for every School  
* Tuition Fee Structure (UG + PG)  
* Hostel Fee Structure (Boys/Girls + Medical Campus)  

### ✔️ 5. Web + Android Integration

* Fully responsive Flask UI  
* Android app uses WebView to open:  
  👉 **[www.DSUCHATBOT.com](http://www.DSUCHATBOT.com)** (or localhost during development)  

### ✔️ 6. Aesthetic UI

* Cyberpunk dark theme  
* Neon accent colors  
* Real chat message bubbles  
* Typing indicator animation  
* Voice input button (speech recognition)  

### ✔️ 7. Graph & Analysis Reports

`graph.py` generates graphs for reports or presentations:  

* Module-wise contribution  
* Before vs After NLM accuracy  
* Performance in handling ambiguity  
* Response-time trends  
* Language usage distribution  
* Comparison of deep learning and non-deep learning  

---

# Tech Stack

### Backend

* Python 3.x  
* Flask  
* SentenceTransformer (MiniLM-L6-v2)  
* Scikit-Learn  
* Deep Translator  
* NumPy  

### Frontend

* HTML, CSS, JavaScript  
* Custom UI (glassmorphism + neon theme)  
* Responsive layout  
* Typing animations  
* Option cards  

### Mobile

* Android Studio (WebView App)  

### Data

* `faq_data.json` (All DSU information)  
* Courses dataset  
* Fee structure dataset  

---

# Performance & Results

Using **NLM (MiniLM)** improved:  

* Understanding accuracy from **60% to 91%**  
* Spelling error handling to **90%**  
* Grammar error handling to **88%**  
* Ambiguity resolution to **86%**  

Graph results include:  

* Contribution of each module  
* Before vs After NLM performance  
* Spelling and ambiguity evaluation  
* Query response times  
* Comparison of deep learning methods  
* Language usage distribution  

Graphs are saved as:

```
nlm_module_contribution.png  
before_after_nlm_accuracy.png  
nlm_spelling_ambiguity_performance.png  
chatbot_response_time.png  
language_usage_pie.png  
deep_learning_comparison.png
```

---

# How It Works

### 1. User enters a query

↓  
The query is translated to English and sent to the NLM model.

### 2. NLM generates an embedding

Using MiniLM (SentenceTransformer).

### 3. Best matching FAQ is found

Using cosine similarity.

### 4. If multiple matches are close

The chatbot shows **clarification cards**.

### 5. Final answer is returned in the selected language

Using GoogleTranslator.

---

# Project Structure

```
DSU-CHATBOT/
│
├── chatbot/
│   ├── model.py               # NLM-based semantic engine
│   ├── small_talk.py          # Greetings & casual conversation
│
├── data/
│   ├── faq_data.json          # All DSU questions + answers
│
├── static/
│   ├── style.css              # Chatbot UI styling
│   ├── script.js              # Frontend logic + animations
│
├── templates/
│   ├── index.html             # Chat UI layout
│
├── graph.py                   # All analysis graphs
│
├── app.py                     # Flask backend
│
└── README.md                  # Project description (this file)
```

---

# Use Cases

* College website chatbot  
* Admission assistance tool  
* Student helpline automation  
* FAQ system  
* NLP academic project  
* Demonstration of NLM-powered semantic search  
