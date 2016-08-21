import sys

def flip(l, n):
    x, y = l[:n + 1], l[n + 1:]
    x = [not a for a in x[::-1]]
    return x + y

lines = open(sys.argv[1], "rb").read().splitlines()
t = int(lines[0])
res = []

for i in xrange(1, t + 1):
    p = [c == '+' for c in lines[i].strip()]

    n = 0
    last = len(p) - 1
    while not all(p):
        for j in xrange(last, -1, -1):
            if not p[j]:
                last = j
                break
        if not p[0]:
            p = flip(p, last)
            n += 1
            continue
        j = 0
        while p[j]:
            j += 1
        p = flip(p, j - 1)
        p = flip(p, last)
        n += 2
    res.append("Case #%d: %d\n" % (i, n))

open(sys.argv[2], "wb").write(''.join(res))
