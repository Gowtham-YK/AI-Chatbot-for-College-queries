def handle_small_talk(user_input: str) -> str | None:
    text = user_input.lower().strip()

    greetings = ["hi", "hello", "hey"]
    thanks = ["thanks", "thank you"]
    bye_words = ["bye", "goodbye"]

    if any(text.startswith(g) for g in greetings):
        return "Hello! 👋 How can I assist you with college queries?"

    if any(t in text for t in thanks):
        return "You're welcome! 😊"

    if any(text.startswith(b) for b in bye_words):
        return "Goodbye! Have a nice day! 👋"

    return None
