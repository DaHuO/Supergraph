__author__ = 'okremer'

import sys

inputFile = open(sys.argv[1], 'r')

lineCount = inputFile.readline()
for i in range(0,int(lineCount)):
    currLine = int(inputFile.readline())
    if currLine == (currLine * 2):
        print "Case #" + str(i+1) + ": INSOMNIA"
        next
    else:
        j = 1
        arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        while 1 in arr:
            currNumber = currLine * j
            lastNumber = currNumber
            while currNumber != 0:
                arr[currNumber % 10] = 0
                currNumber /= 10
            j+=1
        print "Case #" + str(i+1) + ": " + str(lastNumber)
