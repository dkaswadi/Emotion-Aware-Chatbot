def detect_intent(text):
    # Basic question detection by looking for common question words
    question_words = ["what", "how", "when", "why", "where", "who", "can you", "could you", "would you", "is it", "does it"]
    if any(word in text.lower() for word in question_words):
        return "question"
    return "general"
