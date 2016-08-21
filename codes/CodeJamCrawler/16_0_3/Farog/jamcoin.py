#!/usr/bin/python
import sys
import sys

from math import *
#file = sys.argv[1]

def execute():
    N=int(raw_input())
    for i in xrange(1,N+1):
        print(''.join(["Case #",str(i),": "]))
        input = raw_input().split(' ')
        pos = int(input[0])
        num = int(input[1])
        generateJams(pos, num)


def generateJams(pos,num):
    #jamcoin = ''.join(['1','0'*(pos-2),'1'])
    maxcnt = 2**(pos-2)
    rescnt = 0

    #print 'created', jamcoin
    for i in xrange(0,maxcnt-1):

        stri = "{0:b}".format(i)
        stri = '1'+'0'*(pos-2-len(stri)) + stri + '1'

        proof = getProof(stri)
        if proof is not None:
            print stri, ' '.join([str(x) for x in proof])
            rescnt += 1
            if rescnt == num:
                break



def getProof(jamcoin):
    # jamcoinrev = str(jamcoin)[::-1]
    results=[]
    for i in xrange(2,11):
        val = int(jamcoin, i)
        res = betterTestDiv(val)
        if res is not None:
            results.append(res)
        else:
            return None
    return results


def testDiv(val):
    max = int( floor(sqrt(val)) ) + 1
    i = 2
    while i < max:
        if val % i == 0:
            return i
        i += 1
    return None
    #return [x for x in
    #        [_testDiv(val, x) for x in range(2,max)]
    #        if x is not None
    #        ]

def _testDiv(val, num):
    if val % num == 0:
        return num
    return None

def betterTestDiv(val):
    if val in [2,3,5]:
        return None
    if val%2==0:
        return 2
    if val%3 == 0:
        return 3
    x = 5
    y = 2
    while x*x <= val:
        if x > 2**15:
            return None # skip this
        if val % x == 0:
            return x
        x += y
        y = 6-y
    #print 'PRIME'
    return None

def fermatTest(val):
    return (2**val)

# def getVal(jamcoin, base):
    # val = 0
    # acc = base
    # for idx, num in enumerate(jamcoinrev):
    #     val += int(num)*(base**idx)
    # return val

execute()
# generateJams(32, 500)
#betterTestDiv(1237)