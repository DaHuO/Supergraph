#!/usr/bin/env python
# coding=utf-8
import math


cnt = 0

def prime_n(n):
    #print "prime: ", n
    for i in xrange(2, int(math.sqrt(n)) + 2):
        if i >= 1000000:
            break
        if n % i == 0:
            return i
    return -1

def convert(n, bs):
    p = 1
    ans = 0
    while n > 0:
        ans += p * (n % 10)
        p *= bs
        n /= 10
    return ans

def gao(n):
    ret = []
    for i in xrange(2, 11):
        ans = prime_n(convert(n, i))
        if ans == -1:
            return []
        ret.append(ans)
    return ret

def go(n, l):
#    print n, l
    global cnt
    if cnt >= 500:
        return
    if l > 31:
        return
    if l == 31:
        n *= 10
        n += 1
        ans = gao(n)
#        print n, ans
        if len(ans) > 0:
            cnt += 1
#            print "finished", cnt
            print n,
            for i in ans:
                print i,
            print ""
        return
    go(n * 10, l + 1)
    go(n * 10 + 1, l + 1)

print "Case #1:"
go(1, 1)
