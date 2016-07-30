# https://code.google.com/codejam/contest/10224486/dashboard#s=p1
from itertools import chain
filein = open('20162A.in', 'r')
fileout = open('20162A.out', 'w')
reduce_map = {
    'S': ['P', 'S'],
    'P': ['P', 'R'],
    'R': ['R', 'S']
}

T = int(filein.readline())

for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    N, R, P, S = map(int, filein.readline().rstrip().split())
    ans = 'Z'  # Something big
    for start in ['P', 'R', 'S']:
        l = [start]
        for i in range(N):
            l = list(chain(*list(map(lambda x: reduce_map[x], l))))
            if l.count('P') > P or l.count('R') > R or l.count('S') > S:
                break
        if l.count('P') != P or l.count('R') != R or l.count('S') != S:
            continue
        while len(l) != 1:
            l = [min(l[i], l[i + 1]) + max(l[i], l[i + 1])
                 for i in range(0, len(l), 2)]
        print(l)
        ans = min(ans, ''.join(l))
    if ans == 'Z':
        ans = 'IMPOSSIBLE'
    fileout.write(ans + '\n')

filein.close()
fileout.close()
