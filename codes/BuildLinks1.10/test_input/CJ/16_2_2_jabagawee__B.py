#! /usr/bin/env python

T = int(raw_input())
bounds = {1: [0, 10], 2: [0, 100], 3: [0, 1000]}

def match(a, b):
    a, b = str(a), str(b)
    l = max(len(a), len(b))
    a, b = a.zfill(l), b.zfill(l)
    for x, y in zip(a, b):
        if not (x == y or x == '?' or y == '?'):
            return False
    return True

for case in range(T):
    C, J = raw_input().split()
    answer = (1000, 10000)
    l = len(C)
    b = bounds[l]
    for c in range(*b):
        for j in range(*b):
            if match(c, C) and match(j, J):
                if abs(c-j) < abs(answer[0] - answer[1]):
                    answer = (c, j)
                if abs(c-j) == abs(answer[0] - answer[1]):
                    answer = min((c, j), answer)
    print "Case #{}: {}".format(case + 1, ' '.join(map(lambda x: str(x).zfill(l), answer)))
