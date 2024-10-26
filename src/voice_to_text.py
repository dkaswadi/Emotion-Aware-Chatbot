import speech_recognition as sr

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, there seems to be a problem with the service."

