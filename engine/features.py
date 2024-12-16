import os
import re
import struct
import time
import webbrowser
from playsound import playsound
import pvporcupine
import pyaudio
from engine.command import Speak
from engine.constant import ASSISTANT_NAME
import eel
import pywhatkit as kit
import sqlite3

from engine.helper import extract_yt_term

conn = sqlite3.connect("PersonalAi.db")
cursor = conn.cursor()
#--------------------------for playing Assistant Starting Audio-------------------------
@eel.expose
def playAssistantSound():
    music_dir="frontend\\static\\audio\\startingaudio.mp3"
    playsound(music_dir)

#------------------------------for open Command-----------------------------------------
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name!= "":

        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)',(app_name,))
            results = cursor.fetchall()

            if len(results)!=0:
                Speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results)==0:
                cursor.execute("SELECT url FROM web_command WHERE name IN (?)",(app_name,))
                results = cursor.fetchall()

                if len(results)!=0:
                    Speak("Opening "+query)
                    webbrowser.open(results[0][0])
                else:
                    Speak("Opening "+query)
                    try:
                        os.system("start "+query)
                    except:
                        Speak("Not Found")
        except:
            Speak("Some things went wrong")


#-----------------------------for Youtube-----------------------------------------------
def playYoutube(query):
    search_term = extract_yt_term(query)
    Speak("Playing "+search_term+" on Youtube")
    kit.playonyt(search_term)

#------------------------------for hot word detection-----------------------------------
def hotWordDetection():
    porcupine = None
    paud = None
    audio_stream = None

    # Path to your custom keyword file
    keyword_path = "frontend\\static\\wakeupkeyword\\phantom_en_windows_v3_0_0.ppn"

    try:
        # Initialize Porcupine with the custom keyword
        porcupine = pvporcupine.create(
            access_key='YEmae+lXv1bSdRkb8pivn8j/tL48ZYN8tMVWtz1GqSp3GuStAW2bmg==',
            keyword_paths=[keyword_path],
            )


        # Initialize PyAudio stream
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print("Listening for the wake word 'Phantom'...")

        # Main loop to process audio and detect the wake word
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            keyword_index = porcupine.process(keyword)

            if keyword_index >= 0:
                print("Hotword Detected!")

                # Trigger desired action (simulate Alt+S keypress here)
                import pyautogui as autogui
                autogui.keyDown('alt')
                autogui.press('s')
                time.sleep(2)
                autogui.keyUp('alt')

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Cleanup resources
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
        print("Hotword detection terminated.")