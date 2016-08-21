#-------------------------------------------------------------------------------
# Name:        fractile_small.py
# Purpose:
#
# Author:      Akash
#
# Created:     09/04/2016
# Copyright:   (c) Akash 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
solutions_given=[]
def getsol(k, c):
    global solutions_given
    size=k**c
    if size>20000:
        size=20000
    lst=range(size+1)
    for i in range(1, size+1-k):
        if lst[i:i+k] not in solutions_given:
            solutions_given.append(lst[i:i+k])
            return " ".join([str(ch) for ch in lst[i:i+k]])
    for i in range(1, size+1-k):
        if list(reversed(lst[i:i+k])) not in solutions_given:
            solutions_given.append(list(reversed(lst[i:i+k])))
            return " ".join([str(ch) for ch in reversed(lst[i:i+k])])
    solutions_given.append(list(reversed(lst[1:1+k])))
    return " ".join([str(ch) for ch in reversed(lst[1:1+k])])

f=open(raw_input(), "r")
fw=open(raw_input(), "w")
T=int(f.readline())
for i in range(T):
    (K,C,S)=tuple([int(k) for k in f.readline().split()])
    #K==S
    fw.write("Case #"+str(i+1)+": "+getsol(K, C)+"\n")

fw.close()
print solutions_given
