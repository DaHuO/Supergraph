#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(cipher, N=1000000):
    idx = 0
    buf = [0]*10
    cipher = int(cipher)

    lastnum = ""
    while 10 != buf.count(1):
        idx += 1
        if N < idx:
            return "INSOMNIA"

        lastnum = str(cipher*idx)
        for ch in lastnum:
            buf[int(ch)] = 1

    return lastnum


if __name__ == "__main__":

    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
