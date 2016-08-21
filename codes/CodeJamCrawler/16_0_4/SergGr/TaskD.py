import itertools
import time
import operator
# import collections
from collections import Counter

inputFileName = "test.in"
# inputFileName = "D-small-attempt0.in"
inputFileName = "D-small-attempt1.in"
# inputFileName = "D-small-attempt2.in"
# inputFileName = "D-small-attempt3.in"
# inputFileName = "D-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime


def calcSingleTest(f):
    line = f.readline()
    K = int(line.split()[0])
    C = int(line.split()[1])
    S = int(line.split()[2])
    if C == 1:
        if S < K:
            return 'IMPOSSIBLE'
        else:
            return ' '.join(map(str, xrange(1, K + 1)))

    base = K ** (C - 1)
    r = int((K + 1) / 2)
    if S < r:
        return 'IMPOSSIBLE'
    else:
        res = []
        for i in xrange(0, r):
            j = K - i
            res.append(i * base + j)
        return ' '.join(map(str, res))


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            r1 = calcSingleTest(inpF)
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            print ' '
            outF.write('Case #{0}: {1}\n'.format(i, r1))
            outF.flush()

print "Finished!!!! Total time = {0}".format((time.time() - startTime))
