#!/usr/bin/env python

import sys

def c2i(c):
    return ord(c)-ord('A')

def sig(s):
    res = [0 for _ in xrange(26)]
    for c in s:
        res[c2i(c)] += 1
    return res

def comp(s1,s2):
    for i in xrange(26):
        if s1[i]>s2[i]:
            return False
    return True

def decr(s1,s2):
    for i in xrange(26):
        s2[i] -= s1[i]

def incr(s1,s2):
    for i in xrange(26):
        s2[i] += s1[i]

data = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
sigs = [sig(d) for d in data]

res = []
def decomp(s):
    if sum(s)==0:
        return True
    for i in xrange(10):
        if comp(sigs[i],s):
            decr(sigs[i],s)
            res.append(i)
            if decomp(s):
                return True
            incr(sigs[i],s)
            res.pop()
    return False

def main():
    global res
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        S = sys.stdin.readline().strip()
        sgn = sig(S)
        res = []
        decomp(sgn)
        #print res
        print 'Case #%d: %s' % (t,''.join(map(str,sorted(res))))

main()
