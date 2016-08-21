#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(s):
    # print("[debug] solving %s" % (n))

    idx = s.rfind('-')
    s = s[0:idx+1]

    if "-" not in s:
        return 0
    if "+" not in s:
        return 1

    # print("[debug] s: %s" % (s))

    count = 0;
    last_char = None;
    new_s = ""
    for c in str(s):
        if (last_char != c):
            new_s = new_s + c;
        last_char = c

    # print("[debug] new_s: %s" % (new_s))

    return len(new_s)


if __name__ == "__main__":
    testcases = input()

    for i in xrange(1, testcases+1):
        s = raw_input()

        print("Case #%i: %s" % (i, solve(s)))