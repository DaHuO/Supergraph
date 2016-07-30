from __future__ import print_function
import sys

# print to stderr for debugging
enableDebug = False
# enableDebug = True
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
    lineItems = linesIter.next().split(" ")
    N = int(lineItems[0])
    R = int(lineItems[1])
    P = int(lineItems[2])
    S = int(lineItems[3])


    impossible = [False]



    if(max([abs(R-P), abs(R-S), abs(P-S)]) > 1):
        impossible[0] = True


    result = [""]

    def recurse(nR, nP, nS, level):

        if(level == 0):
            if(nR > 0):
                result[0] += "R"
            if(nP > 0):
                result[0] += "P"
            if(nS > 0):
                result[0] += "S"
            return

        level -= 1
        
        count = 2**level / 3
        target = 2**level
        leftP = count
        leftR = count
        leftS = count
        rightP = count
        rightR = count
        rightS = count
        nR -= 2*count
        nP -= 2*count
        nS -= 2*count
        leftCount = 3*count
        rightCount = 3*count
        if nP > 0:
            leftP += 1
            nP -= 1
            leftCount += 1
        if nR > 0 and leftCount < target and nS < 2:
            leftR += 1
            nR -= 1
            leftCount += 1
        if nS > 0 and leftCount < target:
            leftS += 1
            nS -= 1
            leftCount += 1
        if nP > 0:
            rightP += 1
            nP -= 1
        if nR > 0:
            rightR += 1
            nR -= 1
        if nS > 0:
            rightS += 1
            nS -= 1

        if(nR < 0 or nP < 0 or nS < 0 or (leftP + leftR + leftS != 2**level) or (rightP + rightR + rightS != 2**level)):
            impossible[0] = True
            printe(":(")
            printe("level = " + str(level))
            printe("nR = " + str(nR))
            printe("nP = " + str(nP))
            printe("nS = " + str(nS))
            printe("leftP = " + str(leftP) + "   leftR = " + str(leftR) + "    leftS = " + str(leftS))
            printe("rightP = " + str(rightP) + "   rightR = " + str(rightR) + "    rightS = " + str(rightS))
            return

        recurse(leftR, leftP, leftS, level)
        recurse(rightR, rightP, rightS, level)

    recurse(R, P, S, N)

    if impossible[0]:
        print("Case #{}: {}".format(iCase, "IMPOSSIBLE"))
    else:
        print("Case #{}: {}".format(iCase, result[0]))
