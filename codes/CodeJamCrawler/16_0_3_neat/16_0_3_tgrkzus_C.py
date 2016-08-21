import math

def checkPrimeBase2to10(e):
    prime = True
    tempSet = [0 for x in range(10)]
    k = '1' + ''.join(str(b) for b in e) + '1'
    tempSet[0] = k
    for l in range(2, 11):
        m = int(k, base=l)
        if m % 2 == 0:
                tempSet[l - 1] = 2;
                prime = False
        for y in range(3, math.floor(math.sqrt(m)), 2):
            if m % y == 0:
                tempSet[l - 1] = y;
                prime = False
    if prime == False and 0 not in tempSet:
        return tempSet

def solve(n, j):
    finalResults = []
    maximum = '1' * (n - 2)
    for e in range(0, int(maximum, base=2)):
        binConvert = format(e, '0' + str((n - 2)) + 'b')
        tempSet = checkPrimeBase2to10(binConvert)
        if tempSet != None:
            finalResults.append(tempSet)
            print(finalResults)
        if (len(finalResults) == j):
            return finalResults

    
fileName = str(input("File? "))

inputFile = open(fileName)
outputFile = open("C", "w")
caseCount = 1
firstLine = True
for i in inputFile.readlines():
    if (firstLine):
        firstLine = False
        continue
    data = []
    for e in solve(int(i.split()[0]), int(i.split()[1])):
        data.append(' '.join(map(str, e)))
    outputFile.write("Case #" + str(caseCount) + ": " + '\n'.join(data))
    caseCount += 1
inputFile.close()
outputFile.close()

