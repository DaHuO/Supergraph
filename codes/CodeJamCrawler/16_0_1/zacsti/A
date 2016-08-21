import csv
import math

IN = open('A.in','r')
OUT = open('A.txt','w')

T = int(IN.readline())
print T
for case in range(T):
    N = IN.readline()
    n = int(N)
    NK = ""
    if (n!=0):
        nk = n
        NK = N
        digs = [0,]*10
        tot = 0
        for i in range(len(N)-1):
            d = int(N[i])
            if (digs[d]==0):
                digs[d]=1
                tot+=1
        while (tot < 10):
            nk += n
            NK = str(nk)
            for i in range(len(NK)):
                d = int(NK[i])
                if (digs[d]==0):
                    digs[d]=1
                    tot+=1
    else:
        NK = "INSOMNIA"
    OUT.write("Case #" + str(case+1) + ": " + NK)
    print "Case #" + str(case+1) + ": " + NK
