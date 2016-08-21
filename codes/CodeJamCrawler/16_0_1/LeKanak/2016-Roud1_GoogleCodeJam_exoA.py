""" Google Code Jam 2016 - Part A

"""

def getLastSleepNumber(start):
    """ Return the last number before spleeping """
    if start == 0:
        return 'INSOMNIA'
    cnt, digitLst = 1, {}
    while True:
        currentVal = str(cnt * start)
        for dig in currentVal:
            digitLst[int(dig)] = 1
        if len(digitLst) == 10 and sum(digitLst) == 45:
            break
        cnt += 1
        
    return currentVal

"""
Part to be executed with the given input files

"""

path = r'C:\Users\HOME\Desktop\GoogleCodeJam'
fileName = 'A-small-attempt0.in'
inputPath = r'%s\%s' % (path, fileName)
outputPath = r'%s\%s' % (path, fileName.replace('.in', '_out.dat'))

caseNb = None
outputFile = open(outputPath, 'w')
for i, line in enumerate(open(inputPath, 'r')):
    if not caseNb:
        caseNb = int(line)
        continue

    outputFile.write('Case #%s: %s\n' % (i, getLastSleepNumber(int(line.strip()))))
outputFile.close()