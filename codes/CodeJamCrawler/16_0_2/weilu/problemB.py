#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import os
import sys

#print(sys.argv)

f = open(sys.argv[1])
lines = f.readlines()
T = int(lines[0].rstrip('\n'))

for i in range(1,T+1):
    cakes = lines[i].rstrip('\n')
    pos = 0
    need_flip = False
    plus_before = False
    count = 0
    while(pos < len(cakes)):
        if(cakes[pos] == '-'):
            need_flip = True
        if(cakes[pos] == '+'):
            if(need_flip):
                if( plus_before ):
                    count += 2
                    need_flip = False
                else:
                    count += 1
                    need_flip = False
            plus_before = True
        pos += 1
    if(need_flip):
        if(plus_before):
            count += 2
        else:
            count += 1
    print("Case #"+str(i)+": "+str(count))
        # print(cakes[j])
    # if(S==K):
    #     print("Case #"+str(i)+": ",end="" )
    #     for j in range(K):
    #         print(str(j+1)+" "  ,end="")
    #     print()
    # else:
    #     print("Case #"+str(i)+": IMPOSSIBLE")
