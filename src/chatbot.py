import sys
import os
import nltk  # Import nltk

# Adding the `src` directory to the system path for module imports
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '..', 'src')
sys.path.append(src_path)

from voice_to_text import listen_to_user
from emotion_recognition import detect_emotion_from_text
from nlp_module import generate_emotion_aware_response
from text_to_speech import speak_response

# Download necessary NLTK datasets (like stopwords and tokenizer)
nltk.download('punkt')
nltk.download('stopwords')

def chatbot_conversation():
    print("Chatbot is running. Say 'goodbye' to exit.")
    while True:
        user_input = listen_to_user()
        print(f"Recognized input: {user_input}")

        # Check if the user wants to end the conversation
        if user_input.lower() in ["goodbye", "exit", "quit", "stop"]:
            print("Chatbot: Goodbye! Have a great day!")
            speak_response("Goodbye! Have a great day!")
            break

        detected_emotion = detect_emotion_from_text(user_input)
        response = generate_emotion_aware_response(user_input, detected_emotion)
        print(f"Chatbot response: {response}")

        speak_response(response)

if __name__ == "__main__":
    chatbot_conversation()
