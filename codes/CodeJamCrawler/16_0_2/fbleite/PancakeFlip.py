__author__ = 'fbleite'

# from PerformanceMeasure import PerformanceMeasure

def printOutput (outputSet) :
    for i in range(len(outputSet)):
        textToPrint = ''
        for j in range(len(outputSet[i])):
            textToPrint = textToPrint + ' ' + str(outputSet[i][j])
        print("Case #{}:{}".format(i+1, textToPrint))

def flipSingle(pancake):
    if pancake == '+':
        return '-'
    return '+'

def flipStack(pancakes, index):
    auxPancakes = []
    for i in range(index + 1):
        auxPancakes.append(flipSingle(pancakes[index - i]))
    auxPancakes.extend(pancakes[index+1:])
    return auxPancakes


def solveProblem(line):
    numberOfFlips = 0
    pancakes = list(line.replace('\r', '').replace('\n', ''))
    for i in range(len(pancakes) - 1):
        if pancakes[i] != pancakes[i+1]:
            pancakes = flipStack(pancakes, i)
            numberOfFlips += 1
    if '-' in pancakes:
        # pancakes = flipStack(pancakes)
        numberOfFlips +=1
    return [numberOfFlips]


def PancakeFlip():
    testFile = open("/Users/fbleite/Development/CodeJam/Pancakes/B-large.in", "r")
    line1 = False
    numberOfCases = 0
    finalSet = []

    for line in testFile:
        if (not line1):
            line1=True
            numberOfCases = int(line)
        else :
            finalSet.append(solveProblem(line))

    printOutput(finalSet)

PancakeFlip()

# perf = PerformanceMeasure(PancakeFlip)
# perf.runFuntionAndCheckPerformance()