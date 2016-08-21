#!/usr/bin/env python
# -*- coding: utf-8 -*-


def flip(cakes, n):
    cakes[n-1]

    pre = cakes[:n]
    post = cakes[n:]

    pre.reverse()
    pre = [not x for x in pre]
    return pre + post

# True :+
# False: -
def solve(cipher):
    cakes = [ch == '+' for ch in cipher]
    cnt = 0
    while 0 != cakes.count(False):
        # pre
        for idx in range(len(cakes)):
            if False == cakes[idx]:
                break

        idx -= 1
        if -1 != idx:
            cnt += 1
            cakes = flip(cakes, idx+1)

        # post
        for idx in range(-1, len(cakes) * -1 - 1, -1):
            if False == cakes[idx]:
                break
        idx += 1
        if len(cakes) != abs(idx):
            cnt += 1
            cakes = flip(cakes, len(cakes) + idx)

    return str(cnt)



if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))