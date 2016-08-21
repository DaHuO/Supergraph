#
# Google CodeJam 2016
# Code by Nick Pawlowski
# pawlowski.nick@gmail.com
#
# Counting Sheep
#

import sys

numTests = int(sys.stdin.readline().strip())

for i in range(numTests):
    digitsSeen = [0 for _ in range(10)]
    currentNum = int(sys.stdin.readline().strip())
    if currentNum == 0:
        print 'Case #%d: INSOMNIA' % (i+1)
    else:
        newNum = 0
        while sum(digitsSeen) < 10:
            newNum += currentNum
            for digit in str(newNum):
                digitsSeen[int(digit)] = 1
        print 'Case #%d: %d' % (i + 1, newNum)
