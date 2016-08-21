#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sabu
if __name__ == "__main__":
    testcases = int(input())                    #get number of tests     
    for caseNr in range(1, testcases+1):        #for each testcase
        n = int(input())                        #get input based on problem
        seen = [False] * 10
        nseen, m = 0, 0
        #skip for n==0
        if n == 0:
            print("Case #%i: INSOMNIA" % (caseNr))
            continue
        #loop until found
        while (True):
            m += n
            for j in [int(c) for c in str(m)]:
                if not seen[j]:
                    seen[j] = True
                    nseen += 1
            if nseen == 10:
                break
        print("Case #%i: %i" % (caseNr, m))