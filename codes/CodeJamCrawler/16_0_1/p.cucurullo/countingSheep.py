from sys import argv

# Read args
script, filename = argv
# vars
outPath = 'output.out'
outFile = open(outPath,'w')


def hasAllDigits (N):
    hasAllDigitsSol = True
    i = 0
    while (i < 10):
        if not str(i) in N:
            hasAllDigitsSol = False
        i = i + 1
    return hasAllDigitsSol

# Read file line by line into array
with open(filename) as f:
    content = f.readlines()
    numCases = int(content[0])
    for i in range(1, numCases+1):
        caseInput = int(content[i])
        solution = 'INSOMNIA'
        if (caseInput != 0):
            j = 1
            concatenatedMultiples = str(caseInput)
            while (not hasAllDigits(concatenatedMultiples)):
                solution = caseInput * j
                concatenatedMultiples = concatenatedMultiples + str(solution)
                j = j + 1
        solutionStr = 'Case #%d: %s\n' %(i,solution)
        outFile.write(solutionStr)

outFile.close()