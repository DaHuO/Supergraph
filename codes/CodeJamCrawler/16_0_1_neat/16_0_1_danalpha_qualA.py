#!/usr/bin/env python
# -*- coding: utf-8 -*-


def match(not_seen, num):
    return {x for x in not_seen if x not in str(num)}


def solve(cipher):
    n = int(cipher)
    if n == 0:
        return "INSOMNIA"

    not_seen = {str(x) for x in xrange(0, 10)}

    current = 0
    while not_seen:
        current += n
        not_seen = match(not_seen, current)

    return str(current)

if __name__ == "__main__":
    testcases = input()

    for case_num in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (case_num, solve(cipher)))
