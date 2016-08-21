
def readTestCaseFile(fileName):
    cases = []
    with open(fileName, 'r') as fp:
        for line in fp:
            number = line.split('\n')
            number = int(number[0])
            cases.append(number)
    return  cases
def convertNumIntoDigits(N):
    number = str(N)
    digits = []
    for ch in number:
        digits.append(int(ch))
    return digits
def solveSheepCase(N):
    ret = "INSOMNIA"
    numbersDict = dict()

    if N == 0:
        return ret

    base = 1
    numberSeen = 0
    lastSeen = 0
    index = 0
    while 1:
        newNum = N*base
        base = base + 1
        lastSeen = newNum
        digits = convertNumIntoDigits(newNum)
        for digit in digits:
            try:
                seen = numbersDict[digit]
                seen = seen + 1
                numbersDict[digit] = seen
            except KeyError as e:
                numbersDict[digit] = 1
                numberSeen = numberSeen + 1
            if numberSeen == 10:
                break
        if numberSeen == 10:
            break

    return lastSeen
def writeOutput(destDirectory,results):

    fileName = destDirectory+"results.txt"
    filehandle = open(fileName,'w')
    index = 1
    for res in results:
        filehandle.write("Case")
        filehandle.write("\t")
        filehandle.write("#"+str(index)+":")
        filehandle.write("\t")
        filehandle.write(str(res))
        filehandle.write("\n")
        index = index + 1

    return
def solveCountingSheep(cases,destDirectory):
    if len(cases)> 0 :
        N = cases[0]
        del cases[0]
        results = []
        for i in range(N):
            ret = solveSheepCase(cases[i])
            results.append(ret)
        writeOutput(destDirectory,results)

    return
fileName = "C:/Users/Yassien/Desktop/A-large.in"
cases = readTestCaseFile(fileName)
destDirectory = "C:/Users/Yassien/Desktop/"
solveCountingSheep(cases,destDirectory)