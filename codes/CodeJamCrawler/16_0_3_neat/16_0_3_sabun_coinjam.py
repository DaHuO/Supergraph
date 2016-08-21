#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sabu
if __name__ == "__main__":
    testcases = int(input())                    #get number of tests    
    #build table for power of each base
    pvalue = [[b**e for e in range(31,-1,-1)] for b in range(2,11)]
    #build prime table
    primes = [2,3]
    for n in range(5,1<<16,2):
        bprime = True
        for p in primes:
            if n%p == 0:
                bprime = False
                break
        if bprime:
            primes.append(n)
    
    #for each testcase
    for caseNr in range(1, testcases+1):
        #get input
        N, J = [int(x) for x in input().split()]          
        print("Case #%i:" % (caseNr))       
        #get the first number with the constraints (bookended by 1s), offset for first number
        jc = (1<<(N-1))-1
        #loop for J finding jamcoins
        while (J>0):
            fs = []
            jc += 2
            bvalid = True
            sjc = "{0:b}".format(jc)
            if (len(sjc)>N):
                break
            for b in range(2,11):
                #find the value in each base
                bjc = int(sjc, b)             
                #check for divisor
                rtv = bjc**.5
                bprime = True
                for p in primes:
                    if p>rtv:
                        break
                    if bjc%p == 0:
                        bprime = False
                        break
                #if no factor, skip this number
                if bprime:
                    break
                else:
                    fs.append(p)
                #get factor for next base
            #if there are 10 factors, we have a winner
            if len(fs)==9:
                print(sjc, ' '.join(map(str, fs)))
                J -= 1
                