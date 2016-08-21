



def setinput():
    inFile = open("sheep.in", 'r')
    outFile = open("sheep.out", 'w')
    caseCount = inFile.readline()
    for case in range(int(caseCount)):
        startNum = int(inFile.readline())
        response = ""
        if startNum is not 0:
            response = str(sheepInc(startNum))
        else:
            response = "INSOMNIA"
        outFile.write("Case #" + str(case+1) + ": " + response + "\n")

    outFile.flush()
    outFile.close()


def sheepInc(num):
    numList = []
    incrementer = 1
    while 1<2:
        newNum = num*incrementer
        if not integerComp(newNum, numList):
            incrementer += 1
        else:
            return newNum


def integerComp(num, numList):
    productList = [int(x) for x in str(num)]
    numList += productList
    numList = list(set(numList))
    if len(numList) < 10:
        return False
    else:
        return True


if __name__ == "__main__":
    setinput()