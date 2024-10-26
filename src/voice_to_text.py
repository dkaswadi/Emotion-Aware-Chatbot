import sounddevice as sd
import soundfile as sf
import numpy as np
import speech_recognition as sr

# Define recording parameters
SAMPLE_RATE = 16000  # Sample rate for the microphone input
DURATION = 5         # Maximum recording duration in seconds

def listen_to_user():
    # Record audio with sounddevice
    print("I'm listening... Please speak.")
    try:
        # Record the audio
        audio_data = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
        sd.wait()  # Wait for the recording to finish

        # Save the recorded audio to a temporary WAV file
        file_path = "temp_audio.wav"
        sf.write(file_path, audio_data, SAMPLE_RATE)

        # Use the SpeechRecognition library to process the recorded audio file
        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)  # Read the entire audio file

            try:
                # Recognize the speech using Google's recognition service
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                return "Sorry, I didn't catch that."
            except sr.RequestError:
                return "Sorry, there seems to be a problem with the service."

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Sorry, I couldn't process your audio."

# Test the function
if __name__ == "__main__":
    print(listen_to_user())
