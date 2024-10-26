from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_input(text):
    """Preprocess user input by removing stopwords and normalizing the text."""
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [word for word in word_tokens if word.lower() not in stop_words]
    return " ".join(filtered_sentence)

def detect_intent(text):
    """Detect the intent of the input text based on question words."""
    question_words = ["what", "how", "when", "why", "where", "who", "can you", "could you", "would you", "is it", "does it"]
    if any(word in text.lower() for word in question_words):
        return "question"
    return "general"
