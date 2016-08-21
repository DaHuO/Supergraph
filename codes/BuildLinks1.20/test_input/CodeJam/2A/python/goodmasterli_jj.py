from itertools import chain
filein = open('A-large.in.txt', 'r')
fileout = open('A-large.out.txt', 'w')
mp = {
    'R': ['R', 'S'],
    'P': ['P', 'R'],
    'S': ['P', 'S']
}

T = int(filein.readline())

for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    N, R, P, S = map(int, filein.readline().rstrip().split())
    rst = 'T'
    for start in ['P', 'R', 'S']:
        l = [start]
        for i in range(N):
            l = list(chain(*list(map(lambda x: mp[x], l))))
            if l.count('R') > R or l.count('P') > P or l.count('R') > R or l.count('S') > S:
                break
        if l.count('R') != R or l.count('P') != P or l.count('S') != S:
            continue
        while len(l) != 1:
            l = [min(l[i], l[i + 1]) + max(l[i], l[i + 1])
                 for i in range(0, len(l), 2)]
        rst = min(rst, ''.join(l))
    if rst == 'T':
        rst = 'IMPOSSIBLE'
    fileout.write(rst + '\n')

filein.close()
fileout.close()