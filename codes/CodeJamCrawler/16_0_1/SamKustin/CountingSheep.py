#!/usr/bin/env python3
#Sam Kustin
#Google Code Jam 2016 - Qualifying Round
#Counting Sheep

t = int(input())
testCounter = 0
for i in range(1, t + 1):
    n = int(input())
    numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    testCounter += 1
    multCounter = 1
    lastNum = n * multCounter
    if n == 0:
        lastNum = "INSOMNIA"
        print("Case #{}: {}".format(testCounter, lastNum))
    else:
        for char in str(n):
            if int(char) in numList:
                numList.remove(int(char))
        while len(numList) != 0:
            multCounter += 1
            lastNum = n * multCounter
            for char in str(lastNum):
                if int(char) in numList:
                    numList.remove(int(char))
        if len(numList) == 0:
            print("Case #{}: {}".format(testCounter, lastNum))
