
import string, os, time, sys

    
def HandleCase(f, caseIndex):
    caseline = f.readline().rstrip("\r\n")
    firstNum = int(caseline)
    
    if firstNum == 0:
        print "Case #%d: INSOMNIA" % caseIndex
        return

    remainingInts = set([0, 2, 3, 4, 5, 6, 7, 8, 9])
    thisNum = firstNum
    nextNum = firstNum
    while len(remainingInts) > 0:
        thisNum = nextNum
        strInt = str(thisNum)
        for char in strInt:
            remainingInts.discard(int(char))
        nextNum = thisNum + firstNum

    print "Case #%d: %d" % (caseIndex, thisNum)

inputFile = sys.argv[1]
f = open(inputFile, "r")
numCases = int(f.readline())
for i in range(0, numCases):
    HandleCase(f, i+1)


