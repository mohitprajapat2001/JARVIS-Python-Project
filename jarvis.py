import speech_recognition as sr
import win32com.client as pywin

def say(str):
    speaker = pywin.Dispatch("SAPI.SpVoice")
    speaker.Speak(str)

def listen():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print("Listening... Sir!")
            audio = r.listen(mic)
            text = r.recognize_google(audio)
            return text.lower()
    except Exception:
        print("Sorry Sir! Please Say Again")
