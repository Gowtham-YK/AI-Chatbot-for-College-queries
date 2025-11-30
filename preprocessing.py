import string

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = "".join(ch for ch in text if ch not in string.punctuation)
    text = " ".join(text.split())
    return text
