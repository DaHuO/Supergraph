
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

inFile = r'S:\Programming\GCJ2016\D-small-attempt0.in'
outFile = r'S:\Programming\GCJ2016\D-small.out'
tstCase = None
outputFile = open(outFile, 'w')
for i, line in enumerate(open(inFile, 'r')):
    if not tstCase:
        tstCase = int(line)
        continue

    K, C, _ = line.strip().split(" ")
    outputFile.write('Case #%s: %s\n' % (i, getSperTileAndComplexity(int(K), int(C))))
outputFile.close()

