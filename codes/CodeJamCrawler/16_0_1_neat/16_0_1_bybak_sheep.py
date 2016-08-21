def sheep_for(N):
    if N == 0:
        return "INSOMNIA"
    # here N > 0
    digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    origN = N
    while digits:
        oldN = N
        while oldN > 0:
            digits.discard(oldN % 10)
            oldN /= 10
        N += origN
    return N - origN


T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    print "Case #%d: %s" % (i + 1, sheep_for(N))