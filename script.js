/* ==========================
   BASIC ELEMENT REFERENCES
========================== */

const form = document.getElementById("chat-form");
const input = document.getElementById("user-input");
const chatWindow = document.getElementById("chat-window");
const typingIndicator = document.getElementById("typing-indicator");
const optionsContainer = document.getElementById("options-container");
const sendBtn = document.querySelector(".send-btn");
const micBtn = document.getElementById("mic-btn");

/* SETTINGS PANEL */
const settingsToggle = document.getElementById("settings-toggle");
const settingsPanel = document.getElementById("settings-panel");
const fontSlider = document.getElementById("font-slider");
const largeTextToggle = document.getElementById("large-text-toggle");
const contrastToggle = document.getElementById("contrast-toggle");
const languageSelect = document.getElementById("language-select");

/* Clarification topic: "courses", "fee", or null */
let activeClarifyTopic = null;

/* Selected response language ('' = English) */
let selectedLanguage = "";
if (languageSelect) {
    selectedLanguage = languageSelect.value;
    languageSelect.addEventListener("change", () => {
        selectedLanguage = languageSelect.value || "";
    });
}

/* ==========================
      CHAT FUNCTIONS
========================== */

/* smooth auto-scroll */
function scrollChatToBottom() {
    if (!chatWindow) return;
    chatWindow.scrollTo({
        top: chatWindow.scrollHeight,
        behavior: "smooth",
    });
}

function addMessage(text, sender) {
    const div = document.createElement("div");
    div.classList.add("message", sender);
    div.textContent = text;
    chatWindow.appendChild(div);
    scrollChatToBottom();
}

function setTyping(isTyping) {
    if (!typingIndicator) return;
    if (isTyping) typingIndicator.classList.remove("hidden");
    else typingIndicator.classList.add("hidden");
}

function clearOptions() {
    if (optionsContainer) optionsContainer.innerHTML = "";
}

function renderOptions(options) {
    clearOptions();
    if (!options || !options.length) return;

    options.forEach((opt) => {
        const card = document.createElement("div");
        card.className = "option-card";
        card.innerHTML = `
            <span class="option-icon">💡</span>
            <span>${opt.question}</span>
        `;
        card.addEventListener("click", () => {
            sendMessage(String(opt.number));
            clearOptions();
        });
        optionsContainer.appendChild(card);
    });

    scrollChatToBottom();
}

async function sendMessage(text) {
    const clean = (text || "").trim();
    if (!clean) return;

    addMessage(clean, "user");
    input.value = "";
    setTyping(true);

    input.disabled = true;
    sendBtn.disabled = true;

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                message: clean,
                topic: activeClarifyTopic || "",
                lang: selectedLanguage || "",
            }),
        });

        const data = await res.json();

        addMessage(data.reply, "bot");

        if (data.clarify && Array.isArray(data.options)) {
            activeClarifyTopic = data.clarify_topic || null;
            renderOptions(data.options);
        } else {
            activeClarifyTopic = null;
            clearOptions();
        }
    } catch (err) {
        console.error(err);
        addMessage("Error: Could not reach server.", "bot");
    }

    setTyping(false);
    input.disabled = false;
    sendBtn.disabled = false;
    input.focus();
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    sendMessage(input.value);
});

/* ==========================
      VOICE TYPING
========================== */

let recognition = null;
let isListening = false;

if ("SpeechRecognition" in window || "webkitSpeechRecognition" in window) {
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SR();
    recognition.lang = "en-IN";

    recognition.onstart = () => {
        isListening = true;
        if (micBtn) micBtn.classList.add("recording");
    };

    recognition.onend = () => {
        isListening = false;
        if (micBtn) micBtn.classList.remove("recording");
    };

    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        input.value += (input.value ? " " : "") + transcript;
        input.focus();
    };

    recognition.onerror = (event) => {
        console.error("Speech recognition error:", event.error);
        isListening = false;
        if (micBtn) micBtn.classList.remove("recording");
    };
}

if (micBtn) {
    micBtn.addEventListener("click", () => {
        if (!recognition) {
            alert("Voice input not supported in this browser. Try Chrome/Edge.");
            return;
        }
        isListening ? recognition.stop() : recognition.start();
    });
}

/* ==========================
  DOWNLOAD CHAT AS TEXT FILE
========================== */

function downloadChat() {
    let text = "";
    document.querySelectorAll(".message").forEach((msg) => {
        const who = msg.classList.contains("user") ? "You" : "Bot";
        text += `${who}: ${msg.textContent}\n\n`;
    });

    const blob = new Blob([text], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "chat_history.txt";
    a.click();
    URL.revokeObjectURL(url);
}
window.downloadChat = downloadChat;

/* ==========================
      SETTINGS PANEL LOGIC
========================== */

if (settingsToggle && settingsPanel) {
    settingsToggle.addEventListener("click", (event) => {
        event.stopPropagation();
        settingsPanel.classList.toggle("open");
    });

    document.addEventListener("click", (event) => {
        if (
            !settingsPanel.contains(event.target) &&
            !settingsToggle.contains(event.target)
        ) {
            settingsPanel.classList.remove("open");
        }
    });
}

/* TEXT SIZE ADJUSTER */
if (fontSlider) {
    fontSlider.addEventListener("input", () => {
        const scale = fontSlider.value / 100;
        document.documentElement.style.setProperty("--chat-font-scale", scale);
    });
}

/* LARGE TEXT TOGGLE */
if (largeTextToggle) {
    largeTextToggle.addEventListener("click", () => {
        const enabled = document.body.classList.toggle("large-text-mode");
        largeTextToggle.classList.toggle("active", enabled);
        largeTextToggle.textContent = enabled ? "On" : "Off";
    });
}

/* HIGH CONTRAST TOGGLE */
if (contrastToggle) {
    contrastToggle.addEventListener("click", () => {
        const enabled = document.body.classList.toggle("high-contrast-mode");
        contrastToggle.classList.toggle("active", enabled);
        contrastToggle.textContent = enabled ? "On" : "Off";
    });
}

/* HINT FILTERING */
const hintRow = document.querySelector(".hint-row");
if (hintRow && input) {
    input.addEventListener("input", () => {
        const text = input.value.trim().toLowerCase();
        const pills = hintRow.querySelectorAll(".hint-pill");

        pills.forEach((pill) => {
            pill.style.display =
                !text || pill.textContent.toLowerCase().includes(text)
                    ? "inline-flex"
                    : "none";
        });
    });
}
