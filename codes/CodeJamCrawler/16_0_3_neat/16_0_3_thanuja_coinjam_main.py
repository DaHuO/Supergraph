'''
Created on Apr 9, 2016

@author: thanuja
'''

import coinjam

inputFileName = '../inputs/c_coinjam/C-small-attempt2.in';
outputFileName = '../outputs/c_coinjam/C-small.out'

f = open(inputFileName,'r')
fout = open(outputFileName,'w')

lines = f.readlines()
numTests = int(lines[0])

for i in range(numTests):
    splitLine = lines[i+1].split(' ')
    N = int(splitLine[0])
    J = int(splitLine[1])
    #N = 4
    #J = 2
    jamCoinDict = coinjam.getJamCoins(N, J)
    print jamCoinDict
    coinjam.writeDictToFile(fout,jamCoinDict,i)

if __name__ == '__main__':
    pass


