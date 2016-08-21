T = int(raw_input())


def solve(N):
    if not N:
        return "INSOMNIA"

    dict = {}
    current = 0
    while len(dict) < 10:
        current += N
        for c in str(current):
            dict[c] = True
    return str(current)

for i in xrange(T):
    N = int(raw_input())
    print("Case #%d: %s" % (i+1, solve(N)))
