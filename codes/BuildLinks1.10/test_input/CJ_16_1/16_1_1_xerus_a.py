#!/usr/bin/env python3

def answer(S):
    r = [S[0]]
    for i in S[1:]:
        if i < r[0]:
            r.append(i)
        else:
            r = [i] + r
    return "".join(r)

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
    S = input()
    print("Case #{}: {}".format(i, answer(S)))
    # check out .format's specification for more formatting options
