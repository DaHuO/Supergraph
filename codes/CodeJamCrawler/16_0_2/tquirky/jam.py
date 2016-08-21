#CODEJAM BABY

outputStr = ""
problemFile = "B-large.in"

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

def flip(cake):
    if cake == "-":
        return "+"
    else:
        return "-"

def findI(case, movecount, caseCount):
    if "-" in case:
        nextDown = case.index("-")
        for i in range(len(case) - nextDown):
            i += nextDown
            case[i] = flip(case[i])
        findI(case, movecount + 1, caseCount)
    else:
        caseStr = "Case #%d: %s" % (caseCount, movecount)
        print(caseStr)
        return caseStr

caseCount = 1
for case in data:
    if len(case) > 0:
        case = case[::-1]
        stack = list(case)
        findI(stack, 0, caseCount)
        caseCount += 1