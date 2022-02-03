import parselmouth
from parselmouth import call
import pandas as pd
import glob
import os.path
# import ipython
# from ipython.display import Audio
stim_input = " "
stim_base = pd.read_csv(stim_input + "stim.csv")

#read in needed trisyllable from csv
def makeLists(stimuli):
    f

nonce = "ba_da_ga"
#split string into individual syllables
triplet = (nonce.split('_'))
init = []
penult = []
ulti = []


def affixer(triplet,output):
  
    #create sound object of each syllable
    syll1 = parselmouth.Sound(syll_root + triplet[0]+".wav")
    syll2 = parselmouth.Sound(syll_root + triplet[1]+".wav")
    syll3 = parselmouth.Sound(syll_root + triplet[2]+".wav")
    #create list of sound objects
    tri_syll = [syll1,syll2,syll3]

    word = parselmouth.Sound.concatenate(tri_syll,0.0)
    word.save(output + nonce + ".wav","WAV")

# Audio(data=sound.values, rate=sound.sampling_frequency)



syll_root = "/Users/sarah/Git/stress_learn/syllables/"
output_words = "/Users/sarah/Git/stress_learn/words/"