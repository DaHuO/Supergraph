import sys

lines = open(sys.argv[1], "rb").read().splitlines()
t = int(lines[0])
res = []

for i in xrange(1, t + 1):
    n = int(lines[i])
    if n == 0:
        res.append("Case #%d: INSOMNIA\n" % (i,))
        continue

    digits = set()
    j = 0
    while len(digits) != 10:
        j += 1
        digits = digits.union(set(str(j * n)))

    res.append("Case #%d: %d\n" % (i, j * n))

open(sys.argv[2], "wb").write(''.join(res))
