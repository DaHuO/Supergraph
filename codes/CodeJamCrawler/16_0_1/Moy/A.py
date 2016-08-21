#!/usr/bin/env python

import sys
import numpy as np


def solve(word):
    result = word[:1]
    word = word[1:]
    for ch in word:
        if ch < result[0]:
            result = result + ch
        else:
            result = ch + result

    return result


def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        print "Case #{}: {}".format(i+1, solve(sys.stdin.readline().strip()))


if __name__ == "__main__":
    main()


