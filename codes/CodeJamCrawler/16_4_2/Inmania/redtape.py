TEST="""4
2 2
0.50 0.50
4 2
0.00 0.00 1.00 1.00
3 2
0.75 1.00 0.50
16 8
0.75 1.00 0.50 0.75 1.00 0.50 0.50 0.50 0.75 1.00 0.50 0.75 1.00 0.50 0.50 0.50
"""
#raw_input = iter(TEST.splitlines()).next

import itertools

cache = dict()
def solve(n,k,l):
    all_poss = itertools.combinations(l, k)
    best = 0
    for a in all_poss:
        this =  prob_score(list(a), 0)
        best = max(this, best)
    return best

def prob_score(subset, score):
    hashable = tuple(subset)
    if (hashable, score) in cache:
        return cache[(hashable, score)]
    if len(subset) == 0:
        return score == 0

    if abs(score) > len(subset):
        return 0

    p = subset.pop()
    ans = p*prob_score(list(subset), score-1) +(1-p)*prob_score(list(subset), score+1)
    cache[(hashable, score)] = ans
    return ans

if __name__=="__main__":
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n,k = [int(s) for s in raw_input().split(" ")]
        l = [float(s) for s in raw_input().split(" ")]
        print "Case #{}: {}".format(i, solve(n,k,l))
          # check out .format's specification for more formatting options
