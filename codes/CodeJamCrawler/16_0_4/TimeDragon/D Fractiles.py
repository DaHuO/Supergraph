#!python3


def getPos(k, c, s, it):

    maxPower = min(k - 1, c - 1)
    inter = maxPower + 1

    startBound = it * inter
    endBound = min(k, startBound + inter)

    outerBound = k ** maxPower

    res = outerBound * startBound
    curBound = startBound + 1
    while curBound < endBound:
        outerBound //= k
        res += (outerBound * (curBound - startBound))
        curBound += 1

    return res

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

testCases = int(inputFile.readline())

for i in range(0, testCases):

    inStr = inputFile.readline()
    inStr = inStr.split(' ')

    kLen = int(inStr[0])
    cIter = int(inStr[1])
    sTry = int(inStr[2])

    minS = ((kLen - 1) // cIter) + 1

    if minS > sTry:
        print("Case #", i + 1, ": IMPOSSIBLE", sep="", file=outputFile)
        continue

    print("Case #", i + 1, ": ", sep="", end="", file=outputFile)

    totalLen = kLen ** cIter
    perBlockLen = kLen ** (cIter - 1)
    innerBlock = perBlockLen // kLen
    if kLen == 1:
        print(1, file=outputFile)
        continue
    for j in range(0, sTry):
        res = j * perBlockLen
        res += (j * innerBlock)
        print(res + 1, end=" ", file=outputFile)

    print("", file=outputFile)
