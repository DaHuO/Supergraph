# -*- coding: utf-8 -*-

import math
from array import array
import time
    
def getPrimeToSqrtOf(n):
    limit = int(math.sqrt(n))+1
    ans = array('d')
    ans.append(2)
    sta = [-1]*limit
    sta[0] = False
    sta[1] = False
    sta[2] = True
    for i in range(3,limit,2):
        if sta[i] == -1:
            ans.append(i)
            for j in range(i+i+i,limit,i+i):
                sta[j] = i
    
    return ans,sta
    
n = 1111111111111111
prime,sta = getPrimeToSqrtOf(n) 
#%%
def getDiv(n):
    if n == 2 :
        return -1
    if n%2 == 0:
        return 2
    if n < len(sta) :
        return sta[n]
    limit = math.sqrt(n)
    for p in prime:
        if p > limit:
            return -1
        if n%p == 0:
            return p
    return -1

#%%
N = 16
J = 50

fo = open('/home/ton/Desktop/ggcj/Qualification Round 2016/C/small.out','wb')

def check(S):
    div = [0]*11
    for bas in range(2,11):
        n = 0
        for s in S:
            n *= bas
            n += int(s)
        d = getDiv(n)
        if d == -1:
            return -1
        div[bas] = int(d)
    return div[2:11]

def search(S):
    global J
    if J == 0:
        return
    if len(S) == N - 1:
        S = S+'1'
        div = check(S)
        if div == -1:
            return
        J -= 1
        print '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}'.format(S,div[0],div[1],div[2],div[3],div[4],div[5],div[6],div[7],div[8])
        
        fo.write( '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\n'.format(S,div[0],div[1],div[2],div[3],div[4],div[5],div[6],div[7],div[8]))
        return
    search(S+'1')
    search(S+'0')

print 'Case #1:'
fo.write('Case #1:\n')
search('1')

fo.close()