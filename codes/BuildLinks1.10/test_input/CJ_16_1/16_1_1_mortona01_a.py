#!/usr/bin/env python

import sys

stdin = sys.stdin
T = int(stdin.readline())

for i in range(1, T+1):
    S = list(stdin.readline().rstrip())

    last_word = [S.pop(0)]
    for L in S:
        if last_word[0] <= L:
            last_word.insert(0, L)
        else:
            last_word.append(L)

    print "Case #{}: {}".format(i, ''.join(last_word))
