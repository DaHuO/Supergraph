#!/usr/bin/python

import sys
VERBOSE = True

sin = sys.stdin
line = lambda : sin.readline().strip()

class case(object):
    def __init__(self, number):
        self.number = number
        self.r = ""

    def __enter__(self):
        return self

    def __exit__(self, *arg):
        print "Case #%s: %s" % (self.number, self.r)


def parse_result(out):
    return out.readline().strip()


def main():
    TEST_CASES = int(line())
    for CASE_NUMBER in range(1, TEST_CASES+1):
        with case(CASE_NUMBER) as CASE:
            _run(CASE, **parse())


def parse():
    s = sin.readline().strip()
    return dict(s=s)


def _run(CASE, s=None):
    CASE.r = 0
    s = s.rstrip("+")
    while s:
        if s[0] != s[-1]:
            s = "".join(reversed(['-' if _ == '+' else '+' for _ in s[:s.rindex("+")-len(s)+1]])).rstrip("+") + s[s.rindex("+")-len(s)+1:]
        else:
            s = "".join(reversed(['-' if _ == '+' else '+' for _ in s])).rstrip("+")
        CASE.r+= 1

if __name__ == "__main__":
    main()