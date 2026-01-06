import speech_recognition as sr 
from requests_html import HTMLSession
import speak


def spech_to_text():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
      try:
        audio = r.listen(source, timeout=5, phrase_time_limit=5) # method
        voice_data = ''
        voice_data = r.recognize_google(audio)
        return voice_data
      except sr.WaitTimeoutError:
        speak.speak("No speech detected, please try again.")
        return ""
      except sr.UnknownValueError:
             speak.speak("Sorry, I didn't understand that.")
      except sr.RequestError:
            speak.speak('No internet connection, please turn on your internet.')  


