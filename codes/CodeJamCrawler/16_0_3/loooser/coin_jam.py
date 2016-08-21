#!usr/bin/env python
from __future__ import print_function
from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
from random import *

def main():
    cases=int(raw_input())
    for i in xrange(cases):
        n,j = map(int,raw_input().strip().split())
        generated=0
        print("Case #",i+1,":",sep="")
        while generated!=j:
            gen = lambda n: [randint(0,1) for b in range(1,n+1)]
            num=gen(n)
            new=''.join(map(str,num))
            if num[0]!=1 or num[n-1]!=1:
                continue
            if isprime(int(new,2))==True or isprime(int(new,3))==True  or isprime(int(new,4))==True  or isprime(int(new,5))==True  or isprime(int(new,6))==True or isprime(int(new,7))==True  or isprime(int(new,8))==True  or isprime(int(new,9))==True or isprime(int(new,10))==True:
                continue
            generated+=1
            print(new,divisors((int(new,2))),divisors((int(new,3))),divisors((int(new,4))),divisors((int(new,5))),divisors((int(new,6))),divisors((int(new,7))),divisors((int(new,8))),divisors((int(new,9))),divisors((int(new,10))),sep=" ")

def isprime(n):

    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
        
def divisors(n):
    i=2
    while i:
        if n%i==0:
            return i
        i+=1

if __name__=='__main__':
	main()