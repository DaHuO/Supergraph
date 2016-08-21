import sys

sys.stdin = open('C-small-attempt0.in', 'r')
sys.stdout = open('c-small.out', 'w')

import math


def get_k(s):
    res = []
    for i in range(2, 11):
        n = int(s, i)
        hit = False
        for j in range(2, int(math.sqrt(n)) + 1):
            if n % j == 0:
                res.append(j)
                hit = True
                break
        if not hit:
            return []
    res = map(str, res)
    return res


for z in range(int(input())):
    n, j = map(int, raw_input().split())
    s = ''.join(['1', '0' * (n - 2), '1'])
    t = ''.join(['1', '0' * n])
    print 'Case #%d:' % (z + 1)
    while int(s) < int(t):
        res = get_k(s)
        if res:
            print '%s %s' % (s, ' '.join(res))
            j -= 1
            if j == 0:
                break
        s = str(bin(int(s, 2) + 2))[2:]
