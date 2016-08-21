import sys

inf = sys.argv[1]

f = open(inf, 'rU')
outf = open(inf + ".out", 'w')

T = int(f.readline())
for t in xrange(T):
    N  = int(f.readline())
    if N == 0:
        outf.write("Case #{0}: INSOMNIA\n".format(t+1))
        continue

    seen = {}
    i = 1
    n = 0
    while True:
        n = N * i
        i += 1
        for c in str(n):
            seen[c] = True
        if len(seen) == 10:
            break

    outf.write("Case #{0}: {1}\n".format(t+1, n))


f.close()
outf.close()
