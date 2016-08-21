#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Akash
#
# Created:     30/04/2016
# Copyright:   (c) Akash 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import itertools

def getdig(s):
    lstdig=[]
    lstpss=[]
    dicy={'ZERO':0, 'ONE':1, 'TWO':2, 'THREE':3, 'FOUR':4, 'FIVE':5, 'SIX':6, 'SEVEN':7, 'EIGHT':8, 'NINE':9}

    lstper=list(itertools.permutations(s, 3))+list(itertools.permutations(s, 4))+list(itertools.permutations(s, 5))
    for j in dicy.keys():
        if tuple([i for i in j]) in lstper:
            lstdig.append(dicy[j])
            #print dicy[j]
            lstpss.append(j)

    posscombs=[]
    for i in range(1, len(s)/3+1):
        posscombs+=list(itertools.combinations_with_replacement(lstpss, i))
    #print posscombs
    pre=["".join(k) for k in posscombs]
    for t in range(len(pre)):
        m=pre[t]
        #print m
        l1=[l for l in m]
        l1.sort()
        l2=[f for f in s]
        l2.sort()
        if l1==l2:
            #print posscombs[t]
            ans=[dicy[k] for k in posscombs[t]]
            ans.sort()
            return "".join([str(n) for n in ans])

#print getdig('XOOSINEXISNE')

fr=open(raw_input(), "r")
fw=open(raw_input(), "w")

t=int(fr.readline())

for i in range(t):
    s=str(fr.readline()).strip()
    print i+1
    fw.write("Case #"+str(i+1)+": "+getdig(s)+"\n")
fr.close()
fw.close()
print("Done")