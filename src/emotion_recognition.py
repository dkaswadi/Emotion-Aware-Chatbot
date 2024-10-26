from transformers import pipeline

# Load a pre-trained emotion classification model
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def detect_emotion_from_text(text):
    emotions = emotion_classifier(text)
    print(f"Detected emotion: {emotions[0]['label']}")
    return emotions[0]['label']
