#!/bin/python2
T=int(raw_input())
for i in xrange(T):
    N=int(raw_input())
    a=range(10)
    if N==0:
        print ("Case #{0}: INSOMNIA".format(i+1))
        continue
    j=0

    while len(a)>0:
        j=j+1
        for k in list(str(N*j)):
            if int(k) in a:
                del a[a.index(int(k))]
    print ("Case #{0}: {1}".format(i+1,N*j))