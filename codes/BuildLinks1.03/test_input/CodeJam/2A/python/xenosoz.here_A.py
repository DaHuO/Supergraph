#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  Google Code Jam: Round 2 2016
#  Problem A. Rather Perplexing Showdown
#
#  by xenosoz on May 28, 2016.
#

win_table = ["PRS", "PSR", "SPR", "SRP", "RSP", "RPS"]

def evolve(s, level):
    if s == "P":
        return ["PR", "PR", "PR", "RP", "RP", "RP"][level % 6]
    if s == "R":
        return ["RS", "SR", "SR", "SR", "RS", "RS"][level % 6]
    if s == "S":
        return ["PS", "PS", "SP", "SP", "SP", "PS"][level % 6]
    
def grow(S, level):
    fn = lambda s: evolve(s, level)
    return "".join(map(fn, S))

def make_mature(seed, n):
    S = seed
    for level in reversed(range(n)):
        S = grow(S, level)
    return S

def make_sense(adult, R, P, S):
    return adult.count("R") == R and adult.count("P") == P and adult.count("S") == S

def solve(N, R, P, S):
    for seed in "PSR":  # PR(P) - PS(S) - RS(R)
        adult = make_mature(seed, N)
        if make_sense(adult, R, P, S):
            return adult
    return "IMPOSSIBLE"

def main():
    T = int(input())
    for case_id in range(1, T+1):
        N, R, P, S = map(int, input().split())
        print("Case #%d: %s" % (case_id, solve(N, R, P, S)))
    
if __name__ == '__main__':
    main()
