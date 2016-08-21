NUM_OF_ATTEMPTS = 1000
DIGITS_REQUIRED = 10

def getDigits(num):
    return list(map(int,str(num)))

def solveCase(num):
    digits = set()
    newNum = num
    found = False
    for i in range(NUM_OF_ATTEMPTS):
        cDigits = getDigits(newNum)
        for d in cDigits:
            digits.add(d)
        if len(digits) == DIGITS_REQUIRED:
            print("Num %d with %d steps, final is %d" % (num, i, newNum))
            found = True
            break


        newNum += num

    return str(newNum) if found else "INSOMNIA"
    #if not found:
    #    print("### Num %d with %d steps, ### CAN'T FIND ###" % (num, i))





def parseInput(text):
    cases = []
    for i, line in enumerate(text.splitlines()):
        if i == 0:
            continue
        line = line.strip()
        num = int(line)
        cases.append(num)
    return cases


def getCases(filename):
    with open(filename) as h:
        data = h.read()
    return parseInput(data)


def getOutput(solved):
    lines = []
    for i, solvedCase in enumerate(solved):
        lines.append("Case #%d: %s" % (i + 1, solvedCase))
    return '\n'.join(lines)

def generateOutput(filename, outFile = None):
    cases = getCases(filename)
    solvedCases = [solveCase(case) for case in cases]
    output = getOutput(solvedCases)
    if outFile == None:
        outFile = filename[:-2] + "out"
    with open(outFile, "w") as h:
        h.write(output)
    
