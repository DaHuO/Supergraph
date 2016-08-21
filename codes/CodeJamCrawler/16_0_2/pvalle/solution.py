
import string, os, time, sys


def getNumFlips(caseline):
    lastMinus = len(caseline)-1
    flips = 0
    while caseline[lastMinus] != '-':
        if lastMinus == 0:
            return 0
        lastMinus -= 1

    flips += 1
    endOfNextGrouping = lastMinus
    while True:
        while caseline[endOfNextGrouping] != '+':
            if endOfNextGrouping == 0:
                return flips
            endOfNextGrouping -= 1
    
        flips += 1

        while caseline[endOfNextGrouping] != '-':
            if endOfNextGrouping == 0:
                return flips
            endOfNextGrouping -= 1

        flips += 1

    
def HandleCase(f, caseIndex):
    caseline = f.readline().rstrip("\r\n")
    print "Case #%d: %d" % (caseIndex, getNumFlips(caseline))

inputFile = sys.argv[1]
f = open(inputFile, "r")
numCases = int(f.readline())
for i in range(0, numCases):
    HandleCase(f, i+1)

