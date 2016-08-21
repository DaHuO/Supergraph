#!/usr/bin/env python
from collections import defaultdict
import string
import sys

T = int(sys.stdin.readline())

def score_diff(coders, jammers):
    try:
        return abs(int(coders) - int(jammers))
    except ValueError:
        return None

def valid_scores(score):
    if score.isdigit():
        yield score
    else:
        for digit in string.digits:
            yield from valid_scores(score.replace('?', digit, 1))


def minimize_score(coders, jammers):
    min_diff = sys.maxsize
    min_c = min_j = None

    for c in valid_scores(coders):
        for j in valid_scores(jammers):
            diff = score_diff(c, j)
            if diff > min_diff:
                continue
            elif diff < min_diff:
                min_diff = diff
                min_c = c
                min_j = j
            elif int(c) < int(min_c):
                min_diff = diff
                min_c = c
                min_j = j
            elif int(c) == int(min_c) and int(j) < int(min_j):
                min_diff = diff
                min_c = c
                min_j = j


    return min_c, min_j


for t in range(T):
    coders, jammers = sys.stdin.readline().strip().split()
    min_c, min_j = minimize_score(coders, jammers)
    print('Case #%d: %s %s' % (t + 1, min_c, min_j))
