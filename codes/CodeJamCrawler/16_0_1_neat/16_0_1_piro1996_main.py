#!/usr/bin/env python

def solve(n):
    last = n
    nums = set()

    while True:
        nums.update(list(str(last)))
        if len(nums) == 10:
            return last
        last += n

if __name__ == '__main__':
    t = input()
    for i in range(t):
        n = input()
        if n == 0:
            print 'Case #%d: INSOMNIA' % (i + 1)
        else:
            print 'Case #%d: %d' % (i + 1, solve(n))
