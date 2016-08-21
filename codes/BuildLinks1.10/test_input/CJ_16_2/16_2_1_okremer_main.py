__author__ = 'okremer'

import sys
from random import shuffle

inputFile = open(sys.argv[1], 'r')
outputFile = open("output.txt",'w')
numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
           "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
lineCount = inputFile.readline()
currLine = inputFile.readline()
i = 0

def numberToInt(num):
    if num == "ZERO":
        return 0
    elif num == "ONE":
        return 1
    elif num == "TWO":
        return 2
    elif num == "THREE":
        return 3
    elif num == "FOUR":
        return 4
    elif num == "FIVE":
        return 5
    elif num == "SIX":
        return 6
    elif num == "SEVEN":
        return 7
    elif num == "EIGHT":
        return 8
    elif num == "NINE":
        return 9

while currLine != '':
    s = list(currLine)
    tempArr = ""
    currAddition = 0
    for x in range(0, len(numbers)):
        currNum = numbers[x]
        flag = True
        tempS = list(s)
        currAddition = numberToInt(currNum)
        while flag:
            for letter in currNum:
                if letter not in tempS:
                    flag = False
                    break
                tempS.remove(letter)
            if flag:
                tempArr += str(currAddition)
                s = list(tempS)
    if (len(s) > 1):
        shuffle(numbers)
    else:
        tempArr = sorted(list(tempArr))
        outputFile.write("Case #" + str(i + 1) + ": " + "".join(str(x) for x in tempArr) + "\n")
        i += 1
        currLine = inputFile.readline()
