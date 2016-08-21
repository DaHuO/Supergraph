def solve(x):
    s = set()
    cur = 0
    for i in range(1, 100000):
        cur += x
        for e in str(cur):
            s.add(e)
        if len(s) == 10:
            return cur
    else:
        return 'INSOMNIA'

import sys
sys.stdin = open('A-large.in', 'r')
sys.stdout = open('out', 'w')

t = int(input())
for i in range(1, t + 1):
    print('Case #%d:' % i, solve(int(input())))

sys.stdin.close()
sys.stdout.close()
