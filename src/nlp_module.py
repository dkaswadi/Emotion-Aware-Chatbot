from transformers import pipeline
from preprocess import preprocess_input, detect_intent

# Load a larger pre-trained DialoGPT model for conversation
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-large")

def generate_response(user_input):
    # Generate a response directly from the user input with padding and truncation
    response = chatbot(user_input, max_length=50, num_return_sequences=1, pad_token_id=50256, truncation=True)
    
    # Extract and return the generated response text
    return response[0]["generated_text"]

import random

def generate_emotion_aware_response(user_input, detected_emotion):
    greeting_responses = [
        "Hello there! How can I help you today?",
        "Hi! What would you like to talk about?",
        "Hey! How's it going?"
    ]
    happy_responses = [
        "I'm so glad you're happy! What made your day so great?",
        "That sounds amazing! Keep smiling!",
        "Yay! Tell me more about it."
    ]
    sad_responses = [
        "I'm sorry you're feeling sad. Do you want to talk about it?",
        "It's okay to feel sad sometimes. I'm here to listen.",
        "I'm here for you. Take your time."
    ]

    if detect_intent(user_input) == "greeting":
        response = random.choice(greeting_responses)
    elif detected_emotion == "joy":
        response = random.choice(happy_responses)
    elif detected_emotion == "sadness":
        response = random.choice(sad_responses)
    else:
        response = generate_response(user_input)
    
    return response

