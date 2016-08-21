#!/usr/bin/env python3


def flips(S, e, u):
    if S == "":
        return 0

    if S[-1] == e:
        return flips(S[:-1], e, u)
    else:
        return 1 + flips(S[:-1], u, e)


T = int(input())

for i in range(1, T + 1):
    S = input()
    print("Case #%d: %d" % (i, flips(S, '+', '-')))
