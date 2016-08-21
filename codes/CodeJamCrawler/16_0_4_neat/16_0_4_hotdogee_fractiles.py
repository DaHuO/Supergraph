#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

def original_sequences(k):
    for x in itertools.product('GL', repeat=k):
        yield ''.join(x)

def produce_artwork(os, c):
    a = os
    g = 'G' * len(os)
    for i in xrange(c-1):
        a = ''.join([os if t == 'L' else g for t in a])
    return a

"""
6 6 1: 1866=6*311
5 1 5: 1 2 3 4 5
5 2 3: 2 14 15
5 3 3: 8 20
5 4 2: 39 40
5 5 1: 195=5*39 or 3125-194
5 6 1: 195
4 1 4: 1 2 3 4
4 2 3: 2 12
4 3 2: 2 12 or 7 8
4 4 1: 28=4*7 or 256-27
4 5 1: 28
4 6 1: 28
3 1 3: 1 2 3
3 2 2: 2 3
3 3 1: 6=3*2 or 27-5
3 4 1: 6
2 1 2: 1 2
2 2 1: 2
2 3 1: 2
"""
def print_table(k, c, s):
    out = ''
    for os in original_sequences(k):
        out += '{0}: {1}\n'.format(os, produce_artwork(os, c))
    return out
    
def print_table_transpose(k, c, s):
    out = ''
    co = 0
    for t in sorted([(i+1, ta.count('G'), ''.join(ta)) for i, ta in enumerate(zip(*[produce_artwork(os, c) for os in original_sequences(k)]))], key=lambda x: x[1], reverse=True):
        if t[1] < co: break
        co = t[1]
        out += '{0:3} {1:2} {2}\n'.format(t[0], t[1], t[2])
        
    return out

def solve(k, c, s):
    if n == 0: return 'INSOMNIA'
    sum = n
    s = set(str(sum))
    while len(s) < 10:
        sum += n
        s.update(set(str(sum)))
    return sum

def solve_small(k, c, s):
    return ' '.join([str(i) for i in range(1, k+1)])

if __name__ == "__main__":
    for case in xrange(1, 1+input()):
        print "Case #{0}: {1}".format(case, solve_small(*[int(x) for x in raw_input().strip().split()]))
        #print "Case #{0}: {1}".format(case, solve(*[int(x) for x in raw_input().strip().split()])),
        #print "Case #{0}\n{1}".format(case, print_table(*[int(x) for x in raw_input().strip().split()])),
        #print "Case #{0}\n{1}".format(case, print_table_transpose(*[int(x) for x in raw_input().strip().split()])),