from collections import Counter
import string

def solve(ps):
    evacutation = []
    # keep the biggest two parties
    ps = [(string.ascii_uppercase[p],c) for p,c in enumerate(ps)]
    # two bests
    ps = sorted(ps, lambda x, y: cmp(y[1], x[1]))
    # flatten
    f = ps[0][1] - ps[1][1]
    while(f > 0):
        e = min(f, 2)
        evacutation += [ps[0][0]] * e
        f -= e
    # now we evacuate all other parties
    for i in range(2, len(ps)):
        f = ps[i][1]
        while(f > 0):
            e = min(f, 2)
            evacutation += [ps[i][0]] * e
            f -= e

    # now we evactuate couple from the first parties
    f = ps[1][1]
    while(f > 0):
        evacutation += [ps[0][0]+ps[1][0]]
        f -= 1

    return evacutation


def read_input():
    n  = int(raw_input())
    ps = map(int, raw_input().split())
    return ps,

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        res = map(str, solve(*read_input()))
        print "Case #%s: %s" % ( i+1, " ".join(res) )

    # test_cases = [
    #     ((2, 2), ),
    #     ((3, 2, 2), ),
    #     ((1, 1, 2), ),
    #     ((2, 3, 1), ),
    # ]
    # for i, test in enumerate(test_cases):
    #     res = map(str, solve(*test))
    #     print "Case #%s: %s" % ( i+1, " ".join(res) )