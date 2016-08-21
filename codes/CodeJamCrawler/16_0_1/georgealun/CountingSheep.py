# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:59:16 2016

@author: George Carter
"""
problemName = "A-large.out"
outFile = open(problemName, 'w')
lineCount = 1
with open("A-large.in") as inFile:
    numLines = inFile.readline()
    for line in inFile:
        strCase = "Case #" + str(lineCount) + ": "
        lineCount += 1
        blnAllNumbers=False
        numsSeen = []
        blnAllNumbers = False
        if int(line) == 0:
            outFile.write(strCase +'INSOMNIA \n')
        elif int(line) == 1:
            outFile.write(strCase + str(10) + '\n')
        else:
            currentNumber = int(line)
            while not blnAllNumbers:
                for strNumber in str(currentNumber):
                    if strNumber not in numsSeen:
                        numsSeen += strNumber
                if len(numsSeen) == 10:
                    outFile.write(strCase + str(currentNumber) + '\n')
                    blnAllNumbers = True
                else:
                    currentNumber += int(line)
