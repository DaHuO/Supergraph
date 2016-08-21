t = int(raw_input())
for i in xrange(t):
    row = raw_input().strip()
    acc = 0
    last = "+"
    for p in reversed(row):
        if p != last:
            acc += 1
            last = p
    print "Case #{}: {}".format(i+1, acc)
