'''
Created on 9 avr. 2016

@author: jeremie
'''

MYINPUT  = "A-large.in"
MYOUTPUT = "A-large.out"

def inputFileToCasesList():
    myFile = open(MYINPUT)
    fLinesList = myFile.readlines()
    cleanList = []
    for elt in fLinesList:
        if elt[:1] == '\n':
            cleanList.append(int(elt[:-1]))
        else:
            cleanList.append(int(elt))
    nbCases = cleanList.pop(0)
    myFile.close()
    return nbCases, cleanList
    
def solveN(theN):
    theNumbersList = range(10)
    lastNumber = theN
    sameListStepCount = 0
    while len(theNumbersList) != 0:
        print theNumbersList, lastNumber
        for charDigit in str(lastNumber):
            if theNumbersList.count(int(charDigit)) > 0:
                theNumbersList.remove(int(charDigit))
                sameListStepCount = 0
            else:
                sameListStepCount = sameListStepCount + 1
        if len(theNumbersList) == 0:
            return lastNumber
        lastNumber = lastNumber + theN
        if sameListStepCount > 1024:
            return "INSOMNIA"
    
def justSolve(inList):
    resList = []
    for elt in inList:
        resList.append(solveN(elt))
    return resList

def putInOutputFile(resList):
    outputFile = open(MYOUTPUT, "w")
    resLines = []
    iterator = 1
    line = ""
    for res in resList:
        line = "Case #%d: %s\n" % (iterator, res)
        resLines.append(line)
        iterator = iterator + 1
    outputFile.writelines(resLines)
    outputFile.close()


if __name__ == '__main__':
    
    inputNbCases, inputCases = inputFileToCasesList()    
    outputResList = justSolve(inputCases)
    putInOutputFile(outputResList)
    
    pass