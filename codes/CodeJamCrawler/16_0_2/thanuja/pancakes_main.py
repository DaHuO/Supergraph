'''
Created on Apr 9, 2016

@author: thanuja
'''

import pancakesHelper

inputFileName = '../inputs/b_pancakes/B-large.in';
outputFileName = '../outputs/b_pancakes/B-large.out'

f = open(inputFileName,'r')
fout = open(outputFileName,'w')

lines = f.readlines()
numTests = int(lines[0])

for i in range(1,numTests+1):
    inputPattern = lines[i]
    numOperations = pancakesHelper.getOperations(inputPattern.strip())
    str1 = 'Case #' + str(i) + ': ' + str(numOperations) + '\n'
    #print str1
    fout.write(str1)
    
f.close()
fout.close()

if __name__ == '__main__':
    pass