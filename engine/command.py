import sys
import time
import pyttsx3
import speech_recognition as sr
import eel

def Speak(text):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            # Listen with a 10-second timeout and 7-second phrase time limit
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("No speech detected within 10 seconds, terminating.")
            eel.DisplayMessage("No speech detected within 10 seconds, terminating.")
            sys.exit()  # Automatically exit if no speech within the timeout
        except Exception as e:
            print(f"Error: {e}")
            eel.DisplayMessage("Error occurred, exiting.")
            sys.exit()  # Exit on any other exception

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
    
    except Exception as e:
        print("Could not understand audio.")
        eel.DisplayMessage("Could not understand audio.")
        return ""  # Return empty string if speech could not be recognized
    
    return query.lower()

@eel.expose
def AllCommands():
    try:
        query=takecommand()
        if "hello" in query:
            Speak("Hello Sir, How can I help you?")
        elif "open" in query:
            from engine.features import openCommand 
            openCommand(query)
        elif "on youtube":
            from engine.features import playYoutube
            playYoutube(query)
    
        else:
            print("not run")
            eel.DisplayMessage("I am not able to understand")
            Speak("I am not able to understand")
    
        eel.ShowUi()
    except Exception as e:
        print(e)



