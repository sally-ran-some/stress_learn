#let none have a basis for thinking that there are prefixes and suffixes



#avoid first syllables of the same CV sequence
#avoid last syllables of the same CV sequence 

#don't allow more than two of the same initial syllable in a list 
#don't allow more than two of the same codas in a list in a list
#don't allow more than two of all the same vowel quality in a list

#listmaker
def getwords(input):
    file = open(input)
    metaList = file.readlines()
    bb = 0
    while bb < len(metaList):
        Sname = metaList[bb]
        Sname = Sname.strip("\n")
        metaList[bb] = Sname
        bb += 1
    return metaList


def makeLists(input, output):
    list = 0 
    
    

