#!/usr/bin/python
# -*- coding: utf-8 -*-
# python 2.7
# @Author: Moming

import random

def getRandNumber(right):
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    n = random.randint(0, 11)
    while prime_list[n] >= right:
        n = random.randint(0, 11)

    return prime_list[n]


def getMontgomeryPow(n, e, m):
    tmp = 1
    while e > 0:
        if (e & 1) == 1:
            tmp = (tmp * n) % m

        n = (n * n) % m
        e = e >> 1

    return tmp


def isPrime(n):
    if n <= 2:
        if n == 2:
            return True
        return False

    if n % 2 == 0:
        return False

    u = n - 1
    while u % 2 == 0:
        u = u // 2

    S = 5
    for i in range(S):
        a = random.randint(2, n - 1)
        x = getMontgomeryPow(a, u, n)
        tmp = u
        while tmp < n:
            y = (x * x) % n
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
            tmp = tmp * 2

        if x != 1:
            return False

    return True

"""
def getPow(n, e):
    tmp = 1
    while e > 0:
        if (e & 1) == 1:
            tmp = tmp * n

        n = n * n
        e = e >> 1

    return tmp
"""

def getBinary(j, N):
    cmd = bin(j).replace('0b', '')
    length = N - 2 - len(cmd)
    cmd = '1' + '0' * length + cmd + '1'
    return int(cmd)


"""
def getDecimal(n, base):
    if base == 10:
        return n

    result = 0
    e = 1
    while n:
        if 1 == n % 10:
            result += e

        e *= base
        n /= 10

    return result
"""

# main
if __name__ == '__main__':
    fr = open('./C-small-attempt2.in', 'r')
    fw = open('./result.in', 'w')
    T = int(fr.readline())

    for i in range(T):
        cmd = fr.readline().split(' ')
        (N, J) = (int(x) for x in cmd)
        fw.write('Case #%d:\n' % (i + 1))

        num = 0

        for j in range(0, int('1' * (N - 2), 2) + 1):
            if num >= J:
                break

            j = getBinary(j, N)
            flag = True
            tmp = []
            for base in range(2, 11):
                tmp.append(int(str(j), base))
                if isPrime(tmp[base - 2]):
                    flag = False
                    break

            if flag:
                num = num + 1
                fw.write('%d' % j)
                for base in range(2, 11):
                    if tmp[base - 2] % 2 == 0:
                        fw.write(' 2')
                        continue

                    remain = 1
                    while remain < tmp[base - 2]:
                        remain += 2
                        if isPrime(remain):
                            if tmp[base - 2] % remain == 0:
                                fw.write(' %d' % remain)
                                break

                fw.write('\n')

    fr.close()
    fw.close()

