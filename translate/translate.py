# pip install googletrans==4.0.0-rc1

from googletrans import Translator

def translate_malayalam_to_english(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='ml', dest='en')
    translated_text = translation.text
    return translated_text

# Usage
malayalam_text = "എനിക്ക് സഹായം വേണം"
english_text = translate_malayalam_to_english(malayalam_text)
print(english_text)