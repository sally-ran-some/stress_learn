import random


def getSylls(input):
    file = open(input)
    syllList = file.readlines()
    bb = 0
    while bb < len(syllList):
        Sname = syllList[bb]
        Sname = Sname.strip("\n")
        syllList[bb] = Sname
        bb += 1
    return syllList


def makeWords(syllable_list):  
    cc = 0
    wordList = []
    peak = len(syllable_list)
    while cc < peak:
        initial = syllable_list[cc]
        cc += 1
        dd = 0
        while dd < peak:
            tmp = syllable_list[dd]
            if tmp != initial:
                penult = tmp
                dd += 1
            else: 
                dd += 1
                continue
            ee = 0
            while ee < peak:
                tmp = syllable_list[ee]
                if ((tmp == initial) or (tmp == penult)):
                    ee += 1
                    continue
                if (tmp[0] == initial[0]) & (tmp[0] == penult[0]):
                    ee += 1
                    continue
                else: 
                    ultima = tmp 
                    ee+=1
                    word = (initial, penult, ultima)
                    wordList.append(word)
    print(wordList)      
    return wordList
def nonceToFile(wordList, output1, output2):
    f = open(output1, 'w')
    for t in wordList:
        line = ' ' .join(str(x) for x in t)
        f.write(line + '\n')
    f.close()
    randList = random.sample(wordList,300)
    g = open(output2,'w')
    for t in randList:
        line = ' ' .join(str(x) for x in t)
        g.write(line +'\n')
    g.close()  






#Same syllable not repeated in word		
#All three Vs cold be the same		
#Same C no more than twice		



inputSyll = "/Users/sarah/Git/stress_learn/syllables.txt"
outPutWords = "/Users/sarah/Git/stress_learn/nonceWords.txt"
outPutSample = "/Users/sarah/Git/stress_learn/sample.txt"

nonceToFile(makeWords(getSylls(inputSyll)),outPutWords,outPutSample)

