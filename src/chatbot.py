# chatbot.py
from transformers import pipeline, Conversation, AutoModelForCausalLM, AutoTokenizer

# Load the DialoGPT model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize text-generation pipeline
nlp_chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

def chat_with_bot(user_input):
    """
    Chat with the bot using text generation from DialoGPT.
    """
    # Encode the user input and generate a response
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    reply_ids = model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(reply_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        bot_response = chat_with_bot(user_input)
        print(f"Bot: {bot_response}")

