__author__ = 'fbleite'

from PerformanceMeasure import PerformanceMeasure
from OutputFormat import printOutput


def solveProblem(line):
    seenNumbers = []
    N = 0
    originalNumber = int(line)
    while (len(seenNumbers) < 10) and  (N < 10000):
        N = N +1
        lastSeenNumber = originalNumber  * N
        for digit in str(lastSeenNumber):
            if not digit in seenNumbers:
                seenNumbers.append(digit)
    if len(seenNumbers) == 10:
        return [lastSeenNumber]
    else :
        return ['INSOMNIA']




def SheepCount():
    testFile = open("/Users/fbleite/Development/CodeJam/A-large.in", "r")
    line1 = False
    numberOfCases = 0
    lineIndex = 0
    credit = 0
    numberOfItems = 0
    finalSet = []

    for line in testFile:
        if (not line1):
            line1=True
            numberOfCases = int(line)
        else :
            finalSet.append(solveProblem(line))

    printOutput(finalSet)



perfMeasure = PerformanceMeasure(SheepCount)
perfMeasure = perfMeasure.runFuntionAndCheckPerformance()