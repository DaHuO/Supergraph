#!/usr/bin/python
def opp(c):
    if c=='-':
        return '+'
    else:
        return '-'

def flip(s,l):
    for i in range(0,l):
        s[i] = opp(s[i])
    #print s
    return s
         
def solve(s):
    a = list(s)
    N=0
    while (1):
        l=next((i for i in range(0,len(a)) if a[i] == '+'),0)
        m=next((i for i in range(0,len(a)) if a[i] == '-'),0)

        if l:
            a = flip(a,l)
            N+=1
        elif m:    
            a = flip(a,m)
            N+=1
        if '+' not in set(a):
            a = flip (a,len(a)) 
            N+=1

        if '-' not in set(a):
            return N


t = int(input())
for i in range(1, t + 1):
    st = raw_input()
    print "Case #%s: %s" % (i,solve(st))