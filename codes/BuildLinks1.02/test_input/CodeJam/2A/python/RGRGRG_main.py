import numpy as np
import random as rx
import math

f = open('test', 'r')
numcases = int(f.readline().rstrip('\n'))

for i in range(1,numcases+1):
    #x = int(f.readline().rstrip('\n'))
    y = f.readline().rstrip('\n')
    y = y.split()

    N = int(y[0])

    R = np.empty([20])
    P = np.empty([20])
    S = np.empty([20])

    R[0] = int(y[1])
    P[0] = int(y[2])
    S[0] = int(y[3])

    Rname = np.chararray([20], itemsize=10000)
    Pname =  np.chararray([20], itemsize=10000)
    Sname =  np.chararray([20], itemsize=10000)

    Rname[0] = "R"
    Pname[0] = "P"
    Sname[0] = "S"

    for j in range(0,N):
        P[j+1] = (R[j]+P[j]-S[j])/2
        R[j+1] = (R[j]-P[j]+S[j])/2
        S[j+1] = (-R[j]+P[j]+S[j])/2

        if P[j+1] < 0 or R[j+1] < 0 or S[j+1] < 0:
            print "Case #" + str(i) +": " + "IMPOSSIBLE"
            break

        if Rname[j] < Sname[j]:
            Rname[j+1] = Rname[j] + Sname[j]
        else:
            Rname[j+1] = Sname[j] + Rname[j]

        if Pname[j] < Sname[j]:
            Sname[j+1] = Pname[j] + Sname[j]
        else:
            Sname[j+1] = Sname[j] + Pname[j]

        if Pname[j] < Rname[j]:
            Pname[j+1] = Pname[j] + Rname[j]
        else:
            Pname[j+1] = Rname[j] + Pname[j]

        if (j+1) == N:
            if P[j+1]:
                print "Case #" + str(i) +": " +  Pname[j+1]
            elif S[j+1]:
                print "Case #" + str(i) +": " +  Sname[j+1]
            else:
                print "Case #" + str(i) +": " +  Rname[j+1]




    #print "Case #" + str(i) +": " + str(duos)

    #if x[len(x)-1] == '-':
        #count = count+1


