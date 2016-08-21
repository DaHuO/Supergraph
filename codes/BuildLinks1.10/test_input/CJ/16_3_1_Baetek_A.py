import operator
senators = {}

def main(inStr):
    global senators
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    senatorsList = inStr.split()
    senatorsDict = {}
    for i in range(len(senatorsList)):
        senatorsDict[alpha[i]] = senatorsList[i]
    senators = senatorsDict
    return recurReturn("")
        
def recurReturn(senatorsEscape):
    global senators
    if removeLastTwo():
        senatorsEscape += removeMaxOne()
        senatorsEscape += removeMaxOne()
        return senatorsEscape
    if baseCase():
        return senatorsEscape[:-1]
    senatorsEscape += removeMaxOne()
    if baseCase():
        return senatorsEscape
    if not majority(senators):
        senatorsEscape += removeMaxOne()
    return recurReturn(senatorsEscape + " ")
    
def removeLastTwo():
    global senators
    ones = 0
    nonzeros = 0
    for senator in senators:
        if int(senators[senator]) == 1:
            ones += 1
        elif int(senators[senator]) != 0:
            nonzeros += 1
    if ones == 2 and nonzeros == 0:
        return True
    
    
        
def baseCase():
    global senators
    quantL = []
    zeros = 0
    for senator in senators:
        quantL += [senators[senator]]
    for no in quantL:
        if no == "0":
            zeros += 1
    if zeros == len(quantL):
        return True
    return False
    
    
def removeMaxOne():
    global senators
    el = str(max(senators.items(), key=operator.itemgetter(1))[0])
    senators[str(max(senators.items(), key=operator.itemgetter(1))[0])] = str(int(senators[str(max(senators.items(), key=operator.itemgetter(1))[0])]) - 1)
    return el


def removeMaxTwo():
    global senators
    senatorsTemp = senators
    el = senatorsTemp
    senatorsTemp[str(max(senatorsTemp.items(), key=operator.itemgetter(1))[0])] = str(int(senatorsTemp[str(max(senatorsTemp.items(), key=operator.itemgetter(1))[0])]) - 1)
    el += str(max(senators.items(), key=operator.itemgetter(1))[0])
    senatorsTemp[str(max(senatorsTemp.items(), key=operator.itemgetter(1))[0])] = str(int(senatorsTemp[str(max(senatorsTemp.items(), key=operator.itemgetter(1))[0])]) - 1)
    senators = senatorsTemp
    return el
    
def majority(dictMain):
    dictionary = dictMain.copy()
    maxLt = str(max(dictionary.items(), key=operator.itemgetter(1))[0])
    dictionary[maxLt] = str(int(dictionary[maxLt]) - 1)
    maxint = int(max(dictionary.items(), key=operator.itemgetter(1))[1])
    maxLt = str(max(dictionary.items(), key=operator.itemgetter(1))[0])
    dictionary[maxLt] = str(int(dictionary[maxLt]) - 1)
    secondaryMax = int(max(dictionary.items(), key=operator.itemgetter(1))[1])
    if secondaryMax == 0:
        return True
    if (maxint / secondaryMax < 2):
        return False
    return True
    
    
def fileHandler(fileName):
    f = open(fileName, 'r')
    rString = ""
    lineCnt = 1
    for line in f:
        if len(line.split()) < 2:
            continue
        rString += "Case #" + str(lineCnt) + ": " + main(line[:-1]) + "\n"
        lineCnt += 1
    f.close()
    w = open('results.txt','w')
    w.write(rString[:-1])
    w.close()

fileHandler('A-small-attempt0 (4).in')