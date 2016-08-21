import numpy as np
import random as rx
import math

f = open('test', 'r')
numcases = int(f.readline().rstrip('\n'))

for q in range(1,numcases+1):
    #x = int(f.readline().rstrip('\n'))
    y = f.readline().rstrip('\n')
    y = y.split()

    N = int(y[0])
    On = int(y[1])

    y = f.readline().rstrip('\n')
    y = y.split()

    p = np.empty([N])

    for i in range(0,N):
        p[i] = float(y[i])

    best  = 0
    for XFACTOR in range(0,On+1):

        seen = np.zeros([N+1])

        numcorrect = np.zeros([N])
        numcorrect[0] = 1

        #choose highest
        for i in range(0,XFACTOR):
            highest = -1.0
            for j in range(0,N):
                if p[j] > highest and seen[j] == 0:
                    highest = p[j]
                    highestname = j
            #now mark as seen
            seen[highestname] =1
            for j in range(N-1,0,-1):
                numcorrect[j] = numcorrect[j-1]*highest+numcorrect[j]*(1-highest)
            numcorrect[0] = numcorrect[0]*(1-highest)

        for i in range(0,On-XFACTOR):
            highest = 1.1
            for j in range(0,N):
                if p[j] < highest and seen[j] == 0:
                    highest = p[j]
                    highestname = j
            #now mark as seen
            seen[highestname] =1
            for j in range(N-1,0,-1):
                numcorrect[j] = numcorrect[j-1]*highest+numcorrect[j]*(1-highest)
            numcorrect[0] = numcorrect[0]*(1-highest)

        if numcorrect[On/2] > best:
            best = numcorrect[On/2]

    print "Case #" + str(q) +": " + str(best)


