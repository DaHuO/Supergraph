import sys
import numpy as np


def sol(N, ds):
    counts = dict()
    for i in np.array(ds, dtype=int).ravel():
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    res = []
    for v in counts:
        if counts[v] % 2 != 0:
            res.append(v)
    res = sorted(res)

    return ' '.join(map(str, res))

inp = open(sys.argv[1])
out = open(sys.argv[2], 'w')
T = int(inp.readline())
for i in range(T):
    N = int(inp.readline().strip())
    ds = []
    for j in range(2*N-1):
        ds.append(map(int, inp.readline().strip().split()))
    out.write("Case #{}: {}\n".format(i+1, sol(N, ds)))
inp.close()
out.close()