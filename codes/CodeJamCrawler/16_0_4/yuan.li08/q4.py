import math

def list2num(lst, b, C):
    s = 0
    for i, j in enumerate(lst):
        if j >= b:
            break
        s += j * b**(C-i-1)
    return s    

def solve(K, C, S):
##    print('K:%d, C:%d, S:%d' % (K, C, S))
    minS = math.ceil(K/C)
    if S < minS:
        return 'IMPOSSIBLE'
    results = []
    for i in range(minS):
        results.append(1 + list2num(range(i*C, (i+1)*C), K, C))
    return ' '.join(map(str, results))

fname = 'test.txt'
fname = 'D-small-attempt0.in'
fname = 'D-large.in'
fin = open(fname)
lines = fin.readlines()
fin.close()

for k, line in enumerate(lines[1:]):
    [K, C, S] = list(map(int, line.strip().split()))
    print('Case #%d: %s' % (k+1, solve(K, C, S)))
