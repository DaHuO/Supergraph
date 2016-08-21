#!/usr/bin/python

import sys

def solve(nfi):
    with open(nfi, 'r') as fi:
        with open(nfi.replace("in", "out"), "a") as fo:
            fo.truncate(0)
            T = int(fi.readline())
            for case in xrange(1, T+1):
                arr = fi.readline().split()
                K = int(arr[0])
                C = int(arr[1])
                S = int(arr[2])

                if (C == 1 and S < K) or (C > 1 and S < K - 1):
                    fo.write("Case #{}: IMPOSSIBLE\n".format(case))
                elif K == 1:
                    fo.write("Case #{}: 1\n".format(case))
                elif C == 1:
                    fo.write("Case #{}: {}\n".format(case, " ".join([str(i) for i in xrange(1, K+1)])))
                else:
                    fo.write("Case #{}: {}\n".format(case, " ".join([str(i) for i in xrange(2, K+1)])))

solve(sys.argv[1])
