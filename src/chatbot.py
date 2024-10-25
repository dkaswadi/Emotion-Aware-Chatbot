from transformers import pipeline
nlp_chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")
def chat_with_bot():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = nlp_chatbot(user_input)
        print("Bot:", response[0]['generated_text'])
""  
if __name__ == "__main__":
    print("Type 'exit' to end the conversation.")
    chat_with_bot()
