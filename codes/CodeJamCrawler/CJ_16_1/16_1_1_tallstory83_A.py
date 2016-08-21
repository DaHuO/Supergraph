#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
    ret = cipher[0]
    for ch in cipher[1:]:
        if ret[0] <= ch:
            ret = ch + ret
        else:
            ret = ret + ch
    return ret

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
