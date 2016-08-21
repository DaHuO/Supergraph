#!/bin/env python
from __future__ import print_function
import sys
import os
import os.path
import copy
from pprint import pprint

def match_col(grid, i, r):
    for j, row in enumerate(grid):
        if row[i] is not None and row[i] != r[j]:
            return False
    return True
def match_row(grid, i, r):
    for j, c in enumerate(grid[i]):
        if c is not None and c != r[j]:
            return False
    return True
def set_col(grid, i, r):
    global N
    for j in range(N):
        grid[j][i] = r[j]
    return grid
def set_row(grid, i, r):
    global N
    for j in range(N):
        grid[i][j] = r[j]
    return grid

def print_grid(grid):
    for row in grid:
        for c in row:
            print('%5s' % c, end='')
        print()

fi = open(sys.argv[1], 'r')
fo = open(os.path.splitext(sys.argv[1])[0] + '.small.out', 'w')

T = int(fi.readline().strip())
for k in range(T):
    N = int(fi.readline().strip())
    L = []
    for i in range(2 * N - 1):
        s = fi.readline().strip().split()
        s.sort(key=int)
        L.append(s)
    L.sort()
    
    grid = []
    for i in range(N):
        r = []
        for j in range(N):
            r.append(None)
        grid.append(r)
    
    nd = []
    for i in range(N):
        ndd = []
        for j, s in enumerate(L):
            ndd.append((s[i], j))
        ndd.sort(key=lambda x: int(x[0]))
        nd.append(ndd)
        
    shift = 0
    cc = []
    for i in range(N):
        d = 2 * i + shift
        if d + 1 < 2 * N - 1 and nd[i][d][0] == nd[i][d + 1][0]:
            grid[i][i] = nd[i][d][0]
            v1 = nd[i][d][1]
            v2 = nd[i][d + 1][1]
            cc.append((v1, v2))
        else:
            if shift < 0:
                print('WARN: shift!!')
            shift = -1
            grid[i][i] = nd[i][d][0]
            v = nd[i][d][1]
            cc.append((v,))
    
    missing = None
    i = 0
    while i < (1<<N):
        dd = copy.deepcopy(grid)
        succ = True
        for j in reversed(range(N)):
            if (i & (1 << j)) != 0:
                if match_row(dd, j, L[cc[j][0]]):
                    dd = set_row(dd, j, L[cc[j][0]])
                else:
                    succ = False
                    i += (1 << j)
                    break
                if len(cc[j]) > 1:
                    if match_col(dd, j, L[cc[j][1]]):
                        dd = set_col(dd, j, L[cc[j][1]])
                    else:
                        succ = False
                        i += (1 << j)
                        break
                else:
                    missing = j
            else:
                if match_col(dd, j, L[cc[j][0]]):
                    dd = set_col(dd, j, L[cc[j][0]])
                else:
                    succ = False
                    i += (1 << j)
                    break
                if len(cc[j]) > 1:
                    if match_row(dd, j, L[cc[j][1]]):
                        dd = set_row(dd, j, L[cc[j][1]])
                    else:
                        succ = False
                        i += (1 << j)
                        break
                else:
                    missing = j
        if succ:
            # print_grid(dd)
            if (i & (1 << missing)) == 0:
                r = dd[missing]
            else:
                r = map(lambda x: x[missing], dd)
            ret = ' '.join(r)
            break
    
    print('Case #%d:' % (k + 1), ret, file=fo)

fi.close()
fo.close()
