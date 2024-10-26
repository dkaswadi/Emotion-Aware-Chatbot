import sys
import os

# Add the 'src' directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from voice_to_text import listen_to_user
from emotion_recognition import detect_emotion_from_text
from nlp_module import generate_emotion_aware_response
from text_to_speech import speak_response

def chatbot_conversation():
    user_input = listen_to_user()
    print(f"Recognized input: {user_input}")

    detected_emotion = detect_emotion_from_text(user_input)
    response = generate_emotion_aware_response(user_input, detected_emotion)
    print(f"Chatbot response: {response}")

    speak_response(response)

if __name__ == "__main__":
    chatbot_conversation()
