from transformers import pipeline
from preprocess import preprocess_input, detect_intent
from faq_module import find_answer
import random

# Load a larger pre-trained DialoGPT model for conversation
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-large")

def generate_response(user_input):
    # Generate a response directly from the user input with padding and truncation
    response = chatbot(user_input, max_length=50, num_return_sequences=1, pad_token_id=50256, truncation=True)
    return response[0]["generated_text"]

def generate_emotion_aware_response(user_input, detected_emotion):
    # Define a fallback response in case no specific response matches
    fallback_response = "I'm not sure how to respond to that, but I'm here to listen."

    # Check for questions using intent detection and look for answers in the FAQ
    if detect_intent(user_input) == "question":
        answer = find_answer(user_input)
        return answer

    # Add emotion-specific responses or default to a generic generated response
    if detected_emotion == "joy":
        response = random.choice([
            "I'm so glad to hear that! What made you happy?",
            "That's wonderful! Would you like to share more?",
            "Yay! Keep spreading the positivity!"
        ])
    elif detected_emotion == "sadness":
        response = random.choice([
            "I'm sorry you're feeling sad. Do you want to talk about it?",
            "It's okay to feel sad sometimes. I'm here to listen.",
            "I understand. Let me know if there's anything I can do to help."
        ])
    elif detected_emotion == "anger":
        response = random.choice([
            "It's okay to feel angry sometimes. I'm here to listen if you want to vent.",
            "Anger can be tough. Take a deep breath and tell me what happened.",
            "I'm sorry you're feeling angry. Do you want to talk about it?"
        ])
    else:
        # Default to a generic chatbot response if no emotion or question matches
        response = generate_response(user_input) if not user_input.strip() == "" else fallback_response

    return response
