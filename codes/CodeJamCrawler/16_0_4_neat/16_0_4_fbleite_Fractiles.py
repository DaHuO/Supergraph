__author__ = 'fbleite'

# from PerformanceMeasure import PerformanceMeasure
# K = Number of Tiles original sequence
# C = Complexity
# S = Number of clean tiles (Which you know the value)
# K^C final number of tiles
# Which tile should be clean in order to know that there was at least one G?




def printOutput (outputSet) :
    for i in range(len(outputSet)):
        textToPrint = ''
        for j in range(len(outputSet[i])):
            textToPrint = textToPrint + ' ' + str(outputSet[i][j])
        print("Case #{}:{}".format(i+1, textToPrint))



def solveProblem(line):
    solution = []
    numberInOriginalTiles, complexity, numberOfStudents = (int(attribute) for attribute in line.split(' '))
    if numberInOriginalTiles == numberOfStudents:
        solution.extend(i for i in range(1, numberOfStudents+1))
    return solution


def Fractiles():
    testFile = open("/Users/fbleite/Development/CodeJam/Fractiles/D-small-attempt0.in", "r")
    line1 = False
    numberOfCases = 0
    finalSet = []

    for line in testFile:
        if (not line1):
            line1=True
            numberOfCases = int(line)
        else :
            finalSet.append(solveProblem(line.replace('\r', '').replace('\n', '')))
    printOutput(finalSet)


Fractiles()

# perf = PerformanceMeasure(Fractiles)
# perf.runFuntionAndCheckPerformance()