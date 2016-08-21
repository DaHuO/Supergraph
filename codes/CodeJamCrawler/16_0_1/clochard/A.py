#!/usr/bin/env python

import sys


def solve(num):
    if num == 0:
        return 'INSOMNIA'
    cnt = 0
    used = [False for _ in xrange(10)]
    n = num
    for _ in xrange(1000):
        s = str(n)
        for c in s:
            o = ord(c) - ord('0')
            if not used[o]:
                used[o] = True
                cnt += 1
        if cnt == 10:
            return s
        n += num
        
    return 'INSOMNIA'


def main():
    nums = map(int, sys.stdin.readlines()[1:])
    for i, n in enumerate(nums):
        print 'Case #%d: %s' % (i + 1, solve(n))


if __name__ == '__main__':
    main()
