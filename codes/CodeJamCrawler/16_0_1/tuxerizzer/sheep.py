#!/usr/bin/env python
"""
usage: python file.py < X-small/large.in
"""


def get_number(num):
    i = 1
    s = set()
    if num == 0:
        return 'INSOMNIA'

    while True:
        n = i * num
        s.update(list(str(n)))
        if len(s) == 10:
            return n
        i += 1

def main():
    t = int(raw_input())
    for casenum in range(t):
        nums = [int(i) for i in raw_input().split()]
        for num in nums:
            res = get_number(num)

        print 'Case #%d: %s' % (casenum + 1, res)

if __name__ == '__main__':
    main()
