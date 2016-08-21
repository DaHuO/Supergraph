'''
Varun Bharadwaj
'''
import itertools

def lastword(s):
    lw = s[0]
    for i in range(1,len(s)):
        a = s[i] + lw
        b = lw + s[i]
        if a>b:
            lw = a
        else:
            lw = b
    return lw

testcases = int(input())

for t in  range(1,testcases+1):
    res = lastword(input())
    print('Case #',t,': ',res,sep='')
    
