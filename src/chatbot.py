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
import speech_recognition as sr
import pyttsx3
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Initialize the voice engine for TTS (Text-to-Speech)
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speech rate if needed
    engine.setProperty('volume', 0.9)  # Set volume level between 0.0 and 1.0
    engine.say(text)
    engine.runAndWait()

# Initialize the speech recognizer for Voice-to-Text
def listen_to_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Optional: adjust for background noise
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google's recognizer
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand that."
        except sr.RequestError:
            return "Please check your internet connection."

# NLP setup
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Chatbot conversation loop
def chat_with_bot():
    while True:
        # Get user input via voice
        user_input = listen_to_speech()
        if "exit" in user_input.lower():
            speak("Goodbye!")
            break

        print(f"You: {user_input}")
        # Generate response using NLP model
        inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        reply_ids = model.generate(inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
        bot_response = tokenizer.decode(reply_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)

        print(f"Bot: {bot_response}")
        speak(bot_response)

if __name__ == "__main__":
    chat_with_bot()
