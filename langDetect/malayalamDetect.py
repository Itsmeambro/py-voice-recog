# prompt: malayalam audio detect
from charset_normalizer import detect
import speech_recognition as sr

def detect_malayalam_audio(filename):
    r = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = r.record(source)  # Load the audio file

    try:
        print("Detecting language...")
        text = r.recognize_google(audio)
        language = detect(text)
        if language == 'ml':
            print("Detected language: Malayalam")
            return True
        else:
            print(f"Detected language: {language}")
            return False
    except sr.UnknownValueError:
        print("Sorry, the audio could not be converted to text.")
    except sr.RequestError:
        print("Sorry, there was an error while processing the audio.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return False

# Usage
audio_file = "output.mp3"
is_malayalam = detect_malayalam_audio(audio_file)
if is_malayalam:
    print("The audio is in Malayalam.")
else:
    print("The audio is not in Malayalam.")
