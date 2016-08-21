def flipPancakes(arr, numToFlip):
    if (numToFlip == 0): return

    flippedArr = []
    for i in range(numToFlip):
        if (arr[i] == "+"): flippedArr.append("-")
        else: flippedArr.append("+")

    for j in range(len(flippedArr)):
        arr[j] = flippedArr[len(flippedArr)-j-1]

def getNumContSym(arr, symbol, offset=0):
    nc = 0
    # print "InitVal:", offset
    for i in range(offset, len(arr)):
        if (arr[i] != symbol): break
        nc += 1
    return nc

def getNumFixedPancakes(arr):
    fc = 0
    for i in range(len(arr)):
        # Loop through array backwards
        if (arr[len(arr)-i-1] == "-"): break
        fc += 1
    return fc

def solvePancakeProb(stackStr):
    # print "-----------START-----------"
    stackArr = list(stackStr)
    flipCount = 0
    arrSize = len(stackArr)
    fixedCount = getNumFixedPancakes(stackArr)
    # print "Init fixed cnt:", fixedCount

    while (fixedCount < arrSize):
        numContPlus = getNumContSym(stackArr, "+")
        # print "Num cont plus:", numContPlus

        # break out of the loop if all pancakes are "+"
        if (numContPlus == arrSize): break

        # flip first numContPlus pancakes from the top
        flipPancakes(stackArr, numContPlus)
        if (numContPlus > 0):
            flipCount += 1
            # print stackArr

        # Should have at least numContPlus "-" at the top now
        numContMinus = numContPlus
        # Get the rest of the "-" (offset of numContPlus passed in)
        numContMinus += getNumContSym(stackArr, "-", numContPlus);
        # print "Num cont minus:", numContMinus

        # Flip all pancakes that have not been fixed yet
        flipPancakes(stackArr, arrSize-fixedCount)
        flipCount += 1
        # print stackArr

        # Increment fixedCount (b/c numContMinus pancakes have been fixed)
        fixedCount += numContMinus
        # print "Fixed count:", fixedCount

    # print stackArr, "Flip count:", flipCount
    # print "-----------END-----------\n"
    return flipCount

t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input()
    print "Case #{}:".format(i), solvePancakeProb(n)