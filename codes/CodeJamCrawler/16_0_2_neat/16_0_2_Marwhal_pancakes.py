#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    testcases = input()
    def findChangeIndx(start, s):
        firstChar = s[0]
        for i in xrange(start,len(s)):
            if s[i] != firstChar:
                return i 
        return -1
    
    def flip(i, p):
        p = list(p)
        for e in xrange(0,i):
            if p[e] == "+" :
                p[e] = "-" 
            else :
                p[e] =  "+"
        return "".join(p)
            
    def solve(pancakes):
        n = len(pancakes)
        count = 0
        i = 0
        while(pancakes != ("+"*n)):
            count+=1
            if pancakes == "-"*n :
                break
            i = findChangeIndx(i, pancakes)
            pancakes = flip(i,pancakes)
        return str(count)
            
        
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
