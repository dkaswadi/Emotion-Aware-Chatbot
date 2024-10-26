import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import numpy as np
from nlp_model import generate_response, get_intent, load_intent_data, load_conversational_data

# Load datasets
intent_data = load_intent_data()  # Load the intent dataset
conversation_data = load_conversational_data()  # Load the conversational dataset

print("DEBUG: Intent data and conversational data loaded successfully")

# Initialize the voice engine for TTS (Text-to-Speech)
def speak(text):
    print("DEBUG: Entering speak() function")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speech rate if needed
    engine.setProperty('volume', 0.9)  # Set volume level between 0.0 and 1.0
    engine.say(text)
    engine.runAndWait()
    print("DEBUG: Finished speak() function")

# Initialize the speech recognizer for Voice-to-Text using sounddevice
def listen_to_speech():
    print("DEBUG: Entering listen_to_speech() function")
    recognizer = sr.Recognizer()
    sample_rate = 16000  # Set the sample rate (e.g., 16kHz)
    duration = 5  # Duration for listening (in seconds)

    print("Listening...")

    try:
        # Record audio using sounddevice
        audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait for the recording to finish

        # Convert the audio data to a format that SpeechRecognition can use
        audio = sr.AudioData(audio_data.tobytes(), sample_rate, 2)
        text = recognizer.recognize_google(audio)
        print("DEBUG: Successfully recognized speech")
        return text

    except sr.UnknownValueError:
        return "Sorry, I could not understand that."
    except sr.RequestError:
        return "Please check your internet connection."
    except Exception as e:
        print(f"DEBUG: Error occurred: {str(e)}")
        return f"Error: {str(e)}"

# Function to get user input (text or voice)
def get_user_input():
    print("DEBUG: Entering get_user_input() function")
    choice = input("Would you like to type or speak? (type/speak): ").strip().lower()

    if choice == "speak":
        return listen_to_speech()
    else:
        return input("You: ")

# Chatbot conversation loop with text and voice input options
def chat_with_bot():
    print("DEBUG: Starting chat_with_bot() function")
    while True:
        user_input = get_user_input()
        if not user_input:
            continue  # If no input is detected, continue listening

        print(f"You: {user_input}")

        # Identify the intent of the user input
        intent = get_intent(user_input)  # Make sure to call this function here
        print(f"DEBUG: Identified intent: {intent}")

        if intent == "exit":
            speak("Goodbye!")
            print("Goodbye!")
            break

        # Generate a response based on the input
        bot_response = generate_response(user_input)  # Ensure this line is correct
        print(f"Bot: {bot_response}")
        
        # Speak the generated response
        speak(bot_response)

if __name__ == "__main__":
    print("DEBUG: Starting main()")
    chat_with_bot()
