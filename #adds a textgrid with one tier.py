#adds a textgrid with one tier

import os
from os.path import join
from praatio import textgrid
from praatio import praat_scripts
from praatio.utilities.constants import (
    Interval)

def makeGrid(inputWav,outputTG, tierName):
    for fn in os.listdir(inputWav):
        if ".wav" not in fn:
            continue
        tg = textgrid
        newTier = textgrid.IntervalTier(tierName, entryList= [('0', tg.maxTimestamp,
        'test'),],minT=0,maxT=tg.maxTimestamp)
        tg.addTier(newTier)
        tg.save(join(outputTG,fn),'short_textgrid', True)



inputWav = "/Users/sarah/Git/stress_learn/test"
outputTG = "/Users/sarah/Git/stress_learn/output"
tierName = "CV"

makeGrid(inputWav,outputTG,tierName)