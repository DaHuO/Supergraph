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
    return dict(N=int(s))


def _run(CASE, N=None):
    CASE.r = 0
    nums = set(range(10))

    if N == 0:
        CASE.r = "INSOMNIA"
    else:
        while nums:
            CASE.r += N
            n = CASE.r
            while n:
                nums.discard(n%10)
                n /= 10
if __name__ == "__main__":
    main()