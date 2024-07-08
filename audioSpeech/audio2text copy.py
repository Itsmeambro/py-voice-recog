
import speech_recognition as sr

# Create a speech recognition object
r = sr.Recognizer()

# Prompt the user to speak into the microphone
print("Speak into the microphone:")

# Listen for the user's input
with sr.Microphone() as source:
    audio = r.listen(source)

# Recognize the speech and print the result
try:
    recognized_text = r.recognize_google(audio)
    print("You said:", recognized_text)
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said.")
except sr.RequestError:
    print("Sorry, there was an error processing your request.")