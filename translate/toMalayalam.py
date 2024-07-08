from googletrans import Translator

def translate_english_to_malayalam(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='ml')
    translated_text = translation.text
    return translated_text

# Usage
english_text = "I need help"
malayalam_text = translate_english_to_malayalam(english_text)
print(malayalam_text)
