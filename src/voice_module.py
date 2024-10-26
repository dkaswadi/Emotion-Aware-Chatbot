# voice_module.py
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)

def speak(text):
    engine.say(text)
    engine.runAndWait()
import pyttsx3

def speak(text):
    engine = pyttsx3.init()  # Initialize the TTS engine

    # Set properties before speaking
    engine.setProperty('rate', 150)  # Speed of speech (default is around 200)
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, how can I help you today?")
"" 
