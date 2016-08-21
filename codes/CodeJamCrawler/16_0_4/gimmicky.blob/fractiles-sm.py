#! /usr/bin/python

import sys

if __name__ == "__main__":
    num_tests = int(sys.stdin.readline())
    for test_number in range(1, num_tests + 1):
        k, c, s = map(int, sys.stdin.readline().split())
        positions = (i * (k**(c-1)) + 1 for i in range(k))
        print("Case #{}: {}".format(test_number, " ".join(map(str, positions))))