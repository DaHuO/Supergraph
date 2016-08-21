#!/usr/bin/env python

import sys

def main():
    """docstring for main"""
    filename = sys.argv[1]
    f = open(filename)
    T = int(f.readline())
    for i in range(T):
        s = solve(f.readline())
        print "Case #"+str(i+1)+":", s
    f.close()

def solve( instr ):
    N = int(instr)
    if N == 0:
        return 'INSOMNIA'
    n_str = str(N)
    ds = ''.join(set(str(N)))
    count = 1
    while len(ds)<10:
        count = count+1
        ds = ''.join(set(str(count*N)+ds))
    return str(count*N)


if __name__ == '__main__':
    main()
