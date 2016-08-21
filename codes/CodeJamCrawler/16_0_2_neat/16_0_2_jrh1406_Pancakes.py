

def buildStacks():
    inFile = open("cakes.in", 'r')
    outFile = open("cakes.out", 'w')
    caseCount = inFile.readline()
    for case in range(int(caseCount)):
        flipCount = makeStackHappy(list(inFile.readline().rstrip()))
        outFile.write("Case #"+str(case+1)+": " + str(flipCount) + "\n")

    outFile.flush()
    outFile.close()


def makeStackHappy(fullStack):
    flipCount = 0
    while not isHappyStack(fullStack):
        fullStack = flipPoint(fullStack)
        flipCount += 1
    return flipCount


def flipPoint(cakeList):
    for position, cake in reversed(list(enumerate(cakeList))):
        if cake == '-':
            return flip(cakeList[:position+1])+cakeList[position+1:]
    return cakeList


def flip(flipStack):
    for cake in range(len(flipStack)):
        if flipStack[cake] == '-':
            flipStack[cake] = '+'
        elif flipStack[cake] == '+':
            flipStack[cake] = '-'
    return flipStack


def isHappyStack(cakeList):
    sadRank = 0
    while sadRank < len(cakeList):
        if cakeList[sadRank] == '-':
            return False
        sadRank += 1

    return True


if __name__ == "__main__":
    buildStacks()