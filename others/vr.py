
import speech_recognition as sr

recognizer = sr.Recognizer()

def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening")
        audio = recognizer.listen(source=source)
        
    return audio

def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_lex(audio)
        print("You said: "+text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry")
    
    except sr.RequestError as e:
        text = ""
        print("Error: {0}".format(e))
    return text

def process_voice_command(text):
    if "hello" in text.lower():
        print("Hello! How can I help you?")
    elif "goodbye" in text.lower():
        print("Goodbye! Have a great day!")
        return True
    else:
        print("I didn't understand that command. Please try again.")
    return False

def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == "__main__":
    main()