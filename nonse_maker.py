import random


# def getSylls(input):
#     file = open(input)
#     syllList = file.readlines()
#     bb = 0
#     while bb < len(syllList):
#         Sname = syllList[bb]
#         Sname = Sname.strip("\n")
#         syllList[bb] = Sname
#         bb += 1
#     return syllList

#edit to keep same consonants non-adjacent
# no adjacent /e/ vowels
def makeWords(syllable_list):  
    cc = 0
    wordList = []
    peak = len(syllable_list)
    while cc < peak:
        initial = syllable_list[cc]
        cc += 1
        z = False
        if initial[0] == 'z': z = True
        dd = 0
        while dd < peak:
            tmp = syllable_list[dd]
            #no identical adjacent sylls, no adjacent same onset syllables
            if (tmp[0] == 'z') & (z == True):
                dd += 1
                continue
            elif (tmp != initial) & (tmp[0] != initial[0]):
                penult = tmp
                dd += 1
            else: 
                dd += 1
                continue
            ee = 0
            while ee < peak:
                tmp = syllable_list[ee]
                if (z == True) & (tmp[0] == 'z'):
                    ee += 1
                    continue
                elif ((tmp == initial) or (tmp == penult)):
                    ee += 1
                    continue
                elif (tmp[0] == initial[0]) & (tmp[0] == penult[0]):
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
    randList = random.sample(wordList,200)
    g = open(output2,'w')
    for t in randList:
        line = ' ' .join(str(x) for x in t)
        g.write(line +'\n')
    g.close()  






#Same syllable not repeated in word		
#All three Vs cold be the same		
#Same C no more than twice		
onsets = "bdgn"
vowels = "aeo"
syllList = []
for onset in onsets: 
    for vowel in vowels:
        syllList.append(onset+vowel)


#inputSyll = "/Users/sarah/Git/stress_learn/syllables.txt"
outPutWords = "/Users/sarahgilbert/stress_learn_spring/stress_learn/nonceWords.txt"
outPutSample = "/Users/sarahgilbert/stress_learn_spring/stress_learn/sample.txt"

nonceToFile(makeWords(syllList),outPutWords,outPutSample)
