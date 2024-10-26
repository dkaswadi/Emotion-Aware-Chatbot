import pyttsx3

def speak_response(text):
    engine = pyttsx3.init()
    
    # Set the desired speaking rate (default is around 200, increase for faster speech)
    engine.setProperty('rate', 250)  # Adjust this value to control speech speed

    engine.say(text)
    engine.runAndWait()
