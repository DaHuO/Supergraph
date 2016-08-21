#!/usr/bin/python

import numpy as np


def sleepSheep(x): 
    if int(x) == 0: 
        return 'INSOMNIA'
    seenDigits=[False]*10
    y=0
    while not np.all(seenDigits): 
        y=y+x
        digits=set(map(int,str(y)))
        for d in digits: 
            seenDigits[d] = True
    return str(y)


inFile=open('sheepInput.txt', 'r')
outFile=open('sheepOutput.txt', 'w')

nrLines = int(inFile.readline())
caseCounter=0

for i, line in enumerate(inFile):
    x=int(line)
    lastNr=sleepSheep(x)
    outFile.write("Case #"+str(i+1)+": "+lastNr+"\n")
inFile.close()
outFile.close()

        
    
    
