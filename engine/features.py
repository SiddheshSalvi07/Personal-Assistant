import os
import re
from playsound import playsound
from engine.command import Speak
from engine.constant import ASSISTANT_NAME
import eel
import pywhatkit as kit

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

    if query!="":
        Speak("Opening" +query)
        os.system("start" +query)
    else:
        Speak("not found")
#-----------------------------for Youtube-----------------------------------------------
def playYoutube(query):
    search_term = extract_yt_term(query)
    Speak("Playing "+search_term+" on Youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    pattern = r"play\s+(.*?)\s+on\s+youtube"
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None
