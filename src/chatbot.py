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
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen_to_user():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."

def speak_response(text):
    tts_engine.say(text)
    tts_engine.runAndWait()
def chat_with_bot():
    while True:
        user_input = listen_to_user()
        if user_input.lower() == "exit":
            speak_response("Goodbye!")
            break
        print("You:", user_input)
        response = nlp_chatbot(user_input)
        bot_reply = response[0]['generated_text']
        print("Bot:", bot_reply)
        speak_response(bot_reply)
