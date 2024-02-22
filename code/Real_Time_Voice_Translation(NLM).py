import speech_recognition as sr
from googletrans import Translator #used for translation
from gtts import gTTS #google text to speak
import os

def listen_and_translate():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        print("English: 'en', Spanish: 'es', German: 'de', Chinese: 'zh', Japanese: 'ja', Arabic: 'ar', Russian: 'ru', Italian: 'it', Portuguese: 'pt', Hindi: 'hi', French: 'fr', Dutch: 'nl', Swedish: 'sv', Korean: 'ko', Turkish: 'tr', Polish: 'pl', Indonesian: 'id', Greek: 'el'")
        # all above are popular languages and their codes
        print("Hindi: 'hi', Bengali: 'bn', Telugu: 'te', Marathi: 'mr', Tamil: 'ta', Urdu: 'ur', Gujarati: 'gu', Kannada: 'kn', Odia (Oriya): 'or', Malayalam: 'ml', Punjabi: 'pa', Assamese: 'as', Maithili: 'mai', Sanskrit: 'sa', Tulu: 'tcy' ")
        # all above are indian languages and their codes

        target_lang = input("In which language would you like to translate this? (e.g., 'fr' for French): ")

        translator = Translator()
        translation = translator.translate(text, dest=target_lang)
        translated_text = translation.text
        print("Translation:", translated_text)

        tts = gTTS(translated_text, lang=target_lang)
        tts.save("translation.mp3")
        os.system("start translation.mp3")

    except sr.UnknownValueError:
        print("sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("could not request results ; {0}".format(e))
    except Exception as e:
        print("error occurred:", e)

if __name__ == "__main__":
    listen_and_translate()
