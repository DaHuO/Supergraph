'''
Created on 9 avr. 2016

@author: jeremie
'''

MYINPUT  = "B-large.in"
MYOUTPUT = "B-large.out"

def inputFileToCasesList():
    myFile = open(MYINPUT)
    fLinesList = myFile.readlines()
    cleanList = []
    for elt in fLinesList:
        if elt.count('\n') > 0:
            elt = elt[:-1]
        cleanList.append(elt)
    nbCases = cleanList.pop(0)
    myFile.close()
    return nbCases, cleanList
    
def isolateHappyBottom(stack):
    if len(stack) > 1:
        stack.pop()
    s1 = stack.pop()
    s2 = ""
    while len(s1) > 0 and s1[-1:] == '+':
        s2 = s2 + s1[-1:]
        s1 = s1[:-1]
    return [s1, s2]
    
def flipSomePC(stack):
    workingStack = stack[0]
    resultString = ""
    if workingStack[:1] == '-':
        workingStack = workingStack[::-1]
        for myChar in workingStack:
            if myChar == '-':
                resultString = resultString + '+'
            else:
                resultString = resultString + '-'
        return [resultString, stack[1]]
    else:
        stopChangePlusIntoMinus = False
        for myChar in workingStack:
            if myChar == '+':
                if stopChangePlusIntoMinus == False:
                    resultString = resultString + '-'
                else:
                    resultString = resultString + '+'
            else:
                resultString = resultString + '-'
                stopChangePlusIntoMinus = True
        return [resultString, stack[1]]
    
def solveN(theStack):
    counter = 0
    tmpCounter = 0
    print counter, theStack
    theStack = isolateHappyBottom(theStack)
    print counter, theStack
    if theStack[0] == '':
        print "----------------"
        return counter, theStack
    theStack = flipSomePC(theStack)
    counter = counter + 1    
    print counter, theStack
    tmpCounter, theStack = solveN(theStack)
    counter = counter + tmpCounter
    print "----------------"
    return counter, theStack
    
def justSolve(inList):
    resList = []
    noneed = None
    solution = 0
    for elt in inList:
        elt = [elt]
        solution, noneed = solveN(elt)
        print solution, noneed
        resList.append(solution)
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
    print inputNbCases, inputCases
    outputResList = justSolve(inputCases)
    putInOutputFile(outputResList)
    
    pass