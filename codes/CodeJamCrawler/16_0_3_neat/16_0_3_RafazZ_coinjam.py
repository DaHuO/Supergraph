#!/usr/bin/env python

# from primesieve import *
from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')

def str2base(str, base):
    res = 0
    for c in str:
        res *= base
        if c == '1':
           res += 1
        
    return res

def baseConvert(dec):
    dec = bin(dec)[2:]
    res = []

    for idx in range(2, 11):
        res.append(str2base(dec, idx))
    return res


def strConvert(st):
    dec = st
    res = []

    for idx in range(2, 11):
        res.append(str2base(dec, idx))
    return res

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()
    def bar(self):
        lib.Foo_bar(self.obj)

    def isPrime(self, num):
        return lib.Foo_prime(self.obj, num)

def nonPrimes(lower, upper, foo): # Non-inclusive
    candNum = lower + 1
    candDiv = []

    # base = [2,3,4,5,6,7,8,9,10]
    while True:
        # print "Testing", candNum
        candDiv = []
        # iterate until find a correct one
        div = 0
        for num in baseConvert(candNum):
            # if not prime append to the candDiv
            div = foo.isPrime(num)
            # print div
            if div <= 1: # is prime
                break
            
            candDiv.append(div)

        if len(candDiv) == 9:
            break
        
        elif candNum >= upper:
            print "Something Went Wrong!"
            break
        else:
            candNum += 2

    
    res = [bin(candNum)[2:]]
    for el in candDiv:
        res.append(str(el))

    return res
    
def generate(N, J, foo):
    lower = int('1' + '0'*(N-2) + '1', 2)
    lower += lower / 2
    upper = int('1'*N, 2)

    for idx in range(J):
        res = nonPrimes(lower-1, upper+1, foo)
        print ' '.join(res)
        lower = int(res[0], 2) + 2
        if lower >= upper:
            print "Out of bounds!"
            break
    
f = Foo()

for idx in range(1, input()+1):
    N, J = map(int, raw_input().split())
    
    print "Case #%d:"%idx
    generate(N, J, f)

    # print str2base('110', 10)
    # print baseConvert(15)

