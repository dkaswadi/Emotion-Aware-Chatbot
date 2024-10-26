from transformers import pipeline
from preprocess import preprocess_input, detect_intent
import json
import random

# Load a larger pre-trained DialoGPT model for conversation
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-large")

# Function to load responses from a JSON file
def load_responses(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Load responses when the module is imported
responses = load_responses("src/responses.json")

def generate_response(user_input):
    # Generate a response directly from the user input with padding and truncation
    response = chatbot(user_input, max_length=50, num_return_sequences=1, pad_token_id=50256, truncation=True)
    
    # Extract and return the generated response text
    return response[0]["generated_text"]

def generate_emotion_aware_response(user_input, detected_emotion):
    # Define default fallback response in case no match is found
    fallback_response = "I'm not sure how to respond to that, but I'm here to listen."

    # Check for greetings using basic intent detection
    if detect_intent(user_input) == "greeting":
        response = random.choice(responses.get("greeting", [fallback_response]))
    elif detected_emotion == "joy":
        response = random.choice(responses.get("happy", [fallback_response]))
    elif detected_emotion == "sadness":
        response = random.choice(responses.get("sad", [fallback_response]))
    elif detected_emotion == "anger":
        response = random.choice(responses.get("anger", [fallback_response]))
    elif detect_intent(user_input) == "thank_you":
        response = random.choice(responses.get("thank_you", [fallback_response]))
    else:
        response = generate_response(user_input)  # Fallback to generic generation

    return response
