
import speech_recognition as sr
from langdetect import detect

def detect_language_from_audio(filename):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = r.record(source)  # Load the audio file

    try:
        print("Detecting language...")
        text = r.recognize_google(audio)
        detected_language = detect(text)
        print(f"Detected language: {detected_language}")
        return detected_language
    except sr.UnknownValueError:
        print("Sorry, the language could not be detected.")
    except sr.RequestError:
        print("Sorry, there was an error while processing the request.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return ""

# Usage
audio_file = "./output.mp3"
detected_language = detect_language_from_audio(audio_file)
