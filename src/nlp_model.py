# nlp_model.py
from transformers import pipeline
# Initialize a sentiment-analysis pipeline
nlp = pipeline("sentiment-analysis")
def get_intent(user_input):
    """
    Takes a user's text input and returns the detected sentiment.
    """
    result = nlp(user_input)
    # Extract the label and score from the result
    intent = result[0]['label']
    confidence = result[0]['score']
    return intent, confidence
def generate_response(intent):
    """
    Takes the detected intent and returns an appropriate response.
    """
    if intent == "POSITIVE":
        return "I'm glad to hear that! How can I assist you further?"
    elif intent == "NEGATIVE":
        return "I'm sorry to hear that. I'm here to help, please tell me more."
    else:
        return "I see. How can I help you today?"
""  
