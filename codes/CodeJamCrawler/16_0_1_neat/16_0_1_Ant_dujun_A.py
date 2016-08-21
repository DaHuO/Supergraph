import os
import sys

def parse(n):
    res = []
    while n != 0:
        res.append(n%10)
        n /= 10
    return res

def solve(n):
    flag = [0] * 10
    cnt = 10
    nn = n
    if nn == 0:
        return 'INSOMNIA'
    else:
        while cnt != 0:
            res = parse(nn)
            for r in res:
                if flag[r] == 0:
                    flag[r] = 1
                    cnt -= 1
            nn += n
        return nn - n

if __name__ == '__main__':
    with open('A-large.in') as f:
        T = int(f.readline().strip())
        for t in range(T):
            n = int(f.readline().strip())
            res = solve(n)
            print 'Case #%s: %s' % (t+1, res)
