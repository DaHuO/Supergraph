# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:21:59 2016

@author: Benben
"""
def addC(X,Y):
    return [X[0]+Y[0],X[1]+Y[1],X[2]+Y[2]]

def generate(N):
    if N==1:
        return ['PR',[1,1,0],'RS',[0,1,1],'PS',[1,0,1]]
    else:
        temp=generate(N-1)
        oldP=temp[0]
        oldPC=temp[1]
        oldR=temp[2]
        oldRC=temp[3]
        oldS=temp[4]
        oldSC=temp[5]
        
        temp=sorted([oldP,oldR])
        newP=temp[0]+temp[1]
        newPC=addC(oldPC,oldRC)
        
        temp=sorted([oldR,oldS])
        newR=temp[0]+temp[1]
        newRC=addC(oldRC,oldSC)
        
        temp=sorted([oldP,oldS])
        newS=temp[0]+temp[1]
        newSC=addC(oldPC,oldSC)
        
        return [newP,newPC,newR,newRC,newS,newSC]


def sol(IF):
    temp=IF.readline().split()
    N=int(temp[0])
    R=int(temp[1])
    P=int(temp[2])
    S=int(temp[3])
    Possible=generate(N)
    for i in range(1,6,2):
        if [P,R,S]==Possible[i]:
            return Possible[i-1]
    return 'IMPOSSIBLE'
        



IF=open('A-large.in','r')
OF=open('A-large-output','w')
CaseN=int(IF.readline())
for i in range(1, CaseN+1):
    pretext='Case #{}: '.format(i)
    ans=sol(IF)
    if i<CaseN:
        ans=ans+'\n'
    OF.write(pretext+ans)
    
    
    
IF.close()
OF.close()


            
            