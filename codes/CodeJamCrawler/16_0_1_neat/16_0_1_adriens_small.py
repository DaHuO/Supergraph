import sys


def cnt(n):
    seen = set()
    for i in range(1,1000):
        N = i*n
        s = str(N)
        for c in s:
            seen.add(c)
        if len(seen) == 10:
            return i*n
    return "INSOMNIA"

pbsz = int(sys.stdin.readline())
for i in range(pbsz):
    print "Case #%i:"%(i+1), cnt(int(sys.stdin.readline()))


