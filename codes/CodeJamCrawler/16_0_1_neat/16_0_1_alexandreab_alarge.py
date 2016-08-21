#!/usr/bin/env python

q = input('')

for i in range(1,q+1):
    d = set()
    v = input('')
    t=0
    rep=0
    j = 1
    while True:
        n = v*j
        d = d.union(map(int,str(n)))
        if t==len(d):
            rep+=1
        else:
            rep=0
        t = len(d)
        if t==10:
            print("Case #{}: {}".format(i,n))
            break

        if rep>100000:
            break
        j+=1

    if len(d)<10:
        print("Case #{}: {}".format(i,"INSOMNIA"))

