
import parselmouth
import praatio
from praatio import textgrid
from praatio import audio
import glob
import os.path
from os.path import join
import wave



#after cutting the syllables from textgrid intervals

#   methods from pilot paper: 

#   Duration was adjusted to measure 150 ms and 250 ms in short and long Vs 
#   (respectively) by copying or deleting every other voicing period from 
#   the sound wave as needed, preserving the vowel’s natural amplitude contour. 
#   before concat, make stressed V +3dB 
#   Intensity was normalised by changing gain to 65 dB in unstressed Vs and 68 dB 
#   in stressed Vs. 
# unstressed syll intensity: 
# stressed syll intensity: +3dB 
# each stressed syll was given a pitch contour level at 225Hz declining to 180Hz 
# 
#   After concatenation, every trisyllable was given a pitch contour
#   in which f0 was level at 225 Hz during the initial, medial, or
#   final third of the stressed V (depending on whether stress was initial, medial, 
#   or final) and declined smoothly to plateau at 180 Hz in unstressed vowels.

#   Duration was adjusted to measure 150 ms and 250 ms in short and long Vs 
#   (respectively) by copying or deleting every other voicing period from 
#   the sound wave as needed, preserving the vowel’s natural amplitude contour. 



def normDur(input,output,floatLen): 
    
     for fn in os.listdir(input):
        if ".wav" not in fn:
            continue 
        name = join(input,fn)
        audio.extractSubwav(name,join(output,fn +"cut.wav"),0,floatLen)
        
       
        


input = "/Users/sarah/Git/stress_learn/test"
output = "/Users/sarah/Git/stress_learn/output"
floatLen = 0.15

normDur(input,output,floatLen)
# Intensity was normalised by changing gain to 65 dB in unstressed Vs and 68 dB 
# in stressed Vs. 
#def normIntensity(input,float):

#def concatenate(inputList, inputWav):


#After concatenation, every trisyllable was given a pitch contour
#  in which f0 was level at 225 Hz during the initial, medial, or
# final third of the stressed V (depending on whether stress was initial, medial, 
# or final) and declined smoothly to plateau at 180 Hz in unstressed vowels.

#def pitchContour(input):