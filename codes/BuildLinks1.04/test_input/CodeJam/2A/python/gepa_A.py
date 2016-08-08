import sys


def sort_rps(x, N):
    if N == 0:
        return x
    k = 2 ** (N - 1)
    a = sort_rps(x[:k], N - 1)
    b = sort_rps(x[k:], N - 1)
    if a < b:
        return a + b
    else:
        return b + a

def make(N, x, R, P, S):
    m = {'R': "RS", 'P': "PR", 'S': "PS"}
    for i in xrange(N):
        x = ''.join(map(lambda a: m[a], x))
    counts = [0, 0, 0]
    for a in x:
        if a == 'R': counts[0] += 1
        if a == 'P': counts[1] += 1
        if a == 'S': counts[2] += 1
    if counts != [R, P, S]:
        return None
    return sort_rps(x, N)
        

def compute(N, R, P, S):
    x = make(N, "R", R, P, S)
    if x is not None:
        return x
    x = make(N, "P", R, P, S)
    if x is not None:
        return x
    x = make(N, "S", R, P, S)
    if x is not None:
        return x
    return "IMPOSSIBLE"


def parse():
    N, R, P, S = map(int, sys.stdin.readline().strip().split())
    return N, R, P, S


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().strip())
    count = 1
    part = 0
    if len(sys.argv) == 3:
        part = int(sys.argv[1])
        count = int(sys.argv[2])
    for i in xrange(T):
        data = parse()
        if i * count >= part * T and i * count < (part + 1) * T:
            result = compute(*data)
            print "Case #%d: %s" % (i + 1, result)
