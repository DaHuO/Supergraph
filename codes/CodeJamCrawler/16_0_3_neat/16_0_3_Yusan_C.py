#!/usr/bin/python
# vi: set fileencoding=utf-8 :

'''
Google code jam 2016 qualification round
C: Coin Jam
'''


import math


def nontrivial_divisor(n):
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return i
    else:
        return 0


def judge(coin):
    nine_integers = []
    for base in range(2, 11):
        interpretation = 0
        for i in range(len(coin)):
            interpretation += coin[-i-1] * base ** i
        divisor = nontrivial_divisor(interpretation)
        if divisor > 1:
            nine_integers.append(divisor)
        else:
            return ''
    return ' '.join(map(str, nine_integers))


def enumerate_jamcoin_by_stack(N, J):
    '''
    '''

    output = 0
    stack = [[1, 1]]
    while len(stack) > 0:
        if output >= J:
            return
        v = stack.pop()
        if len(v) >= N:
            result = judge(v)
            if len(result) > 0:
                print ''.join(map(str, v)), result
                output += 1
        else:
            stack.append(v[:1] + [0] + v[1:])
            stack.append(v[:1] + [1] + v[1:])


T = int(raw_input())
for case_number in range(1, T + 1):
    N, J = map(int, raw_input().split())
    print 'Case #%d:' % case_number
    enumerate_jamcoin_by_stack(N, J)
