#!/usr/bin/python

import sys
import math

# it convert number represented by list into integer in base = base
def list2num(list, base):
    number = 0
    multiplier = 1
    for i in range(0, len(list)):
        number = number + list[i] * multiplier
        multiplier = multiplier * base
    return number

def num2list(num, base):
    list = []
    while num / base > 0:
        list.append(num % base)
        num = num / base
    list.append(num % base)
    return list

def findDivisor(num):
    divisor = 1
    for i in range(2, int(math.ceil(math.sqrt(num))) + 1):
        if num % i == 0:
            divisor = i
            break
    return divisor



def CoinJam(N, J):
    ht = (1 << N - 1) + 1
    count = 0
    jamcoins = []
    divisors = []
    for i in range(0, 2 ** (N - 2)):
        if count == J:
            break
        num = ht + (i << 1)
        list = num2list(num, 2)
        # print i, list
        divisor = []
        for base in range(2,11):
            num_base = list2num(list, base)
            # print list, num_base, base
            d = findDivisor(num_base)
            # print base, num_base, d, num_base % d
            if d == 1:
                break
            else:
                divisor.append(d)
        if (len(divisor) == 9):
            count = count + 1
            # print count
            listnew = [str(list[i]) for i in range(0,len(list))]
            listnew.reverse()
            # jamcoins.append(num)
            jamcoins.append("".join(listnew))
            divisors.append(divisor[:])
            # for base in range(2,11):
                # print list2num(list,base),
            # print 
    return jamcoins, divisors
        

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(1, t + 1):
        N, J = [int(s) for s in raw_input().split(" ")]
        jamcoins, divisors = CoinJam(N,J)
        print("Case #1: ")
        for j in range(0, len(jamcoins)):
            print jamcoins[j], 
            for k in range(0, 9):
                print divisors[j][k],
            print
