# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 13:41:02 2016

@author: Dane
"""
def switch(pattern, stop):
    a = list(pattern)
    for x in range(stop):
        if a[x] == '-':
            a[x] = '+'
        else:
            a[x] = '-'
    return a    
    
def flip(pattern):
    mcount = pattern.count('-')
    pcount = pattern.count('+')
    length = len(pattern)
    if length == mcount:
        return 1
    if length == pcount:
        return 0
    else:
        last = pattern.rfind('-') +1 
        half = (len(pattern)+1) /2
        if pattern[0] == '+':
            first = pattern.index('-')
            pattern = list(pattern)
            pattern[:first] = ['-' for x in range(first)]
            pattern = switch(pattern, last)
            rpattern = pattern[:last]
            rpattern.reverse()
            pattern[:last] = rpattern
            return 2 + flip("".join(pattern))
        
        if pattern[0] == '-':
            pattern = switch(pattern, last)
            pattern = list(pattern)
            rpattern = []
            rpattern += pattern[:last]
            rpattern.reverse()
            pattern[:last] = rpattern
            return 1 + flip("".join(pattern))
        
            
for x in range(int(raw_input())):
    pattern = raw_input().strip()
    ans = flip(pattern)
    print "Case #{}: {}".format(x+1, ans)

