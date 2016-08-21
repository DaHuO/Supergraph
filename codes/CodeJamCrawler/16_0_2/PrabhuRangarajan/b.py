#!/usr/bin/python

import sys
inFile = str(sys.argv[1])

fptr = open(inFile)
nTc = int(fptr.readline().strip("\n"))
for caseIdx in range(1, nTc+1):
    line = fptr.readline().strip("\n")

    list_line = []  #string is immutable so store in list
    for i in line:
        list_line.append(i)

    count = 0
    currIdx = 0
    endIdx = len(list_line) - 1

    isDone = 0
    while (isDone != 1):
        while (list_line[endIdx] == '+'):
            endIdx -= 1;
            if (endIdx < 0):  #Got +++++
                isDone = 1
                break

        if (isDone != 1):
            chr = list_line[currIdx]
            while (currIdx <= endIdx and list_line[currIdx] == chr): 
                if (chr == '-'):
                    list_line[currIdx] = '+'
                else:
                    list_line[currIdx] = '-'
                currIdx += 1
            count += 1
            if (currIdx > endIdx and chr == '-'):
                isDone = 1

    print "Case #%d: %d" %(caseIdx, count)
