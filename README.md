# AI-Chatbot-for-College-queries
CHATBOT is an NLP + NLM powered college assistant that answers DSU queries, handles spelling/grammar mistakes, supports multiple languages, detects ambiguous questions, and provides course/fee/hostel info instantly with a smart ChatGPT-style UI and Android app support.
Here is a **perfect, professional GitHub project description** for your **DSU-CHATBOT (NLM + NLP Based College Assistant)**.
You can **copy–paste** this directly into your GitHub **README.md**.

---

# Intelligent College Query Assistant (NLP + NLM Project)**

A smart AI-powered chatbot built using **Natural Language Processing (NLP)** and **Natural Language Models (NLM)** that helps students and parents get instant answers about Dayananda Sagar University (DSU).
The chatbot understands **spelling mistakes, grammar errors, multiple languages, similar questions**, and can **ask clarification when queries are ambiguous**.

---

# 📌 **🔍 Project Overview**

DSU-CHATBOT is a fully intelligent assistant designed to automate the most frequently asked questions (FAQ) related to DSU—courses, fees, hostels, admissions, facilities, placements, and more.

It uses:

✅ **SentenceTransformer (all-MiniLM-L6-v2)** for understanding meaning
✅ **Cosine Similarity** for semantic matching
✅ **Custom Semantic Engine (CollegeChatbot)** for reasoning
✅ **Deep Translator (GoogleTranslator API)** for multilingual output
✅ **Flask Web App + Web UI** for interactive chatting
✅ **Android App (WebView)** for mobile access
✅ **Graph-based analysis** using Matplotlib (performance, accuracy, NLM impact)

The entire system mimics real ChatGPT-style interaction—typing indicator, message bubbles, clarification cards, voice input, settings panel, and dynamic language response.

---

# 🧠 **✨ Key Features**

### ✔️ **1. Natural Language Understanding (NLM-powered)**

* Understands *meaning*, not just keywords
* Handles spelling mistakes (ex: "hotell" → "hostel")
* Handles grammar mistakes (ex: “what fee DSU hostel have?”)
* Detects ambiguous questions & shows options

### ✔️ **2. Multilingual Support (Translation Engine)**

User can choose output language:
**Kannada, Hindi, Tamil, Telugu, Malayalam, Marathi, Bengali**, or English.

### ✔️ **3. Smart Clarification Handling**

If the question matches multiple answers (ex: “fees”),
the chatbot shows **options** and asks the user to select.

### ✔️ **4. Detailed Course & Fee Queries**

Includes structured data for:

* All DSU Schools & Departments
* Course Lists for every School
* Tuition Fee Structure (UG + PG)
* Hostel Fee Structure (Boys/Girls + Medical Campus)

### ✔️ **5. Web + Android Integration**

* Fully responsive Flask UI
* Android app uses WebView to open:
  👉 **[www.DSUCHATBOT.com](http://www.DSUCHATBOT.com)** (or localhost during development)

### ✔️ **6. Aesthetic UI**

* Cyberpunk dark theme
* Neon accent colors
* Real ChatGPT-style message bubbles
* Typing indicator animation
* Voice input button (speech recognition)

### ✔️ **7. Graph & Analysis Reports**

`graph.py` generates professional graphs for report/PPT:

* Module-wise contribution
* Before vs After NLM accuracy
* Ambiguity handling performance
* Response-time curve
* Language usage distribution
* Deep learning vs non-deep learning comparison

---

# 🏗️ **🛠️ Tech Stack**

### **Backend**

* Python 3.x
* Flask
* SentenceTransformer (MiniLM-L6-v2)
* Scikit-Learn
* Deep Translator
* NumPy

### **Frontend**

* HTML, CSS, JavaScript
* Custom UI (glassmorphism + neon theme)
* Responsive layout
* Typing animations
* Option cards

### **Mobile**

* Android Studio (WebView App)

### **Data**

* `faq_data.json` (All DSU information)
* Courses dataset
* Fee structure dataset

---

# 📊 **📈 Performance & Results**

Using **NLM (MiniLM)** improved:

* Understanding accuracy from **60% → 91%**
* Spelling error handling to **90%**
* Grammar error handling to **88%**
* Ambiguity resolution to **86%**

Graph results include:

* Contribution of each module
* Before vs After NLM performance
* Spelling & ambiguity evaluation
* Query response times
* Deep learning comparison
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

# 🚀 **How It Works**

### **1. User enters a query**

↓
The query is translated to English → sent to the NLM model.

### **2. NLM generates an embedding**

Using MiniLM (SentenceTransformer).

### **3. Best matching FAQ is found**

Using cosine similarity.

### **4. If multiple matches are close**

Chatbot shows **clarification cards**.

### **5. Final answer returned in selected language**

Using GoogleTranslator.

---

# 📚 **Project Structure**

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

# 🎯 **Use Cases**

* College website chatbot
* Admission assistance tool
* Student helpline automation
* FAQ system
* NLP academic project
* Demonstration of NLM-powered semantic search

---

# 📢 **Contributions**

Pull requests are welcome.
If you'd like to improve UI, add more languages, or enhance AI accuracy—feel free to contribute.

---

# ⭐ **If you like this project, please give it a star!**

Your support motivates continued improvements 💚✨

---


✅ Architecture diagram
Just tell me!
