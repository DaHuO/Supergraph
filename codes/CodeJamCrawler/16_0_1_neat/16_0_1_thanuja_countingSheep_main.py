'''
Created on Apr 9, 2016

@author: thanuja
'''

import countingSheepHelper

# read Input
inputFileName = '../inputs/a_countingSheep/A-large.in';

outputFileName = '../outputs/a_countingSheep/largeOutput.txt'

f = open(inputFileName,'r')
fout = open(outputFileName,'w')


lines = f.readlines()
numTests = int(lines[0])

for i in range(1,numTests+1):
    N = int(lines[i])
    out = countingSheepHelper.countSheep(N)
    str1 = 'Case #' + str(i) + ': ' + out + '\n'
    fout.write(str1)
    
f.close()
fout.close()
if __name__ == '__main__':
    pass