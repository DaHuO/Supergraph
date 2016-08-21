#!/usr/bin/python

import sys
inFile = str(sys.argv[1])

fptr = open(inFile)
nTc = int(fptr.readline().strip("\n"))
for caseIdx in range(1, nTc+1):
    strNum = fptr.readline().strip("\n")
    num = int(strNum)
    origNum = num

    arr = [0] * 10

    isDone = 0
    while (isDone != 1):
        strNum = str(num)
        if (strNum == "0"):
            break
        for i in range(0, len(strNum)):
            arr[int(strNum[i])]+=1

        isDone = 1
        for j in arr:
            if (j == 0):
                isDone = 0
                num += origNum
                break

    if (num):
        print "Case #%d: %d" %(caseIdx, num)
    else:
        print "Case #%d: %s" %(caseIdx, "INSOMNIA")
