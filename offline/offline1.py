# import speech_recognition as sr
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# # Reading Audio file as source
# # Listening the audio file and store in audio_text variable
# with sr.AudioFile('path_to_audio_file.wav') as source:
#     audio_text = recognizer.listen(source)

# # Using Google Speech Recognition (alternative recognizer) 
# try:
#     # Using Sphinx
#     text = recognizer.recognize_sphinx(audio_text)
#     print('Converting audio transcripts into text ...')
#     print(text)

# except Exception as e:
#     print('Error:', str(e))


# Initialize recognizer class (for recognizing the speech)
# recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Adjusting for ambient noise, please wait...")
    recognizer.adjust_for_ambient_noise(source, duration=5)
    print("Ready for speech input. Please speak.")

    while True:
        try:
            # Listen for the first phrase and extract it into audio data
            print("Listening...")
            audio = recognizer.listen(source, timeout=5)

            # Recognize speech using Sphinx
            text = recognizer.recognize_sphinx(audio)
            print("You said: " + text)

        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")

        except sr.UnknownValueError:
            print("Sphinx could not understand audio")

        except sr.RequestError as e:
            print(f"Sphinx error; {e}")

        except KeyboardInterrupt:
            print("Exiting...")
            break
