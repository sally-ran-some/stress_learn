
import praatio
from praatio import audio
import os.path
from os.path import join


#cut sylls to NEXT zero crossing

def cutNext(inputWav,output):
    for fn in os.listdir(inputWav):
        if ".wav" not in fn:
            continue
        wavObj = audio.openAudioFile(join(inputWav,fn))
        end = wavObj.getDuration() - .01
        start = 0
        newStart = audio.AbstractWav.findNextZeroCrossing(wavObj,start,.01,False)
        newEnd = audio.AbstractWav.findNextZeroCrossing(wavObj,end,.01,False)
        newWav = wavObj.new()
        newWav.deleteSegment(start,newStart)
        newWav.deleteSegment(newEnd, wavObj.getDuration())
        newWav.save(join(output,fn))
    
inputWav = "/Users/sarah/Git/stress_learn/test"
output = "/Users/sarah/Git/stress_learn/output"
cutNext(inputWav,output)

