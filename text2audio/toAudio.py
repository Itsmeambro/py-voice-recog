# pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id) 
engine.setProperty('voice', voices[1].id)  

engine.say("I want speak this text")
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()