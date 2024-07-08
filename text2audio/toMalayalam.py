# !pip install gTTS

from gtts import gTTS

def malayalam_word_to_speech(text):
    # Convert the text to speech
    output = gTTS(text=text, lang='ml', slow=False)

    # Save the audio file
    output.save("output.mp3")

    # Play the audio file
    # !mpg321 output.mp3

# Usage
malayalam_text = "എനിക്ക് സഹായം വേണം"
malayalam_word_to_speech(malayalam_text)
