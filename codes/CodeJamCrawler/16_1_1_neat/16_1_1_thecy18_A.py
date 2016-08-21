from itertools import count
from random import randint
from sys import stdout

namein = 'A-large.in'
nameout = 'A-large.out'

def solve(S):
    ret = []
    for s in S:
        if s == '\n' or s == '\r':
            continue
        tmp1 = list(ret)
        tmp1.append(s)
        tmp2 = [s]
        tmp2.extend(ret)
        if tmp1 > tmp2:
            ret = tmp1
        else:
            ret = tmp2
    return ''.join(ret)

fin = open(namein, 'r')
fout = open(nameout, 'w')
# fout = stdout
T = int(fin.readline())
for i in range(1, T+1):
    print('Case #{}: {}'.format(i, solve(fin.readline())), file=fout)
