# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def divisor(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return i
        i += 1
    return 1

T = int(raw_input())
for loop in xrange(1, T + 1):
    print "Case #%d:" % loop
    N, J = map(int, raw_input().split())
    coin = (1 << N - 1) + 1
    # 3 2 3 2 7 2 3 2 3
    while J > 0:
        c = bin(coin)[2:]
        if (sum(int(k) for k in c) % 3 != 0 or 
                c.count("1") % 2 != 0 or
                sum(int(k) for k in str(int(c, 8))) % 3 != 0):
            coin += 2
            continue
        ans = [0]*9
        for i in xrange(2, 11):
            d = divisor(int(c, i))
            if d == 1:
                break
            ans[i - 2] = d
        else:
            print c, " ".join(map(str, ans))
            J -= 1
        coin += 2
