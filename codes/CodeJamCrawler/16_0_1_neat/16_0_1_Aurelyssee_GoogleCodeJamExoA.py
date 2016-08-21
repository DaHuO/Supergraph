def getNumber(start):
    if start == 0:
        return 'INSOMNIA'

    i, digitLst = 1, {}
    while True:
        currentVal = str(i * start)
        for dig in currentVal:
            digitLst[int(dig)] = 1
        if len(digitLst) == 10 and sum(digitLst) == 45:
            break

        i += 1
        
    return currentVal

path = r'C:\Users\HOME\Downloads\CodeJam'
fileName = 'A-small-attempt0.in'
inputPath = r'%s\in\%s' % (path, fileName)
outputPath = r'%s\out\%s' % (path, fileName.replace('.in', '.out'))

outputFile = open(outputPath, 'w')
inFile = open(inputPath, 'r')
inFile.next()
for i, line in enumerate(inFile):
    outputFile.write('Case #%s: %s\n' % (i+1, getNumber(int(line.strip()))))
outputFile.close()