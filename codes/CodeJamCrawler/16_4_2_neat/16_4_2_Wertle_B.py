from __future__ import print_function
import sys
import numpy as np

# print to stderr for debugging
enableDebug = True
# enableDebug = False
def printe(*stuff):
    if enableDebug:
        print(*stuff, file=sys.stderr) 


# Open file for processing
filename = sys.argv[1]
inputFile = open(filename, 'r')
lines = [l.rstrip('\n') for l in inputFile]
linesIter = iter(lines)
nCases = int(linesIter.next())


# Process each case
for iCase in range(1,nCases+1):
    printe("\nProcessing case " + str(iCase))

    # Solve problem
    lineVals = next(linesIter).split(" ")
    N = int(lineVals[0])
    T = int(lineVals[1])
    lineVals = next(linesIter).split(" ")
    vals = ([float(x) for x in lineVals])
    vals.sort()
    
    interleavedVals = []
    for i in range(N/2):
        interleavedVals.append(vals[i])
        interleavedVals.append(vals[N-i-1])
    if(N % 2 == 1):
        interleavedVals.append(vals[N/2])
    interleavedVals = np.array(interleavedVals)

    # printe("interleavedVals = " + str(interleavedVals))


    bestScore = [0.0]
    initProbs = np.zeros(T+1)
    initProbs[0] = 1.0

    def bt(currProbs, nLeft, iChoose):

        # printe("Recursing with nLeft = " + str(nLeft) + " iChoose = " + str(iChoose))
        # printe("Currprobs = " + str(currProbs))

        # base case
        if(nLeft > N - iChoose):
            # printe("...quitting")
            return
        if(nLeft == 0):
            bestScore[0] = max((bestScore[0], currProbs[T/2]))
            # printe("... hit base, score = " + str(currProbs[T/2]))



        # prune
        # if(nLeft % 2 == 0 and currProbs[(T-nLeft)/2] < 0.05 * bestScore[0]):
            # return



        # recurse
        bt(currProbs.copy(), nLeft, iChoose+1)

        if(nLeft > 0):
            currProbsOld = currProbs.copy()
            currProbs *= (1.0 - interleavedVals[iChoose])
            currProbs[1:] += interleavedVals[iChoose] * currProbsOld[:T]
            bt(currProbs, nLeft-1, iChoose+1)

    bt(initProbs, T, 0)

    print("Case #{}: {}".format(iCase, bestScore[0]))
