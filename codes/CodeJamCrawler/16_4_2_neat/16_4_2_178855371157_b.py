import collections
import itertools
import sys

def product(xs):
    ret = 1
    for x in xs:
        ret *= x
    return ret

def tie(ps):
    ret = 0
    for ns in itertools.combinations(range(len(ps)), len(ps)/2):
        t = ps[:]
        for i in ns:
            t[i] = 1 - t[i]
        ret += product(t)
    return ret

def compute(ps):
    curr = [1, 0]
    
    for j, p in enumerate(ps):
        next = [0] * (j+3)
        next[0] = curr[0] * (1 - p)
        for i in range(1, j+2):
            next[i] = curr[i-1]*p + curr[i]*(1-p)
        curr = next

    return curr[len(ps)/2]

def greedy(ps, K):
    ret = []
    t = ps

    while len(ret) < K:
        options = [
            (ret + t[:2], t[2:]),
            (ret + t[-2:], t[:-2]),
            (ret + [t[0], t[-1]], t[1:-1])
        ]
        best_i = 0
        best_p = compute(options[0][0])
        for i in range(1, len(options)):
            p = compute(options[i][0])
            if p > best_p:
                best_p = p
                best_i = i

        (ret, t) = options[best_i]

    print ret
    ret.sort()
    print ret
    return compute(ret)

def greedy2(ps, K):
    ret = []
    t = ps

    while len(ret) < K:
        best_p = -1
        best = None
        for (i, j) in itertools.combinations(range(len(t)), 2):
            p = compute(ret + [t[i], t[j]])
            if p > best_p:
                best_p = p
                best = (ret + [t[i], t[j]], t[:i] + t[i+1:j] + t[j+1:])
        (ret, t) = best

    print ret
    ret.sort()
    print ret
    return compute(ret)


def exhaustive(ps, K):
    ret = 0
    best = []
    for x in itertools.combinations(ps, K):
        t = compute(x)
        if t > ret:
            ret = t
            best = x
    return ret

# print tie([0.1, 0.4, 0.8, 0.9])
# print compute([0.1, 0.4, 0.8, 0.9])

T = int(sys.stdin.readline())

for n in range(1, T+1):
    [N, K] = [int(x) for x in sys.stdin.readline().split()]
    ps = [float(x) for x in sys.stdin.readline().split()]
    ps.sort()

    # print ps
    # print

    # answer = compute(ps[:K/2] + ps[-K/2:])
    # answer = greedy(ps, K)
    # print answer
    # print

    # answer = greedy2(ps, K)
    # print answer
    # print

    answer = exhaustive(ps, K)

    print "Case #{}: {:.7f}".format(n, answer)
