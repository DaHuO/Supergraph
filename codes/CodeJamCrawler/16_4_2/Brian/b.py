def get_prob(P):
    K = len(P)
    cur = [1] + [0] * (K)
    for i in xrange(len(P)):
        next = [0] * (K+1)
        for j in xrange(K+1):
            next[j] = (1-P[i]) * cur[j]
            if j > 0:
                next[j] += P[i] * cur[j-1]
        cur = next
    return cur[K/2]

def recurse(chosen, left, to_choose):
    if to_choose == 0:
        return get_prob(chosen)
    if len(left) == 0:
        return None

    return max(
        recurse(chosen+[left[0]], left[1:], to_choose-1) or 0,
        recurse(chosen, left[1:], to_choose) or 0)

with open("b.in") as f:
    t = int(next(f))
    for case in xrange(t):
        N, K = [int(s) for s in next(f).strip().split(" ")]
        P = [float(s) for s in next(f).strip().split(" ")]

        x = "%.7f" % recurse([], P, K)

        print "Case #{}: {}".format(case+1, x)
