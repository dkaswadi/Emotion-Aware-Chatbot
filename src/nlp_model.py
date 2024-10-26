<<<<<<< HEAD
=======
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
if __name__ == "__main__":
    # Simple test loop
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        intent, confidence = get_intent(user_input)
        response = generate_response(intent)

        print(f"Detected Intent: {intent} (Confidence: {confidence:.2f})")
        print(f"Chatbot: {response}")
""  
>>>>>>> 0049a46e6507f2a46cb1840eaaffcba912877bc9
