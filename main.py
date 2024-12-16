import os

import eel

from engine.features import *

from engine.command import *

def start():
    eel.init("frontend")  

    playAssistantSound() 

    #os.system('start msedge.exe --app="http://localhost:5500/frontend/index.html"')

    eel.start("index.html",  size=(1000, 1000))
