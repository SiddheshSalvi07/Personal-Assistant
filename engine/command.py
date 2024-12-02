import pyttsx3

def Speak(text):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',174)
    print(voices)
    engine.say(text)
    engine.runAndWait()
Speak("i love india")