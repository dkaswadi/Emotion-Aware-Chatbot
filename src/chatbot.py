import speech_recognition as sr
import pyttsx3
from nlp_model import generate_response, get_intent

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
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google's recognizer
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand that."
        except sr.RequestError:
            return "Please check your internet connection."

# Function to get user input (text or voice)
def get_user_input():
    choice = input("Would you like to type or speak? (type/speak): ").strip().lower()

    if choice == "speak":
        return listen_to_speech()
    else:
        return input("You: ")

# Chatbot conversation loop with text and voice input options
def chat_with_bot():
    while True:
        # Get user input via text or voice
        user_input = get_user_input()
        if not user_input:
            continue  # If no input is detected, continue listening

        print(f"You: {user_input}")

        # Identify the intent of the user input
        intent = get_intent(user_input)

        # Handle the exit intent
        if intent == "exit":
            speak("Goodbye!")
            break

        # Generate a response based on the input
        bot_response = generate_response(user_input)
        print(f"Bot: {bot_response}")
        
        # Speak the generated response
        speak(bot_response)

if __name__ == "__main__":
    chat_with_bot()
