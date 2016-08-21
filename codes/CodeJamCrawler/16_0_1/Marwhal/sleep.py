#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    testcases = input()
    def solve(N):
        if N == "0": 
            return "INSOMNIA"
        n = N
        check = [False,False,False,False,False,False,False,False,False,False]
        while (not reduce (lambda x,y: x and y, check)):
            for i in (map (lambda x : int(x), list(n))):
                check[i] = True
            n = str(int(n) + int(N))
        n = str(int(n) - int(N))
        return n
            
     
    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
