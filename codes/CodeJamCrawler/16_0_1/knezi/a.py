#!/bin/env python3
t=int(input())

for x in range(1,t+1):
    i=int(input())
    if i==0:
        print("Case #%d: INSOMNIA" % x)
    else:
        used=[False for x in range(10)]
        no=10
        it=1
        while no>0:
            tmp=str(i*it)
            for z in tmp:
                if not used[int(z)]:
                    used[int(z)]=True
                    no-=1

            it+=1


        print("Case #%d: %d" % (x,(it-1)*i))
