def flipThosePancakes(pancakes):
    flipCount = 0
    for i in range(len(pancakes) - 1):
        if pancakes[i] != pancakes[i+1]:
            flipCount += 1
    if (pancakes[0] == '-' and flipCount % 2 == 0) or (pancakes[0] == '+' and flipCount % 2 == 1):
        flipCount += 1
    return flipCount




inFile = r'S:\Programming\GCJ2016\B-large.in'
outFile = r'S:\Programming\GCJ2016\B-large.out'
tstCase = None
outputFile = open(outFile, 'w')
fct = flipThosePancakes
for i, line in enumerate(open(inFile, 'r')):
    if not tstCase:
        tstCase = int(line)
        continue
    outputFile.write('Case #%s: %s\n' % (i, fct(line.strip())))
outputFile.close()