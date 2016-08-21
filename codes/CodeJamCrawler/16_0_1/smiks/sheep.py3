import sys

from collections import defaultdict

input = list(map(int, sys.stdin.read().strip().split("\n")))[1:]


def cnt(n, dd):
    ret = "INSOMNIA"
    for i in range(1, 301):
        r = n*i

        # check nums
        for s in str(r):
            dd[s] = 1
            if len(dd.keys()) == 10:
                return r

    return ret


for case, n in enumerate(input):
    dd = defaultdict(int)
    res = cnt(n, dd)
    print("Case #{0}: {1}".format((case+1), res))

