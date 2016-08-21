# Python 3.5.1

from common import *

best = [{(0, 1, 0) : 'P', (1, 0, 0) : 'R', (0, 0, 1) : 'S'}]

for n in range(1, 13):
    b = best[n - 1]
    best.append({})
    keys = list(b.keys())
    for k1 in keys:
        for k2 in keys:
            if k1 == k2:
                continue
            k3 = (k1[0]+k2[0], k1[1]+k2[1], k1[2]+k2[2])
            if b[k1] < b[k2]:
                best[n][k3] = (b[k1] + b[k2])
            else:
                best[n][k3] = (b[k2] + b[k1])

def solvable(p, r, s):
    n = p + r + s
    if n == 1:
        return ('P' * p) + ('R' * r) + ('S' * s)
    k = n // 2
    if p > k or r > k or s > k:
        return False
    res = solvable(p + r - k, r + s - k, s + p - k)
    if res == False:
        return res
    res2 = ''
    for c in res:
        if c == 'P':
            res2 += 'PR'
        elif c == 'R':
            res2 += 'RS'
        elif c == 'S':
            res2 += 'PS'
    return res2

def main(casenum):
    n, r, p, s = readints()
    if (r, p, s) in best[n]:
        writecase(casenum, best[n][(r, p, s)])
    else:
        writecase(casenum, 'IMPOSSIBLE')

run(main)
