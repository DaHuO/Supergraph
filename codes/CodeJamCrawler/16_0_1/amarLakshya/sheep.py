#!/usr/bin/env python

def seeDigits(n,seen):
    digits = len(str(n))
    for i in str(n):
        if(i not in seen):
            seen.append(i)
    return seen


inputs = []
count = 1
i = 0
f = open('in','r')
for i in f.readlines():
    inputs.append(int(i))
f.close()
inputs = inputs[1:]
c = 1
for i in inputs:
    temp = i
    seen = []
    count = 1
    while(True):
        if(temp==0):
            print "Case #"+str(c)+":\tINSOMNIA"
            break;
        temp = i * count
        seen = seeDigits(temp, seen);
        if(len(seen) == 10):
            print "Case #"+str(c)+":\t"+str(temp)
            break;
        count = count + 1;
    c = c + 1
