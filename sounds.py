#!/usr/bin/env python

import random
import subprocess
from pathlib import *

def gimmeSomeBanter:
    pathToAudio = Path("./AudioFiles/")
    audioFiles = list(pathToAudio.glob('**/*.mp3'))
    #print audioFiles
    while (randomChoice == lastRandom):
        ramdonChoice = random.randint(0, len(audioFiles)-1)
        lastRandom = randomChoice
        selectedFile = PurePosixPath(audioFiles[ramdonChoice])
        #print selectedFile
        subprocess.Popen(("mpg123", str(selectedFile))).wait()


