#!/usr/bin/python2
from sympy.ntheory import factorint, isprime
import random
state = 0x69696969ABCDEF69;

blacked = set()

def gennum(N):
    ans = []
    ok = True
    cand = 0
    while (True):
        ans = []
        ok = True
        cand = (random.randint(1,(1<<N)-1)%(1<<N)) | (1<<(N-1)) | 1
        if (bin(cand).count("1")%6 != 0):
            continue
        for i in [2,4,6,8]:
            num = int(bin(cand)[2:], i)
            if (isprime(num)):
                ok = False
                break
        if (not ok):
            continue

        for i in range(2, 11):
            num = int(bin(cand)[2:], i)
            if (i in [2,4,6,8]):
                ans += [factorint(num, limit=1000).keys()[0]]
            elif (i in [3,5,7,9]):
                ans += [2]
            elif (i in [10]):
                ans += [3]
            if (num == ans[-1]): #prime number that didnt failed miller rabin, wut?
                ok = False
                break
        if (not ok):
            continue
        if(cand in blacked):
            continue
        blacked.add(cand)
        return (cand, ans)



def _main():
    T = input()
    N, J = raw_input().split()
    N = int(N)
    J = int(J)
    print "Case #1: "
    for i in range(J):
        x = gennum(N)
        out = bin(x[0])[2:]
        for i in x[1]:
            out += " " + str(i)
        print out

_main() #yeah bitch
