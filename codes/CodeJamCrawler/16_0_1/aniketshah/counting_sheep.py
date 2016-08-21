def countingSheep(startNumber):
    if startNumber == 0:
        return "INSOMNIA"
    numbersSeen = set([])
    i = 0
    number = 0
    while (len(numbersSeen) < 10):
    
        i = i + 1
        number = startNumber * i
        for d in str(number):
            numbersSeen.add(d)

    return number


readFile = open("A-large.in")
writeFile = open("A-large.out", "a")

numberOfTestCases = -1
caseNumber = 1
for line in readFile.readlines():
    if(numberOfTestCases == -1):
        numberOfTestCases = int(line)
        continue

    writeFile.write("Case #" + str(caseNumber) + ": " + str(countingSheep(int(line))) + "\n")
    caseNumber = caseNumber + 1

readFile.close()
writeFile.close()

