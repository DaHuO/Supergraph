import sys
import itertools

cases = int(sys.stdin.readline().strip())

def get_score(prob, k):
    k2 = k/2
    tmp = [1] + [0]*(k-1)
    for p in prob:
        tmp1 = [0] + [x*p for x in tmp]
        tmp2 = [x*(1-p) for x in tmp]
        tmp = [x+y for x,y in zip(tmp1,tmp2)]
    return tmp[k2]

def solve(case):
    n,k = map(int, sys.stdin.readline().strip().split())
    probabilities = map(float, sys.stdin.readline().strip().split())
    res = max(get_score(x, k) for x in itertools.combinations(probabilities, k))

    print "Case #%d: %.9f" % (case, res)


for case in range(cases):
    solve(case+1)
