#!/usr/bin/env python
# encoding: utf-8

"""
Submission for problem A: The Last word
of Round1A Google CodeJam 2016

Author: Tsirigotis Christos <tsirif@gmail.com>
Date: April 16, 2016
"""


OUTPUT = "Case #%(nc)s: %(last_word)s"

def solve():
    T = int(raw_input()) # 1 <= T <= 100
    for nc in xrange(1, T+1):
        S = raw_input() # 0 <= N <= 200 <= 1e6
        last_word = S[0]
        best_word = S[0]
        for word in S[1:]:
            if word >= best_word:
                last_word = word + last_word
                best_word = word
            else:
                last_word = last_word + word
        print(OUTPUT % locals())

solve()


