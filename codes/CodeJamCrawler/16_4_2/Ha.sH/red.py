from solver import solver
from collections import defaultdict
from itertools import combinations

def proba(ps):
    d = {0: 1.}
    for p in ps:
        nd = defaultdict(int)
        for k, v in d.items():
            nd[k+1] += v * p
            nd[k-1] += v * (1-p)
        d = nd
    return d[0]

@solver(lines_per_case=2)
def red(lines):
    n, k = map(int, lines[0].split())
    ps = list(map(float, lines[1].split()))
    return max(map(proba, combinations(ps, k)))

if __name__ == '__main__':
    red.from_cli()
