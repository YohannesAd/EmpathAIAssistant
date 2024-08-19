import speech_recognition as sr

from requests_html import HTMLSession
import text_To_speech

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        audio = r.listen(source)
        
        voice_data=''
    try:
        voice_data = r.recognize_google(audio)
        
        return voice_data
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


