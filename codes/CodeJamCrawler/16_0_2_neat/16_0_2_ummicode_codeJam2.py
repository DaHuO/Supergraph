#!/usr/bin/python

import sys

def flipPancakes(tokenList):
    currentCount = 0
    numNeg = 0
    prevNumNeg = 0
    magicNum = 0
    negFlag = False
    for item in tokenList:
        if item is "-":
            negFlag = True
            currentCount = currentCount + 1
            numNeg = numNeg + 1
        else:
            currentCount = currentCount + 1
            if numNeg > prevNumNeg:
                magicNum = currentCount
            numNeg = 0
        if numNeg > prevNumNeg:
            magicNum = currentCount
            prevNumNeg = numNeg
        
    if negFlag is False:
        return tokenList, True
    else:
        for i in range(magicNum):
            if tokenList[i] is "+":
                tokenList[i] = "-"
            else:
                tokenList[i] = "+"
        return tokenList, False

t = int(input())
for i in range(1, t + 1):
    inputToken = raw_input()
    tokenList = list(inputToken)
    iterationNum = 0
    while True:
        tokenList, result = flipPancakes(tokenList)
        if result is True:
           break
        iterationNum = iterationNum + 1
    print("Case #{}: {}".format(i, iterationNum))
