#!/usr/bin/python
# coding:UTF-8
# Author: David
# Email: youchen.du@gmail.com
# Created: 2016-04-09 11:19
# Last modified: 2016-04-09 13:46
# Filename: solution.py
# Description:
from math import sqrt


def is_prime(u):
    if u == 0 or u == 1:
        return False
    if u == 2:
        return True
    if u % 2 == 0:
        return False
    for i in xrange(3, int(sqrt(u+1))+1, 2):
        if u % i == 0:
            return False
    return True


def jamcoin(N):
    jam_base_str = '0b1'+(N-2)*'0'+'1'
    cnt = 0
    while True:
        flag = True
        ans = bin(2*cnt + int(jam_base_str, base=2))[2:]
        for b in xrange(2, 11):
            if is_prime(int(ans, base=b)):
                flag = False
                break
        if flag:
            yield ans
        cnt += 1


def divisor(val):
    for i in xrange(2, int(sqrt(val)+1)):
        if val % i == 0:
            yield i
    yield None

N = 16
J = 50
print 'Case #1:'
j = jamcoin(N)
for i in xrange(J):
    jm = j.next()
    divisors = []
    ans = 2
    legitimate = True
    for i in xrange(2, 11):
        ans_gen = divisor(int(jm, base=i))
        while True:
            ans = ans_gen.next()
            if not ans:
                legitimate = False
                break
            else:
                divisors.append(ans)
                break
        if not legitimate:
            continue
    print jm,
    for i in divisors:
        print ' ', i,
    print
