#!/usr/bin/env python3
def solve(fin, fout):
    k, c, s = map(int, fin.readline().split())
    fout.write(' '.join(map(str, range(1, k + 1))))
    fout.write('\n')
