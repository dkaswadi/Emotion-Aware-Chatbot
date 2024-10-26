from transformers import pipeline

# Load a pre-trained text generation model (like GPT-2)
chatbot = pipeline("text-generation", model="gpt2")

def generate_response(user_input):
    # Generate a response directly from the user input
    response = chatbot(user_input, max_length=50, num_return_sequences=1)
    
    # Extract and return the generated response text
    return response[0]["generated_text"]

def generate_emotion_aware_response(user_input, detected_emotion):
    if detected_emotion in ["joy", "happy"]:
        response = "I'm so glad you're happy! What made your day so great?"
    elif detected_emotion in ["sadness", "sad"]:
        response = "I'm sorry you're feeling sad. Do you want to talk about it?"
    elif detected_emotion in ["anger", "angry"]:
        response = "It's okay to feel angry sometimes. I'm here to listen if you want to vent."
    else:
        response = generate_response(user_input)
    
    return response
