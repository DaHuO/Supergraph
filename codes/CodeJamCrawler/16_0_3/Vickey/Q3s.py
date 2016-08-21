#!/usr/bin/env python

import os
import re
import sys
import json
import time
import math
import shlex
import traceback
import subprocess

def isPrime(number):
    sqrt = int(math.ceil(math.sqrt(number)))
    if number == 1: return 1
    for i in range(2,sqrt+1):
        if number % i == 0:
            return i
    return -1

def main():
    #with open('input.txt', 'r') as f: inp = f.read().split('\n')
    with open('C-small-attempt0.in.txt', 'r') as f: inp = f.read().split('\n')

    inp = inp[1:]
    for c,i in enumerate(inp):
        if not i: continue

        number = i.strip().split(' ')
        digits = int(number[0])
        J = int(number[1])

        count = pow(2,digits-2)
        output = []
        jc = 0

        #print 'count '+str(count)
        for number in xrange(long(0),long(count-1)):
            #print number
            prime = False
            nt = []
            #print 'num '+str(number)
            baseNumber = None
            for b in range(2,11):
                #print 'dig '+str(digits)
                baseNumber = long(1)+pow(long(b), digits-1)
                #print 'base1 ' +str(baseNumber)
                nm = number
                pows = 1
                while nm != 0:
                    if (nm&0x1) !=0:
                        baseNumber += pow(long(b), pows)
                    nm = (nm>>1)
                    pows += 1
                #print 'base '+str(baseNumber)
                ret = isPrime(baseNumber)
                #print 'ret '+str(ret)
                if ret == -1:
                    prime = True
                    break
                else:
                    nt += [str(ret)]

            if prime: continue

            if jc == J: break
            #print baseNumber
            output += [str(baseNumber)+' '+ (' '.join(nt))]
            jc += 1

        print 'Case #'+str(c+1)+':\n'+str('\n'.join(output))

if __name__ == "__main__":
    main()