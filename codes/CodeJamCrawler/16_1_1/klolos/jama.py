#!/usr/bin/env python

import sys


def solve():
    letters = split_line(str)[0]
    res = letters[0]
    for l in letters[1:]:
        if ord(l) >= ord(res[0]):
            res = l + res
        else:
            res = res + l
    return res


def split_line(f=int):
    return map(f, sys.stdin.readline().strip().split())


def main():
    for i in range(split_line(int)[0]):
        sys.stdout.write("Case #%s: %s\n" % (i + 1, solve()))


if __name__ == '__main__':
    main()
