import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    counts = {}
    final = []
    for j in range(2*N-1):
        vals = map(int, sys.stdin.readline().strip().split())
        assert len(vals) == N
        for v in vals:
            if v in counts:
                counts[v] += 1
            else:
                counts[v] = 1
    for v in counts:
        if counts[v] % 2 == 1:
            final.append(v)
    assert len(final) == N, final
    print "Case #%d: %s" % (i+1, " ".join(map(str, sorted(final))))
        
