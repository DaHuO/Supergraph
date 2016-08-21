#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from collections import Counter


def solve(S):
    
    def dict_word(word, n):
        return dict((c, n) for c in word)
    
    C = Counter(S)
    D = {}

    D[0] = C['Z']
    C.subtract(dict_word('ZERO', D[0]))
    
    D[2] = C['W']
    C.subtract(dict_word('TWO', D[2]))

    D[4] = C['U']
    C.subtract(dict_word('FOUR', D[4]))

    D[6] = C['X']
    C.subtract(dict_word('SIX', D[6]))

    D[8] = C['G']
    C.subtract(dict_word('EIGHT', D[8]))

    D[7] = C['S']
    C.subtract(dict_word('SEVEN', D[7]))

    D[5] = C['V']
    C.subtract(dict_word('FIVE', D[5]))

    D[3] = C['T']
    C.subtract(dict_word('THREE', D[3]))

    D[1] = C['O']
    C.subtract(dict_word('ONE', D[1]))

    D[9] = C['I']
    C.subtract(dict_word('NINE', D[9]))
    
    s = ''
    for d in range(10):
        s +=str(d) * D[d]
    
    return s 


T = int(ifs.readline())
for t in range(1, T + 1):
    S = ifs.readline().strip()
    a = solve(S)
    ofs.write('Case #%s: %s\n' % (t, str(a)))
