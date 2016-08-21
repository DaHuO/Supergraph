""" Google Code Jam 2016 - Part D
"""

def getSperTileAndComplexity(K, C):
    """
    """
    if K == 1:
        return '1'
    data = []
    for i in xrange(K):
        data.append(str(1 + (i * (pow(K, C) - 1) / (K - 1))))
    return " ".join(data)

"""
Part to be executed with the given input files

"""

path = r'C:\Users\HOME\Desktop\GoogleCodeJam'
fileName = 'D-small-attempt0.in'
inputPath = r'%s\%s' % (path, fileName)
outputPath = r'%s\%s' % (path, fileName.replace('.in', '_out.dat'))

caseNb = None
outputFile = open(outputPath, 'w')
for i, line in enumerate(open(inputPath, 'r')):
    if not caseNb:
        caseNb = int(line)
        continue

    K, C, _ = line.strip().split(" ")
    outputFile.write('Case #%s: %s\n' % (i, getSperTileAndComplexity(int(K), int(C))))
outputFile.close()