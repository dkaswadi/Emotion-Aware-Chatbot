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

# Test the function
user_input = listen_to_user()
print(f"Recognized input: {user_input}")

from transformers import pipeline

# Load the pre-trained BERT model for text generation
chatbot = pipeline("conversational")

def generate_response(user_input):
    # Create a context or a dialogue-based input if required.
    response = chatbot(user_input)[0]['generated_text']
    return response

# Test NLP
print(generate_response("I'm feeling a little nervous about school."))

from emotion_recognition import EmotionRecognizer
import librosa

def detect_emotion(audio_path):
    recognizer = EmotionRecognizer()
    audio, sample_rate = librosa.load(audio_path)
    emotion = recognizer.predict(audio, sample_rate)
    print(f"Detected emotion: {emotion}")
    return emotion

# Example usage
# detect_emotion("path_to_audio.wav")

from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def detect_emotion_from_text(text):
    emotions = emotion_classifier(text)
    print(f"Detected emotion: {emotions[0]['label']}")
    return emotions[0]['label']

# Example usage
print(detect_emotion_from_text("I am feeling so happy today!"))

import pyttsx3

def speak_response(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speed if needed
    engine.say(text)
    engine.runAndWait()

# Example usage
speak_response("Hello! I'm here to help you.")

def chatbot_conversation():
    user_input = listen_to_user()
    emotion = detect_emotion_from_text(user_input)
    
    # Generate an appropriate response based on the detected emotion.
    response = generate_response(user_input)
    
    # Speak the generated response.
    speak_response(response)

# Run the conversation
chatbot_conversation()

def generate_emotion_aware_response(user_input, detected_emotion):
    if detected_emotion in ["joy", "happy"]:
        response = "I'm so glad you're happy! What made your day so great?"
    elif detected_emotion in ["sadness", "sad"]:
        response = "I'm sorry you're feeling sad. Do you want to talk about it?"
    elif detected_emotion in ["anger", "angry"]:
        response = "It's okay to feel angry sometimes. I'm here to listen if you want to vent."
    else:
        response = generate_response(user_input)
    
    return response

# Modify chatbot_conversation to use emotion-aware responses
def chatbot_conversation():
    user_input = listen_to_user()
    detected_emotion = detect_emotion_from_text(user_input)
    response = generate_emotion_aware_response(user_input, detected_emotion)
    speak_response(response)

# Run the conversation
chatbot_conversation()

