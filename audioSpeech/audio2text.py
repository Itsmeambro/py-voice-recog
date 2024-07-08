# prompt: Speech recognition from mic

import speech_recognition as sr

def recognize_speech_from_mic():
  """
  This function recognizes speech from the microphone and returns the transcribed text.
  """

  # Initialize the recognizer
  r = sr.Recognizer()

  # Set the recognition parameters
  r.pause_threshold = 3 
  r.operation_timeout = 5 

  # Start listening to the microphone
  with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

  try:
    text = r.recognize_google(audio)
    print("You said:", text)
    return text
  except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
  except sr.RequestError as e:
    print("Error:", e)

# Usage
speech = recognize_speech_from_mic()
