# The small data set has a very simple solution. Just read the first S tiles. It will always be enough information

import re

filename = 'D-small-attempt0'
inFile = open(filename + '.in','r')
outFile = open(filename + '.out','w')

numCases = int(inFile.readline())

for i in range(0,numCases):
    splits = re.split(' ',inFile.readline())
    K = int(splits[0])
    C = int(splits[1])
    S = int(splits[2])

    outFile.write('Case #' + str(i+1) + ':')
    for j in range(0,S):
        outFile.write(' ' + str(j+1))
    outFile.write('\n')
