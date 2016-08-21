#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  Google Code Jam: Round 2 2016
#  Problem B. Red Tape Committee
#
#  by xenosoz on May 28, 2016.
#

from collections import defaultdict

def combine_prob(_A, _B):
    X = defaultdict(float)
    A = _A[1]
    B = _B[1]
    M = 0
    for a, pa in A.items():
        for b, pb in B.items():
            X[a + b] += pa * pb
    for x, px in X.items():
        M = max(M, px)
    return (M, X)

def make_prob(p):
    return (max(p, 1-p), {1: p, -1: (1-p)})

def unit_prob():
    return (1, {0: 1})

from itertools import combinations

def solve(N, K, Probs):
    best_p = 0
    best_P = None
    for S in combinations(Probs, K):
        P = unit_prob()
        for p in S:
            P = combine_prob(P, make_prob(p))
            if P[0] < best_p:
                break
        if P[1][0] >= best_p:
            best_p = P[1][0]
            best_P = P
            
    return best_P[1][0]
    
def main():
    T = int(input())
    for case_id in range(1, T+1):
        N, K = map(int, input().split())
        Probs = list(map(float, input().split()))
        print("Case #%d: %.8f" % (case_id, solve(N, K, Probs)))

if __name__ == '__main__':
    main()
