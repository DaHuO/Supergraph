from __future__ import print_function
from array import *
from scipy.spatial import ConvexHull
import math
import random
import sys
import argparse
import sys
import copy
import functools
sys.setrecursionlimit(20000)

debug = True

def pr(s,end=None):
    if debug==True:
        if end!=None:
            print(s,end=end,flush=True, file=sys.stderr)
        else:
            print(s,flush=True, file=sys.stderr)

def out(s,end=None):
    if end!=None:
        print(s,end=end,flush=True)
    else:
        print(s,flush=True)

def compute(bs,n):
    pass



ss = []
grid = None
n = 0
# @functools.lru_cache(maxsize=None)
def find(i,row,col,used=0):
    if i == len(ss):
        for k in range(0,n):
            for j in range(0,n):
                if ( k > 0 and grid[k][j] <= grid[k-1][j] ) or ( j > 0 and grid[k][j] <= grid[k][j-1] ) or ( j>0 and k>0 and grid[k][j] <= grid[k-1][j-1]) :
                    return False
        return True
    s = ss[i]
    # pr(str(i)+' trying '+str(s)+" "+str(grid))
    # try row
    useRow = True
    if row < n:
        for j in range(n):
            if grid[row][j] != 0 and grid[row][j] != s[j]:
                useRow = False
        if useRow:
            oldRow = []
            for j in range(n):
                oldRow.append(grid[row][j])

            for j in range(n):
                grid[row][j] = s[j]
            # pr(str(i)+' trying row:'+str(grid))
            if find(i+1,row+1,col,used) == True:
                return True
            grid[row] = oldRow


    useCol = True
    if col < n:
        for j in range(n):
            if grid[j][col] != 0 and grid[j][col] != s[j]:
                useCol = False
        if useCol:
            oldCol = []
            for j in range(n):
                oldCol.append(grid[j][col])
            for j in range(n):
                grid[j][col] = s[j]
            # pr(str(i)+' trying col:'+str(grid))
            if find(i+1,row,col+1,used) == True:
                return True
            for j in range(n):
                grid[j][col] = oldCol[j]

    return used<1 and ( find(i,row+1,col,used+1) or find(i,row,col+1,used+1) )

T = int(input())
for t in range(1, T+1):
    out("Case #" + str(t) + ": ",end="")

    n = int(input())
    ls = []

    grid = [[0 for x in range(n)] for x in range(n)]

    for i in range(0,2*n-1):
        ls.append([ int(s) for s in input().split() ])

    ss = sorted(ls)
    # pr(ss)
    first = ss[0]

    for i in range(len(first)):
        grid[0][i] = first[i]

    row = 1
    col = 0

    # pr(ss)
    pr( find(1,row,col) )

    # pr(grid)
    for i in range(n):
        lls = []
        for j in range(n):
            lls.append(grid[i][j])

        if lls not in ss:
            for s in lls:
                out(s,end=' ')
            out('')
            break
        else:
            ss.remove(lls)

    for i in range(n):
        lls = []
        for j in range(n):
            lls.append(grid[j][i])

        if lls not in ss:

            for s in lls:
                out(s,end=' ')
            out('')
            break
        else:
            ss.remove(lls)
    # b,n = [ int(s) for s in input().split() ]
    # bs =  [ int(s) for s in input().split() ]
    # out(compute(bs,n))
