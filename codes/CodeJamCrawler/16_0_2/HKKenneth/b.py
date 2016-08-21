import sys

n = None
i = 0
for line in sys.stdin:
    if n is None:
        n = int(line)
        continue
    i += 1
    prev = None
    delta = 0
    for c in line.strip():
        if prev is not None and prev != c:
            delta += 1
        prev = c
    if line.strip()[-1] == '-':
        delta += 1
    print "Case #%d: %d" % (i, delta)
