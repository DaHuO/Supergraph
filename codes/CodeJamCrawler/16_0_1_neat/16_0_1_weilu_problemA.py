#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import os
import sys

#print(sys.argv)

f = open(sys.argv[1])
lines = f.readlines()
T = int(lines[0].rstrip('\n'))

for i in range(1,T+1):
    num = int(lines[i].rstrip('\n'))
    digits = list(map(int,str(num)))
    myset = set()
    done =False
    for j in range(1,101):
        temp = num*j
        myset |= set(list(map(int,str(temp))))
        if(len(myset) == 10):
            done = True
            print("Case #"+str(i)+": "+str(temp) )#print('happy')
            break
    if(done == False):
        print("Case #"+str(i)+": INSOMNIA")
