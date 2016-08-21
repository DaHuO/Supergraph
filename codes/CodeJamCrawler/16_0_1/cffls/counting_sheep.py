


def count_sheep(N):
    if N==0:
        return "INSOMNIA"
    candidates = set(map(str,range(10)))
    base = N
    while len(candidates)!=0:
        candidates = candidates - set(list(str(base)))
        base+=N
    return base-N


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N = int(raw_input())
    # n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i, count_sheep(N))

