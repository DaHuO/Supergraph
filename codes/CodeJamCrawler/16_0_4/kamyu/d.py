from math import ceil

def fractiles():
    K, C, S = map(int, raw_input().strip().split())

    if K // C > S:
        return "IMPOSSIBLE"

    indexes, digit = [], 0
    C = min(C, K)
    for i in xrange(0, K, C):
        idx = 0
        for j in xrange(C):
            idx += digit * (K**j)
            digit = min(digit + 1, K-1)
        indexes.append(idx+1)

    return " ".join(map(str, indexes))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fractiles())
