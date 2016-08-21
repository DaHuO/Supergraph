#!python3


def mulTime(num):
    ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1, 100):
        curNum = num * i
        while curNum:
            curDig = curNum % 10
            curNum //= 10
            try:
                ls.remove(curDig)
            except:
                pass
            if len(ls) == 0:
                break
        if len(ls) == 0:
            return i
    return 0

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

testCases = int(inputFile.readline())

for i in range(0, testCases):
    startValue = int(inputFile.readline())
    endValue = mulTime(startValue) * startValue

    if endValue == 0:
        print("Case #", i + 1, ": INSOMNIA", sep="", file=outputFile)
    else:

        print("Case #", i + 1, ": ", endValue, sep="", file=outputFile)
