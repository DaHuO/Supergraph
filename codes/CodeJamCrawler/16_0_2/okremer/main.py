__author__ = 'okremer'

import sys

def flip(arr, howMany):
    origArr = arr
    arr = arr[0:howMany]
    tempArr = arr

    for i in range(0, len(tempArr)):
        if (arr[i] == "+"):
            tempArr[i] = "-"
        else:
            tempArr[i] = "+"

    tempArr.reverse()
    if (len(origArr) > howMany):
        tempArr += (origArr[howMany:])
    return tempArr

def getBlank(arr):
    result = 0
    for x in arr:
        if (x == '-'):
            result+=1
        else:
            break
    return result

def getNonBlank(arr):
    result = 0
    for x in arr:
        if (x == '+'):
            result+=1
        else:
            break
    return result

inputFile = open(sys.argv[1], 'r')
outputFile = open("output.txt",'w')

lineCount = inputFile.readline()

for i in range(0,int(lineCount)):
    currLine = inputFile.readline()
    s = list(currLine)
    if ('\n' in s):
        s = s[0:len(s) - 1]
    flipCount = 0
    while ('-' in s):
        if (s[0] == '+'):
            nextPos = getNonBlank(s)
            s = flip(s, nextPos)
        else:
            nextPos = getBlank(s)
            s = flip(s, nextPos)
        flipCount += 1
    outputFile.write("Case #" + str(i + 1) + ": " + str(flipCount) + "\n")
