#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

inFile = open("input.txt","r")
outFile = open("output.txt","w")


def is_prime(q,k=50):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1
    for i in xrange(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

int2str_table = '0123456789abcdefghijklmnopqrstuvwxyz'

def int2str(i, base):
    if not 2 <= base <= 36:
        raise ValueError('base must be 2 <= base < 36')

    result = []
    temp = abs(i)
    if temp == 0:
        result.append('0')
    else:
        while temp > 0:
            result.append(int2str_table[temp % base])
            temp /= base

    if i < 0:
        result.append('-')

    return ''.join(reversed(result))


def solve(case, N, J):
    retstr = "Case #%d:\n" % (case)
    coinstr = "1" * N 
    count = 0
    bFirst = True
   
    # J個見つけるためのループ
    while True:
        # jamcoinを見つけるためのループ
        while True:
            if not bFirst:
                temp = int(coinstr, 2)>>1
                temp -= 1
                coinstr = "%s1" % int2str(temp, 2) 
            else:
                bFirst = False

            bCoinJam = True
            divisorList = []

            # 基数を回すループ
            for base in range(2, 11):
                val = int(coinstr, base)
                if is_prime(val):
                    bCoinJam = False
                    break
                j = 2
                while True:
                #for j in range(2, val):
                    if val % j == 0:
                        divisorList.append(j)
                        break
                    j += 1

            if bCoinJam:
                retstr += "%s %d %d %d %d %d %d %d %d %d\n" % (coinstr, divisorList[0], divisorList[1], divisorList[2], divisorList[3], divisorList[4], divisorList[5], divisorList[6], divisorList[7], divisorList[8])        
                break
            
        count += 1
        if count >= J:
            break
    return retstr


if __name__ == "__main__":
    isFirst = True
    totalCase = 0
    currentCase = 1 

    for line in inFile.readlines():
        items = line.split()

        # first Line
        if isFirst == True:
            isFirst = False
            totalCase = int(items[0])
            continue
        
        # execute
        out = solve(currentCase, int(items[0]), int(items[1]))
        outFile.write(out)
        print out
        
        # go next
        currentCase = currentCase + 1
        if currentCase > totalCase:
            break
    
