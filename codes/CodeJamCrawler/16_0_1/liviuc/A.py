#!/usr/bin/python

import sys

def solve(nfi):
    with open(nfi, 'r') as fi:
        with open(nfi.replace("in", "out"), "a") as fo:
            fo.truncate(0)
            T = int(fi.readline())

            for case in xrange(1, T+1):
                N = int(fi.readline())
                if N == 0:
                    fo.write("Case #{}: INSOMNIA\n".format(case))
                    continue

                tot = N
                need = [str(i) for i in xrange(0, 10)]
                while need:
                    for d in str(tot):
                        if d in need:
                            need.remove(d)
                    if not need:
                        break
                    tot += N

                fo.write("Case #{}: {}\n".format(case, tot))

solve(sys.argv[1])
