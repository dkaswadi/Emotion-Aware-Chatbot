# chatbot.py
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Load the DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Custom function to generate a response using the model
def chat_with_bot(user_input):
    """
    Chat with the bot using text generation from DialoGPT.
    """
    # Encode the user input and generate a response
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    reply_ids = model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(reply_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response

# Main program loop
if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to end the conversation.")
    while True:
        # Prompt the user for input
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Generate a response from the chatbot
        bot_response = chat_with_bot(user_input)
        print(f"Bot: {bot_response}")
# chatbot.py
from nlp_model import get_intent
from emotion_recognition import get_emotion
from voice_module import listen, speak

def main():
    while True:
        user_input = listen()
        emotion = get_emotion()
        intent = get_intent(user_input)
        print(f"User said: {user_input}, Detected emotion: {emotion}, Intent: {intent}")
        speak(f"I can sense that you are feeling {emotion}. Let's talk about it.")

if __name__ == "__main__":
    main()
