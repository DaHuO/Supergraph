# -*- coding: utf-8 -*-
######################################################
##                                                  ##
##  Fran Muñoz                                      ##
##  email: fran.mzy@gmail.com                       ##
##  UVA user: franmzy                               ##
##  Linkedin: https://www.linkedin.com/in/franmzy   ##
##                                                  ##
######################################################
import math

MAX_ITERATIONS = 100000

def is_divisible (num):
    if num <=1:
        return 0
    elif (num == 2):
        return 0
    elif (num % 2 == 0):
        return 2
    else:
        divisor = 3
        upperLimit = math.sqrt(num) +1
        iterations = 0
        while divisor <= upperLimit and iterations < MAX_ITERATIONS :
            if (num % divisor == 0) :
                return divisor
            divisor +=2
            iterations += 1

        return 0


def convert_to_base( n, base, long ):
    if( base == 2 ):
        return n

    number = 0
    for i in xrange(long-1, -1, -1):
        number *= base
        number += 1 if ((n & (1 << i)) > 0) else 0

    return number


nontrivial = [None]*12

n_cases = int(raw_input())

for i_case in xrange(n_cases):
    N, J = map(int, raw_input().split())
    print 'Case #{0}:'.format(i_case+1)

    start_jc = 1 << (N-1)
    start_jc += 1
    end_jc = 1 << N

    counter = 0
    for i_jc in xrange( start_jc, end_jc, 2 ):
        if counter >= J: break
        is_jamcoin = True
        for base in xrange(2, 11):
            nontrivial[base] = is_divisible(convert_to_base(i_jc, base, N))
            if( nontrivial[base] == 0 ):
                is_jamcoin = False
                break


        if( is_jamcoin ):
            counter+=1
            print convert_to_base(i_jc, 10, N),
            for base in xrange(2, 11):
                print nontrivial[base],
            print


