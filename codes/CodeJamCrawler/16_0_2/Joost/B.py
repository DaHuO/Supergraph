#! /usr/bin/env python

from collections import defaultdict
from queue import Queue

fname = 'B-small'

fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')


def successors(x, xlen):
    for i in range(xlen):
        n = x >> i
        n ^= ((1 << (xlen-i)) - 1)
        n = sum(1 << ((xlen - i) - 1 - j) for j in range(xlen - i) if n >> j&1)
        yield n << i | ((1 << i) - 1) & x


def solve(fin):
    x = fin.readline().strip()
    xlen =  len(x)
    Y = 0
    for a in x:
        Y <<= 1
        if a == '-':
            Y += 1
    visited = defaultdict(lambda: False)
    visited[Y] = True
    current = Y
    Q = Queue()
    Q.put((Y, 0))
    while not Q.empty():
        current, depth = Q.get()
        if current == 0:
            return depth
        for suc in successors(current, xlen):
            if not visited[suc]:
                Q.put((suc, depth+1))
        visited[current] = True


T = int(fin.readline())
for i in range(1, T+1):
    print(i)
    fout.write("Case #"+str(i)+": "+str(solve(fin))+"\n")
fout.close()
fin.close()
