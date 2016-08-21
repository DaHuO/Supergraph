#!/usr/bin/env python

import sys

def debug_print(line):
    print(line, file=sys.stderr)

def find_winning_word(S):
    new_word = S[0]
    for c in S[1:]:
        if c < new_word[0]:
            new_word += c
        else:
            new_word = c + new_word
    return new_word

def read_input():
    num_test_cases = int(input())
    for t in range(1, num_test_cases + 1):
        S = input()
        debug_print("S:{}".format(S))

        lastword = find_winning_word(S)
        print("Case #{}: {}".format(t, lastword))

read_input()