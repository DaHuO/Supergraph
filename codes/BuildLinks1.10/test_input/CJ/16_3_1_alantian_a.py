#!/usr/bin/env python3


input_file = 'A-large.in'
output_file = 'A-large.out'

def c(*args):
    return ''.join([chr(ord('A') + _) for _ in args])

def solve(N, P):
    res = []
    l = [[nb, i] for i, nb in enumerate(P)]
    l.sort()
        
    while len(l) > 0 and l[-1][0] > 1:
        if len(l) > 1 and l[-1][0] == l[-2][0]:
            res.append(c(l[-1][1], l[-2][1]))
            l[-1][0] -= 1
            l[-2][0] -= 1
        else:
            res.append(c(l[-1][1]))
            l[-1][0] -= 1
        
        l = [_ for _ in l if _[0] > 0]    
        l.sort()
        
    # now l is of 1 only, if every exists
    while len(l) > 0:
        if len(l) % 2 == 0:
            res.append(c(l[-1][1], l[-2][1]))
            l[-1][0] -= 1
            l[-2][0] -= 1
        else:
            res.append(c(l[-1][1]))
            l[-1][0] -= 1
        
        l = [_ for _ in l if _[0] > 0]    
        l.sort()
        
    return ' '.join(res)

fin = open(input_file)
fout = open(output_file, 'w')

T = int(fin.readline())
for Case in range(1, T + 1):
    N = int(fin.readline())
    P = list(map(int, fin.readline().split()))
    
    print('Case #%d: %s' % (Case, solve(N, P)), file=fout)

fin.close()
fout.close()