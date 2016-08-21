__author__ = 'okremer'

import sys

inputFile = open(sys.argv[1], 'r')
outputFile = open("output.txt",'w')
lineCount = inputFile.readline()
k = 0

def getLargestParty(partiesData):
    max = 0
    currParty = 0
    for i in range(0,len(partiesData)):
        if (partiesData[i] > max):
            currParty = i
            max = partiesData[i]
    return currParty

def sameSizeParty(partiesData, biggestParty):
    size = partiesData[biggestParty]
    for i in range(0, len(partiesData)):
        if (partiesData[i] == size and i != biggestParty):
            return i
    return False

def legalRoom(partiesData):
    totalInRoom = 0
    if (roomIsEmpty(partiesData)):
        return True
    for i in range(0, len(partiesData)):
        totalInRoom += partiesData[i]

    for i in range(0, len(partiesData)):
        if (partiesData[i] / totalInRoom > 0.5):
            return False
    return True

def roomIsEmpty(partiesData):
    for i in range(0, len(partiesData)):
        if (partiesData[i] > 0):
            return False
    return True

for line in range(0, int(lineCount)):

    result = ""
    numberOfParties = inputFile.readline()
    partiesData = inputFile.readline().replace('\n', '').split(' ')
    for i in range(0, len(partiesData)):
        partiesData[i] = int(partiesData[i])
    while (roomIsEmpty(partiesData) == False):
        biggestParty = getLargestParty(partiesData)
        sameSize = sameSizeParty(partiesData, biggestParty)
        tempArr = list(partiesData)
        tempResult = result
        if (sameSize != False):
            tempResult += chr(65 + biggestParty) + chr(65 + sameSize)
            tempArr[biggestParty] -= 1
            tempArr[sameSize] -= 1
        else:
            tempResult += chr(65 + biggestParty)
            tempArr[biggestParty] -= 1

        if (legalRoom(tempArr) == True):
            partiesData = list(tempArr)
            result = tempResult
        else:
            partiesData[biggestParty] -= 1
            result += chr(65 + biggestParty)
        result += ' '


    print ("Case #" + str(k + 1) + ": " + str(result) + "\n")
    outputFile.write ("Case #" + str(k + 1) + ": " + str(result) + "\n")
    k += 1