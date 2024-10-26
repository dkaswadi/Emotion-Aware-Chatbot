from transformers import AutoModelForCausalLM, AutoTokenizer

# Load pre-trained conversational model (like DialoGPT)
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(user_input):
    """
    Generate a conversational response using a pre-trained model.
    
    Parameters:
    user_input (str): User's input message.
    
    Returns:
    str: Generated response from the model.
    """
    # Encode user input and add end-of-string token
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    
    # Generate response using the model
    reply_ids = model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
    
    # Decode and return the response
    response = tokenizer.decode(reply_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response

def get_intent(user_input):
    """
    Identify intent from user input. This is a placeholder for a more advanced intent recognition model.
    
    Parameters:
    user_input (str): User's input message.
    
    Returns:
    str: Identified intent (e.g., 'greeting', 'question', 'exit').
    """
    # Simple rule-based intent recognition (can be replaced with a more advanced classifier)
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return "greeting"
    elif "bye" in user_input.lower() or "exit" in user_input.lower():
        return "exit"
    elif "?" in user_input:
        return "question"
    else:
        return "default"

# Test the NLP model functions
if __name__ == "__main__":
    test_message = "Hello, how are you?"
    print(f"User: {test_message}")
    intent = get_intent(test_message)
    print(f"Identified Intent: {intent}")
    bot_response = generate_response(test_message)
    print(f"Bot: {bot_response}")

import pandas as pd

def load_intent_data(file_path="data/intent_data.csv"):
    """
    Load intent data from a CSV file.
    
    Parameters:
    file_path (str): Path to the intent data CSV file.

    Returns:
    pd.DataFrame: Loaded intent data as a DataFrame.
    """
    intent_data = pd.read_csv(file_path)
    return intent_data

# Example usage:
intent_data = load_intent_data()
print(intent_data.head())  # Display the first few rows of the intent data

import json

def load_conversational_data(file_path="data/conversational_data.json"):
    """
    Load conversational data from a JSON file.
    
    Parameters:
    file_path (str): Path to the conversational data JSON file.

    Returns:
    list: List of conversation pairs (prompt and response).
    """
    with open(file_path, "r") as json_file:
        conversational_data = json.load(json_file)
    return conversational_data

# Example usage:
conversation_data = load_conversational_data()
print(conversation_data[:5])  # Display the first few conversation pairs
