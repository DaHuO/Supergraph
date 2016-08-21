from itertools import *
import numpy as np
input = open('input.txt','r')
print 'Name of the file:', input.name

results = []
T = int(input.readline())

def getBase(x,bn):
    x = list(x)
    x = x[::-1]
    product = 0
    for i in xrange(len(x)):
        product += (bn**i)*int(x[i])
    return product

def isComposite(x):
    flag = 0
    for i in xrange(2,1000):
        if x%i==0:
            return i
    return flag


def isJamCoin(x):
    base = []
    for i in xrange(2,11):
        base.append(getBase(x,i))
    for i in xrange(len(base)):
        check = isComposite(base[i])
        if check==0: return [0,0,0,0,0,0,0,0,0]
        base[i] = check
    return base

for t in range(T):
    
    n = input.readline().strip().split(' ')
    
    oNum = 2**(int(n[0])-1)-1
    count = 0
    
    for i in range(100*(int(n[0])-2)):
        nNum = oNum+2
        oNum = nNum
        p = isJamCoin(bin(nNum)[2:int(n[0])+3])
        if sum(p)!=0:
            r = " ".join(str(x) for x in p)
            results.append(bin(nNum)[2:int(n[0])+3]+" "+r)
            count +=1
        if count>int(n[1])-1:
            break





input.close()
print len(results),results
out = open('out.txt','w')
out.write('Case #1: \n')
for i in range(len(results)):
    out.write(results[i]+'\n')

