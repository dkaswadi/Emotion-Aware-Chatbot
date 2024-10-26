from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_input(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [word for word in word_tokens if word.lower() not in stop_words]
    return " ".join(filtered_sentence)

def detect_intent(text):
    greetings = ["hello", "hi", "hey", "greetings"]
    if any(word in text.lower() for word in greetings):
        return "greeting"
    else:
        return "general"

