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

#edit to keep same consonants non-adjacent
#no more than one /z/ per word
def makeWords(word_list):  
    cc = 0
    wordList = []
    wordList.append(word_list)
    peak = len(word_list)
    for element in word_list:   
        firstSyl = word_list[element[0:1]]



        cc += 1
       
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

