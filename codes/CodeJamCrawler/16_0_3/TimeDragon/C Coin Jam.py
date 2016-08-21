#!python3

primeList = []


def primify(maxNum):
    global primeList
    maxNum += 1
    numList = [True] * maxNum

    for i in range(2, (maxNum + 1) // 2):
        if numList[i]:
            nextNum = i * i

            while nextNum < maxNum:
                numList[nextNum] = False
                nextNum += i

    for i in range(2, maxNum):
        if numList[i]:
            primeList += [i]


def stringify(num):
    ans = ""
    while num:
        ans += str(num % 2)
        num //= 2
    return ans


def primeDiv(numStr, div):
    num = 0
    for i in range(0, len(numStr)):
        if numStr[i] == '1':
            num += (div ** i)

    if num <= 3:
        return 1
    for i in range(0, len(primeList)):
        if ((num + 1) // 2) < primeList[i]:
            break
        if (num % primeList[i]) == 0:
            return primeList[i]

    return 1

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

testCases = int(inputFile.readline())

primify(1000000)

result = []

for i in range(0, testCases):
    result = []
    inStr = inputFile.readline()
    inStr = inStr.split(' ')

    length = int(inStr[0])
    total = int(inStr[1])

    startNumber = 2 ** (length - 1)
    if length != 1:
        startNumber += 1

    endNumber = 2 ** length

    for j in range(startNumber, endNumber, 2):
        if len(result) == total:
            break

        strNum = stringify(j)
        correctStr = strNum[::-1]

        curAns = [correctStr]

        for k in range(2, 11):
            retAns = primeDiv(strNum, k)

            if retAns == 1:
                break

            curAns += [retAns]

        if len(curAns) == 10:
            result.append(curAns)

    print("Case #", i + 1, ":", sep="", file=outputFile)

    for l in range(0, len(result)):
        for m in range(0, 10):
            print(result[l][m], end=' ', file=outputFile)

        print('', file=outputFile)
