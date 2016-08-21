#CODEJAM BABY

outputStr = ""
problemFile = "A-large.in"

def readF(fname):
    file = open(fname)
    file = file.read().split('\n')
    return file

def writeF(text):
    print(text)
    f = open('file.txt', 'w')
    f.write(text)

data = readF(problemFile)

testCases = int(data[0])

data.pop(0)

def findNum(initCase):
    numbers = []
    N = 1
    while True:
        case = int(initCase) * N
        if case <= int(initCase) and N > 1:
            return "INSOMNIA"

        digits = list(str(case))

        for digit in digits:
            if digit not in numbers:
                numbers.append(digit)
                numbers.sort()

        if "".join(numbers) == "0123456789":
            return case

        N += 1

caseCount = 1
for case in data:
    if len(case) > 0:
        finalCase = findNum(case)

        caseStr = "Case #%d: %s\n" % (caseCount, finalCase)
        outputStr += caseStr
        caseCount += 1

writeF(outputStr)