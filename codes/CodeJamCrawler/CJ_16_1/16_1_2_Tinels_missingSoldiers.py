def getMissingPrivates(alignList):
    inputList = sorted(alignList)
    firstRow, scndRow, thrdRow = [], [], []
    occDict = {}
    missingAlign = []
    for input in inputList:
        for soldier in input:
            if soldier not in occDict:
                occDict[soldier] = 1
            else:
                occDict[soldier] += 1
    for key, val in occDict.iteritems():
        if (val % 2) != 0:
            missingAlign.append(key)
    missingAlign = sorted(missingAlign)
    return [str(x) for x in missingAlign]

soldierList = []
inFile = r'S:\Programming\GCJ2016\B-large.in'
outFile = r'S:\Programming\GCJ2016\B-large.out'
tstCase = None
sizeGrid = 0
tstCase = 0
firstLine = True
outputFile = open(outFile, 'w')
N = None
fct = getMissingPrivates
for line in open(inFile, 'r'):
    if firstLine:
        firstLine = False
        continue
    if sizeGrid == 0:
        N = int(line)
        tstCase += 1
        sizeGrid = 2*(N) -1
        continue
    rowToAppend = [ int(x) for x in line.strip().split(" ")]
    soldierList.append(rowToAppend)
    sizeGrid -= 1

    if sizeGrid == 0:
        print " ".join(getMissingPrivates(soldierList))
        outputFile.write('Case #%s: %s\n' % (tstCase, " ".join(getMissingPrivates(soldierList))))
        soldierList = []
outputFile.close()