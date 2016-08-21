# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 08:52:10 2016

@author: Admin
"""



def lastNumberBeforeAsleep(N,tcNumber,fileOut):
    digitsSet = set()
    CUTOFFCOUNTER = 1000000000000000
    numbersSet = set(['0','1','2','3','4','5','6','7','8','9'])
    iter = 1
    resultNumber = None
    if N:
        while True:
            tempN = iter * N
            if tempN>CUTOFFCOUNTER:
                break
            tempNumbersStr = str(tempN)
            for digit in tempNumbersStr:
                digitsSet.add(digit)
            iter+=1
            if not numbersSet.difference(digitsSet):
                resultNumber = tempN
                break
    if resultNumber:
        fileOut.write('Case #{}: {}\n'.format(tcNumber,int(resultNumber)))
    else:
        fileOut.write('Case #{}: {}\n'.format(tcNumber,'INSOMNIA'))
    
    

def main():
    fileOut = open(r'D:\SpyderWorkspace\CodeJam\CodeJam16Results\A-large.out','w')
    fileIn = open(r'D:\SpyderWorkspace\CodeJam\CodeJam16Results\A-large.in','r')
    noOfTcs = int(fileIn.readline())    
    for tc in range(1,noOfTcs+1):
        N = int(fileIn.readline())
        lastNumberBeforeAsleep(N,tc,fileOut)
    
    fileOut.flush()
    fileOut.close()

main()