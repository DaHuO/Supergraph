#!/usr/bin/python
import sys
file = sys.argv[1]

def comp(_N, i):
    N=_N
    prefix = "Case #"+str(i+1)+":"
    if N==0:
        print prefix,'INSOMNIA'
        return

    a = {x : False for x in range(10)}

    for i in str(N):
        a[int(i)] = True

    while all(a.values()) == False:
        for i in str(N):
            a[int(i)]=True
        #print N, a
        N += _N
    print prefix, N-_N

with open(file) as f:
    N = int(f.readline())
    for i in range(N):
        num = int(f.readline())
        comp(num,i)
        # N=333
