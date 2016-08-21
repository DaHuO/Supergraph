# -*- coding: utf-8 -*-

T = int(raw_input())

def flip(s):
    r = []
    for c in reversed(s):
        if c == '+':
            r.append('-')
        else:
            r.append('+')

    return r

def findPlusIdx(s):
    # S[0] == '+'
    size = 1
    maxSize = 1
    maxIdx = 1

    for idx, c in enumerate(s):
        if idx == 0:
            continue

        if c == '+':
            size+=1
        elif c == '-':
            if size > maxSize:
                maxIdx = idx
                maxSize = size
                size = 0
    return maxIdx

def solve():
    S = list(raw_input().strip())

    r = 0
    if len(set(S)) == 1 and S[0] == '+':
        return r

    while len(S) > 0:
        if S[-1] == '+':
            S.pop()
        else:
            if S[0] == '-':
                S = flip(S)
                r += 1
            else:
                idx = findPlusIdx(S)
                S[:idx] = flip(S[:idx])
                r += 1
        


    return r

for tn in xrange(1, T+1):
    print "Case #%d: %s" % (tn, solve())
    
