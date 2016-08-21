#!/usr/bin/python

import sys

def solve(k, c, s):
    tiles = []
    for i in range(0, k, c):
        tiles.append(str(findColumn(k, c, i)))
    if len(tiles) > s:
        return "IMPOSSIBLE"
    else:
        return " ".join(tiles)

def findColumn(k, c, i):
    column = 1
    for j in range(min(c, k)):
        column += ((i + j) % k) * (k ** (c - j - 1))
    return column

def testColumn(message, actualResult, expectedResult):
    if actualResult == expectedResult:
        print message + ": PASSED"
    else:
        print message + ": FAILED - expected: " + str(expectedResult) + " got: " + str(actualResult)

def main():
    filename = sys.argv[1]
    filehandle = open(filename, 'r')
    lines = filehandle.readlines()
    #print str(lines)
    #testColumn("k=6 c=3 i=0", findColumn(6, 3, 0), 9)
    #testColumn("k=6 c=3 i=3", findColumn(6, 3, 3), 138)
    #print str(findColumn(3, 2, 2))
    numberOfTests = int(lines.pop(0))
    for i in range(numberOfTests):
        values = lines.pop(0).split(' ')
        k = int(values[0])
        c = int(values[1])
        s = int(values[2])
        r = solve(k, c, s)
        print "Case #" + str(i + 1) + ": " + r

if __name__ == "__main__":
    main()

