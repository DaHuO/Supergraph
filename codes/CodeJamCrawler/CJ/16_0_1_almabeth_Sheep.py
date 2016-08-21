import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


testfile='A-large.in'
outputfile='A-large.out'

fo = open(testfile, "rw+")
print "Name of the file: ", fo.name
firstline = fo.readline()
fo.close()
numcases=int(firstline.split('\n')[0])
print 'numcases: ',numcases
inpt=np.genfromtxt(testfile, skiprows=1, dtype=int)
maxN=200
def checknum(case):
    out=np.zeros(10)
    testint=case*np.arange(1,maxN)
    maxdigits=len(str(np.max(testint)))
    bigarray=np.ones([maxdigits,len(testint)])*np.nan
    for i in np.arange(maxdigits):
        div=testint*10**(-i)
        bigarray[i,:]=np.mod(np.floor(div),10)-1000*(div<1)
    foundarg=np.arange(0,10)*0
    for number in np.arange(0,10): 
        foundnum=(bigarray==number)
        if not np.any(foundnum):
            return 'Insomnia'
        else:
            foundarg[number]=int(np.argwhere(np.any(foundnum,axis=0)==True).min())    
    return testint[max(foundarg)]

outfile=open(outputfile, 'w')
for m,case in enumerate(inpt): 
    print '********'+str(case)+'********'
    answer=checknum(case)
    print answer
    outfile.write('Case #'+str(m+1)+': '+str(answer)+'\n')
    
outfile.close()

b=2
