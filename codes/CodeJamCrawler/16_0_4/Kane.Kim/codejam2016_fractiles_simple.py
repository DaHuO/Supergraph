import fileinput


def solve(K, C, S):
    return map(str, xrange(1, K+1))

a = solve(2, 2, 2)

for i, line in enumerate(fileinput.input()):
    if i == 0:
        continue
    K, C, S = map(int, line.strip().split(" "))
    res = " ".join(solve(K, C, S))
    if K - C + 1 > S:
        res = "IMPOSSIBLE"
    print "Case #%d: %s" % (i, res)
