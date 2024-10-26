
import pyttsx3

def speak_response(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speed if needed
    engine.say(text)
    engine.runAndWait()
