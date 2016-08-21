from sys import argv

# Read args
script, filename = argv
# vars
outPath = 'B-output-large.out'
outFile = open(outPath,'w')

def areAllHappy (pancakes):
    return (not '-' in pancakes)

# Read file line by line into array
with open(filename) as f:
    content = f.readlines()
    numCases = int(content[0])
    for i in range(1, numCases+1):
        caseInput = content[i].replace('\n', '')
        solution = 0
        if not areAllHappy(caseInput):
            if (caseInput[len(caseInput)-1] == '-'):
                solution = solution + 1
            prevChar = caseInput[0]
            for currChar in caseInput:
                if currChar != prevChar:
                    solution = solution + 1
                prevChar = currChar
        solutionStr = 'Case #%d: %s\n' %(i,solution)
        outFile.write(solutionStr)

outFile.close()
f.close()