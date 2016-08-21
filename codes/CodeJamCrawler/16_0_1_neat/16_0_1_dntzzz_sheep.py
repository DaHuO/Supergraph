from sys import stdin

def dig(N):
    c = []
    c.extend(str(N))
    return set([int(x) for x in c])

T = int(stdin.readline())
for c in range(1,T+1):
    N = int(stdin.readline())
    if N != 0:
        d = dig(N)
        rN = N
        while len(set(range(10)) -d) > 0:
            rN += N
            d = d.union(dig(rN))

    print "Case #{}: {}".format(c, rN if N != 0 else "INSOMNIA")
