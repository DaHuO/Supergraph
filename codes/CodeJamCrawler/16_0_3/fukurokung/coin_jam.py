#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Problem C: Coin Jam
#Author: Wongnaret Khantuwan

import math

def nbase(digit, base):
    result = long(0)

    for i in range(1,len(digit)+1):
        tmp_digit = int(digit[i*-1])
        result += tmp_digit*(base**(i-1))

    return result

def find_divisor(digit):
    #print 'find divisor:', digit
    i = 2
    while i < math.sqrt(digit):
        #print 'i:',i
        if (digit % i) == 0:
            return i

        i += 1
    return digit

def is_coin_jam(digit):
    if digit.startswith('0') or digit.endswith('0'):
        return None

    divisor = []

    for i in range(2, 11):
        tmp_val = nbase(digit, i)
        tmp_divisor = find_divisor(tmp_val)
        #print 'base:%d\tval:%d\tdivisor:%d' %(i, tmp_val, tmp_divisor)

        if tmp_divisor != tmp_val:
            divisor.append(tmp_divisor)
        else:
            return None

    return divisor

def all_combination(seed, length):
    result = []
    if length == 1:
        for element in seed:
            result.append(element)
        return result

    else:
        for tmp_comb in all_combination(seed, length-1):
            for element in seed:
                result.append(tmp_comb+element)
        return  result

#main function
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    input = raw_input().split()
    n = int(input[0])
    j = int(input[1])

    print "Case #%d:" % i

    result_count = 0
    combination = all_combination('10', n)
    #print 'all_combination:',len(combination)
    for tmp_comb in combination:
        #print 'tmp_comp',tmp_comb
        if result_count == j:
            exit()

        result = is_coin_jam(tmp_comb)
        if result is None:
            continue

        txt = tmp_comb
        for divisor in result:
            txt = txt+' '+str(divisor)

        print txt
        result_count += 1
