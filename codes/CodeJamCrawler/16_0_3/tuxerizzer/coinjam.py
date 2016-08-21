#!/usr/bin/env python
"""
usage: python file.py < X-small/large.in
"""
def divisor(num):
    if num <= 3:
        return None
    if num % 2 == 0:
        return 2
    if num % 3 == 0:
        return 3

    i = 5
    while i * i < 12345678:
        if num % i == 0:
            return i
        if num % (i + 2) == 0:
            return i + 2
        i += 6
    return None

def solve(n, j):
    i = 0
    res = 0
    while res < j:
        b = '1' + format(i, '0' + str(n - 2) + 'b') + '1'
        jamcoin = True
        ar = []
        for base in range(2, 11):
            d = divisor(int(b, base))
            if d is None:
                jamcoin = False
                break
            ar.append(d)
        if not jamcoin:
            i += 1
            continue
        print b,
        print ' '.join([str(z) for z in ar])
        i += 1
        res += 1

def main():
    t = int(raw_input())
    for casenum in range(t):
        n, j = [int(i) for i in raw_input().split()]

        print 'Case #%d:' % (casenum + 1)
        solve(n, j)

if __name__ == '__main__':
    main()
