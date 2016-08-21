def solve(val):
    n = list(val.strip())
    n.reverse()
    count = 0
    for i in range(0, len(n)):
        if n[i] == '-':
            count += 1
            for x in range(i, len(n)):
                if n[x] == '-':
                    n[x] = '+'
                else:
                    n[x] = '-'
    return count

     
fileName = str(input("File? "))

inputFile = open(fileName)
outputFile = open("B", "w")
caseCount = 1
firstLine = True
for i in inputFile.readlines():
    if (firstLine):
        firstLine = False
        continue
    outputFile.write("Case #" + str(caseCount) + ": " + str(solve(i)) + "\n")
    caseCount += 1
inputFile.close()
outputFile.close()
