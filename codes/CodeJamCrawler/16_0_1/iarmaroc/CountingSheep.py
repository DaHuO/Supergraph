largest = 0

def count(N):
    if N == 0:
        return 'INSOMNIA'

    digits = set()
    tries = 0

    while len(digits) < 10:
        tries += 1
        v = N * tries
        while v:
            d = v % 10
            digits.add(d)
            v /= 10

    return N * tries


T = int(raw_input())
for i in xrange(1, T + 1):
    N = int(raw_input())
    print "Case #{}: {}".format(i, count(N))
