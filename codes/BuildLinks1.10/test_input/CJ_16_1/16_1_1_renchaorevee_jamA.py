#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(S):
    # print("[debug] solving %s" % (S))

    result = ""
    for c in str(S):
        if(result == ""):
            result = c
            continue

        if(c >= result[0]):
            result = c + result
        else:
            result = result + c;

    return result;

if __name__ == "__main__":
    testcases = input()

    for i in xrange(1, testcases+1):
        S = raw_input()

        print("Case #%i: %s" % (i, solve(S)))