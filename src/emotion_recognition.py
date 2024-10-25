import cv2
from deepface import DeepFace

def detect_emotion():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = DeepFace.analyze(frame, actions=['emotion'])
        emotion = results['dominant_emotion']
        print("Detected Emotion:", emotion)
        cv2.imshow('Emotion Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
""  
