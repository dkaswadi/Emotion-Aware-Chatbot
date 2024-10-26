from transformers import pipeline, Conversation

# Load a pre-trained text generation model (like GPT-2)
chatbot = pipeline("text-generation", model="gpt2")

def generate_response(user_input):
    # Create a conversation object and pass the user input
    conversation = Conversation(user_input)
    
    # Generate a response based on the context
    response = chatbot(conversation)
    
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
