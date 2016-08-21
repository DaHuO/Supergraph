#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jesli
# @Date:   2016-04-10 00:18:14
# @Last Modified by:   Jesli
# @Last Modified time: 2016-04-10 02:20:21

import os,sys
import random

sourceDic = {}
primeList = []

keyTested = {}

def testPrime(unnumber):
    for x in xrange(0,len(primeList)):
        if 0 == unnumber%primeList[x] and unnumber != primeList[x]:
            return False,primeList[x]

    return True, 0

def translate(number, base):
    index = 0
    ret = 0
    tmp = number
    
    while tmp > 0:
        ret += (tmp % 2) * (base**index)
        index += 1
        tmp /= 2

    return ret


def testNumber(source):
    retList = []
    for x in xrange(2,11):
        tmp = translate(source, x)
        flag, ans = testPrime(tmp)

        if flag:
            return False, retList
        else:
            retList.append(str(ans))

    return True, retList


def excutePrint(inputStr):
    valuse = inputStr.split(' ')
    N = int(valuse[0])
    J = int(valuse[1])

    count = 0;

    startPos = (1 << (N-1)) + 1
    endPos = 1<<N
    while count !=J:

        tKey = random.randint(startPos,endPos)
        if tKey %2 == 1 and not keyTested.has_key(tKey):
            keyTested[tKey] = 1
            flag, outList = testNumber(tKey)
            if flag:
                print str(bin(tKey).replace('0b', "")) + " " + " ".join(outList)
                count += 1


    #for x in xrange(1, (1<<N)):
    #    if (x&1) == 1 and (x&(1<<(N-1))==(1<<(N-1))):
    #        flag, outList = testNumber(x)
    #        if flag:
    #            print str(bin(x).replace('0b', "")) + " " + " ".join(outList)
    #            count += 1
    #            if count == J:
    #                break



for x in xrange(2, 100000):
    if not sourceDic.has_key(x):
        primeList.append(x)
        for y in xrange(1,100000):
            if x * y >= 100000:
                break
            else:
                sourceDic[x*y]=1



file_obj = open('C-large.in')
try:
    inputList = file_obj.readlines()
    if len(inputList) > 0:
        inputCount = int(inputList[0])
        for x in xrange(0,inputCount):
            print "Case #" + str(x+1) + ":"
            excutePrint(inputList[x+1])
finally:
    file_obj.close()
    pass
