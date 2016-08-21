#!/usr/bin/env python
import sys
import ipdb

def calc(ifile):
    N = int(ifile.readline())
    seen_numbers = set()
    inc = 1
    if N == 0:
        return 'INSOMNIA'
    else:
        while True:
            seen_numbers = seen_numbers.union(set(str(N*inc)))
            if seen_numbers == {'1','2','3','4','5','6','7','8','9','0'}:
                return N*inc
            inc += 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ifile = open(sys.argv[1])
    else:
        ifile = sys.stdin
    if len(sys.argv) > 2:
        ofile = open(sys.argv[2])
    else:
        ofile = sys.stdout
    for i in range(int(ifile.readline())):
        ofile.write("Case #%i: %s\n" % (i+1, calc(ifile)))

