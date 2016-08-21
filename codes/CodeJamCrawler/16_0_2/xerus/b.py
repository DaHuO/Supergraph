#!/usr/bin/env python3

import re

happy_regex = re.compile(r'\++')
blank_regex = re.compile(r'-+')

def answer(S):
    S = happy_regex.sub('+', S)
    S = blank_regex.sub('-', S)
    return len(S) - (S[-1] == '+')

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
    S = input()
    print("Case #{}: {}".format(i, answer(S)))
    # check out .format's specification for more formatting options
