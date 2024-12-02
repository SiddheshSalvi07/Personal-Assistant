from playsound import playsound

import eel

@eel.expose
def playAssistantSound():
    music_dir="frontend\\static\\audio\\startingaudio.mp3"
    playsound(music_dir)
