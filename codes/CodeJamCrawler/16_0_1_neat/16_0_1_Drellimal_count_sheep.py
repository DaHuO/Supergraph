# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 21:58:13 2016

@author: Dane
"""
def count_sheep(n):
    complete = set([str(x) for x in range(10)])
    x = 0
    N = int(n)
    found = set([])
    while(found != complete):
        x+=1
        a= x*N
        found = found.union(set(str(a)))
    return x*N

for x in range(int(raw_input().strip())):
    n = raw_input().strip()
    if n == '0':
        ans = 'INSOMNIA'
    else:
        #ans = count_sheep(n)
        ans = count_sheep(n)
    print "Case #{}: {}".format(x+1, ans)